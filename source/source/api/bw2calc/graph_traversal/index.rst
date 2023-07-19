:py:mod:`bw2calc.graph_traversal`
=================================

.. py:module:: bw2calc.graph_traversal


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2calc.graph_traversal.AssumedDiagonalGraphTraversal
   bw2calc.graph_traversal.CachingSolver
   bw2calc.graph_traversal.GraphTraversal
   bw2calc.graph_traversal.MultifunctionalGraphTraversal




.. py:class:: AssumedDiagonalGraphTraversal

   Traverse a supply chain, following paths of greatest impact.

   This implementation uses a queue of datasets to assess. As the supply chain is traversed, datasets inputs are added to a list sorted by LCA score. Each activity in the sorted list is assessed, and added to the supply chain graph, as long as its impact is above a certain threshold, and the maximum number of calculations has not been exceeded.

   Because the next dataset assessed is chosen by its impact, not its position in the graph, this is neither a breadth-first nor a depth-first search, but rather "importance-first".

   This class is written in a functional style - no variables are stored in *self*, only methods.

   Should be used by calling the ``calculate`` method.

   .. warning:: Graph traversal with multioutput processes only works when other inputs are substituted (see `Multioutput processes in LCA <http://chris.mutel.org/multioutput.html>`__ for a description of multiputput process math in LCA).


   .. py:method:: calculate(lca, cutoff=0.005, max_calc=100000.0, skip_coproducts=False)

      Traverse the supply chain graph.

      :param \* *lca*: An instance of ``bw2calc.lca.LCA``.
      :type \* *lca*: dict
      :param \* *cutoff*: Cutoff criteria to stop LCA calculations. Relative score of total, i.e. 0.005 will cutoff if a dataset has a score less than 0.5 percent of the total.
      :type \* *cutoff*: float, default=0.005
      :param \* *max_calc*: Maximum number of LCA calculations to perform.
      :type \* *max_calc*: int, default=10000

      :returns: Dictionary of nodes, edges, and number of LCA calculations.


   .. py:method:: cumulative_score(index, supply, characterized_biosphere, lca)

      Compute cumulative LCA score for a given activity


   .. py:method:: initialize_heap(lca, supply, characterized_biosphere)

      Create a `priority queue <http://docs.python.org/2/library/heapq.html>`_ or ``heap`` to store inventory datasets, sorted by LCA score.

      Populates the heap with each activity in ``demand``. Initial nodes are the *functional unit*, i.e. the complete demand, and each activity in the *functional unit*. Initial edges are inputs from each activity into the *functional unit*.

      The *functional unit* is an abstract dataset (as it doesn't exist in the matrix), and is assigned the index ``-1``.



   .. py:method:: traverse(heap, nodes, edges, counter, max_calc, cutoff, total_score, supply, characterized_biosphere, lca, skip_coproducts)

      Build a directed graph by traversing the supply chain.

      Node ids are actually technosphere row/col indices, which makes lookup easier.

      :returns: (nodes, edges, number of calculations)


   .. py:method:: unit_score(index, supply, characterized_biosphere)

      Compute the LCA impact caused by the direct emissions and resource consumption of a given activity



.. py:class:: CachingSolver(lca)


.. py:class:: GraphTraversal(*args, **kwargs)


.. py:class:: MultifunctionalGraphTraversal

   Traverse a supply chain, following paths of greatest impact. Can handle the differentiation between products and activities, and makes no assumptions about multifunctionality, substitution, or the special status of numbers on the diagonal.

   As soon as non-diagonal values are allowed, we lose any concept of a reference product. This means that we can trace the edges for an activity (both inputs and outputs, though in the matrix there is no functional difference), but we can't for a product, as we can't use the graph structure to determine *which activity* produced the product. There could be more than one, or even zero, depending on how your mental model of substitution works. Our algorithm is therefore:

   1. Start with products (initially the products in the functional unit)
   2. For each product, determine which activities produced it by solving the linear system
   3a. For each of these activities, add on to our list of products to consider by looking at the edges for that activity, and excluding the edge which led to our original product
   3b. If we have already examined this activity, don't visit it again
   4. Keep iterating over the list of products until we run out of activities or hit our calculation limit

   The ``.calculate()`` function therefore returns the following:

   .. code-block:: python

       {
           'counter': int, # Number of LCA calculations done,
           'products': {
               id: {  # id is either the database integer id (if `translate_indices` is True) or the matrix row index
                   'amount': float # Total amount of this product produced to satisfy the functional unit
                   'supply_chain_score': float # The total impact of producing this product
               }
           },
           'activities': {
               id: {  # id is either the database integer id (if `translate_indices` is True) or the matrix column index
                   'amount': float # Total amount of this activity produced to satisfy the entire functional unit
                   'direct_score': float # The impact of the direct emissions associated to this activity and its amount
           },
           'edges': [{
               'target': int,  # product id if type is activity else activity id
               'source': int,  # activity id if type is product else product id
               'type': str,  # 'product' or 'activity'
               'amount': float,  # Total amount of the flow
               'exc_amount': float,  # Value given in the technosphere matrix
               'supply_chain_score': float,  # Total impact from the production of this product. Only for type 'product'
               'direct_score': float,  # Impact from direct emissions of this activity. Only for type 'activity'
           }]
       }

   As in AssumedDiagonalGraphTraversal, we use a priority queue to examine products in order of their total impact.

   This class is written in a functional style, with only class methods.


   .. py:method:: calculate(lca: bw2calc.LCA, cutoff: float = 0.005, max_calc: int = 100000.0, translate_indices: bool = True)
      :classmethod:

      Traverse the supply chain graph.

      :param \* *lca*: An instance of ``bw2calc.lca.LCA``.
      :type \* *lca*: dict
      :param \* *cutoff*: Cutoff criteria to stop LCA calculations. Relative score of total, i.e. 0.005 will cutoff if a dataset has a score less than 0.5 percent of the total.
      :type \* *cutoff*: float, default=0.005
      :param \* *max_calc*: Maximum number of LCA calculations to perform.
      :type \* *max_calc*: int, default=10000

      :returns: Dictionary of nodes, edges, and number of LCA calculations.


   .. py:method:: clean_small_values(data, kind=dict, cutoff=5e-16)
      :classmethod:


   .. py:method:: consolidate_edges(edges)
      :classmethod:


   .. py:method:: initialize_heap(lca: bw2calc.LCA, solver: CachingSolver, translate_indices: bool, counter: int)
      :classmethod:

      Create a `priority queue <http://docs.python.org/2/library/heapq.html>`_ or ``heap`` to store inventory datasets, sorted by LCA score.

      Populates the heap with each activity in ``demand``. Initial nodes are the *functional unit*, i.e. the complete demand, and each activity in the *functional unit*. Initial edges are inputs from each activity into the *functional unit*.

      The *functional unit* is an abstract dataset (as it doesn't exist in the matrix), and is assigned the index ``-1``.



   .. py:method:: traverse(heap: list, solver: CachingSolver, activities: dict, products: dict, edges: list, max_calc: int, cutoff: float, total_score: float, lca: bw2calc.LCA, translate_indices: bool, counter: int)
      :classmethod:

      Build a directed graph by traversing the supply chain.

      Node ids are actually technosphere row/col indices, which makes lookup easier.

      :returns: (nodes, edges, number of calculations)


   .. py:method:: visit_activity(heap: list, activity_index: int, counter: int, activities: dict, products: dict, edges: list, lca: bw2calc.LCA, characterized_biosphere: scipy.sparse.csr_matrix, solver: CachingSolver, cutoff_score: float, origin_product_index: int, translate_indices: bool)
      :classmethod:



