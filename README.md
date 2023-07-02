# OpenMM workshop

This repository contains the materials for the OpenMM workshop delivered on 12th July 2023 after the CCPBioSim conference.

The workshop consists of an introduction presentation, setup information, and a series of jupyter notebooks.

## Introduction
This is a powerpoint presentation. The slides can be found in [./slides](./slides)


## Setup
There are two ways to run the workshop notebooks:
- In a web browser with Google Colab. 
- Running locally on your own machine in a Conda environment. 
 
The instructions for either can be found in [./setup](./setup/README.md).

Note that we have designed the exercises to not be computationally expensive so they can be run on any hardware.


## Training materials
The material is in the form of jupyter notebooks. It is split up into three sections.

### Section 1 - Introduction to OpenMM
- [**Protein in water**](./exercise_1/exercise_1_part1.ipynb). Aimed at people new to OpenMM. This covers loading in a PDB file, setting up a simulation, running the simulation, basic analysis, and advice for running on HPC resources.
- [**Protein-ligand complex**](./exercise_1/exercise_1_part2.ipynb). Aimed at beginners. Covers parameterising a small molecule, combining topologies, and using other tools to create OpenMM compatible input.

### Section 2 - Custom forces
- [**Custom forces and Umbrella sampling**](./exercise_2/exercise_2.ipynb). Aimed at people looking to use the custom forces functionality of OpenMM (Can be done after section 1 material if you are a beginner). Covers using custom forces with a case-study of umbrella sampling.

### Section 3 - Machine Learning Potentials
- [**Machine Leaning Potentials**](./exercise_3/exercise_3.ipynb). Aimed at people using Machine Learning Potentials. Covers the OpenMM Machine Learning software stack with examples of using ANI and MACE.

## Extras
- [Guide on building OpenMM from source](./extra/compile_openmm.ipynb).
- Using the different platforms.