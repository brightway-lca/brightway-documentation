# Brightway (Versions, Compatibility, etc.)

## Brightway Versions and Compatibility

### Brightway Versions

#### Brightway 1

Brightway (originally without a version number, here referred to as version 1) was originally developed by Chris Mutel as part of his doctoral research in [the group of Prof. Stefanie Hellweg](https://ifu.ethz.ch/)[^1]. It is no longer available for download.

#### Brightway 2 (`Brightway2`)

```{note}
Learn about upgrading your Brightway 1 projects to Brightway 2 [here](../setup/upgrading.md).
```

Brightway2 is a complete rewrite of Brightway 1. It is the most widely used version of Brightway. It supports the [ActivityBrowser graphical user interface](../setup/ui.md).

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

[^1]: The German surname _Hellweg_ translates to _Brightway_ in English 🤯