import openmm
import torch
from typing import Tuple


def removeBonds(system, atoms, removeInSet=True, removeConstraints=True):
    """Copy a System, removing all bonded interactions between atoms in (or not in) a particular set.

    Parameters
    ----------
    system: System
        the System to copy
    atoms: Iterable[int]
        a set of atom indices
    removeInSet: bool
        if True, any bonded term connecting atoms in the specified set is removed.  If False,
        any term that does *not* connect atoms in the specified set is removed
    removeConstraints: bool
        if True, remove constraints between pairs of atoms in the set

    Returns
    -------
    a newly created System object in which the specified bonded interactions have been removed
    """
    atomSet = set(atoms)

    # Create an XML representation of the System.

    import xml.etree.ElementTree as ET
    xml = openmm.XmlSerializer.serialize(system)
    root = ET.fromstring(xml)

    # This function decides whether a bonded interaction should be removed.

    def shouldRemove(termAtoms):
        return all(a in atomSet for a in termAtoms) == removeInSet

    # Remove bonds, angles, and torsions.

    for bonds in root.findall('./Forces/Force/Bonds'):
        for bond in bonds.findall('Bond'):
            bondAtoms = [int(bond.attrib[p]) for p in ('p1', 'p2')]
            if shouldRemove(bondAtoms):
                bonds.remove(bond)
    for angles in root.findall('./Forces/Force/Angles'):
        for angle in angles.findall('Angle'):
            angleAtoms = [int(angle.attrib[p]) for p in ('p1', 'p2', 'p3')]
            if shouldRemove(angleAtoms):
                angles.remove(angle)
    for torsions in root.findall('./Forces/Force/Torsions'):
        for torsion in torsions.findall('Torsion'):
            torsionAtoms = [int(torsion.attrib[p]) for p in ('p1', 'p2', 'p3', 'p4')]
            if shouldRemove(torsionAtoms):
                torsions.remove(torsion)

    # Optionally remove constraints.

    if removeConstraints:
        for constraints in root.findall('./Constraints'):
            for constraint in constraints.findall('Constraint'):
                constraintAtoms = [int(constraint.attrib[p]) for p in ('p1', 'p2')]
                if shouldRemove(constraintAtoms):
                    constraints.remove(constraint)

    # Create a new System from it.

    return openmm.XmlSerializer.deserialize(ET.tostring(root, encoding='unicode'))



@torch.jit.script
def simple_nl(positions: torch.Tensor, cell: torch.Tensor, pbc: bool, cutoff: float, sorti: bool=False) -> Tuple[torch.Tensor, torch.Tensor]:
    """simple torchscriptable neighborlist. 
    
    It aims are to be correct, clear, and torchscript compatible.
    It is O(n^2) but with pytorch vectorisation the prefactor is small.
    It outputs neighbors and shifts in the same format as ASE 
    https://wiki.fysik.dtu.dk/ase/ase/neighborlist.html#ase.neighborlist.primitive_neighbor_list

    neighbors, shifts = simple_nl(..)
    is equivalent to
    
    [i, j], S = primitive_neighbor_list( quantities="ijS", ...)

    Limitations:
        - either no PBCs or PBCs in all x,y,z
        - cutoff must be less than half the smallest box length
        - cell must be rectangular or triclinic in OpenMM format:
        http://docs.openmm.org/development/userguide/theory/05_other_features.html#periodic-boundary-conditions

    Parameters
    ----------
    positions: torch.Tensor
        Coordinates, shape [N,3]
    cell: torch.Tensor
        Triclinic unit cell, shape [3,3], must be in OpenMM format: http://docs.openmm.org/development/userguide/theory/05_other_features.html#periodic-boundary-conditions 
    pbc: bool
        should PBCs be applied
    cutoff: float
        Distances beyond cutoff are not included in the nieghborlist
    soti: bool=False
        if true the returned nieghborlist will be sorted in the i index. The default is False (no sorting).
    
    Returns
    -------
    neighbors: torch.Tensor
        neighbor list, shape [2, number of neighbors]
    shifts: torch.Tensor
        shift vector, shape [number of neighbors, 3], From ASE docs: 
        shift vector (number of cell boundaries crossed by the bond between atom i and j). 
        With the shift vector S, the distances D between atoms can be computed from:
        D = positions[j]-positions[i]+S.dot(cell)
    """

    num_atoms = positions.shape[0]
    device=positions.device

    # get i,j indices where j>i
    uij = torch.triu_indices(num_atoms, num_atoms, 1, device=device)
    triu_deltas = positions[uij[0]] - positions[uij[1]]

    wrapped_triu_deltas=triu_deltas.clone()

    if pbc:
        # using method from: https://github.com/openmm/NNPOps/blob/master/src/pytorch/neighbors/getNeighborPairsCPU.cpp
        wrapped_triu_deltas -= torch.outer(torch.round(wrapped_triu_deltas[:,2]/cell[2,2]), cell[2])
        wrapped_triu_deltas -= torch.outer(torch.round(wrapped_triu_deltas[:,1]/cell[1,1]), cell[1])
        wrapped_triu_deltas -= torch.outer(torch.round(wrapped_triu_deltas[:,0]/cell[0,0]), cell[0])

        # From ASE docs:
        # wrapped_delta = pos[i] - pos[j] - shift.cell
        # => shift = ((pos[i]-pos[j]) - wrapped_delta).cell^-1
        shifts = torch.mm(triu_deltas - wrapped_triu_deltas, torch.linalg.inv(cell))

    else:
        shifts = torch.zeros(triu_deltas.shape, device=device)
    
    triu_distances = torch.linalg.norm(wrapped_triu_deltas, dim=1)

    # filter
    mask = triu_distances > cutoff
    uij = uij[:,~mask]    
    shifts = shifts[~mask, :]

    # get the ij pairs where j<i
    lij = torch.stack((uij[1], uij[0]))
    neighbors = torch.hstack((uij, lij))
    shifts = torch.vstack((shifts, -shifts))

    if sorti:
        idx = torch.argsort(neighbors[0])
        neighbors = neighbors[:,idx]
        shifts = shifts[idx,:]

    return neighbors, shifts