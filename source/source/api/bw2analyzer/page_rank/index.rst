:py:mod:`bw2analyzer.page_rank`
===============================

.. py:module:: bw2analyzer.page_rank


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2analyzer.page_rank.PageRank




.. py:exception:: ConvergenceError

   Bases: :py:obj:`Exception`

   .. autoapi-inheritance-diagram:: bw2analyzer.page_rank.ConvergenceError
      :parts: 1
      :private-bases:

   Common base class for all non-exit exceptions.

   Initialize self.  See help(type(self)) for accurate signature.


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



