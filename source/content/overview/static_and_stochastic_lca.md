```{attention}
__HELP WANTED__ \
You can help update and improve the content on this page. \
Please start by reading the [guide to contributing to the Brightway documentation.](contributing)
```

```{warning}
__NEEDS WORK__ \
This page is not yet complete. \
It is either a rough draft or has been copied over from the legacy documentation.
```

# Normal Static LCA

The actual LCA class (`bw2calc.LCA`) is more of a coordinator then an
accountant, as the matrix builder is doing much of the data
manipulation. The `lca` class only has to do the following:

-   Translate the functional unit into a demand array
-   Find the right parameter arrays, and ask matrix builder for matrices
-   Solve the linear system $Ax=B$ using [SuperLU](http://crd-legacy.lbl.gov/~xiaoye/SuperLU/) or [UMFpack](http://www.cise.ufl.edu/research/sparse/umfpack/).
- Multiply the result by the LCIA CFs, if a LCIA method is present

Due to licensing conflicts, recent versions of SciPy do not include UMFpack. UMFpack is faster than SuperLU, especially for repeated calculations. Python wrappers for UMFpack must be installed separately using [scikits.umfpack](https://github.com/stefanv/umfpack).

The LCA class also has some convenience functions for redoing some calculations with slight changes, e.g. for uncertainty and sensitivity
analysis. See the `redo()*\` and `rebuild_*` methods in the LCA class.

# Stochastic LCA

The various stochastic Monte Carlo LCA classes function almost the same
as the static LCA, and reuse most of the code. The only change is that
instead of building matrices once, [random number generators from
stats_arrays](http://stats-arrays.readthedocs.io/en/latest/mcrng.html#monte-carlo-random-number-generator)
are instantiated directly from each parameter array. For each Monte
Carlo iteration, the `amount` column is then overwritten with the output
from the random number generator, and the system solved as normal. The
code to do a new Monte Carlo iteration is quite succinct:

``` python
def next(self):
    self.rebuild_technosphere_matrix(self.tech_rng.next())
    self.rebuild_biosphere_matrix(self.bio_rng.next())
    if self.lcia:
        self.rebuild_characterization_matrix(self.cf_rng.next())

    self.lci_calculation()

    if self.lcia:
        self.lcia_calculation()
        return self.score
    else:
        return self.supply_array
```

This design is one of the most elegant parts of Brightway2.

Because there is a common procedure to build static and stochastic
matrices, any matrix can easily support uncertainty, e.g. not just LCIA
characterization factors, but also weighting, normalization, and
anything else you can think of; see [Defining a new Matrix - example of
Weighting and Normalization
matrices](https://github.com/brightway-lca/brightway2/blob/master/notebooks/Defining%20a%20new%20Matrix%20-%20example%20of%20Weighting%20and%20Normalization.ipynb).