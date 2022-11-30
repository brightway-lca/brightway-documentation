:py:mod:`bw2analyzer`
=====================

.. py:module:: bw2analyzer


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   comparisons/index.rst
   contribution/index.rst
   econ/index.rst
   health_check/index.rst
   lci/index.rst
   matrix_grapher/index.rst
   page_rank/index.rst
   report/index.rst
   sc_graph/index.rst
   tagged/index.rst
   utils/index.rst
   version/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   bw2analyzer.ContributionAnalysis
   bw2analyzer.DatabaseHealthCheck
   bw2analyzer.PageRank
   bw2analyzer.GTManipulator



Functions
~~~~~~~~~

.. autoapisummary::

   bw2analyzer.compare_activities_by_grouped_leaves
   bw2analyzer.compare_activities_by_lcia_score
   bw2analyzer.find_differences_in_inputs
   bw2analyzer.traverse_tagged_databases
   bw2analyzer.print_recursive_calculation
   bw2analyzer.print_recursive_supply_chain



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


.. py:function:: compare_activities_by_lcia_score(activities, lcia_method, band=0.1)

   Compare selected activities to see if they are substantially different.

   Substantially different means that all LCIA scores lie within a band of ``band * max_lcia_score``.

   Inputs:

       ``activities``: List of ``Activity`` objects.
       ``lcia_method``: Tuple identifying a ``Method``

   :returns: Nothing, but prints to stdout.


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


.. py:class:: ContributionAnalysis

   .. py:method:: sort_array(data, limit=25, limit_type='number', total=None)

      Common sorting function for all ``top`` methods. Sorts by highest value first.

      Operates in either ``number`` or ``percent`` mode. In ``number`` mode, return ``limit`` values. In ``percent`` mode, return all values >= (total * limit); where ``0 < limit <= 1``.

      Returns 2-d numpy array of sorted values and row indices, e.g.:

      .. code-block:: python

          ContributionAnalysis().sort_array((1., 3., 2.))

      returns

      .. code-block:: python

          (
              (3, 1),
              (2, 2),
              (1, 0)
          )

      :param \* *data*: A 1-d array of values to sort.
      :type \* *data*: numpy array
      :param \* *limit*: Number of values to return, or percentage cutoff.
      :type \* *limit*: number, default=25
      :param \* *limit_type*: Either ``number`` or ``percent``.
      :type \* *limit_type*: str, default=``number``
      :param \* *total*: Optional specification of summed data total.
      :type \* *total*: number, default=None

      :returns: 2-d numpy array of values and row indices.


   .. py:method:: top_matrix(matrix, rows=5, cols=5)

      Find most important (i.e. highest summed) rows and columns in a matrix, as well as the most corresponding non-zero individual elements in the top rows and columns.

      Only returns matrix values which are in the top rows and columns. Element values are returned as a tuple: ``(row, col, row index in top rows, col index in top cols, value)``.

      Example:

      .. code-block:: python

          matrix = [
              [0, 0, 1, 0],
              [2, 0, 4, 0],
              [3, 0, 1, 1],
              [0, 7, 0, 1],
          ]

      In this matrix, the row sums are ``(1, 6, 5, 8)``, and the columns sums are ``(5, 7, 6, 2)``. Therefore, the top rows are ``(3, 1)`` and the top columns are ``(1, 2)``. The result would therefore be:

      .. code-block:: python

          (
              (
                  (3, 1, 0, 0, 7),
                  (3, 2, 0, 1, 1),
                  (1, 2, 1, 1, 4)
              ),
              (3, 1),
              (1, 2)
          )

      :param \* *matrix*: Any Python object that supports the ``.sum(axis=)`` syntax.
      :type \* *matrix*: array or matrix
      :param \* *rows*: Number of rows to select.
      :type \* *rows*: int
      :param \* *cols*: Number of columns to select.
      :type \* *cols*: int

      :returns: (elements, top rows, top columns)


   .. py:method:: hinton_matrix(lca, rows=5, cols=5)


   .. py:method:: annotate(sorted_data, rev_mapping)

      Reverse the mapping from database ids to array indices


   .. py:method:: top_processes(matrix, **kwargs)

      Return an array of [value, index] technosphere processes.


   .. py:method:: top_emissions(matrix, **kwargs)

      Return an array of [value, index] biosphere emissions.


   .. py:method:: annotated_top_processes(lca, names=True, **kwargs)

      Get list of most damaging processes in an LCA, sorted by ``abs(direct impact)``.

      Returns a list of tuples: ``(lca score, supply, activity)``. If ``names`` is False, they returns the process key as the last element.



   .. py:method:: annotated_top_emissions(lca, names=True, **kwargs)

      Get list of most damaging biosphere flows in an LCA, sorted by ``abs(direct impact)``.

      Returns a list of tuples: ``(lca score, inventory amount, activity)``. If ``names`` is False, they returns the process key as the last element.



   .. py:method:: get_name(key)


   .. py:method:: d3_treemap(matrix, rev_bio, rev_techno, limit=0.025, limit_type='percent')

      Construct treemap input data structure for LCA result. Output like:

      .. code-block:: python

          {
          "name": "LCA result",
          "children": [{
              "name": process 1,
              "children": [
                  {"name": emission 1, "size": score},
                  {"name": emission 2, "size": score},
                  ],
              }]
          }




.. py:class:: DatabaseHealthCheck(database)

   .. py:method:: check(graphs_dir=None)


   .. py:method:: make_graphs(graphs_dir=None)


   .. py:method:: page_rank()


   .. py:method:: unique_exchanges()


   .. py:method:: uncertainty_check()


   .. py:method:: multioutput_processes()


   .. py:method:: aggregated_processes(cutoff=500)


   .. py:method:: no_self_production()



.. py:class:: PageRank(database)

   .. py:method:: calculate()


   .. py:method:: page_rank(technosphere, alpha=0.85, max_iter=100, tol=1e-06)

      Return the PageRank of the nodes in the graph.

      Adapted from http://networkx.lanl.gov/svn/networkx/trunk/networkx/algorithms/link_analysis/pagerank_alg.py

      PageRank computes a ranking of the nodes in the graph G based on
      the structure of the incoming links. It was originally designed as
      an algorithm to rank web pages.

      The eigenvector calculation uses power iteration with a SciPy
      sparse matrix representation.

      :param \* *technosphere*: The technosphere matrix.
      :type \* *technosphere*: scipy sparse matrix
      :param \* *alpha*: Damping parameter for PageRank, default=0.85
      :type \* *alpha*: float, optional

      :returns:

                * Dictionary of nodes (activity codes) with value as PageRank

      References

      .. [1] A. Langville and C. Meyer,
         "A survey of eigenvector methods of web information retrieval."
         http://citeseer.ist.psu.edu/713792.html
      .. [2] Page, Lawrence; Brin, Sergey; Motwani, Rajeev and Winograd, Terry,
         The PageRank citation ranking: Bringing order to the Web. 1999
         http://dbpubs.stanford.edu:8090/pub/showDoc.Fulltext?lang=en&doc=1999-66&format=pdf



.. py:class:: GTManipulator

   Manipulate ``GraphTraversal`` results.

   .. py:method:: unroll_graph(nodes, edges, score, cutoff=0.005, max_links=2500)
      :staticmethod:

      Unroll a ``GraphTraversal`` result, allowing the same activity to appear in the graph multiple times.


   .. py:method:: add_metadata(nodes, lca)
      :staticmethod:

      Add metadata to nodes, like name, unit, and category.


   .. py:method:: d3_force_directed(nodes, edges, score)
      :staticmethod:

      Reformat to D3 style, which is a list of nodes, and edge ids are node list indices.


   .. py:method:: simplify(nodes, edges, score, limit=0.005)
      :staticmethod:

      Simplify supply chain to include only nodes which individually contribute ``limit * score``.

      Only removes and combines edges; doesn't check to make sure amounts add up correctly.


   .. py:method:: simplify_naive(nodes, edges, score, limit=0.0025)
      :staticmethod:

      Naive simplification which simplifies removes links below an LCA score cutoff. Orphan nodes are also deleted.


   .. py:method:: d3_treemap(nodes, edges, lca, add_biosphere=False)
      :staticmethod:

      Add node data by traversing the graph; assign different metadata to leaf nodes.



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


.. py:function:: print_recursive_calculation(activity, lcia_method, amount=1, max_level=3, cutoff=0.01, file_obj=None, tab_character='  ', use_matrix_values=False, _lca_obj=None, _total_score=None, __level=0, __first=True)

   Traverse a supply chain graph, and calculate the LCA scores of each component. Prints the result with the format:

   {tab_character * level }{fraction of total score} ({absolute LCA score for this input} | {amount of input}) {input activity}

   :param activity: ``Activity``. The starting point of the supply chain graph.
   :param lcia_method: tuple. LCIA method to use when traversing supply chain graph.
   :param amount: int. Amount of ``activity`` to assess.
   :param max_level: int. Maximum depth to traverse.
   :param cutoff: float. Fraction of total score to use as cutoff when deciding whether to traverse deeper.
   :param file_obj: File-like object (supports ``.write``), optional. Output will be written to this object if provided.
   :param tab_character: str. Character to use to indicate indentation.
   :param use_matrix_values: bool. Take exchange values from the matrix instead of the exchange instance ``amount``. Useful for Monte Carlo, but can be incorrect if there is more than one exchange from the same pair of nodes.

   Normally internal args:
       _lca_obj: ``LCA``. Can give an instance of the LCA class (e.g. when doing regionalized or Monte Carlo LCA)
       _total_score: float. Needed if specifying ``_lca_obj``.

   Internal args (used during recursion, do not touch);
       __level: int.
       __first: bool.

   :returns: Nothing. Prints to ``sys.stdout`` or ``file_obj``


.. py:function:: print_recursive_supply_chain(activity, amount=1, max_level=2, cutoff=0, file_obj=None, tab_character='  ', __level=0)

   Traverse a supply chain graph, and prints the inputs of each component.

   This function is only for exploration; use ``bw2calc.GraphTraversal`` for a better performing function.

   The results displayed here can also be incorrect if

   :param activity: ``Activity``. The starting point of the supply chain graph.
   :param amount: int. Supply chain inputs will be scaled to this value.
   :param max_level: int. Max depth to search for.
   :param cutoff: float. Inputs with amounts less than ``amount * cutoff`` will not be printed or traversed further.
   :param file_obj: File-like object (supports ``.write``), optional. Output will be written to this object if provided.
   :param tab_character: str. Character to use to indicate indentation.
   :param __level: int. Current level of the calculation. Only used internally, do not touch.

   :returns: Nothing. Prints to ``stdout`` or ``file_obj``


