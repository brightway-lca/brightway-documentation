# Databases

````{admonition} Prerequisites
:class: important
```python
import bw2analyzer as ba
import bw2calc as bc
import bw2data as bd
import bw2io as bi
```
````

## Manage Databases

> How do I manage my databases?

```python
bd.meta.Databases()
```

````{note}
For your convenience, Brightway also provides a shorthand way 
of calling the dictionary of database metadata:

```python
bd.databases
```

````


```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.meta.Databases`
```

## List Databases

How do I list all databases?

```python
list(bd.databases)
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.meta.Databases`
```

## Delete Database

> How do I delete a database?

The {py:obj}`bw2data.meta.Databases` object is a kind of [Python dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries). 
You can therefore delete a database by using the `del` keyword:

```python
del bd.databases['<database_name>']
```

## Rename Database

> How do I rename an existing database?

The {py:obj}`bw2data.meta.Databases` object is a kind of [Python dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries). 
You can therefore rename a database (the `key` of the dictionary) by:

```python
bd.databases['<new_database_name>'] = bd.databases.pop('<old_database_name>')
```

## Import Example Data

> How can I import some example data?

A small example database is shipped directly with `bw2io`. It is located at: \
[`bw2io/data/examples/sample_parameterized_database.xlsx`](https://github.com/brightway-lca/brightway2-io/blob/main/bw2io/data/examples/sample_parameterized_database.xlsx). \
You can import it with:

```python
bi.add_example_database(searchable=True)
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2io.data.add_example_database`
```

More databases are provided by the `files.brightway.dev` fileserver. 
They can be downloaded using `bw2io`. You can list the available databases with:

```python
bi.remote.PROJECTS_BW25
```

Currently, the Ecoinvent biosphere database and the USEEIO database are available 
for download:

```
{
    'ecoinvent-3.8-biosphere': 'ecoinvent-3.8-biosphere.tar.gz',
    'ecoinvent-3.9.1-biosphere': 'ecoinvent-3.9.1-biosphere.tar.gz',
    'USEEIO-1.1': 'USEEIO-1.1.tar.gz'
}
```

For instance, you can now load the USEEIO database with `bw2io`:


```python
bi.install_project(project_key="USEEIO-1.1")
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2io.remote.install_project`
```

## Import Your Own Data

> How can I import my own data (from an Excel sheet)?

```python
importer = bi.ExcelImporter(filepath='<file_path>')
importer.apply_strategies()
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2io.importers.ExcelImporter`
```

You need to link the exchanges of your inventories to supplying activities.
First, you may start by checking if some exchanges are supplied by activities in
the database you are trying to import:

```python
importer.match_database(
    fields=('name', 'reference product', 'unit', 'location')
)
importer.statistics()
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2io.importers.base_lci.LCIImporter.match_database`
```

Using the fields `('name', 'reference product', 'unit', 'location')` is a good combination
of fields to ensure that the matching is done correctly.

`importer.statistics()` will give you a summary of the matching process.

You must now determine all unlinked flows.

```python
list(importer.unlinked)
```

If the number of unlinked flows isn't zero, some exchanges are either 
linking to other databases (e.g., the biosphere database, ecoinvent) 
or are ill-defined.

Let's try to see if we can link up the unlinked flows to the ecoinvent database:

```python
importer.match_database(
    db_name='<ecoinvent_database_name>',
    fields=('name', 'reference product', 'unit', 'location')
)
importer.statistics()
```

If you still have unlinked flows, you can try to link them to the biosphere database:

```python
importer.match_database(
    db_name='<biosphere_database_name>',
    fields=('name', 'categories', 'unit',)
)
importer.statistics()
```

Note that this time, we change the fields we want a match on to `('name', 'categories', 'unit',)`.


````{note}
Normally, you __must__ find the errors causing unliked flows. \
Usually those are typos, wrong geographies/databases etc.
````

If you __are sure__ that you do not need unlinked flows, you can drop them:

```python
importer.drop_unlinked(i_am_reckless=True)
```

But if the remaining unlinked exchanges are correct, but are simply non-existent in 
the databases of your project (e.g., an elementary flow representing a noise emission),
you can add them into a separate database.

For the unlinked technosphere flows:

```python
importer.add_unlinked_activities()
```

For the unlinked biosphere flows:

```python
importer.add_unlinked_flows_to_biosphere_database()
```

Finally, you can write the database to your project:

```python
importer.write_database()
```

```{admonition} API Documentation

## Import Ecoinvent Data

### Ecoinvent Import (Automatic)

> How do I import the [Ecoinvent](https://ecoinvent.org) database?

You can use the ✨new✨ automatic import function to download and import the latest version of the Ecoinvent database.

```{warning}
__DO NOT__ run `bw2setup` before using this function! \
It is not needed and will cause broken results.
```

```python
bi.import_ecoinvent_release(
    version='<version_number>',
    system_model='<system_model>',
    ecoinvent_user='<ecoinvent_user_name>',
    ecoinvent_password='<ecoinvent_password>'
)
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2io.ecoinvent.import_ecoinvent_release`
```

### Ecoinvent Import (Manual)

> How do I import the [Ecoinvent](https://ecoinvent.org) database?

You can also download and import the database manually. First, you must create the biosphere 

```python
bi.bw2setup()
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2io.bw2setup`
```

```python
importer = bi.SingleOutputEcospold2Importer(
    dirpath='<ecoinvent_database_zip_file>',
    dbname='<database_name>'
)
importer.apply_strategies()
importer.statistics()
```
If you have no unlinked exchanges, you can now write the database to your project:

```python
if len(list(importer.unlinked) == 0):
    importer.write_database()
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2io.importers.ecospold2.SingleOutputEcospold2Importer`
```



