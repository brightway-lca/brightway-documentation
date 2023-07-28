:py:mod:`bw2calc.lca`
=====================

.. py:module:: bw2calc.lca


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2calc.lca.LCA




Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2calc.lca.PackagesDataLoader
   bw2calc.lca.pandas


.. py:class:: LCA(demand, method=None, weighting=None, normalization=None, database_filepath=None, log_config=None, presamples=None, seed=None, override_presamples_seed=False)

   Bases: :py:obj:`object`

   A static LCI or LCIA calculation.

   Following the general philosophy of Brightway2, and good software practices, there is a clear separation of concerns between retrieving and formatting data and doing an LCA. Building the necessary matrices is done with MatrixBuilder objects (:ref:`matrixbuilders`). The LCA class only does the LCA calculations themselves.


   Create a new LCA calculation.

   :param \* *demand*: The demand or functional unit. Needs to be a dictionary to indicate amounts, e.g. ``{("my database", "my process"): 2.5}``.
   :type \* *demand*: dict
   :param \* *method*: LCIA Method tuple, e.g. ``("My", "great", "LCIA", "method")``. Can be omitted if only interested in calculating the life cycle inventory.
   :type \* *method*: tuple, optional

   :returns: A new LCA object

   .. py:property:: score

      The LCIA score as a ``float``.

      Note that this is a `property <http://docs.python.org/2/library/functions.html#property>`_, so it is ``foo.lca``, not ``foo.score()``

   .. py:method:: build_demand_array(demand=None)

      Turn the demand dictionary into a *NumPy* array of correct size.

      :param \* *demand*: Demand dictionary. Optional, defaults to ``self.demand``.
      :type \* *demand*: dict, optional

      :returns: A 1-dimensional NumPy array


   .. py:method:: decompose_technosphere()

      Factorize the technosphere matrix into lower and upper triangular matrices, :math:`A=LU`. Does not solve the linear system :math:`Ax=B`.

      Doesn't return anything, but creates ``self.solver``.

      .. warning:: Incorrect results could occur if a technosphere matrix was factorized, and then a new technosphere matrix was constructed, as ``self.solver`` would still be the factorized older technosphere matrix. You are responsible for deleting ``self.solver`` when doing these types of advanced calculations.




   .. py:method:: fix_dictionaries()

      Fix technosphere and biosphere dictionaries from this:

      .. code-block:: python

          {mapping integer id: matrix row/column index}

      To this:

      .. code-block:: python

          {(database, key): matrix row/column index}

      This isn't needed for the LCA calculation itself, but is helpful when interpreting results.

      Doesn't require any arguments or return anything, but changes ``self.activity_dict``, ``self.product_dict`` and ``self.biosphere_dict``.




   .. py:method:: get_array_filepaths()

      Use utility functions to get all array filepaths


   .. py:method:: lci(factorize=False, builder=TBMBuilder)

      Calculate a life cycle inventory.

      #. Load LCI data, and construct the technosphere and biosphere matrices.
      #. Build the demand array
      #. Solve the linear system to get the supply array and life cycle inventory.

      :param \* *factorize*: Factorize the technosphere matrix. Makes additional calculations with the same technosphere matrix much faster. Default is ``False``; not useful is only doing one LCI calculation.
      :type \* *factorize*: bool, optional
      :param \* *builder*: Default is ``bw2calc.matrices.TechnosphereBiosphereMatrixBuilder``, which is fine for most cases. Custom matrix builders can be used to manipulate data in creative ways before building the matrices.
      :type \* *builder*: ``MatrixBuilder`` object, optional

      .. warning:: Custom matrix builders should inherit from ``TechnosphereBiosphereMatrixBuilder``, because technosphere inputs need to have their signs flipped to be negative, as we do :math:`A^{-1}f` directly instead of :math:`(I - A^{-1})f`.

      Doesn't return anything, but creates ``self.supply_array`` and ``self.inventory``.




   .. py:method:: lci_calculation()

      The actual LCI calculation.

      Separated from ``lci`` to be reusable in cases where the matrices are already built, e.g. ``redo_lci`` and Monte Carlo classes.



   .. py:method:: lcia(builder=MatrixBuilder)

      Calculate the life cycle impact assessment.

      #. Load and construct the characterization matrix
      #. Multiply the characterization matrix by the life cycle inventory

      :param \* *builder*: Default is ``bw2calc.matrices.MatrixBuilder``, which is fine for most cases. Custom matrix builders can be used to manipulate data in creative ways before building the characterization matrix.
      :type \* *builder*: ``MatrixBuilder`` object, optional

      Doesn't return anything, but creates ``self.characterized_inventory``.




   .. py:method:: lcia_calculation()

      The actual LCIA calculation.

      Separated from ``lcia`` to be reusable in cases where the matrices are already built, e.g. ``redo_lcia`` and Monte Carlo classes.



   .. py:method:: load_lci_data(fix_dictionaries=True, builder=TBMBuilder)

      Load data and create technosphere and biosphere matrices.


   .. py:method:: load_lcia_data(builder=MatrixBuilder)

      Load data and create characterization matrix.

      This method will filter out regionalized characterization factors. This filtering needs access to ``bw2data`` - therefore, regionalized methods will cause incorrect results if ``bw2data`` is not importable.



   .. py:method:: load_normalization_data(builder=MatrixBuilder)

      Load normalization data.


   .. py:method:: load_weighting_data()

      Load weighting data, a 1-element array.


   .. py:method:: normalization_calculation()

      The actual normalization calculation.

      Creates ``self.normalized_inventory``.


   .. py:method:: normalize()

      Multiply characterized inventory by flow-specific normalization factors.


   .. py:method:: rebuild_biosphere_matrix(vector)

      Build a new biosphere matrix using the same row and column indices, but different values. Useful for Monte Carlo iteration or sensitivity analysis.

      :param \* *vector*: 1-dimensional NumPy array with length (# of biosphere parameters), in same order as ``self.bio_params``.
      :type \* *vector*: array

      Doesn't return anything, but overwrites ``self.biosphere_matrix``.



   .. py:method:: rebuild_characterization_matrix(vector)

      Build a new characterization matrix using the same row and column indices, but different values. Useful for Monte Carlo iteration or sensitivity analysis.

      :param \* *vector*: 1-dimensional NumPy array with length (# of characterization parameters), in same order as ``self.cf_params``.
      :type \* *vector*: array

      Doesn't return anything, but overwrites ``self.characterization_matrix``.



   .. py:method:: rebuild_technosphere_matrix(vector)

      Build a new technosphere matrix using the same row and column indices, but different values. Useful for Monte Carlo iteration or sensitivity analysis.

      :param \* *vector*: 1-dimensional NumPy array with length (# of technosphere parameters), in same order as ``self.tech_params``.
      :type \* *vector*: array

      Doesn't return anything, but overwrites ``self.technosphere_matrix``.



   .. py:method:: redo_lci(demand=None)

      Redo LCI with same databases but different demand.

      :param \* *demand*: A demand dictionary.
      :type \* *demand*: dict

      Doesn't return anything, but overwrites ``self.demand_array``, ``self.supply_array``, and ``self.inventory``.

      .. warning:: If you want to redo the LCIA as well, use ``redo_lcia(demand)`` directly.



   .. py:method:: redo_lcia(demand=None)

      Redo LCIA, optionally with new demand.

      :param \* *demand*: New demand dictionary. Optional, defaults to ``self.demand``.
      :type \* *demand*: dict, optional

      Doesn't return anything, but overwrites ``self.characterized_inventory``. If ``demand`` is given, also overwrites ``self.demand_array``, ``self.supply_array``, and ``self.inventory``.



   .. py:method:: reverse_dict()

      Construct reverse dicts from technosphere and biosphere row and col indices to activity_dict/product_dict/biosphere_dict keys.

      :returns: (reversed ``self.activity_dict``, ``self.product_dict`` and ``self.biosphere_dict``)


   .. py:method:: solve_linear_system()

      Master solution function for linear system :math:`Ax=B`.

          To most numerical analysts, matrix inversion is a sin.

          -- Nicolas Higham, Accuracy and Stability of Numerical Algorithms, Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 2002, p. 260.

      We use `UMFpack <http://www.cise.ufl.edu/research/sparse/umfpack/>`_, which is a very fast solver for sparse matrices.

      If the technosphere matrix has already been factorized, then the decomposed technosphere (``self.solver``) is reused. Otherwise the calculation is redone completely.




   .. py:method:: switch_method(method)

      Switch to LCIA method `method`


   .. py:method:: switch_normalization(normalization)

      Switch to LCIA normalization `normalization`


   .. py:method:: switch_weighting(weighting)

      Switch to LCIA weighting `weighting`


   .. py:method:: to_dataframe(cutoff=200)

      Return all nonzero elements of characterized inventory as Pandas dataframe


   .. py:method:: top_activities(**kwargs)

      Call ``bw2analyzer.ContributionAnalyses.annotated_top_processes``


   .. py:method:: top_emissions(**kwargs)

      Call ``bw2analyzer.ContributionAnalyses.annotated_top_emissions``


   .. py:method:: weight()

      Multiply characterized inventory by weighting value.

      Can be done with or without normalization.


   .. py:method:: weighting_calculation()

      The actual weighting calculation.

      Multiples weighting value by normalized inventory, if available, otherwise by characterized inventory.

      Creates ``self.weighted_inventory``.



.. py:data:: PackagesDataLoader

   

.. py:data:: pandas

   

