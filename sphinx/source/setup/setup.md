# Setup

Brightway is a Python software package. It can be installed using the [Python package installer `pip`](https://pypi.org/project/pip/) or the [multi-language package management system `conda`](https://docs.conda.io/en/latest/). This guide uses `conda`.

```{note}
Brightway supports Python 2 and 3 (>3.4). However, we recommend you use Python 3. 
```

## Quickstart

```{admonition} Prerequisites
1. A working installation of [Conda](https://docs.conda.io/en/latest/)
2. Basic knowledge of [Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
3. Basic knowledge of [the difference between `brightway 2` and `brightway 2.5`](../faq/brightway.md)
```


::::{tab-set}

:::{tab-item} Linux or macOS (x64)

```{note}
Brightway runs natively on Unix (x64) systems, including Linux distributions and macOS.
```

1. Create a new Conda environment (in this example named `bw`):

```
conda create -n bw -c cmutel brightway2 jupyterlab
```

2. Activate the environment:

```
conda activate bw
```

```{warning}
You will need to activate this environment every time you start a new terminal or command line shell.
```

:::

:::{tab-item} Windows (x64)

```{note}
Brightway runs natively on Windows (x64) systems, including Windows 7-11.
```

1. Create a new Conda environment (in this example named `bw`):

```
conda create -n bw -c cmutel brightway2 jupyterlab
```

2. Activate the environment:

```
conda activate bw
```

3. Install `pywin32`:

```
conda install pywin32
```

```{warning}
You will need to activate this environment every time you start a new terminal or command line shell.
```

:::

:::{tab-item} macOS (Apple Silicon/ARM)

```{note}
Brightway runs on the new Apple Silicon ARM architecture. However, the super-fast linear algebra software library `pypardiso` is not compatible with the ARM processor architecture. To avoid critical errors during instruction that would break core functionality, a different version of Brightway (`brightway_nosolver`) must be installed, which includes a different linear algebra software library (`scikit-umfpack`).
```

1. Create a new Conda environment (in this example named `bw`):

```
conda create -n bw -c cmutel -c conda-forge brightway2_nosolver jupyterlab scikit-umfpack
```

2. Activate the environment:

```
conda activate bw
```

```{warning}
You will need to activate this environment every time you start a new terminal or command line shell.
```

::::


# Upgrading Brightway

Brightway is being actively developed, with frequent new releases. To upgrade Brightway:

``` bash
conda update conda
conda update -c conda-forge brightway
```

```{toctree}
---
hidden:
maxdepth: 2
---
self
ui
cloud
upgrading
```