# Projects

````{admonition} Prerequisites
:class: important
```python
import bw2data as bd
```
````

A Brightway project is a self-contained set of data that can be used for life cycle assessment. Self-contained means that each project has a complete copy of all of its data, and that changes in one project do not propagate to other projects.

Projects need to be activated to be used; when you load `bw2data`, the `default` project is activated.

The current implementation of projects is a separate subdirectories on your local drive. However, this is an *implementation detail*, and could change in the future. We strongly you only interact with Brightway data through the defined interfaces.

```{admonition} Data Management
:class: seealso
[Data Management](../faq/data_management.md)
```

We strongly recommend creating "base projects" with original versions of whatever background data you want to use, and then copying that project and doing your own specific manipulations in the copy. Copying is relatively fast and it can be very convenient to not have to repeatedly install background databases.

## Managing projects

> How do I see the currently active project?

```python
bd.projects.current
```

> How do I activate a project?

```python
bd.projects.set_current(name='<project_name>')
```

> How do I copy the currently active project?

```python
bd.projects.copy_project(name='<new_project_name>')
```

> How do I delete a project?

```python
bd.projects.delete_project(name='<project_name>', delete_dir=True or False)
```

`delete_dir` will delete the project's data; if `False`, then we remove the project name from the list of project names, but you can still switch back to the project and use the saved data.

How do I list all my projects?

```python
sorted(bd.projects)
```

> How do I rename an existing project?

```python
bd.projects.rename("<new_project_name>")
```

## Archiving, restoring, and sharing projects

> How do I backup an existing project?

```python
bi.backup.backup_project_directory(
    project='<project_name>',
    dir_backup='<directory_path_for_backup>'
)
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2io.backup.backup_project_directory`
```

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

The archive format is OS-independent, so you can share project archives with your colleagues or friends.

## `bd.projects` API

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.project.ProjectManager`
```
