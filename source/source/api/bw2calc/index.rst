:py:mod:`bw2calc`
=================

.. py:module:: bw2calc


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   dense_lca/index.rst
   errors/index.rst
   graph_traversal/index.rst
   independent_lca/index.rst
   indexing/index.rst
   lca/index.rst
   least_squares/index.rst
   log_utils/index.rst
   matrices/index.rst
   mc_vector/index.rst
   monte_carlo/index.rst
   multi_lca/index.rst
   single_matrix/index.rst
   speed_test/index.rst
   utils/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   bw2calc.DenseLCA
   bw2calc.IndependentLCAMixin
   bw2calc.LCA
   bw2calc.LeastSquaresLCA
   bw2calc.MatrixBuilder
   bw2calc.MultiLCA
   bw2calc.TechnosphereBiosphereMatrixBuilder



Functions
~~~~~~~~~

.. autoapisummary::

   bw2calc.load_calculation_package



.. py:class:: DenseLCA(demand, method=None, weighting=None, normalization=None, database_filepath=None, log_config=None, presamples=None, seed=None, override_presamples_seed=False)

   Bases: :py:obj:`bw2calc.lca.LCA`

   .. autoapi-inheritance-diagram:: bw2calc.DenseLCA
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





.. py:class:: IndependentLCAMixin

   Bases: :py:obj:`object`

   Mixin that allows `method`, etc. to be filepaths or ``np.ndarray`` instead of DataStore object names.

   Removes dependency on `bw2data`.

   .. py:method:: fix_dictionaries()

      Don't adjust dictionaries even if ``bw2data`` is present, as functional unit is an integer.


   .. py:method:: get_array_filepaths()

      Pass through already correct values



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



.. py:class:: LeastSquaresLCA(demand, method=None, weighting=None, normalization=None, database_filepath=None, log_config=None, presamples=None, seed=None, override_presamples_seed=False)

   Bases: :py:obj:`bw2calc.lca.LCA`

   .. autoapi-inheritance-diagram:: bw2calc.LeastSquaresLCA
      :parts: 1
      :private-bases:

   Solve overdetermined technosphere matrix with more products than activities using least-squares approximation.

   See also:

   * `Multioutput processes in LCA <http://chris.mutel.org/multioutput.html>`_
   * `LSMR in SciPy <http://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.lsmr.html#scipy.sparse.linalg.lsmr>`_
   * `Another least-squares algorithm in SciPy <http://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.lsqr.html#scipy.sparse.linalg.lsqr>`_


   Create a new LCA calculation.

   :param \* *demand*: The demand or functional unit. Needs to be a dictionary to indicate amounts, e.g. ``{("my database", "my process"): 2.5}``.
   :type \* *demand*: dict
   :param \* *method*: LCIA Method tuple, e.g. ``("My", "great", "LCIA", "method")``. Can be omitted if only interested in calculating the life cycle inventory.
   :type \* *method*: tuple, optional

   :returns: A new LCA object

   .. py:method:: decompose_technosphere()
      :abstractmethod:

      Factorize the technosphere matrix into lower and upper triangular matrices, :math:`A=LU`. Does not solve the linear system :math:`Ax=B`.

      Doesn't return anything, but creates ``self.solver``.

      .. warning:: Incorrect results could occur if a technosphere matrix was factorized, and then a new technosphere matrix was constructed, as ``self.solver`` would still be the factorized older technosphere matrix. You are responsible for deleting ``self.solver`` when doing these types of advanced calculations.




   .. py:method:: solve_linear_system(solver=lsmr)

      Master solution function for linear system :math:`Ax=B`.

          To most numerical analysts, matrix inversion is a sin.

          -- Nicolas Higham, Accuracy and Stability of Numerical Algorithms, Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 2002, p. 260.

      We use `UMFpack <http://www.cise.ufl.edu/research/sparse/umfpack/>`_, which is a very fast solver for sparse matrices.

      If the technosphere matrix has already been factorized, then the decomposed technosphere (``self.solver``) is reused. Otherwise the calculation is redone completely.





.. py:class:: MatrixBuilder

   Bases: :py:obj:`object`

   The class, and its subclasses, load structured arrays, manipulate them, and generate `SciPy sparse matrices <http://docs.scipy.org/doc/scipy/reference/sparse.html>`_.

   Matrix builders use an array of row indices, an array of column indices, and an array of values to create a `coordinate (coo) matrix <http://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.coo_matrix.html>`_, which is then converted to a `compressed sparse row (csr) matrix <http://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html>`_.

   See the following for more information on structured arrays:

   * `NumPy structured arrays <http://docs.scipy.org/doc/numpy/reference/generated/numpy.recarray.html#numpy.recarray>`_
   * `Intermediate and processed data <https://docs.brightwaylca.org/intro.html#intermediate-and-processed-data>`_

   These classes are not instantiated, and have only `classmethods <https://docs.python.org/2/library/functions.html#classmethod>`__. They are not really true classes, but more organizational. In other words, you should use:

   .. code-block:: python

       MatrixBuilder.build(args)

   and not:

   .. code-block:: python

       mb = MatrixBuilder()
       mb.build(args)



   .. py:method:: build(paths, data_label, row_id_label, row_index_label, col_id_label=None, col_index_label=None, row_dict=None, col_dict=None, one_d=False, drop_missing=True)
      :classmethod:

      Build a sparse matrix from NumPy structured array(s).

      See more detailed documentation at :ref:`building-matrices`.

      This method does the following:

      TODO: Update

      #. Load and concatenate the :ref:`structured arrays files <building-matrices>` in filepaths ``paths`` using the function :func:`.utils.load_arrays` into a parameter array.
      #. If not ``row_dict``, use :meth:`.build_dictionary` to build ``row_dict`` from the parameter array column ``row_id_label``.
      #. Using the ``row_id_label`` and the ``row_dict``, use the method :meth:`.add_matrix_indices` to add matrix indices to the ``row_index_label`` column.
      #. If not ``one_d``, do the same to ``col_dict`` and ``col_index_label``, using ``col_id_label``.
      #. If not ``one_d``, use :meth:`.build_matrix` to build a sparse matrix using ``data_label`` for the matrix data values, and ``row_index_label`` and ``col_index_label`` for row and column indices.
      #. Else if ``one_d``, use :meth:`.build_diagonal_matrix` to build a diagonal matrix using ``data_label`` for diagonal matrix data values and ``row_index_label`` as row/column indices.
      #. Return the loaded parameter arrays from step 1, row and column dicts from steps 2 & 4, and matrix from step 5 or 6.

      :param \* *paths*: List of array filepaths to load.
      :type \* *paths*: list
      :param \* *data_label*: Label of column in parameter arrays with matrix data values.
      :type \* *data_label*: str
      :param \* *row_id_label*: Label of column in parameter arrays with row ID values, i.e. the integer values returned from ``mapping``.
      :type \* *row_id_label*: str
      :param \* *row_index_label*: Label of column in parameter arrays where matrix row indices will be stored.
      :type \* *row_index_label*: str
      :param \* *col_id_label*: Label of column in parameter arrays with column ID values, i.e. the integer values returned from ``mapping``. Not needed for diagonal matrices.
      :type \* *col_id_label*: str, optional
      :param \* *col_index_label*: Label of column in parameter arrays where matrix column indices will be stored. Not needed for diagonal matrices.
      :type \* *col_index_label*: str, optional
      :param \* *row_dict*: Mapping dictionary linking ``row_id_label`` values to ``row_index_label`` values. Will be built if not given.
      :type \* *row_dict*: dict, optional
      :param \* *col_dict*: Mapping dictionary linking ``col_id_label`` values to ``col_index_label`` values. Will be built if not given.
      :type \* *col_dict*: dict, optional
      :param \* *one_d*: Build diagonal matrix.
      :type \* *one_d*: bool
      :param \* *drop_missing*: Remove rows from the parameter array which aren't mapped by ``row_dict`` or ``col_dict``. Default is ``True``. Advanced use only.
      :type \* *drop_missing*: bool

      :returns: A :ref:`numpy parameter array <building-matrices>`, the row mapping dictionary, the column mapping dictionary, and a COO sparse matrix.


   .. py:method:: build_diagonal_matrix(array, row_dict, index_label, data_label=None, new_data=None)
      :classmethod:

      Build diagonal sparse matrix.


   .. py:method:: build_matrix(array, row_dict, col_dict, row_index_label, col_index_label, data_label=None, new_data=None)
      :classmethod:

      Build sparse matrix.



.. py:class:: MultiLCA(cs_name, log_config=None)

   Bases: :py:obj:`object`

   Wrapper class for performing LCA calculations with many functional units and LCIA methods.

   Needs to be passed a ``calculation_setup`` name.

   This class does not subclass the `LCA` class, and performs all calculations upon instantiation.

   Initialization creates `self.results`, which is a NumPy array of LCA scores, with rows of functional units and columns of LCIA methods. Ordering is the same as in the `calculation_setup`.


   .. py:property:: all

      Get all possible databases by merging all functional units


.. py:class:: TechnosphereBiosphereMatrixBuilder

   Bases: :py:obj:`MatrixBuilder`

   .. autoapi-inheritance-diagram:: bw2calc.TechnosphereBiosphereMatrixBuilder
      :parts: 1
      :private-bases:

   Subclass of ``MatrixBuilder`` that separates technosphere and biosphere parameters

   .. py:method:: build(paths)
      :classmethod:

      Build the technosphere and biosphere sparse matrices.


   .. py:method:: build_technosphere_matrix(array, activity_dict, product_dict, new_data=None)
      :classmethod:


   .. py:method:: fix_supply_use(array, vector)
      :classmethod:

      Make technosphere inputs negative.


   .. py:method:: get_biosphere_inputs_mask(array)
      :classmethod:

      Get boolean mask of biosphere flows from ``array`` (i.e. the ones to include when building the biosphere matrix).


   .. py:method:: get_technosphere_inputs_mask(array)
      :classmethod:

      Get boolean mask of technosphere inputs from ``array`` (i.e. the ones to include when building the technosphere matrix).


   .. py:method:: select_biosphere_array(array)
      :classmethod:

      Create a new array with biosphere matrix exchanges


   .. py:method:: select_technosphere_array(array)
      :classmethod:

      Create a new array with technosphere matrix exchanges



.. py:function:: load_calculation_package(fp)

   Load a calculation package created by ``save_calculation_package``.

   NumPy arrays are saved to a temporary directory, and file paths are adjusted.

   ``fp`` is the absolute file path of a calculation package file.

   Returns a dictionary suitable for passing to an LCA object, e.g. ``LCA(**load_calculation_package(fp))``.



