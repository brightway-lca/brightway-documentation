# Stochastic LCA (with Uncertainty)

## Uncertainty Information

### Storage Location

> Where is uncertainty information stored in Brightway?

Uncertainty information is stored at the level of [exchanges](./exchanges.md). \
You can check the kind of uncertainty associated with an exchange:

```python
[exc for exc in eidb.random().exchanges()][0].as_dict()
```

```{note}
The uncertainty type is stored in the `uncertainty_type` key. This key is numeric. Every number corresponds to a different uncertainty type. [The table is defined in the `stats_arrays` package.](https://stats-arrays.readthedocs.io/en/latest/#mapping-parameter-array-columns-to-uncertainty-distributions) Other mathematical parameters are stored in the `loc`, `scale`, `shape`, `minimum`, and `maximum` keys.
```

## Calculate Stochastic LCA Results

> How can I calculate the life-cycle impact assessment (LCIA) results for a given activity with uncertainty?

```{admonition} API Documentation
:class: seealso
{py:obj}`bw2calc.iterative_lca.IterativeLCA`
```
