# Running on your own machine with a Conda environment.

The steps are different depending on your OS

## Linux

### Prequesites

You need to be able to open and use Terminal

### Steps

1. Install conda. (If you already have conda installed jump to step 2.)

We will use miniconda. You can download the bash install script here: https://docs.conda.io/en/latest/miniconda.html#linux-installers

Or in terminal you can run the command:
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

Now run the bash script and follow the steps.
```bash
bash Miniconda3-latest-Linux-x86_64.sh
```

Once installed you may need to reopen terminal for conda to work.

If it has installed properly the command
```bash
conda info
```
Should print information about your install and system.

2. Create a new conda environment.
The following command creates a new empty conda enviroment
```bash
conda create -n openmm
```

3. Activate new environment
```bash
conda activate openmm
```

3. Install OpenMM into the environment
OpenMM can be installed from conda-forge using the following command
```bash
conda install -c conda-forge openmm
```

4. Test installation
```bash
python -m openmm.testInstallation
```

If working the ouput should look similar to below (Note that if you do not have a GPU you will not see the OpenCL or CUDA platforms):

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


## MacOS


## Windows


