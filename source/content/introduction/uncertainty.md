```{attention}
__HELP WANTED__ \
You can help update and improve the content on this page. \
Please start by reading the [guide to contributing to the Brightway documentation.](../contributing/contributing.md)
```

```{warning}
__NEEDS WORK__ \
This page is not yet complete. \
It has been transfered over from the legacy documentation.
```

# Uncertainty

## Storing uncertain values

While some numeric data is precise, like unit conversions, real-world
data is often uncertain. In Brightway2, uncertain data is stored in a
`uncertainty dictionary`, which is a normal Python dictionary of keys
and values. It has one required key: `amount`, which specifies the most
representative value of the distribution. The most representative value
can be the mean, median (like in the lognormal in the ecoinvent
database), mode (like in the triangular in the ecoinvent database), or
something else - the decision is up to you.

The uncertainty distribution is defined by the key `uncertainty type`.
Depending on the distribution, some or all of the following fields can
also be specified: *loc*, *scale*, *shape*, *minimum*, and *maximum*.

The schema for an `uncertainty dictionary` is:

``` python
uncertainty_dict = {
    "amount": number,  ## This is the only required field
    "uncertainty type": int,
    "loc": number,
    "scale": number,
    "shape": number,
    "minimum": number,
    "maximum": number
}
```

The integer `uncertainty type` fields are defined in a separate software
package called
[stats_arrays](https://stats-arrays.readthedocs.io/en/latest/). The
uncertainty types are given below, and their parameters are explained in
detail in the [stats_arrays
table](https://stats-arrays.readthedocs.io/en/latest/#mapping-parameter-array-columns-to-uncertainty-distributions):

> -   `0`: Undefined or unknown uncertainty.
> -   `1`: No uncertainty.
> -   `2`: Lognormal distribution. This is a tricky distribution to work
>     with, but is [very popular in
>     LCA](http://chris.mutel.org/ecoinvent-lognormal.html). The
>     `amount` field is the median of the data, and the `sigma` field is
>     the standard deviation of the data **when it is log-transformed**,
>     i.e. the σ from the formula for the log-normal PDF.
> -   `3`: Normal distribution.
> -   `4`: Uniform distribution.
> -   `5`: Triangular distribution.
> -   `6`: Bernoulli distribution.
> -   `7`: Discrete uniform.
> -   `8`: Weibull.
> -   `9`: Gamma.
> -   `10`: Beta distribution.
> -   `11`: Generalized Extreme Value.
> -   `12`: Student\'s T.

The default value for `uncertainty type` is `0`, i.e. unknown
uncertainty.

```{note}
All distributions (where bounds make sense) can be bounded, i.e. you can specify a minimum and maximum value in addition to other parameters. This can be helpful in ensuring, for example, that distributions are always positive.
```

In most cases, if you don\'t have uncertain values, or don\'t know
enough to be able to characterize that uncertainty, you can enter a
number **instead of** an uncertainty dictionary, and it will be
automatically converted to an uncertainty dictionary with no
uncertainty.