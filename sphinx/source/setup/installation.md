# Installation

Brightway is a Python software package. It can be installed using the [Python package installer `pip`](https://pypi.org/project/pip/) or the [multi-language package management system `conda`](https://docs.conda.io/en/latest/). This guide uses `conda`.

For the time being (October 2021), the latest version of Python is 3.10, but as this is brand new many useful libraries are not yet compiled against it, and 3.9 works just fine, so we use that.

## Quickstart

### Prerequisites

1. a working installation of [Conda](https://docs.conda.io/en/latest/)
2. basic knowledge of [Conda environments]((https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html))

### Instructions

1. create a new Conda environment (in this example named `bw`):

``` bash
conda create -n bw -c conda-forge brightway2 jupyterlab
```

2.  activate the environment:

``` bash
conda activate bw
```

⚠️ You will need to activate this environment every time you start a new
terminal or command line shell.

## Platforms

### Linux (x64)

No additional steps needed.
### Windows (x64)

1. install [`pywin32`](https://pypi.org/project/pywin32/)

``` bash
conda install pywin32
```
### macOS (x64)

No additional setup needed.
### macOS (M1/ARM CPU Architecture)

Brightway and the Activity Browser run on the M1 ARM architecture. However, the super-fast linear algebra solver software library `pypardiso` is not compatible with the M1 ARM architecture. To run Brightway on Macs with the M1 ARM architecture:

1.  Install [Rosetta](https://support.apple.com/en-us/HT211861).
2.  Create a new conda environment - the name given below is
    [ab]{.title-ref}, but this can be changed. As this environment will
    use x64 instructions, we install it into its own subdirectory:

``` bash
CONDA_SUBDIR=osx-64 conda create -n bw_rosetta python=3.9
conda activate bw_rosetta
conda env config vars set CONDA_SUBDIR=osx-64
```

3.  Install Brightway and the UMFPACK sparse linear algebra library:

``` bash
conda install -c conda-forge brightway2 scikit-umfpack
```

## FAQ

### Python 2 or Python 3

Brightway supports Python 2 and 3 (>3.4). However, we recommend you use Python 3. 

The library [eight](https://github.com/kislyuk/eight) is used to
forward-port python 2.7 code to 3.X. This means that `super`, `str`, and
`bytes` have 3.X semantics. The print function and true division are
imported from `__future__`, as are `unicode_literals`.

# Notebook directory

It is best practice to store your notebooks in separate directories for
each project you are working on. One reasonable place would be in your
`Documents` or `Desktop`.

# Graphical User Interface (GUI)

Brightway is a command-line tool intended primarily for use with [Jupyter Notebooks and the iPython shell](https://jupyter.org/). It does not provide a native graphical user interface. However, this functionality is provided by the Activity Browser project. To set up Activity Browser for use with Brightway, follow the [official installation instructions](https://github.com/LCA-ActivityBrowser/activity-browser#installation).

![image](images/activity-browser-new.png)

# Upgrading Brightway

Brightway is being actively developed, with frequent new releases. To upgrade Brightway, do the following:

``` bash
conda update conda
conda update -c conda-forge brightway
```