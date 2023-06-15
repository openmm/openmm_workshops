# OpenMM workshop

This repo contains the materials for the OpenMM workshop delivered on 12th July 2023 after the CCPBioSim conference.


The workshop consists of an introduction presentation, information on setting up an environment to runs the exercises, and three exercises.

## Introduction
This is a powerpoint presenation, the slides can be found in [./slides](./slides)


## Setup
There are two ways to run the exercises:
- In a web browser with Google Colab. See instructions here:
- Running locally on your own machine in a Conda environment. See the instructions here:

Note that we have designed the exercises to not be computationally expensive so they can be run on any hardware.


## Exercises
There are three exercises aimed at different types of user.
1. *Protein in water.* Aimed a beginners, people running standard MD. Covers: setting up a simulation, running the simulation, basic analysis, using the different platforms, and advice on running on HPC resources.
2. *Umbrella sampling.* Aimed at people looking to use the custom forces functionality of OpenMM (Can be done after exercise 1 if you are a beginner). Covers setting up and running an umbrella sampling simulation .
3. *MLPs.* Aimed at people using Machine Learning Potentials

## Extras
- Guide on building OpenMM from source