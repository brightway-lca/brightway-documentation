# Brightway (Versions, Compatibility, etc.)

```{warning}
This version of the documentation is for older releases of Brightway (`legacy` or `brightway2`). It includes only those pages which are relevant to the legacy releases. To access the complete documentation, please switch the the [latest version](https://docs.brightway.dev/en/latest/). The legacy releases [supports the popular Activity Browser user interface](../setup/ui.md), but do not have the latest features of Brightway. You can learn more about [the different versions of Brightway here](../faq/brightway.md).
```

## Brightway Versions and Compatibility

### Brightway2 vs. Brightway25

> Brightway 2.5 is the next generation of the [Brightway2](https://brightway.dev/) framework for life cycle assessment. It provides new capabilities for cloud computing and model interaction, with the use of a new [processed data library](https://github.com/brightway-lca/bw_processing) and a separation between the calculation library and a library for [matrix construction and manipulation](https://github.com/brightway-lca/matrix_utils).

-- from the [Brightway 2.5 repository readme file](https://github.com/brightway-lca/brightway25)

Brightway 2.5 is the next step on the way to the next version of Brightway, as detailed in the [Brightway Strategic Development Plan](https://github.com/brightway-lca/enhancement-proposals/blob/main/Brightway%20strategic%20development%20plan.md). In practice, this means that the meta-packages `brightway-lca/brightway2` and `brightway-lca/brightway25` will install different versions of the Brightway packages. For instance:

| package | Brightway 2 version | Brightway 2.5 version |
| ------- | ------------------- | --------------------- |
| `bw2analyzer` | < 0.10.99 | >= 0.11.1 |
| `bw2calc` | < 1.8.1 | >= 2.0.dev5 |
| `bw2data` | < 3.99 | >= 4.0.dev11 |
| `bw2io` | < 0.8.9 | >= 0.9.dev6 |

This is specified in the respective `setup.py` and `pyproject.toml` files: [Brightway2 packages](https://github.com/brightway-lca/brightway2/blob/master/setup.py)
and [Brightway2.5 packages](https://github.com/brightway-lca/brightway25/blob/main/pyproject.toml).
