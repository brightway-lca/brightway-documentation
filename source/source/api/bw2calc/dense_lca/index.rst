:py:mod:`bw2calc.dense_lca`
===========================

.. py:module:: bw2calc.dense_lca


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2calc.dense_lca.DenseLCA




.. py:class:: DenseLCA(demand, method=None, weighting=None, normalization=None, database_filepath=None, log_config=None, presamples=None, seed=None, override_presamples_seed=False)

   Bases: :py:obj:`bw2calc.lca.LCA`

   .. autoapi-inheritance-diagram:: bw2calc.dense_lca.DenseLCA
      :parts: 1
      :private-bases:

   A static LCI or LCIA calculation.

   Following the general philosophy of Brightway2, and good software practices, there is a clear separation of concerns between retrieving and formatting data and doing an LCA. Building the necessary matrices is done with MatrixBuilder objects (:ref:`matrixbuilders`). The LCA class only does the LCA calculations themselves.


   Create a new LCA calculation.

   :param \* *demand*: The demand or functional unit. Needs to be a dictionary to indicate amounts, e.g. ``{("my database", "my process"): 2.5}``.
   :type \* *demand*: dict
   :param \* *method*: LCIA Method tuple, e.g. ``("My", "great", "LCIA", "method")``. Can be omitted if only interested in calculating the life cycle inventory.
   :type \* *method*: tuple, optional

   :returns: A new LCA object

   .. py:method:: solve_linear_system()

      Master solution function for linear system :math:`Ax=B`.

          To most numerical analysts, matrix inversion is a sin.

          -- Nicolas Higham, Accuracy and Stability of Numerical Algorithms, Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 2002, p. 260.

      We use `UMFpack <http://www.cise.ufl.edu/research/sparse/umfpack/>`_, which is a very fast solver for sparse matrices.

      If the technosphere matrix has already been factorized, then the decomposed technosphere (``self.solver``) is reused. Otherwise the calculation is redone completely.





