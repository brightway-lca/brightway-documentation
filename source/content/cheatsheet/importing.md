# Importing Data

The philosophy and workflow for importing data is explained on [the Overview page](../overview/index.md).

```{admonition} Before starting an Import
:class: important
Make sure you have the basic data, such as background data and biosphere flows available. It will probably be needed to create links with your imported data.
```

## Creating Importers

### How do I start an import from the Brightway excel template?

```python
importer = bi.ExcelImporter('<file_path>')
```

See {py:obj}`bw2io.importers.excel.ExcelImporter` for additional information.

### How do I start an import from SimaPro CSV?

```python
from pathlib import Path
importer = bi.SimaProBlockCSVImporter(Path('<file_path>'))
```

See {py:obj}`bw2io.importers.simapro_block_csv.SimaProBlockCSVImporter` for additional information.

### How do I start an import from Ecospold 1?

```python
importer = bi.SingleOutputEcospold1Importer('<directory_path>', '<database_name>')
```

See {py:obj}`bw2io.importers.ecospold1.SingleOutputEcospold1Importer` for additional information.

### How do I start an import from Ecospold 1?

```python
importer = bi.SingleOutputEcospold2Importer('<directory_path>', '<database_name>')
```

See {py:obj}`bw2io.importers.ecospold2.SingleOutputEcospold2Importer` for additional information.

## Ecoinvent

### How can I import an ecoinvent release using the online portal?

```python
bi.import_ecoinvent_release(
    version='<version_number>',
    system_model='<system_model>',
    username='<ecoinvent_user_name>',
    password='<ecoinvent_password>'
)
```

The `import_ecoinvent_release` function will create a namespaced set of impact categories and a separate namespaced biosphere `Database`.

```{warning}
The setup function `bw2setup()` is deprecated and should no longer be used.
```

See {py:obj}`bw2io.ecoinvent.import_ecoinvent_release` for customization options, and the [`ecoinvent_interface` documentation](https://github.com/brightway-lca/ecoinvent_interface/?tab=readme-ov-file#authentication-via-settings-object) for instructions on how to download additional ecoinvent data and save your credentials.

### How can I import a local copy of an ecoinvent release?

Start with a basic project which has the correct set of elementary flows for your given release - see [Creating initial project data](initial-project-data). You can then use the standard ecospold2 importer:

```python
importer = bi.SingleOutputEcospold2Importer(
    dirpath='<ecoinvent_database_zip_file>',
    db_name='<database_name>'
)
importer.apply_strategies()
importer.write_database()
```

We strongly recommend that you follow the `ecoinvent-<version>-<system model>` database naming pattern.

## Applying Transformations

### How do I apply the default transformation strategies?

```python
importer.apply_strategies()
```

### How do I apply a custom transformation strategy?

```python
importer.apply_strategy(<my_function>)
```

### How do I write a custom transformation strategy?

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

### How do I change the default strategies?

`importer.strategies` is a list, and the normal Python list methods can be used to modify the list before `.apply_strategies()` is called. You can also replace `importer.strategies` completely:

```python
importer.strategies = [<some functions>]
```

### How can I apply static transformations from [randonneur_data](https://github.com/brightway-lca/randonneur_data)?

```python
importer.randonneur('<transformation_label')
```

See {py:obj}`bw2io.importers.base_lci.LCIImporter.randonneur` for customization of this function's behavior.

## Creating Links

### How do I realize internal links among the nodes in my imported data?

```python
importer.match_database()
```

See {py:obj}`bw2io.importers.base_lci.LCIImporter.match_database` for customization of this function's behavior.

### How do I realize external links from my imported data to other `Databases`?

```python
importer.match_database('<database_label>')
```

See {py:obj}`bw2io.importers.base_lci.LCIImporter.match_database` for customization of this function's behavior.

## Linking Status

### How can I quickly check if all edges are linked?

```python
importer.all_linked
```

### How can I see how many edges have been linked so far?

```python
importer.statistics()
```

### How can I export an Excel file of the unlinked edges?

```python
filepath = importer.write_excel(only_unlinked=True)
```

### How can I export a Randonneur template for matching unlinked edges?

```python
filepath = importer.create_randonneur_excel_template_for_unlinked()
```

See {py:obj}`bw2io.importers.base_lci.LCIImporter.create_randonneur_excel_template_for_unlinked` for customization of this function's behavior.

## Handling Unlinked Edges

### How can I iterate over all unique unlinked edges?

```python
for edge in importer.unlinked:
    do_something(edge)
```

### How can I delete unlinked edges?

```python
importer.drop_unlinked(i_am_reckless=True)
```

### How can I add biosphere nodes from my imported data?

You can leave such biosphere nodes in the `Database` you are going to create, but you can separate them out into a new `Database`:

```python
importer.create_new_biosphere('<new_database_name>')
```

You can also add them to an existing database:

```python
importer.add_unlinked_flows_to_biosphere_database('<existing_database_name>')
```

### How can I create placeholder process or product nodes referenced in my imported data but without any producers?

```python
importer.add_unlinked_activities()
```
