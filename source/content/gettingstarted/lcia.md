# Impact Assessment

## Impact Assessment Methods

```python
bw2data.meta.Methods()
```

````{note}
For your convenience, Brightway also provides a shorthand way of calling the dictionary of methods metadata:

```python
bp.methods
```
````


## Interacting with the Database

## Calculate _one_ LCIA Result

How can I calculate the life-cycle impact assessment (LCIA) results for a given activity?

Define the functional unit and the impact assessment method:

```python
lca = bw2calc.LCA(
    demand={my_activity: 1}, # the functional unit
    method=('IPCC 2013', 'climate change', 'GWP 100a')
)
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2calc.lca.LCA`
```

```python
lca.lci() # builds matrices, solves the inventory problem, generates an LCI matrix
lca.lcia() # solves the impact assessment problem, generates an LCIA matrix
lca.score() # returns the LCIA results
```

```{admonition} API Documentation
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2calc.lca.LCA`
```

## Calculate _multiple_ LCIA Results

How can I calculate the life-cycle impact assessment (LCIA) results for multiple activities?

Define the functional units and the impact assessment methods:

```python
functional_units = [
    {my_activity_1: 1},
    {my_activity_2: 1},
    {my_activity_3: 1},
]
```

```python
bd.meta.CalculationSetups['<setup_name>'] = (
    inv=list_functional_units,
    methods=list_methods
)
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2data.meta.CalculationSetups`
```

```python
mlca = bc.multi_lca.MultiLCA('<setup_name>')
mlca.results
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2calc.multi_lca.MultiLCA`
```
