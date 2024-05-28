```{attention}
__HELP WANTED__ \
You can help update and improve the content on this page. \
Please start by reading the [guide to contributing to the Brightway documentation.](contributing)
```

# Terminology

LCA is performed and discussed in many different places. Because it is used so widely, different _dialects_ of terminology exists. Below, we list different terms used by Brightway, the [ISO 14044 standard](https://www.iso.org/standard/38498.html) and the proposed "LCA Core Ontology for the Semantic Web" by [Ghose et al. (2021)](https://doi.org/10.1111/jiec.13220).

| Brightway | ISO | Ghose et al. | Description |
| --- | --- | --- | --- |
| __Inventory__ | | | |
| `activity` | `(unit) process`<br/><br/>`elementary flow`[^1] | `Activity` | An `activity` in Brightway is the name used for both processes and elementary flows. |
| `production exchange` | `product`[^2] | `DeterminingFlow` | This is what is produced or supplied by the `activity` (e.g. manufacturing of a product, provisioning of waste treatment services, etc.). |
| `technosphere exchange` | `intermediate flow` | `Flow` | An exchange between two technosphere `activities`. |
| `biosphere exchange` | `elementary flow` | `Flow` | An exchange between a biosphere `activity` and a technosphere `activity` |
| __Impact assessment__ | | | |
| `characterization factor` | `characterization factor` | | A biosphere `exchange` characterized (scaled) to a unit. |
| `method` | `impact category` | | A set of `characterization factors`. |
| __Calculation__ | | | |
| `LCA` | `LCI` | | Life Cycle Inventory |
| `LCIA` | `LCIA` | | Life Cycle Impact Assessment |
| `demand` | `functional unit` | `ReferenceUnit` | The demand from the system to calculate for (e.g. "one kilogram of steel", etc.). |

[^1]: ISO defines this more as a 'flow' than a 'process', see also biosphere exchange.
[^2]: A production exchange is not exactly a product in ISO terms, but can also be an energy or material flow.