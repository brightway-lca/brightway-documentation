# Exchanges (Edges)

````{admonition} Prerequisites
:class: important

```{admonition} Brightway Documentation
:class: seealso
[Brightway Structure Page](../theory/structure.md) \
[Glossary/Terminology Page](../theory/terminology.md)
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

## Exchange Selection

> How do I list the technosphere exchanges and biosphere exchanges of an activity?

```python
my_database.random().exchanges()
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.backends.proxies.Exchanges`, the data type for the list of exchanges \
{py:obj}`bw2data.backends.proxies.Exchange`, the data type of an exchange object
```

```{note}
The list of exchanges is a kind of [Python iterable](https://docs.python.org/3/glossary.html#term-iterable).
```

You can use a [list comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) to iterate over the objects in the exchange list. This can be used to build lists of exchanges from complex search parameters. For example:

```python
list_car_exchanges = [
    exchange for exchange in my_database.random().exchanges()
    if 'car' in exchange['name']
]
```

## Exchange Properties

> How do I list the properties of an exchange?

```{note}
Exchanges are {py:obj}`bw2data.backends.proxies.Exchange` objects. \
These are based on Python [`mappings`](https://docs.python.org/3/glossary.html#term-mapping), which are similar to `dict`s.
```

In order to list the properties of an activity or biosphere flow, you can use the `as_dict` method, which turns the object into a real Python dictionary:

```python
[exc for exc in eidb.random().exchanges()][0].as_dict()
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.backends.proxies.Exchange` \
{py:obj}`bw2data.proxies.ProxyBase.as_dict`
```