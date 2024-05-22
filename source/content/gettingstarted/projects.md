# Projects

````{admonition} Prerequisites
:class: important
```python
import bw2analyzer as ba
import bw2calc as bc
import bw2data as bd
import bw2io as bi
```
````

## Manage Projects

> How do I manage my projects?

```python
bd.project.ProjectManager()
```

````{note}
For your convenience, Brightway also provides a shorthand way of calling the project manager:

```python
bd.projects
```
````

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.project.ProjectManager`
```

## List Projects

How do I list all projects?

```python
list(bd.projects)
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.project.ProjectManager`
```

## Select Project

> How do I select a project?

```python
bd.projects.set_current(name='<project_name>')
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.project.ProjectManager.set_current`
```

## Project Locations

> How do I find where my projects are stored on disk?

```python
bd.projects.dir
bd.projects.logs_dir
bd.projects.output_dir
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.project.ProjectManager`
```

## Rename Project

> How do I rename an existing project?

```{note}
You can not _just_ rename an existing project. You must copy the project to a new name and then switch to the new project.
Then, you can delete the old project.
```

```python
bd.projects.copy_project(<new_project_name>, switch=True)
bd.projects.delete_project(name=<old_project_name>, delete_dir=True)
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.project.ProjectManager.copy_project` \
{py:obj}`bw2data.project.ProjectManager.delete_project`
```

## Backup Project

> How do I backup an existing project? \
> How do I save a project to disk?

```python
bd.backup.backup_project_directory(
    project='<project_name>',
    dir_backup='<target_location_for_backup>'
)
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2io.backup.backup_project_directory`
```

## Restore Project

> How do I restore a project from a backup?

```python
bi.backup.restore_project_directory(
    fp='<path_to_backup>',
    project_name='<project_name>'
)
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2io.backup.restore_project_directory`
```

## Delete Project

> How do I delete an existing project?

```python
bd.projects.delete_project(<project_name>, delete_dir=True)
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.project.ProjectManager.delete_project`
```