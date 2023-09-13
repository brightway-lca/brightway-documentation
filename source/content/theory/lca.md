# LCA

## Specifying a functional unit

The functional unit for any LCA calculation is a dictionary of keys and
amounts:

``` python
{
    ("a database", "the answer"): 42,
    ("a database", "pi"): 3.14159265358979
}
```

However, you can also use a `Activity` proxy:

``` python
In [1]: from brightway2 import *

In [2]: activity = Database("ecoinvent 3.2 cutoff").random()

In [3]: type(activity), activity
Out[3]:
(bw2data.backends.peewee.proxies.Activity,
 'quicklime production, milled, packed' (kilogram, CH, None))

In [4]: lca = LCA({activity: 1})

In [5]: lca.demand
Out[5]: {'quicklime production, milled, packed' (kilogram, CH, None): 1}
```

How does this work? It is quite simple - the `Activity` proxy knows how
to pretend to be a key tuple:

``` python
In [7]: activity[0], activity[1]
Out[7]: ('ecoinvent 3.2 cutoff', 'ab2f7a551a06a59de9191065128233e4')

In [8]: activity == ('ecoinvent 3.2 cutoff', 'ab2f7a551a06a59de9191065128233e4')
Out[8]: True
```

This is an instance of [duck
typing](https://en.wikipedia.org/wiki/Duck_typing) - if it walks like a
duck and quacks like a duck, then we can treat it like a duck.

If you are interested in the details, see how
`bw2data.proxies.ActivityProxyBase` defines `__getitem__` and other `__`
magic methods.

## Turning processed data arrays in matrices {#building-matrices}

A parameter array is a NumPy [structured or record
array](http://docs.scipy.org/doc/numpy/user/basics.rec.html), where each
column has a label and data type. Here is an sample of the parameter
array for the US LCI:

  input   output   row          col          type   amount
  ------- -------- ------------ ------------ ------ --------
  9829    9829     4294967295   4294967295   0      1.0
  9708    9708     4294967295   4294967295   0      1.0
  9633    9633     4294967295   4294967295   0      1.0
  9276    9276     4294967295   4294967295   0      3.0999
  8778    8778     4294967295   4294967295   0      1.0
  9349    9349     4294967295   4294967295   0      1000.0
  5685    9349     4294967295   4294967295   2      14.895
  9516    9349     4294967295   4294967295   1      1032.7
  9433    9349     4294967295   4294967295   1      4.4287
  8838    9349     4294967295   4294967295   1      1.5490

There are also some columns for uncertainty information, but these would
only be a distraction for now. The complete spec for the uncertainty
fields is given in the [stats_arrays
documentation](http://stats-arrays.readthedocs.io/en/latest/).

We notice several things:

> -   Both the `input` and `output` columns have numbers, but we don\'t
>     know what they mean yet
> -   Both the `row` and `col` columns are filled with a large number
> -   The `type` column has only a few values, but they are also
>     mysterious
> -   The `amount` column is the only one that seems reasonable, and
>     gives the values that should be inserted into the matrix

### Input and Output

The `input` and `output` columns gives values for biosphere flows or
transforming activity data sets. The `mapping`
is used to translate keys like `("Douglas Adams", 42)` into
integer values. So, each mapping number uniquely identifies an activity
dataset.

If the `input` and `output` values are the same, then this is a
production exchange - it describes how much product is produced by the
transforming activity dataset.

::: warning
::: title
Warning
:::

Integer mapping ids are not transferable from machine to machine or
installation to installation, as the order of insertion (and hence the
integer id) is more or less at random. Always `.process()` datasets on a
new machine.
:::

### Rows and columns

The `row` and `col` columns have the data type *unsigned integer, 32
bit*, and the maximum value is therefore $2^{32} - 1$, i.e. 4294967295.
This is just a dummy value telling Brightway2 to insert better data.

The method `MatrixBuilder.build_dictionary` is used to take `input` and
`output` values, respectively, and figure out which rows and columns
they correspond to. The actual code is succinct - only one line - but
what it does is:

> 1.  Get all unique values, as each value will appear multiple times
> 2.  Sort these values
> 3.  Give them integer indices, starting with zero

For our example parameter array, the dictionary from `input` values to
`row` would be:

``` python
{5685: 0,
 8778: 1,
 8838: 2,
 9276: 3,
 9349: 4,
 9433: 5,
 9516: 6,
 9633: 7,
 9708: 8,
 9829: 9}
```

And the dictionary from `output` to `col` would be:

``` python
{8778: 0,
 9276: 1,
 9349: 2,
 9633: 3,
 9708: 4,
 9829: 5}
```

The method `MatrixBuilder.add_matrix_indices` would replace the
4294967295 values with dictionary values based on `input` and `output`.
At this point, we have enough to build a sparse matrix using
`MatrixBuilder.build_matrix`:

  row   col   amount
  ----- ----- --------
  9     5     1.0
  8     4     1.0
  7     3     1.0
  3     1     3.0999
  1     0     1.0
  4     2     1000.0
  0     2     14.895
  6     2     1032.7
  5     2     4.4287
  2     2     1.5490

Indeed, the [coordinate (coo)
matrix](http://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.coo_matrix.html)
takes as inputs exactly the row and column indices, and the values to
insert.

Of course, there are some details for specific matrices - technosphere
matrices need to be square, and should have ones by default on the
diagonal, etc. etc., but this is the general idea.

### Types

The `type` column indicates whether a value should be in the
technosphere or biosphere matrix: `0` is a transforming activity
production amount, `1` is a technosphere exchange, and `2` is a
biosphere exchange.



## Brightway2 LCA Reports


The Brightway2 report data format is evolving, and this section should
not be understood as definitive.
:::

LCA reports calculated with `bw2analyzer.report.SerializedLCAReport` are
written as a JSON file to disk. It has the following data format:

``` python
{
    "monte carlo": {
        "statistics": {
            "interval": [lower, upper values],
            "median": median,
            "mean": mean
        },
        "smoothed": [  ## This is smoothed values for drawing empirical PDF
            [x, y],
        ],
        "histogram": [  ## This are point coordinates for each point when drawing histogram bins
            [x, y],
        ]
    },
    "score": LCA score,
    "activity": [
        [name, amount, unit],
    ],
    "contribution": {
        "hinton": {
            "xlabels": [
                label,
            ],
            "ylabels": [
                label,
            ],
            "total": LCA score,
            "results": [
                [x index, y index, score], ## See hinton JS implementation in bw2ui source code
            ],
        },
        "treemap": {
            "size:" LCA score,
            "name": "LCA result",
            "children": [
                {
                "name": activity name,
                "size": activity LCA score
                },
            ]
        }
        "herfindahl": herfindahl score,
        "concentration": concentration score
    },
    "method": {
        "name": method name,
        "unit": method unit
    },
    "metadata": {
        "version": report data format version number (this is 1),
        "type": "Brightway2 serialized LCA report",
        "uuid": the UUID of this report,
        "online": URL where this report can be accessed. Optional.
    }
}
```