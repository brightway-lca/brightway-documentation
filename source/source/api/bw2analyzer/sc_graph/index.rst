:py:mod:`bw2analyzer.sc_graph`
==============================

.. py:module:: bw2analyzer.sc_graph


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2analyzer.sc_graph.GTManipulator



Functions
~~~~~~~~~

.. autoapisummary::

   bw2analyzer.sc_graph.tupify



.. py:class:: GTManipulator

   Manipulate ``GraphTraversal`` results.

   .. py:method:: add_metadata(nodes, lca)
      :staticmethod:

      Add metadata to nodes, like name, unit, and category.


   .. py:method:: d3_force_directed(nodes, edges, score)
      :staticmethod:

      Reformat to D3 style, which is a list of nodes, and edge ids are node list indices.


   .. py:method:: d3_treemap(nodes, edges, lca, add_biosphere=False)
      :staticmethod:

      Add node data by traversing the graph; assign different metadata to leaf nodes.


   .. py:method:: simplify(nodes, edges, score, limit=0.005)
      :staticmethod:

      Simplify supply chain to include only nodes which individually contribute ``limit * score``.

      Only removes and combines edges; doesn't check to make sure amounts add up correctly.


   .. py:method:: simplify_naive(nodes, edges, score, limit=0.0025)
      :staticmethod:

      Naive simplification which simplifies removes links below an LCA score cutoff. Orphan nodes are also deleted.


   .. py:method:: unroll_graph(nodes, edges, score, cutoff=0.005, max_links=2500)
      :staticmethod:

      Unroll a ``GraphTraversal`` result, allowing the same activity to appear in the graph multiple times.



.. py:function:: tupify(o)

   Transform edge from dict to tuples. Multiply impact by -1 because sort by min, not max


