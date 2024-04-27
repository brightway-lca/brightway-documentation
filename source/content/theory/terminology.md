```{attention}
__HELP WANTED__ \
You can help update and improve the content on this page. \
Please start by reading the [guide to contributing to the Brightway documentation.](../contributing/contributing.md)
```

```{warning}
__NEEDS WORK__ \
This page is not yet complete. \
It is either a rough draft or has been copied over from the legacy documentation.
```

# Terminology
LCA is performed and discussed in many different places. Becuase it is used so widely, some different 'dialects' of terms exist. Below, we show the different terms used in Brightway, [ISO 14044](https://www.iso.org/standard/38498.html)and the Core ontology from Ghose et al. [(2021](https://onlinelibrary.wiley.com/doi/full/10.1111/jiec.13220)).

| Brightway | ISO | Ghose et al. [(2021](https://onlinelibrary.wiley.com/doi/full/10.1111/jiec.13220)) | Note |
| --- | --- | --- | --- |
| __Inventory__ | | | |
| activity | (unit) process<br/><br/>elementary flow*<br/><br/>\*<sub/>ISO defines this more as a 'flow' than a 'process', see also biosphere exchange<sub/> | Activity | An activity in Brightway is the name used for both processes and elementary flows |
| production exchange | _product_*<br/><br/>\*<sub/>a production exchange is not exactly a product in ISO terms, but can also be an energy or material flow<sub/> | DeterminingFlow | The activity exists to do this, e.g. produce a product, service of transporting something, service of treating waste etc. |
| technosphere exchange | intermediate flow | Flow | A flow between two technosphere activities |
| biosphere exchange | elementary flow | Flow | A flow between a biosphere activity to/from a technosphere activity |
| __Impact assessment__ | | | |
| characterization factor | characterization factor | | A biosphere exchange characterized (scaled) to a unit|
| method | impact category | | A set of characterization factors |
| __Calculation__ | | | |
| LCA | LCI | | Life Cycle Inventory |
| LCIA | LCIA | | Life Cycle Impact Assessment |
| demand | functional unit | ReferenceUnit | The demand from the system to calculate for |
