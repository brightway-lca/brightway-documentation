:py:mod:`bw2analyzer.contribution`
==================================

.. py:module:: bw2analyzer.contribution


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2analyzer.contribution.ContributionAnalysis




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




