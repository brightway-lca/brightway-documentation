# Upgrading

```{admonition} Prerequisites
1. A working installation of [Conda](https://docs.conda.io/en/latest/)
2. Basic knowledge of [Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
3. Basic knowledge of [the difference between `brightway`, `brightway2` and `brightway25`](../faq/brightway.md)
```

## Upgrading from Version 1

Upgrading from version 1 requires a full export of your data objects, and reimporting them after upgrading the software.

1.  First export your databases and methods into Brightway packages:

``` python
from bw2data import *
from bw2data.io import BW2Package

for index, name in enumerate(databases):
    BW2Package.export_obj(Database(name), "db-{}".format(index), "upgrade")

for index, name in enumerate(methods):
    BW2Package.export_obj(Method(name), "lcia-{}".format(index), "upgrade")

# Add in any other objects you want to export here

# Might have to remove parenthese around print statement
print("Your exported objects are here:", config.request_dir("upgrade"))
```

2.  Upgrade your software following the [setup guide](./setup.md).
3.  Each data directory would now be a new project. You can import the objects you exported earlier like this:

``` python
from brightway2 import *
import os

preferences['allow incomplete imports'] = True

filepath = "path that was printed earlier in section 1"
projects.current = "name of this project"

for filename in sorted(os.listdir(filepath)):
    print(filename)
    BW2Package.import_file(os.path.join(filepath, filename))
```

You will need to do this for each data directory you want to upgrade.

## Upgrading from Version 2

```{note}
`<project_name>` is the name of the project you want to upgrade. You can find the name of your project by running `bw2data.projects.current`.
```

``` python
from bw2data import *

bw2data.projects.set_current('<project_name>')
bw2data.projects.migrate_project_25()
```