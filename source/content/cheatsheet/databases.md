# Databases 

## Basic Operations

### How do I list all databases?

```python
sorted(bd.databases)
```

### How do I test if a given database is installed?

```python
'<my database label>' in bd.databases
```

### How do I instantiate a `Database` object?

```python
my_db = bd.Database('<database_name>')
```

### How do I copy a `Database`?

```python
copied_database = bd.Database('<database_name>').copy('<new_name>')
```

### How do I rename a `Database`?

```python
new_database = bd.Database('<database_name>').rename('<new_name>')
```

### How do I delete a `Database`?

```python
del bd.databases['<database_name>']
```

## Metadata

### How do I see the `Database` metadata?

```python
bd.Database('<database_name>').metadata
```

### How do I change the `Database` metadata?

```python
bd.Database('<database_name>').metadata['<some_key>'] = '<some_value>'
```

### How do I see which other databases this `Database` refers to?

```python
bd.Database('<database_name>').metadata['depends']
```

### How can I see what kind of modelling paradigm and storage engine a `Database` uses?

This information is given to a limited degree by the database backend:

```python
bd.Database('<database_name>').metadata['backend']
```

There are three backends in a normal Brightway installation:

* `sqlite`: The default backend. Uses SQLite like a graph database.
* `iotable`: Uses the SQLite database for nodes, but stores edges only in datapackages. Limits edges to a single numerical value without uncertainty, but gives better performance for large IO data.
* `multifunctional`: Stores `multifunctional` processes as a custom node type, and automatically allocates following the given database or process preferences when creating datapackages.

## Searching

### How do I search a `Database`?

```python
bd.Database('<database_name>').search('<my_query_string>')
```

See {py:obj}`bw2data.backends.base.SQLiteBackend.search` for documentation and function options.

## Datapackages

### How do I get the `bw_processing` datapackage for this `Database`?

```python
bd.Database('<database_name>').datapackage()
```
