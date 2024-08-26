#!/usr/bin/env python

import BioSimSpace as BSS

# Initialise the node object
node = BSS.Gateway.Node("Prepare a protein-ligand complex for MD simulations.")

# Set the node author and license.
node.addAuthor(
    name="Julien Michel",
    email="julien.michel@ed.ac.uk",
    affiliation="University of Edinburgh",
)
node.setLicense("GPLv3")

# Set the node inputs
node.addInput("ligand", BSS.Gateway.FileSet(help="A 3D representation of a ligand."))
node.addInput("protein", BSS.Gateway.FileSet(help="A 3D representation of a protein."))

node.addInput(
    "ligandff",
    BSS.Gateway.String(
        help="The forcefield to use to parameterise the ligand.",
        allowed=["gaff", "gaff2", "openff_unconstrained_2_0_0"],
        default="gaff2",
    ),
)

node.addInput(
    "waterff",
    BSS.Gateway.String(
        help="The forcefield to use to parameterise water.",
        allowed=["spc", "spce", "tip3p", "tip4p", "tip5p"],
        default="tip3p",
    ),
)

node.addInput(
    "proteinff",
    BSS.Gateway.String(
        help="The forcefield to use to parameterise proteins.",
        allowed=["ff03", "ff14SB", "ff99", "ff99SB", "ff99SBildn"],
        default="ff14SB",
    ),
)

node.addInput(
    "ion_conc",
    BSS.Gateway.Float(
        help="The concentration (in mol/L) of neutralising NaCl solution.",
        default=0.150,
    ),
)
# node.addInput("boxtype", BSS.Gateway.String(help="The shape of the periodic box",
#                                             allowed=['cubic', 'rhombicDodecahedronHexagon', 'rhombicDodecahedronSquare', 'truncatedOctahedron'],
#                                             default="truncatedOctahedron"))

node.addInput(
    "freeboxpadding",
    BSS.Gateway.Length(
        help="The length of padding to add around the free ligand bounding .",
        default=20,
        unit="angstrom",
    ),
)

node.addInput(
    "boundboxpadding",
    BSS.Gateway.Length(
        help="The length of padding to add around the protein-ligand complex bounding.",
        default=10,
        unit="angstrom",
    ),
)

# Set the node outputs
node.addOutput("free", BSS.Gateway.FileSet(help="The solvated ligand system."))
node.addOutput(
    "bound", BSS.Gateway.FileSet(help="The solvated protein-ligand complex.")
)
node.showControls()

# --------------------------------------------------------------------------- #
# Load the ligand and parameterise it using the specified forcefield.         #
# --------------------------------------------------------------------------- #
lig = BSS.IO.readMolecules(node.getInput("ligand"))[0]
lig_p = BSS.Parameters.parameterise(lig, node.getInput("ligandff")).getMolecule()

# --------------------------------------------------------------------------- #
# Work out bounding box for the ligand and solvate                            #
# --------------------------------------------------------------------------- #
box_min, box_max = lig_p.getAxisAlignedBoundingBox()
bounding_distances = [y - x for x, y in zip(box_min, box_max)]
padded_distances = [x + node.getInput("freeboxpadding") for x in bounding_distances]
# Orthorhombic only
box_angles = 3 * [90 * BSS.Units.Angle.degree]
lig_solvated = BSS.Solvent.solvate(
    node.getInput("waterff"),
    molecule=lig_p,
    box=padded_distances,
    angles=box_angles,
    ion_conc=node.getInput("ion_conc"),
)
print(lig_solvated)

# --------------------------------------------------------------------------- #
# Load the protein and parameterise it using the specified forcefield.        #
# --------------------------------------------------------------------------- #
protein = BSS.IO.readMolecules(node.getInput("protein"))[0]
prot_p = BSS.Parameters.parameterise(protein, node.getInput("proteinff")).getMolecule()

# --------------------------------------------------------------------------- #
# Combine the ligand and protein topologies.                                  #
# --------------------------------------------------------------------------- #
complex = lig_p + prot_p
box_min, box_max = complex.getAxisAlignedBoundingBox()
bounding_distances = [y - x for x, y in zip(box_min, box_max)]
padded_distances = [x + node.getInput("boundboxpadding") for x in bounding_distances]

# Orthorhombic only
box_angles = 3 * [90 * BSS.Units.Angle.degree]
complex_solvated = BSS.Solvent.solvate(
    node.getInput("waterff"),
    molecule=complex,
    box=padded_distances,
    angles=box_angles,
    ion_conc=node.getInput("ion_conc"),
)
print(complex_solvated)

# Save systems
node.setOutput("free", BSS.IO.saveMolecules("free", lig_solvated, ["PRM7", "RST7"]))
node.setOutput(
    "bound", BSS.IO.saveMolecules("bound", complex_solvated, ["PRM7", "RST7"])
)

node.validate()
