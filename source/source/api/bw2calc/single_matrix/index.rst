:py:mod:`bw2calc.single_matrix`
===============================

.. py:module:: bw2calc.single_matrix


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2calc.single_matrix.SingleMatrixLCA




Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2calc.single_matrix.PackagesDataLoader
   bw2calc.single_matrix.pandas


.. py:class:: SingleMatrixLCA(demand, data_filepath, log_config=None, presamples=None, seed=None, override_presamples_seed=False)

   Bases: :py:obj:`object`

   An LCA which puts everything into one matrix.

   Comes with advantages and disadvantages, and designed exclusively for `BONSAI <https://bonsai.uno/>`__ via `beebee <https://github.com/BONSAMURAIS/beebee/>`__.

   Create a new single-matrix LCA calculation.

   :param \* *demand*: The demand or functional unit. Needs to be a dictionary to indicate amounts, e.g. ``{("my database", "my process"): 2.5}``.
   :type \* *demand*: dict

   :returns: A new ``SingleMatrixLCA`` object

   .. py:method:: build_demand_array(demand=None)

      Turn the demand dictionary into a *NumPy* array of correct size.

      :param \* *demand*: Demand dictionary. Optional, defaults to ``self.demand``.
      :type \* *demand*: dict, optional

      :returns: A 1-dimensional NumPy array


   .. py:method:: calculate(factorize=False, builder=SingleMatrixBuilder)

      Calculate an LCA score.

      Creates ``self.supply_array``, a vector of activities, flows, and characterization pathways which satisfy the demand.

      Creates ``self.scores``, a dictionary of ``{'LCIA identifier': LCA score}``.

      Create ``self.contributions``, a dictionary of ``{'LCIA identifier': []}``.

      :param \* *factorize*: Factorize the technosphere matrix. Makes additional calculations with the same technosphere matrix much faster. Default is ``False``; not useful is only doing one LCI calculation.
      :type \* *factorize*: bool, optional
      :param \* *builder*: Custom matrix builders can be used to manipulate data in creative ways before building the matrices.
      :type \* *builder*: ``SingleMatrixBuilder`` object, optional

      Doesn't return anything.



   .. py:method:: calculate_scores()


   .. py:method:: decompose_technosphere()

      Factorize the technosphere matrix into lower and upper triangular matrices, :math:`A=LU`. Does not solve the linear system :math:`Ax=B`.

      Doesn't return anything, but creates ``self.solver``.

      .. warning:: Incorrect results could occur if a technosphere matrix was factorized, and then a new technosphere matrix was constructed, as ``self.solver`` would still be the factorized older technosphere matrix. You are responsible for deleting ``self.solver`` when doing these types of advanced calculations.




   .. py:method:: fix_dictionaries(row_mapping, col_mapping)

      Fix the row and column dictionaries from ``{integer: row/col index}`` to ``{label: row/col index}``.


   .. py:method:: lcia(*args, **kwargs)


   .. py:method:: load_beebee_data(builder=SingleMatrixBuilder)

      Load ``beebee`` export data package.

      This is a compressed file which contains:

      * A `stats_arrays <https://bitbucket.org/cmutel/stats_arrays>`__ file used to create the single matrix.
      * A mapping dictionary from meaningful labels to the integer row ids
      * A mapping dictionary from meaningful labels to the integer column ids
      * A mapping dictionary from ``{"method URI": {labels}}`` which allows for LCIA sums



   .. py:method:: rebuild_matrix(vector)

      Build a new technosphere matrix using the same row and column indices, but different values. Useful for Monte Carlo iteration or sensitivity analysis.

      :param \* *vector*: 1-dimensional NumPy array with length (# of technosphere parameters), in same order as ``self.tech_params``.
      :type \* *vector*: array

      Doesn't return anything, but overwrites ``self.technosphere_matrix``.



   .. py:method:: redo_calculate(demand=None)

      Redo LCI with same databases but different demand.

      :param \* *demand*: A demand dictionary.
      :type \* *demand*: dict

      Doesn't return anything, but overwrites ``self.demand_array``, ``self.supply_array``, and ``self.inventory``.

      .. warning:: If you want to redo the LCIA as well, use ``redo_lcia(demand)`` directly.



   .. py:method:: reverse_dict()

      Construct reverse dicts from technosphere and biosphere row and col indices to activity_dict/product_dict/biosphere_dict keys.

      :returns: (reversed ``self.activity_dict``, ``self.product_dict`` and ``self.biosphere_dict``)


   .. py:method:: solve_linear_system()

      Master solution function for linear system :math:`Ax=B`.

          To most numerical analysts, matrix inversion is a sin.

          -- Nicolas Higham, Accuracy and Stability of Numerical Algorithms, Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 2002, p. 260.

      We use `UMFpack <http://www.cise.ufl.edu/research/sparse/umfpack/>`_, which is a very fast solver for sparse matrices.

      If the technosphere matrix has already been factorized, then the decomposed technosphere (``self.solver``) is reused. Otherwise the calculation is redone completely.





.. py:data:: PackagesDataLoader

   

.. py:data:: pandas

   

