# Environment Management

## How do I save my conda environment for later use?

```{admonition} Prerequisites
:class: important
1. A working installation of [Conda](https://docs.conda.io/en/latest/)
2. Basic knowledge of the [command line shell](https://en.wikipedia.org/wiki/Shell_(computing)#Command-line_shells) on your operating system.
3. Basic knowledge of [Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
```

Perhaps you have already created a Conda environment that you would like to use at a later point (a year after your current LCA project is finished, for example). [You can save your environment to a file](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#exporting-an-environment-file-across-platforms) using the following shell command:

```{note}
Replace `<ENVIRONMENT_NAME>` with the name of the environment you want to save. \
Replace `<FILE_NAME>` with the name you want to give the file. \
Replace `<PATH_TO_FILE>` with the path to the file you want to save the environment to.
```

::::{tab-set}

:::{tab-item} Linux or macOS

```{note}
Brightway runs natively on Unix (x64) systems, including Linux distributions and macOS.
```

```bash
conda activate <ENVIRONMENT_NAME>
conda env export --from-history > <PATH_TO_FILE>/<FILE_NAME>.yml
```

:::

:::{tab-item} Windows (x64)

```bash
conda activate <ENVIRONMENT_NAME>
conda env export --from-history > "<PATH_TO_FILE>/<FILE_NAME>.yml"
```

:::

::::

This will create a file called `<FILE_NAME>.yml` at the location you specified. The `--from-history` flag ensures that only those packages are included that you installed into the environment (and not all their dependencies). You can then use this file to recreate the environment at a later point using the following command:

```{note}
Replace `<ENVIRONMENT_NAME>` with the name of the environment you want to restore.
```

```bash
conda env create -f <PATH_TO_FILE>/environment.yml
```