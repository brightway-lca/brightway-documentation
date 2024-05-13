# Getting Started

## Setup

### Import Python Packages

Which Python packages do I have to import?

```{note}
`brightway2` is a metapackage. It just loads other Brightway packages like `bw2data`, `bw2calc`, `bw2io`, etc.
It is recommended to import the individual packages directly. That way, you can see where each function comes from.
```

```python
import bw2analyzer as ba
import bw2calc as bc
import bw2data as bd
```

You may also want to import some of the most important data science packages:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

## Project Management

### Manage Projects

How do I manage my projects?

```python
bd.project.ProjectManager()
```

````{note}
For your convenience, Brightway also provides a shorthand way of calling the project manager:

```python
bp.projects
```

````


```{admonition} API Documentation
:class: note
{py:obj}`bw2data.project.ProjectManager`
```

### List Projects

How do I list all projects?

```python
list(bp.projects)
```

```{admonition} API Documentation
:class: note
{py:obj}`bw2data.project.ProjectManager`
```

### Project Locations

How do I find where my projects are stored on disk?

```python
bp.projects.dir
bp.projects.logs_dir
bp.projects.output_dir
```

```{admonition} API Documentation
:class: note
{py:obj}`bw2data.project.ProjectManager`
```

### Rename Project

How do I rename an existing project?

```{note}
You can not _just_ rename an existing project. You must copy the project to a new name and then switch to the new project.
Then, you can delete the old project.
```

```python
bd.projects.copy_project(<new_project_name>, switch=True)
bd.projects.delete_project(name=<old_project_name>, delete_dir=True)
```

```{admonition} API Documentation
:class: note
{py:obj}`bw2data.project.ProjectManager.copy_project` \
{py:obj}`bw2data.project.ProjectManager.delete_project`
```

### Delete Project

How do I delete an existing project?

```python
bd.projects.delete_project(<project_name>, delete_dir=True)
```

```{admonition} API Documentation
:class: note
{py:obj}`bw2data.project.ProjectManager.delete_project`
```