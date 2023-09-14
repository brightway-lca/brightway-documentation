# Ecoinvent Database

## Import

### Which `Ecoinvent` file should I download?

Ecoinvent makes several versions of each system model available. For instance:

```
ecoinvent 3.3_xxx_ecoSpold02.7z
ecoinvent 3.3_xxx_lci_ecoSpold02.7z
ecoinvent 3.3_xxx_lcia_ecoSpold02.7z
ecoinvent 3.3_xxx_lcia-cumulated-matrices_xls.7z
ecoinvent 3.3_xxx_lci-cumulated-matrices_xls.7z
```

You want to download and import `ecoinvent 3.3_xxx_ecoSpold02.7z`. If your import process is taking a long time or a lot of memory, double check to make sure you have the right version.

### Unmatched exchanged when importing `Ecoinvent`

Trying to import Ecoinvent 3.8 with `bw2io` like so

```{note}
`<path_to_ecoinvent>` is the path to your Ecoinvent data directory.
```


```python
import bw2io
import bw2data

importer_ei38 = bw2io.SingleOutputEcospold2Importer(
    dirpath = <path_to_ecoinvent>,
    db_name = 'ei38'
)
importer_ei38.apply_strategies()
importer_ei38.statistics()
```

might leave you with many unlinked exchanges:

```python
19565 datasets
629959 exchanges
388452 unlinked exchanges
  Type biosphere: 1018 unique unlinked exchanges
```

Unfortunately, the latest version of `bw2io` can not import older versions of Ecoinvent. Currently, you have to use:

| Ecoinvent version | `bw2io` version |
|-------------------|-----------------|
| <=3.8             | =.8.7           |
| >3.8              | >0.8.7          |


## Why are activity dataset keys so confusing?

`('ecoinvent 2.2', '5bbf...')` seems insane!

It is insane, in the sense that it doesn't make any sense at all to people. Rather, `5bbf2e66f2d75d60726974ac44ab4225` is a computer-generated unique ID. The basic problem is that we need one unique ID for an activity dataset, but there is no ID provided in the ecospold 1 data format. Instead, an activity is uniquely identified by its name, location, category, subcategory, unit, and whether or not it is an infrastructure process! `5bbf2e66f2d75d60726974ac44ab4225` is just an easy way of representing all this information in one string. It is a pain, but there is no good way around it.

Unfortunately, ecospold 2 (the data format used in ecoinvent 3) isn't more approachable - keys will now look like `('ecoinvent 3', 'fff06f42-6c5f-4aea-b695-93bcaba55fed')`. Sorry. At least this time it is ecoinvent generating the unique ID, and not Brightway2.