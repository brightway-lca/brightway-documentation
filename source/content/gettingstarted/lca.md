# Static LCA

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

## Calculate LCA Results

### Calculate _one_ LCIA Result

> How can I calculate the life-cycle impact assessment (LCIA) results for a given activity?

We must define the functional unit and the impact assessment method.

First, we must create a variable that contains the activity we want to assess. The activity must be of type {py:obj}`bw2data.backends.proxies.Activity`.

```{admonition} Getting Started
:class: seealso
[](#object-selection)
```

```python
functional_unit_activity = my_database.random()
```

Next, we must create a variable that contains the impact assessment method we want to use. The method must be of type `tuple`.

```python
impact_assessment_method = bd.methods.random()
```

Now, we can create an instance of the {py:obj}`bw2calc.lca.LCA` class.

```python
lca = bc.LCA(
    demand={functional_unit_activity:1},
    method=impact_assessment_method
)
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2calc.lca.LCA`
```

This has only prepared the LCA calculation. Now, we must perform it:

```python
lca.lci() # builds matrices, solves the inventory problem, generates an LCI matrix
lca.lcia() # solves the impact assessment problem, generates an LCIA matrix
```

Now, the system has been solved. You can simply access the results:

```python
lca.score # returns the LCIA results
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2calc.lca_base.LCABase.lci` \
{py:obj}`bw2calc.lca_base.LCABase.lcia` \
{py:obj}`bw2calc.lca.LCA.score`
```

✨ Congratulations, you have conducted your first life-cycle impact assessment in Brightway!

### Calculate _multiple_ LCIA Results

> How can I calculate the life-cycle impact assessment (LCIA) results for multiple activities?

First, we must define a list of functional units and a list of the impact assessment methods:

```python
functional_units = [
    {bd.my_database.random(): 1},
    {bd.my_database.random(): 1},
    {bd.my_database.random(): 1},
]
methods = [
    bd.methods.random(),
    bd.methods.random(),
    bd.methods.random(),
]
```

Next, we must set up the calculation:

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

Now, we can perform the calculation:

```python
mlca = bc.multi_lca.MultiLCA('<setup_name>')
```

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2calc.multi_lca.MultiLCA`
```

Now, the system has been solved. You can simply access the results:

```python
mlca.results
```
