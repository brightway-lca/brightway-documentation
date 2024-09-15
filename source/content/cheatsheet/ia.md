## Impact Assessment

### Impact Categories (`Method`)

**Q:** How do I list the installed impact categories?

```python
sorted(bd.methods)
```

**Q:** How do I test if a given impact category is installed?

```python
('<impact>', '<category>') in bd.methods
```

**Q:** How can I get a random impact category?

```python
bd.methods.random()
```

**Q:** How do I search for an impact category using list comprehensions?

```python
[
    method for method in bd.methods
    if 'ilcd 2.0' in method[0].lower()
    and 'LT' not in method[2]
]
```

**Q:** How do I see the data in a given impact category?

```python
my_method_object = bd.Method(('<impact>', '<category>'))
list(my_method_object)
```

**Q:** How is the data in impact categories structured?

Iterating over a `Method` object yields tuples.

* The first element in the tuple will be the biosphere `Node`
* The second element will be the characterization factor, either as a number, or as a dictionary which includes uncertainty information
* There could be a third element, which gives the *location* for the characterization factor. This third element is not required.

**Q:** How do I interpret the uncertainty dictionary?

See the [`stats_arrays` documentation](https://stats-arrays.readthedocs.io/en/latest/#mapping-parameter-array-columns-to-uncertainty-distributions).

**Q:** How do I create a new impact category?

Start by defining characterization data following the tuple format defined in `How is the data in impact categories structured?`:

```python
import stats_arrays as sa
my_cf_data = [
    (biosphere_node_1, 42),
    (biosphere_node_1, 23, 'BR'),
    (biosphere_node_2, {
        'uncertainty_type': sa.TriangularUncertainty.id,
        'amount': 7,
        'loc': 7,
        'maximum': 21
    })
]
```

Then write the characterization factor to the `Method`:

```python
bd.Method(('<impact>', '<category>')).write(my_cf_data)
```

**Q:** How do I see the impact category metadata?

```python
bd.Method(('<impact>', '<category>')).metadata
```

**Q:** How do I change the impact category metadata?

```python
bd.Method(('<impact>', '<category>')).metadata['<some_key>'] = '<some_value>'
```
