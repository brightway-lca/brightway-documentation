```{attention}
__HELP WANTED__ \
You can help update and improve the content on this page. \
Please start by reading the [guide to contributing to the Brightway documentation.](../contributing/contributing.md)
```

```{warning}
__NEEDS WORK__ \
This page is not yet complete. \
It has been transfered over from the legacy documentation.
```

# Import and Export

## Introduction

There are some standards for life cycle inventory data, but the sad
truth is that there are no really good standards, and each
implementation of the standards has its own quirks. The basic strategy
for importing data from other programs is the following:

-   First, data is extracted from the export format (ecospold 1,
    ecospold 2, SimaPro CSV) into the same format as the activity and
    exchanges discussed above. Extraction is done using a
    format-specific extractor. Currently, there are extractors for
    `ecospold1`, `ecospold1-lcia`,
    `ecospold2`, `excel`,
    `exiobase`, `simapro CSV`, and `simapro CSV-lcia`.
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

### Importing from the standard Excel template

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

### Importing LCIA methods from the standard Excel template

Proper implementation of life cycle impact assessment methods requires a complete set of metadata. However, for simple LCIA methods, Brightway
has a simplified importer for Excel and CSV files: `bw2io.ExcelLCIAImporter` and `bw2io.CSVLCIAImporter`. These function the same as other importer (i.e. you extract data, apply strategies until you are satisfied with the matching, and write the modified data). There are example [Excel workbooks](https://github.com/brightway-lca/brightway2-io/raw/legacy/tests/fixtures/excel/lcia.xlsx) and [CSV files](https://github.com/brightway-lca/brightway2-io/raw/legacy/tests/fixtures/csv/lcia.csv).

Please note the following:

* Excel workbooks should only have one worksheet.
* Default matching to biosphere flows is based on ``name`and`categories`.

The convention for`categories`is the same as for inventory datasets: subcategories should be separated with `::`, e.g.`natural resource::in ground`. You can also list the main category and subcategory in separate columns, and use a strategy function to combine them. * The call function to instantiate the LCIA importer objects requires`filepath`,`name`(method name as a tuple),`description`, and`unit`.  What to do with unmatched exchanges? If there are unlinked exchanges, you have several options. If you aren't sure what to do yet, you can save a temporary copy (that can be loaded later) using `.write_unlinked("some name")`. Calling `.statistics()` will show what kind of exchanges aren't linked, e.g.: 

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

### Importing an LCIA method

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

#### Data format for LCIA methods

In order to allow for the re-use of strategies, the data format for LCIA
methods is the same as for inventory databases. `name` is the name (as a
tuple) of the impact category, and `exchanges` is the list of
characterization factors. It is a bit awkward, but makes other things
easier.

#### Adding other inputs to a strategy

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

#### Applying custom strategies

You apply strategies using the
`{ImporterClass}.apply_strategy(name_of_callable)` method. You could
also append your custom strategy to `{ImporterClass}.strategies`, so it
is used when you call `{ImporterClass}.apply_strategies`.

## Export

