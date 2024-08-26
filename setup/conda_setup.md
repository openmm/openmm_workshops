# Running on your own machine with a Conda environment

## Installing Conda

Please refer to the [Conda documentation](https://conda.io/projects/conda/en/stable/user-guide/install/index.html) and follow the steps for installing Miniconda for your operating system.

## Creating and activating a Conda environment 

Create a new empty conda environment:

```bash
conda create -n openmm
```

Activate the new environment:

```bash
conda activate openmm
```

OpenMM can now be installed in this environment from the `conda-forge` repository using the following command:

```bash
conda install -c conda-forge openmm
```

Finally, test the OpenMM installation by running:

```bash
python -m openmm.testInstallation
```

If everything is working, the output should look similar to below (note that if you do not have a GPU, you will not see the OpenCL or CUDA platforms):

<details>
<summary> Output </summary>

```
OpenMM Version: 8.1.2
Git Revision: 440a9c7ae5df23ea1ab93798a422b6d9fd3ada99

There are 4 Platforms available:

1 Reference - Successfully computed forces
2 CPU - Successfully computed forces
3 CUDA - Successfully computed forces
4 OpenCL - Successfully computed forces

Median difference in forces between platforms:

Reference vs. CPU: 6.288e-06
Reference vs. CUDA: 6.74286e-06
CPU vs. CUDA: 7.34247e-07
Reference vs. OpenCL: 6.73115e-06
CPU vs. OpenCL: 7.46613e-07
CUDA vs. OpenCL: 1.68633e-07

All differences are within tolerance.
```
</details>


## Jupyter

To run the Jupyter notebooks in this workshop, you need to install Jupyter in your conda environment:

```
conda install -c conda-forge jupyter
```

Then, you can open the notebook in your web browser using the following command:

```
jupyter notebook <notebook>.ipynb
```

Alternatively, you can open the notebook in [VS Code](https://code.visualstudio.com/) and install the Jupyter extension.

## Mamba _vs_ Conda

Note that our example notebooks all use `mamba install ...` commands. 

`mamba` is a drop in replacement for `conda` that is significantly faster at solving environments and installing the packages. We recommend using `mamba` for improved performance. Note, however, that all `mamba install` commands can be replaced with `conda install` and should work the same way.

Once you have a working conda installation, you can install mamba with the following line:

```
conda install mamba -n base -c conda-forge
```

## Getting the notebooks

You can get the notebooks and materials for this workshop by git cloning this repo:

```
git clone https://github.com/openmm/openmm_workshop_july2023.git
```