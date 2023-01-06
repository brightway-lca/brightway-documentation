# Installation

Brightway is a Python software package. It can be installed using the [Python package installer `pip`](https://pypi.org/project/pip/) or the [multi-language package management system `conda`](https://docs.conda.io/en/latest/). This guide uses `conda`.

```{note}
Brightway supports Python 2 and 3 (>3.4). However, we recommend you use Python 3. 
```

## Quickstart

```{admonition} Prerequisites
1) a working installation of [Conda](https://docs.conda.io/en/latest/)
2) basic knowledge of [Conda environments]((https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html))
```

```{warning}
For instructions specific to the novel Apple M1 ARM architecture, see below.
```

### Instructions

1. Create a new Conda environment (in this example named `bw`):

``` bash
conda create -n bw -c conda-forge brightway2 jupyterlab
```

2.  Activate the environment:

``` bash
conda activate bw
```

3. For platforms other than Unix (x64), follow the below platform-specific instructions to complete the setup. This includes _Microsoft Windows_ and _macOS (M1)_.

```{attention}
You will need to activate this environment every time you start a new
terminal or command line shell.
```

## Platforms

### Windows (x64)

1. Install [`pywin32`](https://pypi.org/project/pywin32/):

``` bash
conda install pywin32
```
### macOS (M1/ARM CPU Architecture)

Brightway and the [Activity Browser](https://documentation.brightway.dev/en/latest/source/setup/installation.html#graphical-user-interface-gui) run on the new M1 ARM architecture. However, the super-fast linear algebra software library `pypardiso` is not compatible with the M1 ARM architecture. To avoid critical errors during instruction that would break core functionality, a different version of Brightway (`brightway_nosolver`) must be installed, which includes a different linear algebra software library (`scikit-umfpack`):

1. Create a new Conda environment (in this example named `m1bw`):

``` bash
conda create -n m1bw -c cmutel -c conda-forge brightway2_nosolver jupyterlab scikit-umfpack
```

2.  Activate the environment:

``` bash
conda activate m1bw
```

# Notebook directory

It is best practice to store your notebooks in separate directories for
each project you are working on. One reasonable place would be in your
`Documents` or `Desktop`.


# Upgrading Brightway

Brightway is being actively developed, with frequent new releases. To upgrade Brightway, do the following:

``` bash
conda update conda
conda update -c conda-forge brightway
```