# Installation

Brightway is a Python software package. A user interface [is available](./ui.md), but not necessary for use. Brightway can be installed using the [Python package installer `pip`](https://pypi.org/project/pip/) or the multi-language package management system [conda](https://docs.conda.io/en/latest/) and its friend [mamba](https://mamba.readthedocs.io/en/latest/).

```{note}
Brightway supports Python >=3.8. This guide is for the current stable Brightway release (2.5); Activity-browser users should use the legacy Brightway 2 version Basic. See the [difference between `brightway2` and `brightway 25`](../faq/brightway.md).
```

## Installing Brightway using `pip`

::::{tab-set}

:::{tab-item} Linux, Windows, or MacOS (x64)

1. Install `python` from [the website](https://www.python.org/downloads/), your system package manager, or [Homebrew](https://docs.brew.sh/Homebrew-and-Python).

2. Create a directory for your virtual environments, such as `C:/Users/me/virtualenvs/`

3. In a console or terminal window, create a new virtual environment. Note that command must be executed in parent directory of your virtual environments directory, e.g. `C:/Users/me/` in our example above:

```console
python -m venv virtualenvs/brightway
```

4. Activate the virtual environment. The exact syntax depends on your operating system; it will look something like:

```console
source virtualenvs/brightway/bin/activate
```

5. Install Brightway:

```console
pip install brightway25 pypardiso
```

6. (Optional) You can also use pip to install useful libraries like `jupyterlab`.

:::

:::{tab-item} MacOS (Apple Silicon/ARM)

```{note}
Due to [an upstream bug](https://github.com/scikit-umfpack/scikit-umfpack/issues/98), there is currently no reliable way to install the fast sparse library `umfpack` on Apple Silicon using `pip`. Please install Brightway using `conda` or `mamba` for now.
```

1. Install [Homebrew](https://docs.brew.sh/Installation).

2. Install `python` from [Homebrew](https://docs.brew.sh/Homebrew-and-Python).

3. Install dependencies in a terminal window:

```console
brew install swig suite-sparse
```

4. Create a directory for your virtual environments. This can be anywhere; we will use the home directory here as an example:

```console
cd
mkdir virtualenvs
```

5. Create and activate a virtualenv:

```console
python -m venv virtualenvs/brightway
source virtualenvs/brightway/bin/activate
```

Note: You might need to specify the python version, like `python3.11`.

6. Create a configuration file to help [scikit-umfpack](https://pypi.org/project/scikit-umfpack/) build correctly. This can be called anything (with a `.ini` extension); we will use `custom-config.ini`. Add the following to that file:

```
[properties]
umfpack-libdir = '/opt/homebrew/Cellar/suite-sparse/7.6.0/lib/'
umfpack-includedir = '/opt/homebrew/Cellar/suite-sparse/7.6.0/include/suitesparse/'
```

This assumes you installed version `7.6.0`, you may need to adjust the version number. You should be able to run `ls /opt/homebrew/Cellar/suite-sparse/` to see what was installed.

7. Install `scikit-umfpack`:

```console
pip install scikit-umfpack -Csetup-args=--native-file=$PWD/custom-config.ini
```

This assumes that the `custom-config.ini` file is in your current working directory (`PWD` means print working directory).

8. Install Brightway:

```console
pip install brightway25 scikit-umfpack
```

9. (Optional) You can also use pip to install useful libraries like `jupyterlab`.

::::

## Installing Brightway using `conda` or `mamba`

```{admonition} Prerequisites
:class: important
1. A working installation of [`conda`](https://docs.conda.io/en/latest/) or `mamba`. If you are using `conda`, we recommend installing the [libmamba solver](https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community).
2. Basic knowledge of [Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
```

::::{tab-set}

:::{tab-item} Linux, Windows, or MacOS (x64)

1. Create a new Conda environment (in this example named `brightway`):

```console
conda create -n brightway -c conda-forge -c cmutel brightway25
```

2. Activate the environment:

```console
conda activate brightway
```

3. (Optional but recommended) You can also use conda to install useful libraries like `jupyterlab`:

```console
conda install -c conda-forge jupyterlab
```

:::

:::{tab-item} macOS (Apple Silicon/ARM)

```{note}
Brightway runs on the new Apple Silicon ARM architecture. However, the super-fast linear algebra software library `pypardiso` is not compatible with the ARM processor architecture. To avoid critical errors during instruction that would break core functionality, a different version of Brightway (`brightway25_nosolver`) and a a different linear algebra software library (`scikit-umfpack`) must be installed.
```

1. Create a new Conda environment (in this example named `brightway`):

```
conda create -n brightway -c conda-forge -c cmutel brightway25_nosolver scikit-umfpack
```

2. Activate the environment:

```
conda activate brightway
```

3. (Optional but recommended) You can also use conda to install useful libraries like `jupyterlab`:

```console
conda install -c conda-forge jupyterlab
```

::::

## Updating Brightway

Brightway is being actively developed, with frequent new releases. To update Brightway using `pip`, activate your virtual environment, and run:

```console
pip install -U brightway25
```

To update Brightway using `conda` or `mamba`, activate your environment, and run:

``` bash
conda update -c conda-forge -c cmutel brightway25
```

```{warning}
Apple Silicon users should update `brightway25_nosolver`.
```

```{warning}
Newer versions of Brightway can introduce breaking changes. We recommend you create a new environment for each project, and only update Brightway when you are ready to update your project.
```

```{toctree}
---
hidden:
maxdepth: 2
---
self
upgrading
ui
cloud
docker
```
