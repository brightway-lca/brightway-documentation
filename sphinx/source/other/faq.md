# FAQ

## Data Management

### Where is my data saved?

You can find the current project data directory with the command `projects.dir`. Everything is stored in this folder or a subdirectory. Similarly, you can find the logs directory with the command `projects.logs_dir`. Brightway uses the `appdirs` library to select an appropriate, platform-specific path, namely:

```{eval-rst}
.. tabs::

    .. tab:: Linux

        .. code-block::
            :caption: Brightway default data storage location

            C:\Documents and Settings\<User>\Application Data\Local Settings\pylca\Brightway2

    .. tab:: macOS

        .. code-block::
            :caption: Brightway default data storage location

            /Users/<User>/Library/Application Support/Brightway2
    
    .. tab:: Windows

        .. code-block::
            :caption: Brightway default data storage location

            /home/<User>/.local/share/Brightway2
```

### How do I change the location of my data directory?

You can specify a custom data directory path by setting the environment variable `BRIGHTWAY2_DIR`. Brightway will raise an `OSError` if this is not a writable directory.

```{warning}
This is not recommended for use by beginners, but if you have multiple or non-standard installations of Brightway it might be useful.
```

```{eval-rst}
.. tabs::

    .. tab:: Unix (Z Shell)

        To change the storage location of Brightway data to a directory of your choice, set an environment variable in the default shell of your Unix system. 

        .. code-block::
            :caption: replace <PATH> with your desired absolute directory path and restart the shell

            echo 'export BRIGHTWAY2_DIR=<PATH>' >> ~/.zshenv
    
    .. tab:: Windows (Power Shell)

        To change the storage location of Brightway data to a directory of your choice, set an environment variable using the Windows Power Shell.

        .. code-block::
            :caption: replace <PATH> with your desired absolute directory path

            [Environment]::SetEnvironmentVariable("BRIGHTWAY2_DIR", "<PATH>", "User")
```

### How do I backup my data?

Each project is just a subdirectory, and this can be backed up using any normal tools, including cloud backups like Dropbox. You can save a snapshot of entire project directory with `backup_data_directory`, or save a single project with `backup_project_directory`. Both functions return the filepath of the created archive file.

## Ecoinvent Import

### Which `Ecoinvent` file should I download?

Ecoinvent makes several versions of each system model available. For instance:

```
ecoinvent 3.3_xxx_ecoSpold02.7z
ecoinvent 3.3_xxx_lci_ecoSpold02.7z
ecoinvent 3.3_xxx_lcia_ecoSpold02.7z
ecoinvent 3.3_xxx_lcia-cumulated-matrices_xls.7z
ecoinvent 3.3_xxx_lci-cumulated-matrices_xls.7z
```

You want to download and import `ecoinvent 3.3_xxx_ecoSpold02.7z`. If your import process is taking a long time or a lot of memory, double check to make sure you have the right version.

## Brightway Versions and Compatibility

## Brightway2 vs. Brightway25

> Brightway 2.5 is the next generation of the [Brightway2](https://brightway.dev/) framework for life cycle assessment. It provides new capabilities for cloud computing and model interaction, with the use of a new [processed data library](https://github.com/brightway-lca/bw_processing) and a separation between the calculation library and a library for [matrix construction and manipulation](https://github.com/brightway-lca/matrix_utils).

-- from the [Brightway 2.5 repository readme file](https://github.com/brightway-lca/brightway25)

Brightway 2.5 is the next step on the way a future Brightway version, as detailed in the [Brightway Strategic Development Plan](https://github.com/brightway-lca/enhancement-proposals/blob/main/Brightway%20strategic%20development%20plan.md). In practice, this means that the meta-packages `brightway-lca/brightway2` and `brightway-lca/brightway25` will install different versions of the Brightway packages. For instance:

| package | Brightway 2 version | Brightway 2.5 version |
| ------- | ------------------- | --------------------- |
| `bw2analyzer` | < 0.10.99 | >= 0.11.1 |
| `bw2calc` | < 1.8.1 | >= 2.0.dev5 |
| `bw2data` | < 3.99 | >= 4.0.dev11 |
| `bw2io` | < 0.8.9 | >= 0.9.dev6 |

This is specified in the respective `setup.py` files: [Brightway2 packages](https://github.com/brightway-lca/brightway25/blob/main/setup.py) and [Brightway2.5 packages](https://github.com/brightway-lca/brightway2/blob/master/setup.py).