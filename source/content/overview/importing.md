# Importing

```{admonition} Leaning from examples
:class: seealso
Importing data is the worst part of the LCA world, and it is easy to get overwhelmed. This document discusses basic concepts, but also includes a set of examples that show the concepts in practice.
```

```{admonition} Prepared projects
:class: seealso
Some data has already been prepared for Brightway, so you can skip doing the import yourself. Look at the [initial project data](../cheatsheet/index.md#creating-initial-project-data) and at {py:obj}`bw2io.ecoinvent.import_ecoinvent_release`.
```

## Introduction

There are some standards for life cycle inventory data, but the sad truth is that there are no really good standards, and each implementation of the standards by different software providers has its own quirks.

The biggest difficulty we face is in constructing the supply chain graph from its serialization in the given data format. In the most basic case, a graph can be written:

```python
nodes = ['A', 'B']
edges = [{'from': 'A', 'to': 'B', 'amount': 42}]
```

In this case, there is a a single unambiguous identifier for each node, and everything is easy. In the real world, edges are normally defined by the *attributes* of the referenced nodes, like this:

```python
nodes = [{
    'id': 1,
    'name': 'foo'
}, {
    'id': 2,
    'name': 'bar'
}]
edges = [{'from': 'foo', 'to': 'bar', 'amount': 42}]
```

This type of data exchange format is convenient for data creators, as some formats simply lack a single unambiguous identifier, and in others this identifier is generated at run-time. **However**, to use this data we now need to figure out that the node with name "foo" is the one with "id" `1` - and real world matching is more complex than this simple example, and needs to be done hundreds or thousands of times. In general, we need to write our import logic assuming that we will have to do attribute matching.

Each main LCA data format comes with its own set of challenges:

| Format | Gotchas |
| --- | --- |
| ecospold 1 | Unique identifier is `number`, but some software doesn't use this correctly, so it can't be counted on |
| ecospold 2 | Separate UUIDs for activity and product, but they aren't easy to find, and you need to combine them to get a single identifier for a process with a reference process located in time and space |
| SimaPro CSV | No guarantee of any attribute uniqueness, exports don't always include internal ids, attributes changed from original data for common background databases, exported data can include errors[^1] |
| Excel | Potential whitespace errors, no support for anything but primitive data types, custom templates require custom code |
| OLCA JSON-LD | Format can change in incompatible ways, lots of NIH |
| ILCD | Everything we love about XML, better for individual datasets than complete databases, in practice requires using EU elementary flow list and UUID mapping |
| Exiobase | Not a single format, elementary flow list changes over time |

The basic strategy for importing data is the following:

First, data is extracted from the given format. Extraction is done using a format-specific extractor. Currently, there are extractors for `ecospold1`, `ecospold2`, `simapro CSV`, `exiobase`, and the standard Brightway `excel` template.

Next, we have to choose where and how to transform the data, either for direct import or for linking to other databases already present. Harmonization could mean transforming the data to fit a certain taxonomy, to fit a certain data model, or to meet other data modelling assumptions. There is a lot of variety in LCA data formats, and the most popular software allows for a lot of flexibility, so there are no general rules.

We then need to create concrete links in each edge - i.e. to turn `'from': 'foo'` to `'from': 1`. To do this, we define the fields we want to link with, and use the built-in `Brightway` linking functionality. This is normally an iterative process, trying different linking approaches combined with harmonization and examining the linking status until the imported data is completely linked.

Finally, we can load the data into our relational data store, and use it in models or calculations.

## Transforming Nodes or Edges

In general, we want to avoid transformations, as it is cleaner and less future work to use the original data as it was provided. Transformations are a necessary evil used for two main purposes:

* To align the data with a given data schema or set of modelling assumptions
* To allow for linking, and especially for linking across databases.

Linking is always finding a suitable edge candidate, so transformations for linking are almost always on edges, not nodes, as we can normally assume that imported data is internally consistent. Transforming nodes can be done, though; here are some common scenarios:

* You want all data to be harmonized to a certain taxonomy. Brightway prefers that units be written in full, for example, so you could normalize all unit strings to "kilogram", etc.
* You want to reverse changes made by a data provider. For example, some databases are built on top of other databases, and if we have those other databases already imported, we would like to remove the existing link and re-link to our versions of the background data. This normally means removing the copied nodes in the imported data.
* You need to adapt the provided data to better fit a specific set of assumptions, a data quality standard, or a data schemas.

## Static Transformations

Static transformations are pre-computed, and come prepared in a fixed format. `Brightway` has a number of static transformations available in the [randonneur_data](https://github.com/brightway-lca/randonneur_data) library.

Static transformations are great when they work. Please be careful to read their descriptions, match versions precisely, and check to make sure they are doing what you expect! Static transformations will also not perform linking - they will prepare the data to be compatible so that it can be linked afterwards.

The most common static transformations in normal practice are updating references from one background database version to a newer version before linking, and undoing modifications to allow for linking against original data. Here is an example of updating references:

```python
import randonneur_data as rd
registry = rd.Registry()
registry.sample('ecoinvent-3.9.1-biosphere-ecoinvent-3.10-biosphere')
{
    'replace': [{
        'source': {
            'name': 'Xylene',
            'uuid': '0e6cf9f9-44ff-4395-ad3b-36109a32e6eb'
        },
        'target': {
            'name': 'Xylenes, unspecified',
            'formula': 'C8H10',
            'uuid': '0e6cf9f9-44ff-4395-ad3b-36109a32e6eb'
        },
        'comment': 'Flow attribute change not listed in change report'
    },
    {
        'source': {
            'uuid': 'ce11d77b-c85a-4f03-816e-714dcda260ea',
            'name': 'Americium-241'
        },
        'target': {
            'uuid': 'a0e98cdc-79cd-4073-9713-c1a48238883a',
            'name': 'Americium-241'
        }
    }]
}
```

Similarly, here is a transformation from one nomenclature system to another for the same data:

```python
import randonneur_data as rd
registry = rd.Registry()
registry.sample('simapro-ecoinvent-3.9.1-cutoff', 1)
{
    'replace': [{
        'source': {
            'identifier': 'EI3ARUNI000011519609842',
            'name': 'Ventilation of dwellings, decentralized, 6 x 120 m3/h {CH}| ventilation of dwellings, decentralized, 6 x 120 m3/h, polyethylene ducts, with earth tube heat exchanger | Cut-off, U',
            'platform_id': '35E3AE4E-798C-40F1-A9A2-626BE36D8367'
        },
        'target': {
            'filename': '2578e5c8-8fdd-5a68-bb93-525f992fafd8_60c21de1-a8e8-4f50-8949-78759bf96c62.spold',
            'name': 'ventilation of dwellings, decentralized, 6 x 120 m3/h, polyethylene ducts, with earth tube heat exchanger',
            'location': 'CH',
            'reference product': 'ventilation of dwellings, decentralized, 6 x 120 m3/h',
            'unit': 'm2*year'
        }
    }
]}
```

The complete transformation data format includes [useful metadata](https://github.com/brightway-lca/randonneur?tab=readme-ov-file#data-format) in addition to the raw changes.

### Applying Static Transformations

TBD

In order to use these transformations, we need to think about and specify the following:

* Do I want to do destructive changes (delete and create), or just modifications (replace, update, and disaggregate)?
* Are the labels used in the transformation data correct for my data schema?
* What fields do we want to use for matching to determine if the transformation should be applied?

### Creating New Static Transformations

TBD

Static transformations should be added to a `randonneur_data` regis

See {py:obj}`bw2io.importers.base_lci.LCIImporter.randonneur` on how to customize these choices.

Prepared static transformations can be generated in two ways - programmatically, or manually. Programmatic generation is always preferred, as it should be tested, is reproducible, and can be adapted for new contexts or input lists. However, manual matching is sometimes necessary. Manual matches should be noted clearly in the transformation file comment.

The [flowmapper](https://github.com/cmutel/flowmapper/) tool allows for automatic matching of elementary flow lists. Technosphere flow matching is usually custom developed, as there are few generic patterns to follow. The [ecoinvent_migrate](https://github.com/brightway-lca/ecoinvent_migrate) library is an exception, and generates prepared static transformations for ecoinvent technosphere and biosphere upgrades.

## Dynamic Transformations

Dynamic transformations are done programmatically - i.e. a function takes in a dataset, does some changes, and returns the altered dataset. There are many such functions already available in the Brightway framework. Here are a few:

* {py:obj}`bw2io.strategies.generic.add_database_name`
* {py:obj}`bw2io.strategies.generic.convert_uncertainty_types_to_integers`
* {py:obj}`bw2io.strategies.ecospold2.add_cpc_classification_from_single_reference_product`
* {py:obj}`bw2io.strategies.ecospold2.remove_uncertainty_from_negative_loss_exchanges`
* {py:obj}`bw2io.strategies.simapro.change_electricity_unit_mj_to_kwh`

In general, even if you are just writing a quick script for a one-off import, it's best practice to write transformation functions which have documentation and some simple unit tests. This development work forces you to think about what you are trying to accomplish, and what could go wrong.



Here are some examples of typical harmonization steps:

-   Next, each dataset is normalized or transformed to make it better
    conform to what Brightway2 expects. This could mean, for example,
    copying the only production exchange to the list of
    `products`, or normalizing the units or biosphere
    category names. This step could also include applying migrations,
    which are additional dataset that can be used to transform data to
    new forms. For example, SimaPro changes ecoinvent activity and
    product names, and the `simapro-ecoinvent-3` changes
    these names back to what ecoinvent provided. Migrations are
    explained in more detail below.
-   The third step is to link exchanges to activities within the
    imported data. Brightway2 has a powerful generic linking function
    called `link_iterable_by_fields` that does the heavy
    lifting. This function will link an exchange if the fields match,
    i.e. it has the same name, location, unit, etc.
    `link_iterable_by_fields` can also be told to only link
    certain types of exchanges, such as biosphere exchanges.
-   Many imported datasets will link to other databases already
    installed on your computer. You can link these exchanges using the
    `.match_database()` function. You can customize this
    function by specifying the fields to use, as well as other options.
-   You should then check on the quality of linking using the
    `statistics()` function, which will tell you how many
    exchanges are in the data, and how many unlinked exchanges are
    present, as well as the types of unlinked exchanges.
-   You are finally ready to choose what to do with the imported data.
    If all exchanges are linked, you can write a new database with
    `.write_database()`. You can also save your work with
    `.write_unlinked(name)`, which will save a new unlinked
    database for further processing at a later time. You can also write
    details on linking with `.write_excel()`, which can
    write the entire data or just the unlinked exchanges. Of course, you
    can always continue with steps 2, 3, and 4, refining your linking
    until you are satisfied.

If this seems a bit overwhelming, that\'s because it is - and a huge
pain. The current data formats and lack of well-defined strategies for
interchange between databases and even updating databases makes life
much more difficult than it should be. There are concrete examples of
importing databases in `example-io-notebooks`.

### Importing from `ecospold 1`

Importing from ecospold 1 is relatively simple. Multioutput products are
allocated to single output products using the given allocation factors
using the strategy `es1_allocate_multioutput`. The reference product is
then assigned using the strategy `assign_only_product_as_production`.

Next, some basic data cleanup is performed. Integer codes are removed,
as these are not used consistently by different LCA software
(`clean_integer_codes`). Unspecified subcategories are removed (i.e.
`('air', 'unspecified')` is changed to `('air',)`) using
`drop_unspecified_subcategories`. Biosphere exchange names and
categories are normalized using `normalize_biosphere_categories` and
`normalize_biosphere_names`. Biosphere exchanges are removed, as
biosphere flows do not have locations (`strip_biosphere_exc_locations`).

Next, a unique activity code is generated for each dataset, using a
combination of the name, categories, location, and unit
(`set_code_by_activity_hash`).

Finally, biosphere flows are linked to the default biosphere database,
and internal technosphere flows are linked using
`link_technosphere_by_activity_hash`.

## Import

### Importing from `ecospold 2`

Importing from ecospold 2 is a bit complex, because although ecospold 2
gives unique IDs for many fields, which helps in linking, the current
implementation has some `known
issues`(http://www.ecoinvent.org/database/ecoinvent-version-3/ecoinvent-v30/known-data-issues/)
which have to be resolved or ignored by the importer.

```{warning}
Brightway2 cannot precisely reproduce the LCI and LCIA results given by
the ecoinvent centre. The technosphere matrix used by ecoinvent cannot
be reproduced from the provided unit process datasets. However, the
differences for most products are quite small.
```

We start by removing some exchanges from most datasets. Specifically, we
remove exchanges with amounts of zero, both coproducts and technosphere
or biosphere inputs (`remove_zero_amount_coproducts` and
`remove_zero_amount_inputs_with_no_activity`).

We then assign reference products. Although each unit process should
have a single output, coproducts which have been allcoated away are
often still included, with amounts of zero. We use two strategies to
choose the reference product:
`es2_assign_only_product_with_amount_as_reference_product` and
`assign_only_product_as_production`.

Next, a composite code is generated, using the UUID of the activity and
the product (`create_composite_code`).

Biosphere flow exchanges are now normalized
(`drop_unspecified_subcategories`) and linked
(`link_biosphere_by_flow_uuid`). Internal technosphere exchanges are
also linked, using the composite codes
(`link_internal_technosphere_by_composite_code`).

Not all technosphere exchanges are linked, however. We need to drop two
different types of exchanges, as we have no way of linking them. First,
there are some exchanges with listed products but no listed activities -
and no activity in the database produces these products. Removal is done
with the strategy `delete_exchanges_missing_activity`.

Additionally, there are some exchanges with listed products and
activities - but the given activity doesn\'t produce the listed product.
These exchanges also have to be deleted, using the strategy
`delete_ghost_exchanges`.

```{note}
Ecoinvent 3.1 includes some dummy biosphere flows (`Fluoranthene_temp`, `Chrysene_temp`, etc.). They can be safely deleted using using `.drop_unlinked(True)`.
```

### Importing from SimaPro

Importing SimaPro CSV files is also a bit of a headache. Pré, the makers
of SimaPro, have done a lot of work to make LCA software accessible and
understandable. This work includes making changes to process names and
other metadata, which makes linking these processes back to original
ecoinvent data difficult. Fortunately, Pré has been very helpful is
supplying correspondence files, which we can use to move (to the best of
our ability) from the \"SimaPro world\" to \"ecoinvent world\".

```{note}
Importing SimaPro XML export files is not recommended, as there are bugs with exporting ecoinvent 3 processes.
```

### Importing from the Standard Excel Template

```{note}
You can see these ideas in practive in `basic
database`(https://github.com/brightway-lca/brightway2-io/blob/master/tests/fixtures/excel/basic_example.xlsx?raw=true)
and `parameterized
database`(https://github.com/brightway-lca/brightway2-io/blob/master/tests/fixtures/excel/sample_activities_with_variables.xlsx?raw=true)
Excel templates.
```

You can define inventory datasets in many ways in Excel, but there is a
standard template which is supported by the `ExcelImporter`. The
template should be pretty self-explanatory, and follows this general
format:

```
Project parameters (optional)
<column label, <column label, <column label
<value, <value, <value

Database, <name of database
<database field name, <database field value

Database Parameters (Optional)
<column label, <column label, <column label
<value, <value, <value

Activity, <name of activity
<database field name, <database field value
(Optional blank line(s))
Parameters (Optional), <name of parameter group (optional)
<column label, <column label, <column label
<value, <value, <value
(Optional blank line(s))
Exchanges
<column label, <column label, <column label
<value, <value, <value
<value, <value, <value
```

Data can be split over many worksheets. To mark a worksheet as one that
should be skipped by the importer, put the string \"skip\" in cell 1A.

Sections are split by the presence of blank lines. There are two kinds
of sections: data and metadata. Metadata sections are used for the
descriptions of databases (`Database`) and activities (`Activity`, until
`Exchanges`). In metadata sections, only the first two columns are
read - all other columns are ignored. In the data sections ---
`Project parameters`, `Parameters`, and `Exchanges` - all columns are
read, and should have column headings. You can limit the number of
columns read by inserting the string `cutoff` in cell 1A, and the column
index **after which** the importer should start ignoring columns in cell
1B. For example, if you put `4` in cell 1B, the first four columns would
be included, and the rest ignored.

Keep in mind the following general restrictions and notes:

 -   Provide useful codes! There is no reason to use e.g. UUIDs, unless
     you are feeling masochistic. You can also skip providing codes at
     all, they will be autogenerated.
 -   As in the activity data format, there are no required fields, and
     you can also insert your own.
 -   Each workbook can only describe data for one `Database`. Multiple
     `Database` sections will raise an error!
 -   Input exchanges must be linked using the data provided in the
     spreadsheet. That means that you may need to provide an activity
     name and a reference product when trying to link against
     ecoinvent.
 -   Linking is done using the column headings exactly as provided. You
     should check to make sure the capitalization, spelling, and
     spacing are consistent with the attributes in the background
     databases you want to link against.
 -   Worksheet names don\'t have any special meaning to the importer,
     and are only used to indicate where errors occurred.

Parameters are a bit different - as they are trickier to handle, their
sections are stricter:

 -   All parameter sections must have the column \"name\". Names should
     be unique within a parameter section.
 -   Stochastic variables should have the usual uncertainty columns,
     e.g. uncertainty type, loc, scale, minimum, maximum.
 -   Variables which are defined by formulas should have the column
 -   Parameters can have an \"amount\" column, but if there is also a
     \"formula\" column, the amount will be overwritten on import as
     the formula is evaluated.
 -   Formulas should be for consumption by Python, not Excel; they will
     be interpreted by `asteval`(https://newville.github.io/asteval/).
 -   The `Database`, `Project parameters`, and `Database parameters`
     don\'t have to be in any order or in any particular worksheet.
     There can be multiple `Project parameters` and
     `Database parameters` sections, they will be concatenated.

The following data transformations are applied by the `ExcelImporter`:

 -   Numbers are translated from text into actual numbers.
 -   Tuples, separated in the cell by the `::` string, are
     reconstructed, i.e. \"this::example\" would become
     `("this", "example")`.
 -   The strings \"True\" and \"False\" (by themselves, not as part of
     a larger string) are transformed to their respective boolean
     values.
 -   Fields with the value `(Unknown)` are omitted on a per-row basis.

### Importing LCIA Methods from the Standard Excel Template

Proper implementation of life cycle impact assessment methods requires a complete set of metadata. However, for simple LCIA methods, Brightway
has a simplified importer for Excel and CSV files: `bw2io.ExcelLCIAImporter` and `bw2io.CSVLCIAImporter`. These function the same as other importer (i.e. you extract data, apply strategies until you are satisfied with the matching, and write the modified data). There are example [Excel workbooks](https://github.com/brightway-lca/brightway2-io/raw/legacy/tests/fixtures/excel/lcia.xlsx) and [CSV files](https://github.com/brightway-lca/brightway2-io/raw/legacy/tests/fixtures/csv/lcia.csv).

Please note the following:

* Excel workbooks should only have one worksheet.
* Default matching to biosphere flows is based on `name` and `categories`.

The convention for `categories`is the same as for inventory datasets: subcategories should be separated with `::`, e.g. `natural resource::in ground`. You can also list the main category and subcategory in separate columns, and use a strategy function to combine them. * The call function to instantiate the LCIA importer objects requires `filepath`, `name`(method name as a tuple), `description`, and `unit`.  What to do with unmatched exchanges? If there are unlinked exchanges, you have several options. If you aren't sure what to do yet, you can save a temporary copy (that can be loaded later) using `.write_unlinked("some name")`. Calling `.statistics()` will show what kind of exchanges aren't linked, e.g.:

```python
> sp.statistics()
366 datasets     3991 exchanges     2639 unlinked exchanges
Type biosphere: 170 unique unlinked exchanges
Type technosphere: 330 unique unlinked exchanges
```

The options to examine or resolve the unlinked exchanges are:

* You can write a spreadsheet of the characterization factors, including their linking status, with `.write_excel("some name")`.
* You can apply new linking strategies with `.apply_strategies(some_new_strategy)`. Note that this method requires a *list* of strategies.
* You can match technosphere or biosphere exchanges to other background databases using `.match_database("another database")`.

To resolve unlinked biosphere exchanges which simply don't exist in your current biosphere database, you can:

* Add them to the biosphere database with `add_unlinked_flows_to_biosphere_database()`
* Create a new biosphere database with`create_new_biosphere("new biosphere name")`
* Add the biosphere flows to the database you are currently working on (LCI databases can include both process and biosphere flows) with `add_unlinked_biosphere_flows_to_current_database()

```{note}
These methods have several options, and you should understand what they do and read their documentation before choosing between them.
```

```{note}
You can't write an LCI database with unlinked exchanges.
```

### Migrations

Sometimes the only way to correctly link activities or biosphere flows is by applying a list of name (or other field) transforms. For example,SimaPro will export a process named \"\`sulfonyl\`urea-compound {RoW}\| production \| Alloc Rec, S\", which corresponds to the ecoinvent process \"\`sulfonyl\`urea-compound production\", with reference product \"\`sulfonyl\`urea-compound\" and location \"RoW\". In another example, in ecoinvent 2, emissions of water to air were measured in kilograms, and in ecoinvent 3, emissions of water to air are measured in cubic
meters. In this case, our migration would look like this:

``` python
{
    'fields': `'name', 'categories', 'type', 'unit'`,
    'data': `
        (
            ## First element is input data in the order of `fields` above
            ('Water', ('air',), 'biosphere', 'kilogram'),
            ## Second element is new values to substitute
            {
                'unit': 'cubic meter',
                'multiplier': 0.001
            }
        )
    `
}
```

We call the application of transform lists \"migrations\", and they are applied with the `.migrate(migrations_name)` method.

If the numeric values in an exchange need to changed, the special key \'multiplier\' is used, where new_amount = multiplier \* old_amount. Uncertainty information and formulas are adjusted automatically, if possible (see `utils.rescale_exchange`).

A few additional notes:

-   Migrations change the underlying data, but do not do any linking -
    you will also have to apply linking strategies after a migration.
-   Migrations can specify any number of fields, but of course the
    fields must be present in the importing database.
-   TODO: Migrations can be specified in an excel template. Template
    files must be processed using `convert_migration_file`.
-   Subcategories are not expanded automatically, so a separate row in
    the migrations file would be needed for e.g.
    `water (air, non-urban air or from high stacks)`.

### Importing an LCIA Method

LCIA methods can be imported from ecospold 1 XML files
(`EcoinventLCIAImporter`) and SimaPro CSV files
(`SimaProLCIACSVImporter`).

When importing an LCIA method or set of LCIA methods, you should specify
the biosphere database to link against e.g.
`EcoinventLCIAImporter("some file path", "some biosphere database name")`.
If no biosphere database name is provided, the default `biosphere3`
database is used.

Both importers will attempt to normalize biosphere flow names and
categories to the ecospold2 standard, using the strategies:

 -   `normalize_simapro_lcia_biosphere_categories`
 -   `normalize_simapro_biosphere_names`
 -   `normalize_biosphere_names`
 -   `normalize_biosphere_categories`

Next, the characterization factors are examined to see if they are only
given for root categories, e.g. `('air',)` and not
`('air', 'urban air close to ground')`. If only root categories are
characterized, then we assume that the characterization factors also
apply to all subcategories, using the strategy `match_subcategories`.

Finally, linking to the given or default biosphere database is
attempted, using the strategy `link_iterable_by_fields` and the standard
fields: name, categories, unit, location. Note that biosphere flows do
not actually have a location.

You can now check the linking statistics. If all biosphere flows are
linked, write the LCIA methods with `.write_methods()`. Note that
attempting to write an existing method will raise a `ValueError` unless
you use `.write_methods(overwrite=True)`, and trying to write methods
which aren\'t completely linked will also raise a `ValueError`.

If there are unlinked characterization factors, you have several
options. If you aren\'t sure what to do yet, you can save a temporary
copy (that can be loaded later) using `.write_unlinked("some name")`.
The options to examine or resolve the unlinked characterization factors
are:

 -   You can write a spreadsheet of the characterization factors,
     including their linking status, with `.write_excel("some name")`.
 -   You can apply new linking strategies with
     `.apply_strategies(`some_new_strategy`)`. Note that this method
     requires a *list* of strategies.
 -   TODO: You can write all biosphere flows to a new biosphere
     database with `.create_new_biosphere("some name")`.
 -   If you are satisfied that you don\'t care about the unlinked
     characterization factors, you can drop them with
     `.drop_unlinked()`.
 -   Alternatively, you can add the missing biosphere flows to the
     biosphere database using `.add_missing_cfs()`.

### Custom Strategies

A `strategy` is just a Python callable (usually a function) that follows
a few simple conventions: it takes the input data as a single input
argument, and returns the modified data as the only returned value.
Inventory data is store in `{ImporterClass}.data`, and has the following
form:

``` python
`
    {
        'name': "some name",
        ..., ## other metadata in key: value form
        'exchanges': `
            {
              'amount': float,
              ..., ## other data in key: value form
            }
        `
    }
`
```

Here is an example strategy (from
`bw2io.strategies.csv.py`(https://github.com/brightway-lca/brightway2-io/blob/master/bw2io/strategies/csv.py)):

``` python
def csv_add_missing_exchanges_section(data):
    for ds in data:
        if "exchanges" not in ds:
            ds`"exchanges"` = ``
    return data
```

This is short function, and is not complicated - most strategies will do
more.

#### Data Format for LCIA Methods

In order to allow for the re-use of strategies, the data format for LCIA
methods is the same as for inventory databases. `name` is the name (as a
tuple) of the impact category, and `exchanges` is the list of
characterization factors. It is a bit awkward, but makes other things
easier.

#### Adding Other Inputs to a Strategy

Strategy functions should only take one input, but sometimes you want to
add other input arguments. For example, imagine the following silly
strategy:

``` python
def add_silly_string(data, string):
    for ds in data:
        ds`'name'` += string
    return data
```

If you tried to use this, it would raise an error, as `string` wouldn\'t
be defined. The right approach here is
`currying`(https://en.wikipedia.org/wiki/Currying), which allows you to
give the values of some input arguments in advance:

``` python
from functools import partial

add_silly_string_fixed = partial(add_silly_string, string="something silly")
```

You would then apply the strategy `add_silly_string_fixed`.

#### Applying Custom Strategies

You apply strategies using the
`{ImporterClass}.apply_strategy(name_of_callable)` method. You could
also append your custom strategy to `{ImporterClass}.strategies`, so it
is used when you call `{ImporterClass}.apply_strategies`.

## Export

[^1]: The usual text errors, such as bytes outside the defined character page, and the creative, like dates in amount fields, formulas which evaluate to `1 / 0`, and defining the same unit multiple times in different ways.
