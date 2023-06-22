# OpenMM workshop

This repo contains the materials for the OpenMM workshop delivered on 12th July 2023 after the CCPBioSim conference.


The workshop consists of an introduction presentation, information on setting up an environment to runs the exercises, and three exercises.

## Introduction
This is a powerpoint presentation, the slides can be found in [./slides](./slides)


## Setup
There are two ways to run the exercises:
- In a web browser with Google Colab. See instructions here:
- Running locally on your own machine in a Conda environment. See the instructions here:

Note that we have designed the exercises to not be computationally expensive so they can be run on any hardware.


## Exercises
There are three exercises aimed at different types of user.
1. [Part 1 - **Protein in water** and part 2 - **Protein-ligand complex**.](./exercise_1/) Aimed at beginners. Covers setting up a simulation, running the simulation, basic analysis, advice on running on HPC resources,parameterising a small molecule, combining topologies, using other tools to create OpenMM compatible input.
2. [**Umbrella sampling.**](./exercise_2/) Aimed at people looking to use the custom forces functionality of OpenMM (Can be done after exercise 1 if you are a beginner). Covers setting up and running an umbrella sampling simulation.
3. **Machine Leaning Potentials.** Aimed at people using Machine Learning Potentials. Covers some of the OpenMM Machine Learning software stack.

## Extras
- [Guide on building OpenMM from source](./extra/compile_openmm.ipynb).
- Using the different platforms.