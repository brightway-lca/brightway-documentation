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

(object-selection)=
### Object Selection

How do I select (=search for) an activity from the technosphere database? \
How do I select (=search for) a biosphere flow from the biosphere database? 

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
german_coal_activities = [
    activity for activity in my_database
    if 'electricity production' in activity['name']    
    and 'coal' in aactivity['name']   
    and activity['location'] == 'DE'
]
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

### Object Properties

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

### Inspecting Exchanges

How do I list the technosphere exchanges and biosphere exchanges of an activity?

```python
list(my_activity.technosphere())
list(my_activity.biosphere())
list(my_activity.production())
```

## Impact Assessment Methods

In order to interact with _impact assessment methods_ we must first load the appropriate storage object:

```python
bw2data.meta.Methods()
```

````{note}
For your convenience, Brightway also provides a shorthand way of calling the dictionary of methods metadata:

```python
bp.methods
```
````

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.meta.Methods` ([`dict`](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) of [`tuple`s](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)), the data type for this storage object
```

### Object Selection

```{warning}
[Unlike the technosphere and biosphere databases](#object-properties), the impact assessment methods are stored as a Python [dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) of [tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences). This means, that no `search` function is available. Instead, a [list comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) with the [Python membership operator `in`](https://docs.python.org/3/reference/expressions.html#membership-test-operations) can be used to search.

```

```python
method_search_results = [
    method for method in bw.methods
    if 'ILCD 2.0' in str(method) and 'LT' not in str(method)
]
```

````{note}
🎲 You can also _randomly_ select a method:

```python
random_method = bw.methods.random()
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.serialization.SerializedDict.random`
```
````