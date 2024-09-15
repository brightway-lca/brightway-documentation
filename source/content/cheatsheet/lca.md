## LCA Calculations

### Single Functional Unit and LCIA Set

**Q:** How do I define a functional unit?

A functional unit is some amount of one or more products. Because chimaera process+products act like products (see the overview documentation), they can also be used as functional units.

Brightway wants functional units to be provided as a dictionary, with keys given the product `Nodes`, and values giving the amount of each product. A single functional unit can have one or more products.

```python
{my_node: 42, my_other_node: 7}
```

**Q:** How do I calculate an life cycle inventory?

```python
my_functional_unit, data_objs, _ = bd.prepare_lca_inputs({my_node: 42})
my_lca = bc.LCA(demand=my_functional_unit, data_objs=data_objs)
my_lca.lci()
```

This will create `my_lca.inventory`, a matrix with the life cycle inventory data, with rows of biosphere flows and columns of processes.

**Q:** How do I calculate a characterized inventory?

```python
my_functional_unit, data_objs, _ = bd.prepare_lca_inputs(
    {my_node: 42},
    method=('<impact>', '<category>')
)
my_lca = bc.LCA(demand=my_functional_unit, data_objs=data_objs)
my_lca.lci()
my_lca.lcia()
```

This will create `my_lca.characterized_inventory`, a matrix with the life cycle inventory data, with rows or biosphere flows and columns of processes.

**Q:** How do I calculate a normalized inventory?

```python
my_functional_unit, data_objs, _ = bd.prepare_lca_inputs(
    {my_node: 42},
    method=('<impact>', '<category>'),
    normalization=('<normalization>', '<factors>')
)
my_lca = bc.LCA(demand=my_functional_unit, data_objs=data_objs)
my_lca.lci()
my_lca.lcia()
```

This will create `my_lca.normalized_inventory`, a matrix with the normalized life cycle inventory data, with rows or biosphere flows and columns of processes.

**Q:** How do I calculate a weighted inventory?

```python
my_functional_unit, data_objs, _ = bd.prepare_lca_inputs(
    {my_node: 42},
    method=('<impact>', '<category>'),
    weighting=('<weighting>', '<factors>')
)
my_lca = bc.LCA(demand=my_functional_unit, data_objs=data_objs)
my_lca.lci()
my_lca.lcia()
```

This will create `my_lca.weighted_inventory`, a matrix with the weighted life cycle inventory data, with rows or biosphere flows and columns of processes.

Weighting can be done with normalization, but does not require normalization.

**Q:** How do I get the LCA score after calculating a characterized inventory, possibly including normalization and/or weighting?

```python
my_lca.score
```

**Q:** How do I see the most important elements in the result matrix?

```python
my_lca.to_dataframe(matrix_label="characterized_inventory")
```

See {py:obj}`bw2calc.lca.LCA.to_dataframe` for more information on this functionality.

**Q:** How do I filter down to a row in the `inventory` or `<any>_inventory` matrix?

Rows in these matrices are biosphere flows.

```python
row_index = lca.dicts.biosphere[my_biosphere_flow_node.id]
filtered_matrix = lca.inventory[row_index, :]
filtered_matrix = lca.characterized_inventory[row_index, :]
filtered_matrix = lca.normalized_inventory[row_index, :]
filtered_matrix = lca.weighted_inventory[row_index, :]
```

**Q:** How do I filter down to a column in the `inventory` or `characterized_inventory` matrix?

Columns in these matrices are processes.

```python
col_index = lca.dicts.activity[my_process_node.id]
filtered_matrix = lca.inventory[:, col_index]
filtered_matrix = lca.characterized_inventory[:, col_index]
filtered_matrix = lca.normalized_inventory[:, col_index]
filtered_matrix = lca.weighted_inventory[:, col_index]
```

**Q:** How do I go from matrix indices to `Node` objects?

First, you need to find out what kind of object you need to look up. Assuming you have created an LCA instance `lca_instance`:

* In the `technosphere_matrix`, `inventory`, and all `<any>_inventory` matrices, columns are processes. Use `lca_instance.dicts.activity`.
* In the `technosphere_matrix`, and in the `demand_array`, rows are products. Use `lca_instance.dicts.product`.
* In the `biosphere_matrix`, `inventory`, and all `<any>_inventory` matrices, rows are biosphere flows. Use `lca_instance.dicts.biosphere`.
* The `characterization_matrix`, `normalization_matrix`, and `weighting_matrix` are all [diagonal matrices](https://en.wikipedia.org/wiki/Diagonal_matrix), with both rows and columns being biosphere flows. Use `lca_instance.dicts.biosphere`.

You can then use `dicts.<foo>.reversed` to go from row or column indices to `Nodes`:

```python
bd.get_node(id=my_lca.dicts.activity.reversed[my_column_index])
bd.get_node(id=my_lca.dicts.product.reversed[my_row_index])
```

### Multiple Functional Units and LCIA Sets

**Q:** How do I calculate an life cycle inventory for multiple functional units?

For the `MultiLCA` class, we need to *label* each functional unit:

```python
functional_units = {
    "γ": {node_1.id: 1},
    "ε": {node_2.id: 2},
}
data_objs = bd.get_multilca_data_objs(functional_units, {})
lca = bc.MultiLCA(
    demands=functional_units,
    method_config={},
    data_objs=data_objs,
)
lca.lci()
```

```{admonition} Functional unit data types
:class: important
In `MultiLCA` functional units, the keys must be integer ids, not `Node` instances
```

This will create `lca.inventories`, a dictionary which gives inventory matrices for each combination of functional unit label and impact category.

```python
{
    ("γ",): sparse_matrix,
    ("ε",): sparse_matrix,
}
```

**Q:** How do I calculate a life cycle impact assessment for multiple functional units and a combination of LCIA impact categories, normalizations, and weightings?

We start by describing how the impact categories, normalization, and weightings are related. The safest way to do this is by creating an instance of `bw2calc.MethodConfig`; the {py:obj}`bw2calc.method_config.MethodConfig` documentation describes how to provide this data.

```python
method_config = bd.MethodConfig(<some_data>)
```

For the `MultiLCA` class, we need to *label* each functional unit in a dictionary:

```python
functional_units = {
    "γ": {node_1.id: 1},
    "ε": {node_2.id: 2},
}
```

Finally, we need to get the datapackages needed for all inventory databases and LCIA steps. We can then create a `MultiLCA` instance:

```python
data_objs = bd.get_multilca_data_objs(functional_units, method_config)
lca = bc.MultiLCA(
    demands=functional_units,
    method_config=impact_categories,
    data_objs=data_objs,
)
lca.lci()
lca.lcia()
```

You should also do `lca.normalization()` and `lca.weighting()` if those steps have data given in `method_config`.

The results are provided as dictionaries, with keys showing which weighting, normalization, and characterization methods were applied for each functional unit. For example, if `method_config` was:

```python
method_config = bd.MethodConfig(
    impact_categories=[
        ('<impact_category>', '<a>'),
        ('<impact_category>', '<b>'),
    ]
)
```

Then `lca.characterized_inventories` would be the following dictionary:

```python
{
    (('<impact_category>', '<a>'), "γ"): sparse_matrix,
    (('<impact_category>', '<a>'), "ε"): sparse_matrix,
    (('<impact_category>', '<b>'), "γ"): sparse_matrix,
    (('<impact_category>', '<b>'), "ε"): sparse_matrix,
}
```

Additional elements would be added to the dictionary keys if normalization and weighting were included.


As these dictionaries have multiple matrices at each calculation step, the `MultiLCA` attributes are plural:

* `supply_array` ➟ `supply_arrays`
* `inventory` ➟ `inventories`
* `characterized_inventory` ➟ `characterized_inventories`
* `normalized_inventory` ➟ `normalized_inventories`
* `weighted_inventory` ➟ `weighted_inventories`
* `score`  ➟ `scores`

### Stochastic LCA Calculations

Both `LCA` and `MultiLCA` classes support stochastic calculations. New values for all matrices can be generated from probability distribution functions, or from pre-calculated arrays of sample or population values.

**Q:** How do I use probability distribution functions in stochastic LCA?

```python
bc.LCA(..., use_distributions=True)
bc.MultiLCA(..., use_distributions=True)
```

**Q:** How do I use presampled values from arrays in my datapackages?

```python
bc.LCA(..., use_arrays=True)
bc.MultiLCA(..., use_arrays=True)
```

You can use both `use_distributions` *and* `use_arrays` in a calculation.

**Q:** How do I generate a new set of results iteration when doing stochastic LCA?

```python
next(lca_object)
```

This will draw new data samples and generate new versions of all matrices defined, including characterization, normalization, and weighting, solve the linear system, and generate all result matrices.
