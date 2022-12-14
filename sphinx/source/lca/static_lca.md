# Normal static LCA

The actual LCA class (`bw2calc.LCA`) is more of a coordinator then an
accountant, as the matrix builder is doing much of the data
manipulation. The `lca`{.interpreted-text role="ref"} class only has to
do the following:

> -   Translate the functional unit into a demand array
> -   Find the right parameter arrays, and ask matrix builder for
>     matrices
> -   Solve the linear system $Ax=B$ using
>     [SuperLU](http://crd-legacy.lbl.gov/~xiaoye/SuperLU/) or
>     [UMFpack](http://www.cise.ufl.edu/research/sparse/umfpack/).
> -   Multiply the result by the LCIA CFs, if a LCIA method is present


Due to licensing conflicts, recent versions of SciPy do not include
UMFpack. UMFpack is faster than SuperLU, especially for repeated
calculations. Python wrappers for UMFpack must be installed separately
using [scikits.umfpack](https://github.com/stefanv/umfpack).

The LCA class also has some convenience functions for redoing some
calculations with slight changes, e.g. for uncertainty and sensitivity
analysis. See the \"[redo]()*\" and \"rebuild\_*\" methods in the LCA
class.