:py:mod:`bw2calc.graph_traversal`
=================================

.. py:module:: bw2calc.graph_traversal


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2calc.graph_traversal.GraphTraversal




Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2calc.graph_traversal.databases


.. py:class:: GraphTraversal

   Bases: :py:obj:`object`

   Traverse a supply chain, following paths of greatest impact.

   This implementation uses a queue of datasets to assess. As the supply chain is traversed, datasets inputs are added to a list sorted by LCA score. Each activity in the sorted list is assessed, and added to the supply chain graph, as long as its impact is above a certain threshold, and the maximum number of calculations has not been exceeded.

   Because the next dataset assessed is chosen by its impact, not its position in the graph, this is neither a breadth-first nor a depth-first search, but rather "importance-first".

   This class is written in a functional style - no variables are stored in *self*, only methods.

   Should be used by calling the ``calculate`` method.

   .. warning:: Graph traversal with multioutput processes only works when other inputs are substituted (see `Multioutput processes in LCA <http://chris.mutel.org/multioutput.html>`__ for a description of multiputput process math in LCA).



   .. py:method:: build_lca(demand, method)

      Build LCA object from *demand* and *method*.


   .. py:method:: calculate(demand, method, cutoff=0.005, max_calc=100000.0, skip_coproducts=False)

      Traverse the supply chain graph.

      :param \* *demand*: The functional unit. Same format as in LCA class.
      :type \* *demand*: dict
      :param \* *method*: LCIA method. Same format as in LCA class.
      :type \* *method*: tuple
      :param \* *cutoff*: Cutoff criteria to stop LCA calculations. Relative score of total, i.e. 0.005 will cutoff if a dataset has a score less than 0.5 percent of the total.
      :type \* *cutoff*: float, default=0.005
      :param \* *max_calc*: Maximum number of LCA calculations to perform.
      :type \* *max_calc*: int, default=10000

      :returns: Dictionary of nodes, edges, LCA object, and number of LCA calculations.


   .. py:method:: cumulative_score(index, supply, characterized_biosphere, lca)

      Compute cumulative LCA score for a given activity


   .. py:method:: initialize_heap(demand, lca, supply, characterized_biosphere)

      Create a `priority queue <http://docs.python.org/2/library/heapq.html>`_ or ``heap`` to store inventory datasets, sorted by LCA score.

      Populates the heap with each activity in ``demand``. Initial nodes are the *functional unit*, i.e. the complete demand, and each activity in the *functional unit*. Initial edges are inputs from each activity into the *functional unit*.

      The *functional unit* is an abstract dataset (as it doesn't exist in the matrix), and is assigned the index ``-1``.




   .. py:method:: traverse(heap, nodes, edges, counter, max_calc, cutoff, total_score, supply, characterized_biosphere, lca, skip_coproducts)

      Build a directed graph by traversing the supply chain.

      Node ids are actually technosphere row/col indices, which makes lookup easier.

      :returns: (nodes, edges, number of calculations)


   .. py:method:: unit_score(index, supply, characterized_biosphere)

      Compute the LCA impact caused by the direct emissions and resource consumption of a given activity



.. py:data:: databases

   

