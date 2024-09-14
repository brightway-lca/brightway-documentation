# Cheat sheet

This section contains a basic list of all common Brightway commands.

```{admonition} Prerequisites
:class: important
1. A working [installation of Brightway](../installation/index.md).
2. Basic knowledge of [Python data types](https://docs.python.org/3/library/datatypes.html).
3. Basic understanding of matrix-based LCA data and calculations
```

All the commands below assume you have imported the Brightway core libraries:

````{admonition} Assumed imports
:class: important
```python
import bw2analyzer as ba
import bw2calc as bc
import bw2data as bd
import bw2io as bi
```
````

We will also use the convention that `'<replace_me>'` is a string which you need to change for your particular use case.

````{admonition} Recommended practice
Python is a flexible language, and there are many ways to do some of the following operations. We list below our *recommended* commands to execute these common tasks, and this is the interface we will try to keep compatible with future development. We therefore encourage using these patterns, even if you are used to something different.
````

## Projects

### Project activation and manipulation

**Q:** How do I see the currently active project?

```python
bd.projects.current
```

**Q:** How do I activate a project?

```python
bd.projects.set_current(name='<project_name>')
```

**Q:** How do I copy the currently active project?

```python
bd.projects.copy_project(name='<new_project_name>')
```

**Q:** How do I delete a project?

```python
bd.projects.delete_project(name='<project_name>', delete_dir=True or False)
```

`delete_dir` will delete the project's data; if `False`, then we remove the project name from the list of project names, but you can still switch back to the project and use the saved data.

**Q:** How do I list all my projects?

```python
sorted(bd.projects)
```

**Q:** How do I rename an existing project?

```python
bd.projects.rename("<new_project_name>")
```

(initial-project-data)=
### Creating initial project data

**Q:** How do I create a new project with basic data on elementary flows and LCIA?

To create a new project with some basic data:

```python
bi.remote.install_project('<project_tag>', '<my_desired_project_name>')
```

Where `<project_tag>` is one of:

* ecoinvent-3.10-biosphere
* ecoinvent-3.8-biosphere
* ecoinvent-3.9.1-biosphere
* forwast
* USEEIO-1.1

The ecoinvent biosphere projects also include LCIA impact categories.

We welcome the contribution of other taxonomies and data!

```{warning}
:class: important
The setup function `bw2setup()` is deprecated and should no longer be used.
```

### Archiving, restoring, and sharing projects

**Q:** How do I backup an existing project?

```python
bi.backup.backup_project_directory(
    project='<project_name>',
    dir_backup='<directory_path_for_backup>'
)
```

See {py:obj}`bw2io.backup.backup_project_directory` for more information.

**Q:** How do I restore a project from a backup?

```python
bi.backup.restore_project_directory(
    fp='<path_to_backup>',
    project_name='<project_name>'
)
```

See {py:obj}`bw2io.backup.restore_project_directory` for more information and customization options.

## Databases

**Q:** How do I list all databases?

```python
sorted(bd.databases)
```

**Q:** How do I test if a given database is installed?

```python
'<my database label>' in bd.databases
```

**Q:** How do I instantiate a `Database` object?

```python
my_db = bd.Database('<database_name>')
```

**Q:** How do I copy a `Database`?

```python
copied_database = bd.Database('<database_name>').copy('<new_name>')
```

**Q:** How do I rename a `Database`?

```python
new_database = bd.Database('<database_name>').rename('<new_name>')
```

**Q:** How do I delete a `Database`?

```python
del bd.databases['<database_name>']
```

### Metadata

**Q:** How do I see the `Database` metadata?

```python
bd.Database('<database_name>').metadata
```

**Q:** How do I change the `Database` metadata?

```python
bd.Database('<database_name>').metadata['<some_key>'] = '<some_value>'
```

**Q:** How do I see which other databases this `Database` refers to?

```python
bd.Database('<database_name>').metadata['depends']
```

**Q:** How can I see what kind of modelling paradigm and storage engine a `Database` uses?

This information is given to a limited degree by the database backend:

```python
bd.Database('<database_name>').metadata['backend']
```

There are three backends in a normal Brightway installation:

* `sqlite`: The default backend. Uses SQLite like a graph database.
* `iotable`: Uses the SQLite database for nodes, but stores edges only in datapackages. Limits edges to a single numerical value without uncertainty, but gives better performance for large IO data.
* `multifunctional`: Stores `multifunctional` processes as a custom node type, and automatically allocates following the given database or process preferences when creating datapackages.

### Searching

**Q:** How do I search a `Database`?

```python
bd.Database('<database_name>').search('<my_query_string>')
```

See {py:obj}`bw2data.backends.base.SQLiteBackend.search` for documentation and function options.

### Datapackages

**Q:** How do I get the `bw_processing` datapackage for this `Database`?

```python
bd.Database('<database_name>').datapackage()
```

## Inventory Graph

### Nodes

**Q:** How do I iterate over nodes in a `Database`?

```python
for node in bd.Database('<database_name>'):
    do_something(node)
```

Iteration over nodes is helpful for complicated filter cases:

```python
[
    node for node in bd.Database('<database_name>')
    if 'electricity production' in node['name']
    and 'coal' in node['name']
    and node['location'].lower() == 'de'
]
```

**Q:** How do I get a random node from a `Database`?

```python
bd.Database('<database_name>').random()
```

**Q:** How do I get a specific node?

```python
my_node = bd.get_node(my_attr="<some_value>")
```

You can pass in any attribute value, including "database" and "code". Combine multiple filters with commas, e.g. `bd.get_node(name="<foo>", location="bar")`. To search for attribute keys with spaces, use a dictionary: `bd.get_node(**{"some value with spaces": True})`.

**Q:** How do I create a new node?

```python
my_node = bd.Database('<database_name>').new_node(**attributes)
my_node.save()
```

Where `attributes` is a dictionary of the desired node attributes.

### Node properties

**Q:** How do I get all the data attributes of a node?

```python
my_node.as_dict()
```

**Q:** How do I change data attributes of a node?

```python
my_node['<some_key>'] = "<some_new_value>"
my_node.save()
```

### Edges

**Q:** How do I list edges of a process where inputs are consumed?

```python
list(my_node.technosphere())
```

**Q:** How do I list edges of a process where outputs are produced?

```python
list(my_node.production())
```

**Q:** How do I list all edges which consume the node `my_node`?

```python
list(my_node.consumers())
```

**Q:** How do I list all biosphere edges of a process?

```python
list(my_node.biosphere())
```

**Q:** How do I list all edges defined on a process?

```python
list(my_node.edges())
```

You can use a [list comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) to iterate over the edges to do more complex filtering:

```python
[
    edge for edge in my_node.edges()
    if 'car' in edge.input['name']
]
```

**Q:** How do I delete an edge?

```python
my_edge.delete()
```

### Edge properties

**Q:** How do I get all the data attributes of an edge?

```python
my_edge.as_dict()
```

**Q:** How do I access the input and output nodes of an edge?

```python
my_edge.input
my_edge.output
```

**Q:** How do I change the input or output of an edge?

```python
my_edge.input = new_node
my_edge.output = new_node
my_edge.save()
```

**Q:** How do I change data attributes of an edge?

```python
my_edge['<some_key>'] = "<some_new_value>"
my_edge.save()
```

**Q:** How do I create a new edge?

```python
my_edge = my_node.new_edge(**attributes)
my_edge.save()
```

Where `attributes` are the desired attributes of the edge; must include `type`, `amount`, and `input`.

## Impact Assessment

### Impact categories (`Method`)

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

## LCA Calculations

### Single functional unit and LCIA set

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

### Multiple functional units and LCIA sets

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

### Stochastic LCA calculations

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

## Importing data

The philosophy and workflow for importing data is explained in the "Overview".

```{admonition} Before starting an import
:class: important
Make sure you have the basic data, such as background data and biosphere flows available. It will probably be needed to create links with your imported data.
```

### Creating importers

**Q:** How do I start an import from the Brightway excel template?

```python
importer = bi.ExcelImporter('<file_path>')
```

See {py:obj}`bw2io.importers.excel.ExcelImporter` for additional information.

**Q:** How do I start an import from SimaPro CSV?

```python
from pathlib import Path
importer = bi.SimaProBlockCSVImporter(Path('<file_path>'))
```

See {py:obj}`bw2io.importers.simapro_block_csv.SimaProBlockCSVImporter` for additional information.

**Q:** How do I start an import from Ecospold 1?

```python
importer = bi.SingleOutputEcospold1Importer('<directory_path>', '<database_name>')
```

See {py:obj}`bw2io.importers.ecospold1.SingleOutputEcospold1Importer` for additional information.

**Q:** How do I start an import from Ecospold 1?

```python
importer = bi.SingleOutputEcospold2Importer('<directory_path>', '<database_name>')
```

See {py:obj}`bw2io.importers.ecospold2.SingleOutputEcospold2Importer` for additional information.

### Ecoinvent

**Q:** How can I import an ecoinvent release using the online portal?

```python
bi.import_ecoinvent_release(
    version='<version_number>',
    system_model='<system_model>',
    ecoinvent_user='<ecoinvent_user_name>',
    ecoinvent_password='<ecoinvent_password>'
)
```

The `import_ecoinvent_release` function will create a namespaced set of impact categories and a separate namespaced biosphere `Database`.

```{warning}
The setup function `bw2setup()` is deprecated and should no longer be used.
```

See {py:obj}`bw2io.ecoinvent.import_ecoinvent_release` for customization options, and the [`ecoinvent_interface` documentation](https://github.com/brightway-lca/ecoinvent_interface/?tab=readme-ov-file#authentication-via-settings-object) for instructions on how to download additional ecoinvent data and save your credentials.

**Q:** How can I import a local copy of an ecoinvent release?

Start with a basic project which has the correct set of elementary flows for your given release - see [Creating initial project data](initial-project-data). You can then use the standard ecospold2 importer:

```python
importer = bi.SingleOutputEcospold2Importer(
    dirpath='<ecoinvent_database_zip_file>',
    dbname='<database_name>'
)
importer.apply_strategies()
importer.write_database()
```

We strongly recommend that you follow the `ecoinvent-<version>-<system model>` database naming pattern.

### Applying transformations

**Q:** How do I apply the default transformation strategies?

```python
importer.apply_strategies()
```

**Q:** How do I apply a custom transformation strategy?

```python
importer.apply_strategy(<my_function>)
```

**Q:** How do I write a custom transformation strategy?

Transformation functions must take the entire import data as the single input argument, and return the modified entire import data. They should follow this general pattern:

```python
from typing import List

def my_custom_strategy(data: List[dict]) -> List[dict]:
    """Add very import information to each dataset"""
    for dataset in data:
        dataset["this is a dataset"] = True
    return data
```

If you need to provide additional information to a transformation strategy, you can [curry](https://en.wikipedia.org/wiki/Currying) the transformation function:

```python
from typing import List
from functools import partial

def my_custom_strategy(data: List[dict], favorite_color: str) -> List[dict]:
    """Add very import color information"""
    for dataset in data:
        dataset["my favorite color"] = favorite_color
    return data

importer.apply_strategy(partial(my_custom_strategy, favorite_color="blue"))
```

**Q:** How do I change the default strategies?

`importer.strategies` is a list, and the normal Python list methods can be used to modify the list before `.apply_strategies()` is called. You can also replace `importer.strategies` completely:

```python
importer.strategies = [<some functions>]
```

**Q:** How can I apply static transformations from [randonneur_data](https://github.com/brightway-lca/randonneur_data)?

```python
importer.randonneur('<transformation_label')
```

See {py:obj}`bw2io.importers.base_lci.LCIImporter.randonneur` for customization of this function's behavior.

### Creating links

**Q:** How do I realize internal links among the nodes in my imported data?

```python
importer.match_database()
```

See {py:obj}`bw2io.importers.base_lci.LCIImporter.match_database` for customization of this function's behavior.

**Q:** How do I realize external links from my imported data to other `Databases`?

```python
importer.match_database('<database_label>')
```

See {py:obj}`bw2io.importers.base_lci.LCIImporter.match_database` for customization of this function's behavior.

### Linking status

**Q:** How can I quickly check if all edges are linked?

```python
importer.all_linked
```

**Q:** How can I see how many edges have been linked so far?

```python
importer.statistics()
```

**Q:** How can I export an Excel file of the unlinked edges?

```python
filepath = importer.write_excel(only_unlinked=True)
```

**Q:** How can I export a Randonneur template for matching unlinked edges?

```python
filepath = importer.create_randonneur_excel_template_for_unlinked()
```

See {py:obj}`bw2io.importers.base_lci.LCIImporter.create_randonneur_excel_template_for_unlinked` for customization of this function's behavior.

### Handling unlinked edges

**Q:** How can I iterate over all unique unlinked edges?

```python
for edge in importer.unlinked:
    do_something(edge)
```

**Q:** How can I delete unlinked edges?

```python
importer.drop_unlinked(i_am_reckless=True)
```

**Q:** How can I add biosphere nodes from my imported data?

You can leave such biosphere nodes in the `Database` you are going to create, but you can separate them out into a new `Database`:

```python
importer.create_new_biosphere('<new_database_name>')
```

You can also add them to an existing database:

```python
importer.add_unlinked_flows_to_biosphere_database('<existing_database_name>')
```

**Q:** How can I create placeholder process or product nodes referenced in my imported data but without any producers?

```python
importer.add_unlinked_activities()
```
