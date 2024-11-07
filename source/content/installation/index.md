# Installation

Brightway can be installed using the [Python package installer `pip`](https://pypi.org/project/pip/) or the multi-language package management system [conda](https://docs.conda.io/en/latest/) and its friend [mamba](https://mamba.readthedocs.io/en/latest/).

```{note}
Brightway supports Python >=3.9. This guide is for the current stable Brightway 2.5 release; see the [difference between `brightway2` and `brightway 25`](../faq/brightway.md).
```

(installing-pip)=
## Installing Brightway using `pip`

::::{tab-set}

:::{tab-item} Linux, Windows, or MacOS (x64)

1. Install `python` from [the website](https://www.python.org/downloads/), your system package manager, or [Homebrew](https://docs.brew.sh/Homebrew-and-Python).

2. Create a directory for your virtual environments, such as `C:/Users/me/virtualenvs/`

3. In a console or terminal window, create a new virtual environment.:

```console
python -m venv C:/Users/me/virtualenvs/brightway
```

4. Activate the virtual environment. The exact syntax depends on your operating system; it will look something like:

```console
source C:/Users/me/virtualenvs/brightway/bin/activate
```

5. Install Brightway:

```console
pip install brightway25 pypardiso
```

Note that `brightway25` is just an easy way to install libraries; it doesn't provide any functionality, and you shouldn't import it in Python scripts.

You can also use pip to install useful libraries like `jupyterlab`.

:::

:::{tab-item} MacOS (Apple Silicon/ARM)

```{note}
Due to [an upstream bug](https://github.com/scikit-umfpack/scikit-umfpack/issues/98), there is currently no reliable way to install the fast sparse library `umfpack` on Apple Silicon using `pip`, and the `pypardiso` library is only for x64 systems. If you are doing computationally-intensive workflows, we recommend installing Brightway using `conda` or `mamba` for now. If you are doing fewer calculations or software development installation via `pip` is fine.
```

1. Install `python` from [the website](https://www.python.org/downloads/), your system package manager, or [Homebrew](https://docs.brew.sh/Homebrew-and-Python).

2. In a terminal window, create a directory for your virtual environments. This can be anywhere; we will use the home directory here as an example:

```console
cd
mkdir virtualenvs
```

3. Create and activate a virtualenv:

```console
python -m venv virtualenvs/brightway
source virtualenvs/brightway/bin/activate
```

4. Install Brightway:

```console
pip install brightway25
```

Note that `brightway25` is just an easy way to install libraries; it doesn't provide any functionality, and you shouldn't import it in Python scripts.

You can also use pip to install useful libraries like `jupyterlab`.

::::

(installing-conda-mamba)=
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
conda create -n brightway -c conda-forge -c cmutel brightway25_nosolver scikit-umfpack numpy"<1.25"
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

```{toctree}
---
hidden:
maxdepth: 2
---
self
upgrading
ui
docker
```
