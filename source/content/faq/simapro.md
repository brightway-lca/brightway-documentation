# SimaPro Interoperability

## The global warming potential values are different in SimaPro!

The default LCIA characterization factors in Brightway2 come from version 3.5 of the ecoinvent database. For most LCIA methods, these are identical to those found in SimaPro. However, there are important differences for global warming potential:

1. SimaPro does not include a characterization factors for carbon monoxide, but ecoinvent does. Here is the ecoinvent language:

> Emitted CO is transformed in the atmosphere to CO$_2$ after some time. Not all LCIA methods do consider the global warming potential of CO. Most methods are based on factors published by the IPCC (IPCC 2001). It is assumed that CO$_2$ emissions are calculated with the carbon content of the burned fuels and thus all carbon in the fuel is considered. In ecoinvent CO emissions are subtracted from the theoretical CO$_2$ emissions. Thus a GWP factor is calculated for CO (1.57 kg CO$_2$-eq per kg CO). Otherwise processes with higher CO emissions would benefit from this gap. This is especially important for biomass combustion. Neglecting the formation of CO2 from CO would lead in this case to a negative sum of the global warming potential score.

The value of 1.57 is the ratio of the molecular weights of CO$_2$ and CO.

2. SimaPro gives biogenic methane a characterization factor of 22 kg CO$_2$-eq, while ecoinvent gives 25, the same value as for other types of methane.

```{note}
There may be other differences as well - these are the ones we have found.
```