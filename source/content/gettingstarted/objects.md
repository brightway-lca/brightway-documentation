# Objects

```{admonition} Brightway Documentation
:class: seealso
[Glossary/Terminology Page](../theory/terminology.md)
```

## Technosphere and Biosphere

In order to interact with _technosphere activities_ and _biosphere flows_, we must first load the appropriate storage objects:

```python
my_database = bd.Database('<database_name>')
my_biosphere = bd.Database('biosphere3')
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.backends.base.SQLiteBackend`, the data type for these storage objects
```

### Selecting Objects

How do I select an activity from the technosphere database? \
How do I select a biosphere flow from the biosphere database? 

You can use the `search` function to find and return a list of objects that match your search term:

```python
my_database.search('<search_term>')
my_biosphere.search('<search_term>')
```

This will return a list of objects that match your search term.

You can also use a list comprehension to iterate over the objects in the database:


```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.backends.proxies.Activity`, the data type of an activities/flows
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

### Objects Properties

How do I list the properties of an activity? \
How do I list the properties of a biosphere flow?

```{note}
Activities and biosphere flows are {py:obj}`bw2data.backends.proxies.Activity` objects. \
These are based on Python [`mappings`](https://docs.python.org/3/glossary.html#term-mapping), which are similar to `dict`s.
```

In order to list the properties of an activity or biosphere flow, you can use the `as_dict` method, which turns the object into a real Python dictionary:

```python
obj.as_dict() 
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.backends.proxies.Activity` \
{py:obj}`bw2data.proxies.ProxyBase.as_dict`
```

### Specific Searches

How can I list the different (searchable) metadata fields of an activity? \
How can I list the different (searchable) metadata fields of a biosphere flow?

[As we have seen above](#objects-properties), activities and biosphere flows are similar to Python dictionaries. We can therefore quickly check which metadata fields are available for search:

```python
list(my_database.random().as_dict().keys())
```

We can also quickly list all unique values for a given metadata field, for example the `categories` field of all activities in a database:

```python
set(list(activity.as_dict()['categories'] for activity in my_database))
```




### Inspecting Object Exchanges

How do I list the technosphere exchanges and biosphere exchanges of an activity?

```python
list(my_activity.technosphere())
list(my_activity.biosphere())
list(my_activity.production())
```

### Search Basics

How do I search all possible metadata fields of a database?

```python
my_database.search('<search_term>')
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.backends.base.SQLiteBackend.search`
```

## Impact Assessment Methods

In order to interact with _impact assessment methods_ we must first load the appropriate storage object:

```python
my_methods = bd.methods
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.meta.Methods` ([`dict`](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) of [`tuple`s](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)), the data type for this storage object
```

```python
bio.search('carbon dioxide', filter = {'categories': 'urban', 'name': 'fossil'})
```

How do I find out which fields I can search for?

```{admonition} Python Documentation
:class: seealso
[List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
```