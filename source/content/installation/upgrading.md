# Updating and upgrading

## Updating Brightway libraries

Brightway is being actively developed, with frequent new releases. The update procedure varies slightly depending on whether you have installed Brightway using `pip`, `conda`, or `mamba`. In a terminal or command line shell *with your Brightway environment activated*, run one of the following:

```console
pip install -U brightway25
conda update -c conda-forge -c cmutel brightway25
mamba update -c conda-forge -c cmutel brightway25
```

```{warning}
Apple Silicon users should update `brightway25_nosolver`.
```

You can use the same syntax to update individual packages:

```console
pip install -U <my_cool_package>
```

## Upgrading from Brightway version 2

Individual projects can be migrate to Brightway version 2.5

``` python
import bw2data as bd

bd.projects.set_current('<project_name>')
bd.projects.migrate_project_25()
```
