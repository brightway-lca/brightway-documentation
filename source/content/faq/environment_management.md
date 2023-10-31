# Environment Management

## How do I save my conda environment for later use?

```{admonition} Prerequisites
:class: important
1. A working installation of [Conda](https://docs.conda.io/en/latest/)
2. Basic knowledge of [Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
```

Perhaps you have already created a Conda environment that you would like to use at a later point (a year after your current LCA project is finished, for example). You can save your environment to a file using the following command:

```{note}
Replace `<ENVIRONMENT_NAME>` with the name of the environment you want to save.
```

```bash
conda list -n <ENVIRONMENT_NAME> --export > ./environment.yml
```

This will create a file called `environment.yml` in your current working directory. You can then use this file to recreate the environment at a later point using the following command:

```bash
conda env create -f environment.yml
```
