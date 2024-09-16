# Negative or Confusing LCA Results

(difference-stochastic)=
## Why is my average stochastic LCA score so different from my static score?

When performing Monte Analysis, we are at the mercy of the uncertainty descriptions given in our data. If these values are different than the fixed static value, then our uncertainty analysis will naturally produce different results and statistical moments.

The exact cause of this difference varies depending on the modelling assumptions you have used and the databases you are using. We have seen the following:

* Databases which use the [lognormal distribution](https://en.wikipedia.org/wiki/Log-normal_distribution) extensively, but use the [*median* value of the distribution for the static value](https://chris.mutel.org/too-confusing.html). The median of the lognormal is always less than the average, and the difference between these results depends on how wide the distribution is. This is [often the case with ecoinvent](https://chris.mutel.org/ecoinvent-lognormal.html), for example. Consider reporting the median instead of the mean of the uncertainty analysis distribution to weaken this effect.
* Databases have errors in their uncertainty data which bias uncertainty results toward higher numbers. Databases which use asymmetric distributions like the lognormal extensively need to pay special attention to the uncertainty parameters, as even a single incorrect value can significantly change LCA scores. See [this notebook](https://github.com/brightway-lca/brightway2/blob/master/notebooks/Investigating%20interesting%20Monte%20Carlo%20results.ipynb) on diagnosing such a problem in ecoinvent 3.8, and [this notebook](https://github.com/brightway-lca/brightway2/blob/master/notebooks/Fixing%20large%20uncertainty%20distributions.ipynb) on how to fix it.

## Do my unit processes need to produce a *net* or *gross* production amount of one?

You don't need to normalize your data in Brightway! This is just another step where math or data errors can enter the process. Instead, it's much easier to put in the actual measure amounts of all inputs and outputs. Consumers of your outputs can still ask for however much of the functional products they need, and Brightway will get the math right. See [this blog post](https://chris.mutel.org/non-unitary.html) on non-unitary production amounts, and [this blog post](https://chris.mutel.org/too-confusing.html) on self-consumption in LCA.

## Why do I get negative static LCA results?

Depending on the LCIA method and functional unit, some LCA scores might be negative. Not everything is bad for the environment! We often do LCA of carbon capture or [phytoremediation](https://en.wikipedia.org/wiki/Phytoremediation).

See the [LCA cheat sheet](../cheatsheet/lca.md) for ways to isolate where negative impacts are coming from.

## Why do I get negative stochastic LCA results?

If you static score is positive, but you see negative scores when doing Monte Carlo analysis, there can be several factors at play:

* The uncertainty data could just be [be incorrect](difference-stochastic).
* The uncertainty data could include agricultural processes where some flows are modelled with a [normal distribution](https://en.wikipedia.org/wiki/Normal_distribution) which has a very small mean value, and a very high standard deviation. In these cases, there is a roughly fifty percent chance that the scores will be negative.
* There could be cases where an input is both produced and consumed in a process. For example, it is common to have both land transformation into and out of a process; water use is often modelled the same way. In this case, the database does not include logical links between the input and the output, and each has their own uncertainty distributions. These two distributions are sampled *independently*, and it relatively common for the output amount to draw a higher sample than the input amount, meaning that a resource is being net produced or an emission is being net removed from the environment. The only way to fix this is with a different modelling paradigm which reflects logical relationships or physical constraints, and better data.
* Similarly, if a process models water intake and output separately, but uses different flows for the input and output, then its possible for the impact category to characterize them differently (or not characterize one at all), allowing for unusual results to appear during Monte Carlo analysis.

See more discussion on a [Brightway development discussion thread](https://brightway.groups.io/g/development/topic/negative_values_in/105163086).
