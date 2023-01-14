# Data Management

## Where is my data saved?

You can find the current project data directory with the command `projects.dir`. Everything is stored in this folder or a subdirectory. Similarly, you can find the logs directory with the command `projects.logs_dir`. Brightway uses the `appdirs` library to select an appropriate, platform-specific path, namely:



::::{tab-set}

:::{tab-item} Windows

```
C:\Documents and Settings\<User>\Application Data\Local Settings\pylca\Brightway2
```
:::

:::{tab-item} macOS

```
/Users/<User>/Library/Application Support/Brightway2
```

:::

:::{tab-item} Linux

```
/home/<User>/.local/share/Brightway2
```

:::

::::


## How do I change the location of my data directory?

You can specify a custom data directory path by setting the environment variable `BRIGHTWAY2_DIR`. Brightway will raise an `OSError` if this is not a writable directory.

```{warning}
This is not recommended for use by beginners, but if you have multiple or non-standard installations of Brightway it might be useful.
```

::::{tab-set}

:::{tab-item} Unix (Z Shell)

To change the storage location of Brightway data to a directory of your choice, set an environment variable in the default shell of your Unix system. 

```{note}
Replace \<PATH\> with your desired absolute directory path and restart the shell.
```

```
echo 'export BRIGHTWAY2_DIR=<PATH>' >> ~/.zshenv
```

:::

:::{tab-item} Windows (Power Shell)

To change the storage location of Brightway data to a directory of your choice, set an environment variable using the Windows Power Shell.

```{note}
Replace \<PATH\> with your desired absolute directory path and restart the shell.
```

```
[Environment]::SetEnvironmentVariable("BRIGHTWAY2_DIR", "<PATH>", "User")
```

:::

::::

## How do I backup my data?

Each project is just a subdirectory, and this can be backed up using any normal tools, including cloud backups like Dropbox. You can save a snapshot of entire project directory with `backup_data_directory`, or save a single project with `backup_project_directory`. Both functions return the filepath of the created archive file.
