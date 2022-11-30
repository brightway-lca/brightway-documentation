:py:mod:`bw2analyzer.econ`
==========================

.. py:module:: bw2analyzer.econ


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2analyzer.econ.gini_coefficient
   bw2analyzer.econ.herfindahl_index
   bw2analyzer.econ.concentration_ratio
   bw2analyzer.econ.theil_index



.. py:function:: gini_coefficient(x)

   Return computed Gini coefficient.

   See https://en.wikipedia.org/wiki/Gini_coefficient

   Adapted from econpy library.
   copyright: 2005-2009 Alan G. Isaac
   license: MIT license
   contact: aisaac AT american.edu

   :param \*x*: Data
   :type \*x*: list or array

   :returns: Gini coefficient (float)


.. py:function:: herfindahl_index(x, normalize=True)

   Return computed Herfindahl index.

   See https://en.wikipedia.org/wiki/Herfindahl_index

   Normalized scores are bounded [0, 1]; non-normalized scores are [1/len(x), 1]. Normalization only counts non-zero values.

   :param \*x*: Data
   :type \*x*: list or array
   :param \*normalize*: Flag to normalize scores.
   :type \*normalize*: bool, default=True

   :returns: Herfindahl index (float)


.. py:function:: concentration_ratio(x, number=4)

   Return computed concentration ratio.

   See https://en.wikipedia.org/wiki/Concentration_ratio

   The concentration ratio measures the share of the market controlled by the top *number* firms. Returned ratio values vary from 0 to 1.

   :param \*x*: Data
   :type \*x*: list or array
   :param \*number*: Number of values to consider. 4 and 8 are commonly used.
   :type \*number*: int, default=4

   :returns: Concentration ratio (float)


.. py:function:: theil_index(x)

   Return Theil entropy index.

   See https://en.wikipedia.org/wiki/Theil_Index

   The Theil index is a measure of economic inequality based on information theory. It is the difference between a dataset's maximum possible entropy and observed entropy.

   :param \*x*: Data
   :type \*x*: list or array

   :returns: Theil index (float)


