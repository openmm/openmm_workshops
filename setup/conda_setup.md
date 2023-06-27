# Running on your own machine with a Conda environment.

## Installing Conda

Please look at the Conda documentation and follow the steps for Miniconda for your operating system.
https://conda.io/projects/conda/en/stable/user-guide/install/index.html


## Creating and activating a conda environment 

Create a new conda environment.
The following command creates a new empty conda environment
```bash
conda create -n openmm
```

Activate new environment
```bash
conda activate openmm
```

Install OpenMM into the environment
OpenMM can be installed from conda-forge using the following command
```bash
conda install -c conda-forge openmm
```

Test installation
```bash
python -m openmm.testInstallation
```

If working the output should look similar to below (Note that if you do not have a GPU you will not see the OpenCL or CUDA platforms):

<details>
<summary> output </summary>

```
OpenMM Version: 8.0
Git Revision: a7800059645f4471f4b91c21e742fe5aa4513cda

There are 4 Platforms available:

1 Reference - Successfully computed forces
2 CPU - Successfully computed forces
3 CUDA - Successfully computed forces
4 OpenCL - Successfully computed forces

Median difference in forces between platforms:

Reference vs. CPU: 6.30521e-06
Reference vs. CUDA: 6.73158e-06
CPU vs. CUDA: 7.42296e-07
Reference vs. OpenCL: 6.74399e-06
CPU vs. OpenCL: 7.80735e-07
CUDA vs. OpenCL: 2.17122e-07

All differences are within tolerance.
```
</details>


## Jupyter

To run the jupyter notebooks in this workshop you will need to install Jupyter in your conda environment.
```
conda install -c conda-forge jupyter
```

You then load open the notebook with jupyter in your webrowser with the command
```
jupyter notebook <notebook>.ipynb
```

Alternatively you can open the notebook in [vscode](https://code.visualstudio.com/) and install the jupyter extension.

## mamba vs conda

Note that our example notebooks all use `mamba install ...` commands. 

`mamba` is a drop in replacement for `conda` and is significantly faster at solving environments and installing the packages. We recommend you use mamba but all `mamba install` commands can be replaced with `conda install` and they should work the same.

Once you have a working conda installation you can install mamba with the following line:
```
conda install mamba -n base -c conda-forge
```


## Getting the notebooks

You can get the notebooks and materials by git cloning this repo
```
git clone https://github.com/sef43/openmm_workshop.git
```