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

# Structure

(brightway_components)=
## Brightway Components

Brightway is split into several main packages:

-   [Brightway25](https://github.com/brightway-lca/brightway25) is the 
    umbrella package, as well as documentation. When installing this
    package, it will pull as dependencies the following packages:

    -   [Brightway2-data](https://github.com/brightway-lca/brightway2-data)
        handles storing and searching all data sources (databases, LCIA methods,
        etc.).
    -   [Brightway2-calc](https://github.com/brightway-lca/brightway2-calc) does
        LCA calculations.
    -   [Brightway2-io](https://github.com/brightway-lca/brightway2-io) tools
        for the import, export, and management of inventory databases and impact
        assessment methods. LCA calculations.
    -   [Brightway2-analyzer](https://github.com/brightway-lca/brightway2-analyzer)
        analyzes input data like databases and methods, as well as the result of
        LCA calculations.
    -   [Brightway2-parameters](https://github.com/brightway-lca/brightway2-parameters)
        Library for storing, validating, and calculating with parameters.

## Projects

Data in Brightway2 is structured in a hierarchy. At the top level, we
have projects. A project is self-contained, with its own copy of data,
LCIA methods, calculations, assumptions, and any other data you need.
Each project is completely independent of other projects.Projects are
saved as subdirectories in the file system.

![image](_images/org-scheme.png)

Inside a project we have a number of objects that store data. The most
common data objects are inventory *databases* and impact assessment
*methods*. However, non-LCA data can also be included. For example, a
set of vehicle registrations and lifetimes could also be stored in a
project, and used to generate fleet-based scenarios for sustainability
assessment of mobility services.

Project are created in a suitable location for your operating system
with the help of the [appdirs](https://github.com/ActiveState/appdirs)
library.

Projects can be easily created, copied, manipulated, or deleted. See the
[projects example
notebook](https://github.com/brightway-lca/brightway2/blob/master/notebooks/Projects.ipynb).

```{warning}
Brightway2 uses [atomic file
writes](https://github.com/abarnert/fatomic) to prevent data corruption,
but [files are hard](http://danluu.com/file-consistency/); you should
make regular backups using the `backup-data-directory` function.
```

## Inventory Databases

In Brightway2, a *database* is the object used to organize a set of
nodes and edges in a life cycle inventory graph of the industrial supply
chain and natural world. For example, a specific version of ecoinvent
could be a database, but so would a set of biosphere flows, as biosphere
flows are also nodes in our inventory graph. Databases can be big, like
ecoinvent, or as small as a single dataset. You can have as many
databases as you like, and databases can have links into other
databases. You can also have databases that each depend on each other.

SimaPro differentiates between what it calls *projects* and *libraries*,
but both would be a *database* in Brightway2.

Databases can be easily created, copied, modified, iterated over,
searched, and delted. See the [databases example
notebook](https://github.com/brightway-lca/brightway2/blob/master/notebooks/Databases.ipynb).

## Activities and Exchanges

In the database, nodes are called *activities*, and include transforming
and market activities, but also products and biosphere flows. Edges are
called *exchanges*, and describe a link between two nodes. An exchange
could describe the input of a product to a transforming activity, or an
emission of a biosphere flow by an activity, or the name and amount of a
product produced by an activity.

### Activity data format

A database consists of inventory datasets, and inventory datasets are
text documents, human-readable data that you can manipulate manually in
a text editor, or change en masse programmatically. Because they can be
exported as text, and in a format that is accessible to almost every
computer language ([JSON](http://www.json.org/)), activity datasets can
be easily exported and used by other programs.

Inventory datasets have a very flexible and free text form; even an
empty dictionary (e.g. `{}`) is a valid LCI dataset in Brightway2.
However, some fields are suggested for common use. Note that you can
always add extra fields as needed by your application. Here is a
selection from an example dataset from the US LCI:

``` python
{
 'categories': ['Wood Product Manufacturing', 'Softwood Veneer and Plywood Mnf.'],
 'location': 'RNA',
 'name': 'Green veneer, at plywood plant, US PNW',
 'type': 'process',
 'unit': 'kilogram'}
 'exchanges': [{
   'amount': 1.0,
   'code': 6,
   'group': 2,
   'input': ('US LCI', '6ddb4cc00f9e42aa48515248256c31dc'),
   'type': 'production',
   'uncertainty type': 0},
  {'amount': 7.349999999999999e-06,
   'code': 5,
   'group': 4,
   'input': ('biosphere', '51447e58e03a40a2bbd9abf45214b7d3'),
   'type': 'biosphere',
   'uncertainty type': 0}],
}
```

The document structure is:

-   *name* (string): Name of this activity.

-   *type* (string): If this is `"process"`, or omitted completely,
    Brightway2 will treat this as a inventory process with inputs and
    output(s). If you want to store additional information in a Database
    outside of the list of processes, specify a custom type here. For
    example, the list of biosphere flows is also an inventory database,
    but as these are flows, not processes, they have the type
    `"emission"`. Similarly, if you wanted to separate processes and
    products, you could create database entries for the products, with
    the type `"product"`.

-   *categories* (list of strings, optional): A list of categories and
    subcategories. No length limits.

-   *location* (string, optional): A location identifier. Default is
    *GLO*, but this can be changed in the
    `user-preferences`.

-   *unit* (string): Unit of this activity. [Units are
    normalized](https://github.com/brightway-lca/brightway2-io/blob/master/bw2io/units.py)
    when written to disk.

-   *exchanges* (list): A list of activity inputs and outputs, with its own schema.

    -   *input* (database name, database code): The technological
        activity that is linked to, e.g.
        `("my new database", "production of ice cream")` or
        `('biosphere', '51447e58e03a40a2bbd9abf45214b7d3')`. See
        also `dataset-codes`.
    -   *type* (string): One of `production`, `technosphere`, and
        `biosphere`. See `exchanges`.
    -   *amount* (float): Amount of this exchange.
    -   *uncertainty type* (integer): Integer code for uncertainty
        distribution of this exchange, see
        `uncertainty-type` for more
        information. There can be other uncertainty fields as well.
    -   *comment* (string, optional): A comment on this exchange.
        Used to store pedigree matrix data in ecoinvent v2.

---

## Uniquely identifying activities

Linking activity datasets within and between databases requires a way to
uniquely identify each dataset - Brightway2 calls this unique identifier
a code. A code can be a number, like `1`, or a string of numbers and
letters, like `swiss ch33se`. When you create datasets manually, you
will need to assign each dataset a code. When you import a database, the
codes will be automatically generated for you.

### Activity hashes

When you import an *ecospold* or *SimaPro* dataset, the data format does
not provide a way to uniquely identify each dataset. Brightway2 will
generate codes that look like a bunch of nonsense, e.g.:
`6d336c64e3a0ff08dee166a1dfdf0946`. In this case, Brightway2 identifies
an activity or flow with the [MD5](http://en.wikipedia.org/wiki/MD5)
hash of a few attributes: For ecoinvent 2, the `name`, `location`,
`unit`, and `categories`. For ecoinvent 3, the `activity` and
`reference product` names.

### Activities must be uniquely identified

Activities are identified by their database name and a unique `code`. A
code is a string of letters and numbers that uniquely identifies an
activity within the database. Codes can be written by humans, e.g.
`"Chris's first pony"`, or generated by by the computer using an
algorithm.

Activities do not have very many required fields; aside from `database`
and `code`, the only other required field is `name`, but most activities
will have a `location` and `unit` as well. If no `type` is specified for
an activity, then the activity is assumed to be a `process`. Other types
include `product` and `biosphere` for biosphere flows. Activity `type`
is used to determine whether an activity should be placed in the
biosphere or technosphere matrices during LCA calculations.

Exchanges are links between two activities of any type. Exchanges have
an `input` and an `output`: `input` is the activity being consumed or
produced, and `output` is the consumer or producer. Exchanges should
also have an `amount` and a `type`. Common types include `technosphere`,
`biosphere`, and `production`. Multiple exchanges between two activities
are allowed, and will be added together during LCA calculations.

Many activities have a reference product, which is an exchange of type
`production` where the `input` is the same as the `output`.

Brightway2 allows multioutput processes; you are responsible for making
sure the final system make mathematical sense (see [multioutput
processes in LCA](http://chris.mutel.org/multioutput.html)).

### Exchange data format

Exchanges are a list of the inputs and outputs of an activity. For
example an activity might consume some resources, emit some emissions,
and have other technological goods as emissions. Each activity also has
at least one technological output.

Each exchange has a `type`. There are three standard exchange types in
Brightway2, but you can define your own if you need to define different
kinds of systems.

#### Production exchanges

A production exchange defines how much of the output is produced by an
activity. For example, the process \"make a fizzbang\" would produce one
kilogram of fizzbang (the amount is normally one, but doesn\'t have to
be).

Production exchanges have the type `production`.

```{note}

A production exchange is **not** required. A default value of one will
be applied if no production exchange is defined. This default value is
usually the most logical amount, so should only be changed in special
circumstances.
```

```{warning}

Using a production value other than one can be confusing. See the blog
post [What happens with a non-unitary production amount in
LCA?](http://chris.mutel.org/non-unitary.html).
```

```{warning}

Multioutput processes (i.e. more than one production process) can be
used in Brightway2, but only under special circumstances. See the blog
post [Multi-output processes in matrix-based LCA](http://example.com).
```

#### Substitution exchanges

A substitution exchange is used in multi-output processes to indicate
the avoided production of a product by another activity. Substitution
exchanges have positive values, and the type [substitution].

#### Technosphere exchanges

A technosphere exchange is a process input from the technosphere, i.e.
the industrial economy. For example, the process \"make a fizzbang\"
could have an input of seven kilograms of lollies.

Technosphere exchanges have the type `technosphere`.

#### Biosphere exchanges

A biosphere exchange is a consumption of a resource or and emission to
the environment associated with a process; its value will be placed in
the biosphere matrix.

Biosphere exchanges have the type `biosphere`.

### Database is a subclass of DataStore

Much of the functionality of Database objects is provided by its parent
class, `datastore`. The normal methods
provided by a data store are:

> -   **write(data)**: Write data to disk
> -   **load**: Load data from disk
> -   **register**: Register object with metadata store
> -   **deregister**: Remove object from metadata store
> -   **copy(name)**: Create a new object with name `name`
> -   **backup**: Write backup of data
> -   **validate(data)**: Validate data using this object\'s validator

Data store objects are instantiated with the object name, e.g.
`DataStore("name goes here")`.

Brightway2-data defines the following data stores:

-   `SingleFileDatabase <single-file-database>`
-   `JSONDatabase <json-database>`
-   `method`
-   `weighting`
-   `normalization`

The schema for an `LCI dataset` in [voluptuous](https://pypi.python.org/pypi/voluptuous/) is:

``` python
{
    Optional("categories"): Any(list, tuple),
    Optional("location"): object,
    Optional("unit"): basestring,
    Optional("name"): basestring,
    Optional("type"): basestring,
    Optional("exchanges"): [exchange]
}
```

Where an `exchange` is:

``` python
{
    Required("input"): valid_tuple,
    Required("type"): basestring,
    Required("amount"): Any(float, int),
    Optional("uncertainty type"): int,
    Optional("loc"): Any(float, int),
    Optional("scale"): Any(float, int),
    Optional("shape"): Any(float, int),
    Optional("minimum"): Any(float, int),
    Optional("maximum"): Any(float, int)
}
```

```{note}

Database documents can be validated with
`bw2data.validate.db_validator(my_data)`, or
`Database("my database name").validate(my_data)`.
```

### Getting the signs right

Brightway uses the following rules to set values in the technosphere and
biosphere matrices:

-   [biosphere] exchange values are inserted into the
    biosphere matrix without any modification.
-   [production] and [substitution] exchanges
    are inserted into the technosphere matrix without any modification.
-   [technosphere] exchanges values are multiplied by
    negative one, and then inserted into the technosphere matrix.

In the technosphere matrix, negative values represent the consumption of
products, while positive values represent the production of products.
Substitution exchanges are positive because this forces the substituted
activity to have a negative production amount, representing the avoided
production pathway.

These rules are consistent with and grow out of the traditional Leontief
inverse of IO tables $x = (I - A)^{-1}d$.

As a consequence of these rules, a technosphere exchange with a negative
value is the same as a production exchange, and vice-versa.

Biosphere exchange amounts can occasionally be negative, and some
characterization factors are also negative. The default metadata in
Brightway follows ecoinvent system assumptions about biosphere flow
categories:

-   Biosphere flows whose categories are [air],
    [soil], and [water] are emissions into the
    natural environment.
-   Biosphere flows with the category [natural resource] are
    consumption of natural resources from the natural environment.

Biosphere exchanges with negative values reverse these assumption; so, a
biosphere flow of -2 kg of carbon dioxide with the category air would be
the *removal* of carbon dioxide from the natural environment. The signs
of biosphere exchanges don\'t really matter, but they should be
consistent with the signs of your impact assessment characterization
factors. See also the notebook on [negative Biosphere flows and
CFs](https://github.com/brightway-lca/brightway2/blob/master/notebooks/Negative%20Biosphere%20flows%20and%20CFs.ipynb).

### Databases can be stored in different ways

The default storage backend for databases stores each database in a
separate file. This is the easiest and most convenient approach for most
cases. However, Brightway2 also supports pluggable database backends,
which can change how databases are stored and queried.

Brightway2-data also provides `bw2data.backends.JSONDatabase`, which
stores each dataset as a separate file serialized to
[JSON](http://en.wikipedia.org/wiki/JSON). This approach works well with
version-control systems, as each dataset change can be saved
individually. Use of `JSONDatabase` is shown in a simple [ipython
notebook](https://github.com/brightway-lca/brightway2/blob/master/notebooks/JSON%20database.ipynb).

Before using `JSONDatabase`, please read its technical documentation
carefully: `json-database`. To create a
`JSONDatabase`, use `Database("my db name", backend="json")`. To switch
backends for a database, use
`convert_backend <switching-backends>`.

`custom-backends`, such as using an actual
relational database, can also be defined.

### Biosphere database

When you run `bw2setup()` in a python shell, Brightway2 will install a
special `biosphere3` database. This database has all the resource and
emission flows from the ecoinvent database, version 2.

You can define biosphere flows - resources and emissions - in any
database you like, but it is probably best to use the pre-defined flows
in the `biosphere` database whenever you can. If you need to add some
custom flows, feel free to create a separate database.

You can also change the name for the default biosphere database in the
`user preferences <user-preferences>`.

## Impact Assessment

In Brightway2, each impact assessment method is a set of
characterization factors for a set of biosphere flows. Each impact
category and subcategory is a separate method, and each method is stored
and calculated separately.

Methods are identified by a list of names, which could be as simple as:

``` python
("I scream", "you scream", "we all scream", "for ice cream")
```

which is probably most applicable for those who are particularly
concerned with ice cream resource depletion; a more typical example is:

``` python
('ecological scarcity 1997', 'total', 'total')
```

Impact assessment method names can have any length and number of
qualifiers - there is nothing special or sacred about three levels - but
must always be a list of strings.

```{warning}
For technical reasons, impact assessment names must be stored as a
[tuple](http://docs.python.org/2/tutorial/datastructures.html#tuples-and-sequences),
not a [list](http://docs.python.org/2/tutorial/introduction.html#lists),
i.e. they must have `()` at the beginning and end, and not `[]`.
```

### Method metadata

Method metadata is a normal dictionary, and is indexed in the `methods`
object. The object `methods` is a special dictionary that saves itself
whenever values change, but is otherwise still a normal dictionary.
`new_method.metadata` is an alias for `methods`. So, to change the
metadata, do:

``` python
methods[('foo',)] = {'bar': True, ...}
```

Or to chance a single value:

``` python
methods[('IPCC 2007', 'climate change', 'GWP 100a')]['timeframe'] = 100
```

Note that after changing a single value, you will need to flush the
changes to disk:

``` python
methods.flush()
```

Methods should have the following metadata:

> -   *description*: A description of this method or submethod.
> -   *unit*: The unit of this method or submethod.

In addition, the metadata `abbreviation` is generated automatically.

### LCIA method documents

The impact assessment method documents are quite simple - indeed, it is
a bit of a stretch to call them documents at all. Instead, they are a
list of biosphere flow references, characterization factors, and
locations. All LCIA methods in Brightway2 are regionalized, though the
default installed methods only provide global characterization factors.
Here is a simple example:

``` python
from brightway2 import *
Method(('ecological scarcity 1997', 'total', 'total')).load()[:5]
```

This returns the following:

``` python
[[(u'biosphere', u'21c70338ff2e1cdc8e468f4c90f113a1'), 32000, u'GLO'],
 [(u'biosphere', u'86a37cf9e44593f1c41fdce53de27715'), 32000, u'GLO'],
 [(u'biosphere', u'a8cc9c61aa343fa01532bb16cec7f90d'), 32000, u'GLO'],
 [(u'biosphere', u'b0a29177e77471a49b5a7d6a88212bf8'), 32000, u'GLO'],
 [(u'biosphere', u'72c1cf2fee31a2cb6cdc39abda29a0df'), 32000, u'GLO']]
```

Each list elements has two required components and a third optional
component.

> 1.  A reference to a biosphere flow, e.g.
>     `(u'biosphere', u'21c70338ff2e1cdc8e468f4c90f113a1')`.
> 2.  The numeric characterization factor. This can either be a number,
>     or a uncertainty dictionary (see
>     `uncertainty-type`).
> 3.  An *optional* location, used for regionalized impact assessment.
>     The global location `GLO` is inserted as a default if not location
>     is specified.

```{note}

LCIA method documents can be validated with
`bw2data.validate.ia_validator(my_data)`, or
`Method(("my", "method", "name")).validate(my_data)`.
```

### Default LCIA methods

When you run `bw2setup()`, Brightway2 will install around 700 default
LCIA methods, as provided by the ecoinvent center. These LCIA methods
will work for both ecoinvent 2 and 3.

## Parameterized datasets

Brightway2 supports variables and formulas stored as strings, similar to
other LCA software. So instead of defining a fixed value for an
exchange, you could enter a formula of \"fuel_efficiency \*
average_distance\", where both \"fuel_efficiency\" and
\"average_distance\" were variables stored in a special way, and maybe
even parameterized themselves. Parsing strings is not trivial, and so
the machinery to handle such parameterization is a bit complex:

![image](_images/parameters.png)


```{warning}
Parameterized inventory datasets only work with databases that use the default SQLite backend.
```

### Groups

Parameters are tricky because you have to parse and understand
dependencies in formula strings - where if \"efficiency\" defined, and
is it a Python reserved term or a function or a variable, etc. To make
these dependencies explicit, Brightway2 uses the ideas of **groups** to
collect parameters, just like databases collect inventory datasets. Each
parameter belongs to a group, and inside a group each parameter has to
have a unique name. Groups also have unique names, and are defined at
the three different levels that parameters exist: project, database, or
a set of activities. Groups cannot cross levels.

Groups form a hierarchy used to evaluate and find symbols, with project
parameters at the top, and activity parameters at the bottom. When
parsing an activity parameter formula, unknown variable names will be
searched in that activity parameter set of variables, then in the
database parameters defined for the database the activity is in, and
finally in the project parameters. An missing value will be taken as
soon as it is found - so if \"efficiency\" exists in a database
parameter group and the project parameter group, its value will be taken
from the database parameters.

Note the following restrictions on groups:

-   The group name \'project\' is reserved for the group of project
    parameters
-   Database names are reserved for database parameters (it is also
    their group name)
-   Activity parameter groups can include more than one activity, but
    cannot span multiple databases
-   Single activities cannot be in multiple groups
-   Group dependencies cannot be circular

These restrictions are enforced in the database, so you can\'t screw up
your data, but they might explain any errors you encounter.

### Active versus passive parameters

Some background datasets have lots of parameters, and one doesn\'t
necessarily want them all to be imported into the Brightway parameter
machinery - after all, they have been resolved already. We therefore use
a distinction between active and passive parameters. Active parameters
are stored in a special SQLite database for parameters, and their
formulas are parsed and checked to make sure there are no missing or
unknown symbols. Active parameters are recalculated whenever their
upstream groups change, and can be used in dynamic calculation. Passive
parameters are stored in either `Database` instances (as the key
`parameters` in the metadata), `Activity` objects (as the key
`parameters` in the metadata), or in `Exchanges` (as the key `formula`
in the exchange data). They are not evaluated or otherwise used.

The parameters manager has functions for activating activities and
exchanges.

### Parameters manager

The most common way to interact with parameters data is through the
parameters manager, provided as `parameters`.


### Peewee objects

At a finer level of control, the parameterized table objects use [peewee
objects](http://docs.peewee-orm.com/en/latest/index.html) directly, so
you will use some different syntax than with [Activity] and
[Exchange] (see the [parameters source
code](https://github.com/brightway-lca/brightway2-data/blob/master/bw2data/parameters.py)).
The long-term goal is to transition all objects to peewee directly,
instead of using proxies.

The parameters framework is centered around the
`Group, ProjectParameter, DatabaseParameter, and ActivityParameter classes <parameters>`.

Here are some examples of peewee-style queries:

``` python
Group.create(name="some name")

group, created = Group.get_or_create(name="some name")

for obj in DatabaseParameter.select().where(
    DatabaseParameter.database="some db"):
  print(obj.name, obj.amount, obj.formula)

ActivityParameter.update(amount = some_new_value
    ).where(ActivityParameter.name="some name").execute()

ProjectParameter.delete().where(ProjectParameter.name="some name"
    ).execute()
```

## Intermediate and processed data

Both inventory datasets and impact assessment methods are stored as
structured text files, stored in the `intermediate` folder. These files
are not efficient when constructing the technosphere, biosphere, and
characterization matrices. Brightway2 also has a `processed` folder,
which stores only the data needed to construct the various computational
matrices. These data are stored as [numpy structured
arrays](http://docs.scipy.org/doc/numpy/user/basics.rec.html).

For both databases and LCIA methods, the method `.write(some_data)` will
write an *intermediate* data file, while the subsequent method
`.process()` will transform the `intermediate data` file to an array.
All extraneous information is removed, and only the numeric values
needed are retained. Put another way, *processing* transforms
unstructured data documents to a highly-structured binary form for
calculations. `write` and `process` are intentionally separate, as it is
sometimes desirable to do one and not the other.

`building-matrices` describes how
processed data are turned into matrices for LCA calculations.

```{warning}
Every time you save a new version of an inventory database or an impact assessment method, e.g. with `my_database.write(my_data)`, be sure to also call `my_database.process()`, or your changes will not be used in LCA calculations.
```

### Processing data

*Processing data* converts document data to a binary form tailored for
creating matrices (a NumPy array).

### Mappings

Some LCA data is not numerical, like locations and dataset codes. We
need numerical representations of these values to construct the
processed data arrays, however. In this case, we create a special
dictionary that maps each unique data value to an integer index.
Brightway2 uses two such mappings:

> -   `mapping <mapping>`: Maps inventory
>     objects (activities, biosphere flows, and anything else that would
>     appear in a supply chain graph) to indices.
> -   `geomapping`: Map locations (both
>     inventory and regionalized impact assessment) to indices.

Items are added to mappings using `.add(keys)`, and removed using
`.delete(keys)`. However, managing the different mappings is done for
you automatically.

## Cataloging what we have - Metadata stores

The building blocks in Brightway2 are LCI databases, LCIA methods, etc.
However, we also need to keep track of which LCI databases and LCIA
methods we have, as well as some additional information about them. For
example, LCIA methods have units, and databases can have version
numbers. A *metadata store* stores information about data objects like
databases and methods.

The base class for metadata is `serialized-dict`, which is basically a normal Python dictionary that can be
easily saved or loaded (i.e. serialized) to or from a
[JSON](http://en.wikipedia.org/wiki/JSON) file. These files can be
easily edited in a normal text editor.

Brightway2 defines the following metadata stores:

-   `databases`: LCI databases
-   `methods`: LCIA methods
    (characterization factors)
-   `normalizations`: LCIA normalization
    factors
-   `weightings`: LCIA weighting factors

### Metadata should be singletons

There should be only one instance of each metadata store, to avoid
having conflicting data (the [singleton
pattern](http://en.wikipedia.org/wiki/Singleton_pattern)). The normal
pattern is to instantiate each class in the same file as the class
pattern:

``` python
class MyObjects(bw2data.serialization.SerializedDict):
    file = "sweet-peppers.json"

myobjects = MyObjects()
```

### Using metadata stores

Metadata stores are mostly useful when examining which objects are
available:

``` python
for name in databases:
   print name
"a database name" in databases
```

Metadata stores are also used when deleting data objects:

``` python
del databases["some database to delete"]
```

Finally, and hopefully not surpisingly, metadata stores can be used to
get the actual data object metadata:

``` python
methods[methods.random()]
>> {u'abbreviation': u'recipe-endpoint-ha-wo-lthc.0ba25d5fd76e35b3125224ce78d37151',
    u'unit': u'points'}
```