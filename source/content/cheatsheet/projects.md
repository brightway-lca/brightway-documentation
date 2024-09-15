## Projects

### Project Activation and Manipulation

**Q:** How do I see the currently active project?

```python
bd.projects.current
```

**Q:** How do I activate a project?

```python
bd.projects.set_current(name='<project_name>')
```

**Q:** How do I copy the currently active project?

```python
bd.projects.copy_project(name='<new_project_name>')
```

**Q:** How do I delete a project?

```python
bd.projects.delete_project(name='<project_name>', delete_dir=True or False)
```

`delete_dir` will delete the project's data; if `False`, then we remove the project name from the list of project names, but you can still switch back to the project and use the saved data.

**Q:** How do I list all my projects?

```python
sorted(bd.projects)
```

**Q:** How do I rename an existing project?

```python
bd.projects.rename("<new_project_name>")
```

(initial-project-data)=
### Creating Initial Project Data

**Q:** How do I create a new project with basic data on elementary flows and LCIA?

To create a new project with some basic data:

```python
bi.remote.install_project('<project_tag>', '<my_desired_project_name>')
```

Where `<project_tag>` is one of:

* ecoinvent-3.10-biosphere
* ecoinvent-3.8-biosphere
* ecoinvent-3.9.1-biosphere
* forwast
* USEEIO-1.1

The ecoinvent biosphere projects also include LCIA impact categories.

We welcome the contribution of other taxonomies and data!

```{warning}
:class: important
The setup function `bw2setup()` is deprecated and should no longer be used.
```

### Archiving, Restoring, and Sharing Projects

**Q:** How do I backup an existing project?

```python
bi.backup.backup_project_directory(
    project='<project_name>',
    dir_backup='<directory_path_for_backup>'
)
```

See {py:obj}`bw2io.backup.backup_project_directory` for more information.

**Q:** How do I restore a project from a backup?

```python
bi.backup.restore_project_directory(
    fp='<path_to_backup>',
    project_name='<project_name>'
)
```

See {py:obj}`bw2io.backup.restore_project_directory` for more information and customization options.
