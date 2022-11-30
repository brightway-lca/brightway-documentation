:py:mod:`bw2analyzer.comparisons`
=================================

.. py:module:: bw2analyzer.comparisons


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2analyzer.comparisons.aggregated_dict
   bw2analyzer.comparisons.compare_dictionaries
   bw2analyzer.comparisons.find_differences_in_inputs
   bw2analyzer.comparisons.compare_activities_by_lcia_score
   bw2analyzer.comparisons.find_leaves
   bw2analyzer.comparisons.get_cpc
   bw2analyzer.comparisons.get_value_for_cpc
   bw2analyzer.comparisons.group_leaves
   bw2analyzer.comparisons.compare_activities_by_grouped_leaves



.. py:function:: aggregated_dict(activity)

   Return dictionary of inputs aggregated by input reference product.


.. py:function:: compare_dictionaries(one, two, rel_tol=0.0001, abs_tol=1e-09)

   Compare two dictionaries with form ``{str: float}``, and return a set of keys where differences where present.

   Tolerance values are inputs to `math.isclose <https://docs.python.org/3/library/math.html#math.isclose>`__.


.. py:function:: find_differences_in_inputs(activity, rel_tol=0.0001, abs_tol=1e-09, locations=None, as_dataframe=False)

   Given an ``Activity``, try to see if other activities in the same database (with the same name and
   reference product) have the same input levels.

   Tolerance values are inputs to `math.isclose <https://docs.python.org/3/library/math.html#math.isclose>`__.

   If differences are present, a difference dictionary is constructed, with the form:

   .. code-block:: python

       {Activity instance: [(name of input flow (str), amount)]}

   Note that this doesn't reference a specific exchange, but rather sums **all exchanges with the same input reference product**.

   Assumes that all similar activities produce the same amount of reference product.

   ``(x, y)``, where ``x`` is the number of similar activities, and ``y`` is a dictionary of the differences. This dictionary is empty if no differences are found.

   :param activity: ``Activity``. Activity to analyze.
   :param rel_tol: float. Relative tolerance to decide if two inputs are the same. See above.
   :param abs_tol: float. Absolute tolerance to decide if two inputs are the same. See above.
   :param locations: list, optional. Locations to restrict comparison to, if present.
   :param as_dataframe: bool. Return results as pandas DataFrame.

   :returns: dict or ``pandas.DataFrame``.


.. py:function:: compare_activities_by_lcia_score(activities, lcia_method, band=0.1)

   Compare selected activities to see if they are substantially different.

   Substantially different means that all LCIA scores lie within a band of ``band * max_lcia_score``.

   Inputs:

       ``activities``: List of ``Activity`` objects.
       ``lcia_method``: Tuple identifying a ``Method``

   :returns: Nothing, but prints to stdout.


.. py:function:: find_leaves(activity, lcia_method, results=None, lca_obj=None, amount=1, total_score=None, level=0, max_level=3, cutoff=0.025)

   Traverse the supply chain of an activity to find leaves - places where the impact of that
   component falls below a threshold value.

   Returns a list of ``(impact of this activity, amount consumed, Activity instance)`` tuples.


.. py:function:: get_cpc(activity)


.. py:function:: get_value_for_cpc(lst, label)


.. py:function:: group_leaves(leaves)

   Group elements in ``leaves`` by their `CPC (Central Product Classification) <https://unstats.un.org/unsd/classifications/Econ/cpc>`__ code.

   Returns a list of ``(fraction of total impact, specific impact, amount, Activity instance)`` tuples.


.. py:function:: compare_activities_by_grouped_leaves(activities, lcia_method, mode='relative', max_level=4, cutoff=0.0075, output_format='list', str_length=50)

   Compare activities by the impact of their different inputs, aggregated by the product classification of those inputs.

   :param activities: list of ``Activity`` instances.
   :param lcia_method: tuple. LCIA method to use when traversing supply chain graph.
   :param mode: str. If "relative" (default), results are returned as a fraction of total input. Otherwise, results are absolute impact per input exchange.
   :param max_level: int. Maximum level in supply chain to examine.
   :param cutoff: float. Fraction of total impact to cutoff supply chain graph traversal at.
   :param output_format: str. See below.
   :param str_length; int. If ``output_format`` is ``html``:
   :param this controls how many characters each column label can have.:

   :raises ValueError: ``activities`` is malformed.

   :returns:

             * ``list``: Tuple of ``(column labels, data)``
             * ``html``: HTML string that will print nicely in Jupyter notebooks.
             * ``pandas``: a pandas ``DataFrame``.
   :rtype: Depends on ``output_format``


