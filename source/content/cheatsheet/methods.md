# Impact Assessment Methods


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

## Methods Management

In Brightway, _impact assessment methods_ are organized by the `Methods` dictionary.

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

## Method Selection

> How do I select (=search for) an impact assessment method?

```{warning}
[Unlike the technosphere and biosphere databases](#object-properties), the impact assessment methods are usually stored as a Python [dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) of [tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences). This means, that no `search` function is available. Instead, a [list comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) with the [Python membership operator `in`](https://docs.python.org/3/reference/expressions.html#membership-test-operations) can be used to search.
```

```python
method_search_results = [
    method for method in bw.methods
    if 'ILCD 2.0' in str(method) and 'LT' not in str(method)
]
```

If you already know the exact name of the method, query the method from the tuple:

```python
method_tuple = ('IPCC 2021', 'climate change', 'global warming potential (GWP100)')
method = bd.Method(method_tuple)
```

````{note}
🎲 You can also _randomly_ select a method:

```python
random_method: tuple = bw.methods.random()
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.serialization.SerializedDict.random`
```
````

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.method.Method`, the data type of a method object
```

(method-biosphere-flows)=
## Method Flows Inspection

> How do I list (=inspect) the biosphere flows of an impact assessment method?

```python
bd.Method(bd.methods.random()).load()
```

This will return a list of tuples of the form `(id,cf)`, where `id` is the biosphere flow ID and `cf` is the characterization factor. To get the `name` and `code` of the biosphere flow, you can use the `get` method of the `ActivityDataset` object:

```python
import pandas as pd
df_gwp_method_flows = pd.DataFrame(bd.Method(bd.methods.random()).load(), columns=['id', 'cf'])
df_gwp_method_flows['name'] = df_gwp_method_flows['id'].apply(lambda x: bd.get_node(id=x)['name'])
df_gwp_method_flows['code'] = df_gwp_method_flows['id'].apply(lambda x: bd.get_node(id=x)['code'])
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.data_store.DataStore.load` \
{py:obj}`bw2data.backends.schema.ActivityDataset`, list of node properties (including `code` and `name`)
```

## Method Creation

> How do I create a new impact assessment method based on my own characterization factors?

First, you must register your new method. The method name must be a [tuple](https://docs.python.org/3/library/stdtypes.html#tuple) of strings, and must be unique.

```python
new_method_name: tuple = ("string 1", "string 2", "string 3")
bd.Methods(new_method_name)
```

You can now prepare your methods data. Data must be in this format:

```
list(
    list(
        tuple(<biosphere_database_name>, <biosphere_flow_code>), <characterization_factor>
    ),
)
```

For instance:

```python
new_method_data = [
    [('biosphere3', '60d424f7-d5a9-4549-9540-da06684bc3bb'), -1],
    [('biosphere3', '375bc95e-6596-4aa1-9716-80ff51b9da77'), -1],
    [('biosphere3', 'f757365c-c6fd-41fe-ad32-3594ccd97ef0'), 29.8]
]
```

You should now validate your data, checking that it is in the correct format and that all biosphere flows are present in the biosphere database.

```python
bd.Method(new_method_name).validate(new_method_data)
```

If the data is valid and the function returns `True`, you can write it to the method object:

```python
bd.Method(new_method_name).write(new_method_data)
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.method.Method` \
{py:obj}`bw2data.backends.schema.ActivityDataset`, list of node properties (including `code` and `name`)
```