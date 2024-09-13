# Cheat sheet

This section contains a basic list of all common Brightway commands.

```{admonition} Prerequisites
:class: important
1. A working [installation of Brightway](../installation/index.md).
2. Basic knowledge of [Python data types](https://docs.python.org/3/library/datatypes.html).
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

````{admonition} Assumed imports
Python is a flexible language, and there are many ways to do some of the following operations. We list below our *recommended* commands to execute these common tasks, and this is the interface we will try to keep compatible with future development. We therefore encourage using these patterns, even if you are used to something different.
````

## Projects

### Project activation and manipulation

How do I see the currently active project?

```python
bd.projects.current
```

How do I activate a project?

```python
bd.projects.set_current(name='<project_name>')
```

How do I copy the currently active project?

```python
bd.projects.copy_project(name='<new_project_name>')
```

How do I delete a project?

```python
bd.projects.delete_project(name='<project_name>', delete_dir=True or False)
```

`delete_dir` will delete the project's data; if `False`, then we remove the project name from the list of project names, but you can still switch back to the project and use the saved data.

How do I list all my projects?

```python
sorted(bd.projects)
```

How do I rename an existing project?

```python
bd.projects.rename("<new_project_name>")
```

### Creating initial project data

How do I create a new project with basic data on elementary flows and LCIA?

Before project creation, run:

```python
bi.remote.install_project('<project_tag>', '<my_desired_project_name>')
```

Where `<project_tag>` is one of:

* 'ecoinvent-3.10-biosphere'
* 'ecoinvent-3.8-biosphere'
* 'ecoinvent-3.9.1-biosphere'
* 'forwast'
* 'USEEIO-1.1'

We welcome the contribution of other taxonomies and data systems!

```{admonition} Prerequisites
:class: important
The setup function `bw2setup()` is deprecated and should no longer be used.
```

### Archiving, restoring, and sharing projects

How do I backup an existing project ({py:obj}`bw2io.backup.backup_project_directory`)?

```python
bi.backup.backup_project_directory(
    project='<project_name>',
    dir_backup='<directory_path_for_backup>'
)
```

How do I restore a project from a backup? ({py:obj}`bw2io.backup.restore_project_directory`)

```python
bi.backup.restore_project_directory(
    fp='<path_to_backup>',
    project_name='<project_name>'
)
```

## Databases

How do I list all databases? ({py:obj}`bw2data.meta.Databases`)

```python
sorted(bd.databases)
```

How do I instantiate a `Database` object?

```python
my_db = bd.Database('<database_name>')
```

How do I copy a `Database`?

```python
copied_database = bd.Database('<database_name>').copy('<new_name>')
```

How do I rename a `Database`?

```python
new_database = bd.Database('<database_name>').rename('<new_name>')
```

How do I delete a `Database`?

```python
del bd.databases['<database_name>']
```

### Metadata

How do I see the `Database` metadata?

```python
bd.Database('<database_name>').metadata
```

How do I change the `Database` metadata?

```python
bd.Database('<database_name>').metadata['<some_key>'] = '<some_value>'
```

How do I see which other databases this `Database` refers to?

```python
bd.Database('<database_name>').metadata['depends']
```

How can I see what kind of modelling paradigm and storage engine a `Database` uses?

```python
bd.Database('<database_name>').metadata['backend']
```

### Searching

How do I search a `Database`?

```python
bd.Database('<database_name>').search('<my_query_string>')
```

### Datapackage

How do I get the datapackage for this `Database`?

```python
bd.Database('<database_name>').datapackage()
```

## Node and Edge Graph Objects

### Nodes

How do I iterate over nodes in a `Database`?

```python
for node in bd.Database('<database_name>'):
    do_something(node)
```

Iteration over nodes is helpful for complicated filter cases:

```python
[
    node for node in bd.Database('<database_name>')
    if 'electricity production' in node['name']
    and 'coal' in node['name']
    and node['location'].lower() == 'de'
]
```

How do I get a random node from a `Database`?

```python
bd.Database('<database_name>').random()
```

How do I get a specific node?

```python
my_node = bd.get_node(my_attr="<some_value>")
```

You can pass in any attribute value, including "database" and "code". Combine multiple filters with commas, e.g. `bd.get_node(name="<foo>", location="bar")`. To search for attribute keys with spaces, use a dictionary: `bd.get_node(**{"some value with spaces": True})`.

How do I get all the `Node` data as a dictionary?

```python
my_node.as_dict()
```

How do I create a new node?

```python
my_node = bd.Database('<database_name>').new_node(**attributes)
my_node.save()
```

Where `attributes` is a dictionary of the desired node attributes.

### Edges
