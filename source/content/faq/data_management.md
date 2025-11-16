# Data Management

## Where is my data saved?

You can find the current project data directory with the command `projects.dir`. Everything is stored in this folder or a subdirectory. Similarly, you can find the logs directory with the command `projects.logs_dir`. Brightway uses a Python library to select an appropriate, platform-specific path, namely:

::::{tab-set}

:::{tab-item} Windows

```
C:\Users\<User>\AppData\Local\pylca\Brightway3
```
For current user:
```
%LocalAppData%\pylca\Brightway3
```

:::

:::{tab-item} macOS

```
/Users/<User>/Library/Application Support/Brightway3
```
For current user:
```
~/Library/Application Support/Brightway3
```

:::

:::{tab-item} Linux

```
/home/<User>/.local/share/Brightway3
```
For current user:
```
~/.local/share/Brightway3
```

:::

::::

(BRIGHTWAY2_DIR)=
## How do I change my data directory?

You can specify a custom data directory path by setting the environment variable `BRIGHTWAY2_DIR`. Brightway will raise an `OSError` if this is not a writable directory.

```{warning}
This is not recommended for use by beginners, but if you have multiple or non-standard installations of Brightway it might be useful.
```

::::{tab-set}

:::{tab-item} Unix (Z Shell)

To change the storage location of Brightway data to a directory of your choice, set an environment variable in the default shell of your Unix system. 

```{note}
Replace `<PATH>` with your desired absolute directory path and restart the shell.
```

```
echo 'export BRIGHTWAY2_DIR=<PATH>' >> ~/.zshenv
```

:::

:::{tab-item} Windows (Power Shell)

To change the storage location of Brightway data to a directory of your choice, set an environment variable using the Windows Power Shell.

```{note}
Replace `<PATH>` with your desired absolute directory path and restart the shell.
```

```
[Environment]::SetEnvironmentVariable("BRIGHTWAY2_DIR", "<PATH>", "User")
```

:::

::::

## How do I change my data directory in a Conda environment?

When you create a [Conda environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#managing-environments), it lives in a directory located at:

```<YOUR_ANACONDA_INSTALL_DIR>/envs/<YOUR_ENV_NAME>```

When Conda activates or deactivates an environment, it looks for additional scripts in the two subfolders `etc/conda/activate.d` and `etc/conda/deactivate.d` _within this directory_. To set persistent environment variables [(like `BRIGHTWAY2_DIR`)](BRIGHTWAY2_DIR) in your Conda environment:

::::{tab-set}

:::{tab-item} Unix (Z Shell)


1. Navigate to your Conda environment directory:

```bash
cd <YOUR_ANACONDA_INSTALL_DIR>/envs/<YOUR_ENV_NAME>
```

2. If not already present, create two directories `etc/conda/activate.d` and `etc/conda/deactivate.d`

```bash
mkdir -p etc/conda/activate.d
mkdir -p etc/conda/deactivate.d
```

4. Create scripts in the folders that _set_ and _unset_ the environment variables (in this case `BRIGHTWAY2_DIR`). The names of the files don't matter, but the file extensions do. Inside the folder `activate.d` create the file `<WHATEVER_NAME_YOU_LIKE.sh` and inside it write `export BRIGHTWAY2_DIR=<YOUR_NEW_DIR_PATH>`. Inside the folder `deactivate.d` create the file `<WHATEVER_NAME_YOU_LIKE.sh` and inside it write `unset BRIGHTWAY2_DIR`.

The scripts should look like this:
In the `activate.d`:

```bash
#!/bin/sh
export BRIGHTWAY2_DIR="<YOUR_NEW_DIR_PATH>"
```

In the `deactivate.d`:

```bash
#!/bin/sh
unset BRIGHTWAY2_DIR
```

5. Make sure both scripts are executable by running:

```bash
chmod +x etc/conda/activate.d/<WHATEVER_NAME_YOU_LIKE>.sh
chmod +x etc/conda/deactivate.d/<WHATEVER_NAME_YOU_LIKE>.sh
```

:::

:::{tab-item} Windows (Power Shell)

1. Navigate to your Conda environment directory:

```bash
cd <YOUR_ANACONDA_INSTALL_DIR>/envs/<YOUR_ENV_NAME>
```

2. If not already present, create two directories `etc/conda/activate.d` and `etc/conda/deactivate.d`

3. Create scripts in the folders that set and unset the environment variables (in this case `BRIGHTWAY2_DIR`). The names of the files don't matter, but the file extensions do. Inside the folder `activate.d` create the file `<WHATEVER_NAME_YOU_LIKE.bat` and inside it write `export BRIGHTWAY2_DIR=<YOUR_NEW_DIR_PATH>`. Inside the folder `deactivate.d` create the file `<WHATEVER_NAME_YOU_LIKE.bat` and inside it write `BRIGHTWAY2_DIR=`.

:::

::::

## How do I backup my data?

Each project is just a subdirectory, and this can be backed up using any normal tools, including cloud backups like Dropbox. You can save a snapshot of entire project directory with `backup_data_directory`, or save a single project with `backup_project_directory`. Both functions return the filepath of the created archive file.
