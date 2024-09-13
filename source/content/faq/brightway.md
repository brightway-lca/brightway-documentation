# Brightway (Versions, Compatibility, etc.)

## Versions and Compatibility

### Versions

#### Brightway 1

Brightway (originally without a version number, here referred to as version 1) was originally developed by Chris Mutel as part of his doctoral research in [the group of Prof. Stefanie Hellweg](https://ifu.ethz.ch/)[^1]. It is no longer available for download.

#### Brightway 2 (`Brightway2`)

```{note}
Learn about upgrading your Brightway 1 projects to Brightway 2 [here](../setup/upgrading.md).
```

Brightway2 was a complete rewrite of the oBrightway 1. It is the most widely used version of Brightway.

```{warning}
Brightway2 is currently the _only_ version of Brightway that is compatible with the [ActivityBrowser graphical user interface](../setup/ui.md).
```

#### Brightway 2.5 (`Brightway25`)

```{note}
Learn about upgrading your Brightway 2 projects to Brightway 2.5 [here](../setup/upgrading.md).
```

> Brightway 2.5 is the next generation of the [Brightway2](https://brightway.dev/) framework for life cycle assessment. It provides new capabilities for cloud computing and model interaction, with the use of a new [processed data library](https://github.com/brightway-lca/bw_processing) and a separation between the calculation library and a library for [matrix construction and manipulation](https://github.com/brightway-lca/matrix_utils).

-- from the [Brightway 2.5 repository readme file](https://github.com/brightway-lca/brightway25)

Brightway 2.5 is the next step on the way to the next version of Brightway, as detailed in the [Brightway Strategic Development Plan](https://github.com/brightway-lca/enhancement-proposals/blob/main/Brightway%20strategic%20development%20plan.md). In practice, this means that the meta-packages `brightway-lca/brightway2` and `brightway-lca/brightway25` will install different versions of the Brightway packages. For instance:

| package | Brightway 2 version | Brightway 2.5 version |
| ------- | ------------------- | --------------------- |
| `bw2analyzer` | < 0.10.99 | >= 0.11.1 |
| `bw2calc` | < 1.8.1 | >= 2.0.dev5 |
| `bw2data` | < 3.99 | >= 4.0.dev11 |
| `bw2io` | < 0.8.9 | >= 0.9.dev6 |

This is specified in the respective `setup.py` files: [Brightway25 packages](https://github.com/brightway-lca/brightway25/blob/main/setup.py) and [Brightway2 packages](https://github.com/brightway-lca/brightway2/blob/master/setup.py).

## Technical Stack

### Storing Python objects in a SQLite3 database is silly! Why not use *X* document database?

Where *X* is one of [MongoDB](https://www.mongodb.com), [CouchDB](http://couchdb.apache.org/), [UnQLite](https://unqlite-python.readthedocs.io/en/latest/), [Vedis](https://vedis-python.readthedocs.io/en/latest/), [CDB](https://cr.yp.to/cdb.html), [TinyDB](http://tinydb.readthedocs.io/en/latest/intro.html), etc.

This approach may seem strange at first, but is the result of coding, evaluating, and ultimately rejecting several alternatives. Most document databases can't store all Python objects directly, because they use JSON or some other serialization. We have actually built and tested database backends built on pickle files, JSON files, MongoDB CodernityDB and BlitzDB. SQLite3 also has several real advantages:

* Most importantly, it is included with Python, no new dependencies or installation steps are required.
* It is famous for being well tested, and is completely cross-platform.
* It is also more than fast enough. For example, loading every activity from ecoinvent 3+ takes only a few seconds.

[^1]: The name "Brightway" comes from two ideas. In German, the pilgrimage paths around Europe are called "Weg", e.g. [Jakobsweg](https://en.wikipedia.org/wiki/Camino_de_Santiago), and there was a (minor) path called the "Bright way" (Hellweg in German 🤯). The idea of a path towards salvation fits open source sustainability assessment software. Brightway was also tremendously supported by Professor Hellweg during its initial development.
