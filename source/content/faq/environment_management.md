# Environment Management

## How do I save my conda environment for later use?

```{admonition} Prerequisites
:class: important
1. A working installation of [Conda](https://docs.conda.io/en/latest/)
2. Basic knowledge of [Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
```

Perhaps you have already created a Conda environment that you would like to use at a later point (a year after your current LCA project is finished, for example). [You can save your environment to a file using the following command](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#exporting-an-environment-file-across-platforms):

```{note}
Replace `<ENVIRONMENT_NAME>` with the name of the environment you want to save. \
Replace <PATH_TO_FILE> with the path to the file you want to save the environment to.
```

```bash
conda activate <ENVIRONMENT_NAME>
conda export --from-history <PATH_TO_FILE>/environment.yml
```

This will create a file called `environment.yml` at the location you specified. The `--from-history` flag ensures that only those packages are included that you installed into the environment (and not all their dependencies). You can then use this file to recreate the environment at a later point using the following command:

```{note}
Replace `<ENVIRONMENT_NAME>` with the name of the environment you want to save.
```

```bash
conda env create -f <PATH_TO_FILE>/environment.yml
```
