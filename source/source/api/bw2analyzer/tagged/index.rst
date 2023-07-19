:py:mod:`bw2analyzer.tagged`
============================

.. py:module:: bw2analyzer.tagged


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2analyzer.tagged.aggregate_tagged_graph
   bw2analyzer.tagged.get_cum_impact
   bw2analyzer.tagged.get_multi_cum_impact
   bw2analyzer.tagged.multi_aggregate_tagged_graph
   bw2analyzer.tagged.multi_recurse_tagged_database
   bw2analyzer.tagged.multi_traverse_tagged_databases
   bw2analyzer.tagged.recurse_tagged_database
   bw2analyzer.tagged.traverse_tagged_databases



.. py:function:: aggregate_tagged_graph(graph)

   Aggregate a graph produced by ``recurse_tagged_database`` by the provided tags.

   Outputs a dictionary with keys of tags and numeric values.

   .. code-block:: python

       {'a tag': summed LCIA scores}



.. py:function:: get_cum_impact(graph, max_levels=100)

   Add cumulative impact ``cum_impact`` to each ``technosphere`` level of a tagged graph.

   This function recurses until all levels in the graph have been checked, or the ``max_levels`` cutoff is reached

   Input arguments:
       * ``graph``: A tagged supply chain graph from ``recurse_tagged_database``.
       * ``max_levels``: maximum number of graph levels to check before giving up. Default is 100.

   :returns: Tagged supply chain graph with additional cumulative impact ``cum_impact`` key at each ``technosphere`` level.


.. py:function:: get_multi_cum_impact(graph, max_levels=100)

   Add cumulative impact ``cum_impact`` to each ``technosphere`` level of a multi method tagged graph.

   This function recurses until all levels in the graph have been checked, or the ``max_levels`` cutoff is reached

   Input arguments:
       * ``graph``: A tagged supply chain graph from ``multi_recurse_tagged_database``.
       * ``max_levels``: maximum number of graph levels to check before giving up. Default is 100.

   :returns: Tagged supply chain graph with additional cumulative impact ``cum_impact`` key at each ``technosphere`` level.


.. py:function:: multi_aggregate_tagged_graph(graph)

   Aggregate a graph produced by ``multi_recurse_tagged_database`` by the provided tags.

   Outputs a dictionary with keys of tags and numeric values.

   Note: this only aggregates on the primary tag, secondary tags are not aggregated

   .. code-block:: python

       {'a tag': [list of summed LCIA scores with one sum per method]}



.. py:function:: multi_recurse_tagged_database(activity, amount, methods, method_dicts, lca, label, default_tag, secondary_tags=[])

   Traverse a foreground database and assess activities and biosphere flows by tags using multiple methods.

   Input arguments:

       * ``activity``: Activity tuple or object
       * ``amount``: float
       * ``methods``: list of LCA methods (tuples)
       * ``method_dicts``: list of dictionaries of biosphere flow tuples to CFs, e.g. ``{("biosphere", "foo"): 3}`` corresponding to methods in ``methods``
       * ``lca``: An ``LCA`` object that is already initialized, i.e. has already calculated LCI
       * ``label``: string
       * ``default_tag``: string
       * ``secondary_tags``: list of tuples in the format (secondary_label, secondary_default_tag). Default is empty list.

   Returns:

   .. code-block:: python

       {
           'activity': activity object,
           'amount': float,
           'tag': string,
           'secondary_tags': [list of strings],
           'impact': [list of floats (impact of inputs from outside foreground database) with one element per method],
           'biosphere': [{
               'amount': float,
               'impact': [list of floats with one element per method],
               'tag': string,
               'secondary_tags': [list of strings]
           }],
           'technosphere': [this data structure]
       }



.. py:function:: multi_traverse_tagged_databases(functional_unit, methods, label='tag', default_tag='other', secondary_tags=[])

   Traverse a functional unit throughout its foreground database(s), and
   group impacts (for multiple methods) by tag label.

   Input arguments:
       * ``functional_unit``: A functional unit dictionary, e.g. ``{("foo", "bar"): 42}``.
       * ``methods``: A list of method names, e.g. ``[("foo", "bar"), ("baz", "qux"), ...]``
       * ``label``: The label of the tag classifier. Default is ``"tag"``
       * ``default_tag``: The tag classifier to use if none was given. Default is ``"other"``
       * ``secondary_tags``: List of tuples in the format (secondary_label, secondary_default_tag). Default is empty list.

   :returns: Aggregated tags dictionary from ``aggregate_tagged_graph``, and tagged supply chain graph from ``recurse_tagged_database``.


.. py:function:: recurse_tagged_database(activity, amount, method_dict, lca, label, default_tag, secondary_tags=[], fg_databases=None, warned=False)

   Traverse a foreground database and assess activities and biosphere flows by tags.


   Input arguments:

       * ``activity``: Activity tuple or object
       * ``amount``: float
       * ``method_dict``: Dictionary of biosphere flow tuples to CFs, e.g. ``{("biosphere", "foo"): 3}``
       * ``lca``: An ``LCA`` object that is already initialized, i.e. has already calculated LCI and LCIA with same method as in ``method_dict``
       * ``label``: string
       * ``default_tag``: string
       * ``secondary_tags``: List of tuples in the format (secondary_label, secondary_default_tag). Default is empty list.

       * ``fg_databases``: a list of foreground databases to be traversed, e.g. ['foreground', 'biomass', 'machinery']
                           It's not recommended to include all databases of a project in the list to be traversed, especially not ecoinvent itself

   Returns:

   .. code-block:: python

       {
           'activity': activity object,
           'amount': float,
           'tag': string,
           'secondary_tags': [list of strings],
           'impact': float (impact of inputs from outside foreground database),
           'biosphere': [{
               'amount': float,
               'impact': float,
               'tag': string,
               'secondary_tags': [list of strings]
           }],
           'technosphere': [this data structure]
       }



.. py:function:: traverse_tagged_databases(functional_unit, method, label='tag', default_tag='other', secondary_tags=[], fg_databases=None)

   Traverse a functional unit throughout its foreground database(s) or the
   listed databses in fg_databses, and group impacts by tag label.

   Contribution analysis work by linking impacts to individual activities.
   However, you also might want to group impacts in other ways. For example,
   give individual biosphere exchanges their own grouping, or aggregate two
   activities together.

   Consider this example system, where the letters are the tag labels, and the
   numbers are exchange amounts. The functional unit is one unit of the tree
   root.

   .. image:: images/tagged-traversal.png
      :alt: Example tagged supply chain

   In this supply chain, tags are applied to activities and biosphere exchanges.
   If a biosphere exchange is not tagged, it inherits the tag of its producing
   activity. Similarly, links to other databases are assessed with the usual
   LCA machinery, and the total LCA score is tagged according to its consuming
   activity. If an activity does not have a tag, a default tag is applied.

   We can change our visualization to show the use of the default tags:

   .. image:: images/tagged-traversal-2.png
      :alt: Example tagged supply chain

   And then we can manually calculate the tagged impacts. Normally we would
   need to know the actual biosphere flows and their respective
   characterization factors (CF), but in this example we assume that each
   CF is one. Our result, group by tags, would therefore be:

       * **A**: :math:`6 + 27 = 33`
       * **B**: :math:`30 + 44 = 74`
       * **C**: :math:`5 + 16 + 48 = 69`
       * **D**: :math:`14`

   This function will only traverse the foreground database, i.e. the
   database of the functional unit activity. A functional unit can have
   multiple starting nodes; in this case, all foreground databases are
   traversed.

   Input arguments:

       * ``functional_unit``: A functional unit dictionary, e.g. ``{("foo", "bar"): 42}``.
       * ``method``: A method name, e.g. ``("foo", "bar")``
       * ``label``: The label of the tag classifier. Default is ``"tag"``
       * ``default_tag``: The tag classifier to use if none was given. Default is ``"other"``
       * ``secondary_tags``: List of tuples in the format (secondary_label, secondary_default_tag). Default is empty list.
       * ``fg_databases``: a list of foreground databases to be traversed, e.g. ['foreground', 'biomass', 'machinery']
                           It's not recommended to include all databases of a project in the list to be traversed, especially not ecoinvent itself

   :returns: Aggregated tags dictionary from ``aggregate_tagged_graph``, and tagged supply chain graph from ``recurse_tagged_database``.


