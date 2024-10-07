# Cheat Sheet

This section contains a basic list of all common Brightway commands.

```{admonition} Prerequisites
:class: important
1. A working [installation of Brightway](../installation/index.md).
2. Basic knowledge of [Python data types](https://docs.python.org/3/library/datatypes.html).
3. Basic understanding of matrix-based LCA data and calculations
```

All the commands below assume you have imported the Brightway core libraries:

````{admonition} Assumed imports
:class: important
```python
import bw2analyzer as ba
import bw2calc as bc
import bw2data as bd
import bw2io as bi
```
````

We will also use the convention that `'<replace_me>'` is a string which you need to change for your particular use case.

````{admonition} Recommended practice
Python is a flexible language, and there are many ways to do some of the following operations. We list below our *recommended* commands to execute these common tasks, and this is the interface we will try to keep compatible with future development. We therefore encourage using these patterns, even if you are used to something different.
````

## Table of Contents

```{toctree}
---
hidden:
maxdepth: 2
---
self
projects
databases
inventory
ia
lca
importing
```
