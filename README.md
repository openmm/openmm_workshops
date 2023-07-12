# OpenMM workshop

This repository contains the materials for the OpenMM workshop that will be delivered on the 12th July 2023 after the CCPBioSim conference.

The workshop consists of an introduction presentation, setup information, and a series of jupyter notebooks.

The workshop will be delivered in person and on Zoom where demonstrators will be on hand to answer questions. The schedule has been sent to attendees.

Only the intro slides are specific to the live course. The workshop materials are designed to be done by anyone at anytime! We aim to keep the notebooks up to date. If you have any questions, find any bugs, or want to contribute a new notebook please raise an issue in the github repository.


## Introduction
This is a powerpoint presentation. The slides can be found in [./slides](./slides).


## Setup
There are two ways to run the workshop notebooks:
- In a web browser with Google Colab. 
- Running locally on your own machine in a Conda environment. 
 
The instructions for either can be found in [./setup](./setup/README.md).

We aim to keep the notebooks fully tested in Colab so we suggest you run them in Colab.

Note that we have designed the exercises to not be computationally expensive so they can be run on any hardware.


## Training materials
The material is in the form of jupyter notebooks. It is split up into three sections.

### Section 1 - Introduction to OpenMM
- [**Protein in water**](./section_1/protein_in_water.ipynb). Aimed at people new to OpenMM. This covers loading in a PDB file, setting up a simulation, running the simulation, basic analysis, and advice for running on HPC resources.
- [**Protein-ligand complex**](./section_1/protein_ligand_complex.ipynb). Aimed at beginners. Covers parameterising a small molecule, combining topologies, and using other tools to create OpenMM compatible input.

### Section 2 - Custom forces
- [**Custom forces and Umbrella sampling**](./section_2/custom_forces.ipynb). Aimed at people looking to use the custom forces functionality of OpenMM (Can be done after section 1 material if you are a beginner). Covers using custom forces with a case-study of umbrella sampling.

### Section 3 - Machine Learning Potentials
- [**Machine Leaning Potentials**](./section_3/machine_learning_potentials.ipynb). Aimed at people using Machine Learning Potentials. Covers the OpenMM Machine Learning software stack with examples of using ANI and MACE.

## Extras
- [Guide on building OpenMM from source](./extra/compile_openmm.ipynb).


## Acknowledgments
- This workshop was prepared by Stephen Farr (University of Edinburgh, Michel research group) with support from EPSRC grant EP/W030276/1 ''Supporting the OpenMM Community-led Development of Next-Generation Condensed Matter Modelling Software'' and with help from Julien Michel (University of Edinburgh) and Will Poole (University of Southampton, Essex research group).
