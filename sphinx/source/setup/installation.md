# Installation

Brightway is a Python software package. It can be installed using the [Python package installer `pip`](https://pypi.org/project/pip/) or the [multi-language package management system `conda`](https://docs.conda.io/en/latest/). This guide uses `conda`.

```{note}
Brightway supports Python 2 and 3 (>3.4). However, we recommend you use Python 3. 
```

## Quickstart

```{admonition} Prerequisites
1. a working installation of [Conda](https://docs.conda.io/en/latest/)
2. basic knowledge of [Conda environments]((https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html))
```

```{eval-rst}
.. tabs::

    .. tab:: Unix (x64)

        .. NOTE::

            Brightway runs natively on Unix (x64) systems, including Ubuntu and macOS.

        1. Create a new Conda environment (in this example named :code:`bw`):

        .. code-block::

            conda create -n bw -c conda-forge brightway2 jupyterlab

        2.  Activate the environment:

        .. code-block::
            
            conda activate bw

        .. WARNING::

            You will need to activate this environment every time you start a new terminal or command line shell.

    .. tab:: Windows (x64)

        .. NOTE::

            Brightway runs natively on Windows (x64) systems, including Windows 7-11.

        1. Create a new Conda environment (in this example named :code:`bw`):

        .. code-block::

            conda create -n bw -c conda-forge brightway2 jupyterlab

        2.  Activate the environment:

        .. code-block::
            
            conda activate bw

        3. Install :code:`pywin32`:

        .. code-block::
        
            conda install pywin32

        .. WARNING::

            You will need to activate this environment every time you start a new terminal or command line shell.

    .. tab:: macOS (M1/ARM)

        .. NOTE::

            Brightway run on the new M1 ARM architecture. However, the super-fast linear algebra software library :code:`pypardiso` is not compatible with the M1 ARM architecture. To avoid critical errors during instruction that would break core functionality, a different version of Brightway (:code:`brightway_nosolver`) must be installed, which includes a different linear algebra software library (:code:`scikit-umfpack`):

        1. Create a new Conda environment (in this example named :code:`bw`):

        .. code-block::

            conda create -n bw -c cmutel -c conda-forge brightway2_nosolver jupyterlab scikit-umfpack

        2.  Activate the environment:

        .. code-block::
            
            conda activate bw

        .. WARNING::

            You will need to activate this environment every time you start a new terminal or command line shell.

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