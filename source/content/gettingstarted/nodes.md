# Nodes (Activities and Flows)

````{admonition} Prerequisites
:class: important

```{admonition} Brightway Documentation
:class: seealso
[Brightway Structure Page](../theory/structure.md) \
[Glossary](glossary)
```

```python
import bw2analyzer as ba
import bw2calc as bc
import bw2data as bd
import bw2io as bi
```

You can also [load an example database](./databases.md) to get started:

```python
bi.add_example_database()
my_database = bd.Database('Mobility example')
my_biosphere = bd.Database('biosphere3')
my_methods = bd.methods
```
````

## Node Management

In Brightway, _technosphere activities_ and _biosphere flows_ are organized by the `Database` function.

```python
my_database = bd.Database('<database_name>')
my_biosphere = bd.Database('biosphere3')
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.database.DatabaseChooser`, alias for the `Database` function \
{py:obj}`bw2data.backends.base.SQLiteBackend`, the data type of the databases
```

(node-selection)=
## Node Selection

> How do I select (=search for) an activity from the technosphere database? \
> How do I select (=search for) a biosphere flow from the biosphere database? 

You can use the `search` function to find and return a list of objects that match your search term:

```python
my_database.search('<search_term>')
my_biosphere.search('<search_term>')
```

This will return a list of objects that match your search term.

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.backends.base.SQLiteBackend.search` \
{py:obj}`bw2data.backends.proxies.Activity`, the data type of an activity/flow object
```

You can also use a [list comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) to iterate over the objects in the database. This can be used to build lists of activities from complex search parameters. For example:

```python
list_german_coal_activities = [
    activity for activity in my_database
    if 'electricity production' in activity['name']    
    and 'coal' in activity['name']   
    and activity['location'] == 'DE'
]
```

The same can be achieved by using the `get_node` function. Note that here, the arguments must be exact matches:

```python
list_activities = bd.utils.get_node(
    database = '<database_name>',
    name = '<exact_name>',
    location = '<exact_location>'
)
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.utils.get_node`
```

````{note}
🎲 You can also _randomly_ select an object from a database:

```python
random_activity = my_database.random()
random_biosphere_flow = my_biosphere.random()
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.backends.base.SQLiteBackend.random`
```
````

## Node Properties

> How do I list the properties of an activity? \
> How do I list the properties of a biosphere flow?

```{note}
Activities and biosphere flows are {py:obj}`bw2data.backends.proxies.Activity` objects. \
These are based on Python [`mappings`](https://docs.python.org/3/glossary.html#term-mapping), which are similar to `dict`s.
```

In order to list the properties of an activity or biosphere flow, you can use the `as_dict` method, which turns the object into a real Python dictionary:

```python
my_database.random().as_dict() 
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.backends.proxies.Activity` \
{py:obj}`bw2data.proxies.ProxyBase.as_dict`
```

## Specific Searches

> How can I list the different (searchable) metadata fields of an activity? \
> How can I list the different (searchable) metadata fields of a biosphere flow?

[As we have seen above](#object-properties), activities and biosphere flows are similar to Python dictionaries. We can therefore quickly check which metadata fields are available for search:

```python
list(my_database.random().as_dict().keys())
```

We can also quickly list all unique values for a given metadata field, for example the `categories` field of all activities in a database:

```python
set(list(activity.as_dict()['categories'] for activity in my_database))
```

```note
The {py:obj}`bw2data.backends.base.SQLiteBackend.search` function allows for more specific search queries through its keyword arguments. These include `limit`, `filter`, mask`, etc.
```

## Inspecting Exchanges

> How do I list the technosphere exchanges and biosphere exchanges of an activity?

```python
list(my_activity.technosphere())
list(my_activity.biosphere())
list(my_activity.production())
```