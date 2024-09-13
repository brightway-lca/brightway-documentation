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
