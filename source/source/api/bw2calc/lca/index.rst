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

   bw2calc.lca.get_node
   bw2calc.lca.logger


.. py:class:: LCA(demand: dict, method: Optional[tuple] = None, weighting: Optional[str] = None, normalization: Optional[str] = None, data_objs: Optional[Iterable[Union[pathlib.Path, fs.base.FS, bw_processing.DatapackageBase]]] = None, remapping_dicts: Optional[Iterable[dict]] = None, log_config: Optional[dict] = None, seed_override: Optional[int] = None, use_arrays: bool = False, use_distributions: bool = False)

   Bases: :py:obj:`collections.abc.Iterator`

   .. autoapi-inheritance-diagram:: bw2calc.lca.LCA
      :parts: 1
      :private-bases:

   An LCI or LCIA calculation.

   Compatible with Brightway2 and 2.5 semantics. Can be static, stochastic, or iterative (scenario-based), depending on the ``data_objs`` input data..


   Create a new LCA calculation.

   :param \* *demand*: The demand or functional unit. Needs to be a dictionary to indicate amounts, e.g. ``{7: 2.5}``.
   :type \* *demand*: dict
   :param \* *method*: LCIA Method tuple, e.g. ``("My", "great", "LCIA", "method")``. Can be omitted if only interested in calculating the life cycle inventory.
   :type \* *method*: tuple, optional

   :returns: A new LCA object

   .. py:property:: activity_dict


   .. py:property:: biosphere_dict


   .. py:property:: product_dict


   .. py:property:: score
      :type: float

      The LCIA score as a ``float``.

      Note that this is a `property <http://docs.python.org/2/library/functions.html#property>`_, so it is ``foo.lca``, not ``foo.score()``

   .. py:attribute:: matrix_labels
      :value: ['technosphere_mm', 'biosphere_mm', 'characterization_mm', 'normalization_mm', 'weighting_mm']

      

   .. py:method:: __check_demand(demand: Optional[dict] = None)


   .. py:method:: _switch(obj: Union[tuple, Iterable[Union[fs.base.FS, bw_processing.DatapackageBase]]], label: str, matrix: str, func: Callable) -> None

      Switch a method, weighting, or normalization


   .. py:method:: build_demand_array(demand: Optional[dict] = None) -> None

      Turn the demand dictionary into a *NumPy* array of correct size.

      :param \* *demand*: Demand dictionary. Optional, defaults to ``self.demand``.
      :type \* *demand*: dict, optional

      :returns: A 1-dimensional NumPy array


   .. py:method:: decompose_technosphere() -> None

      Factorize the technosphere matrix into lower and upper triangular matrices, :math:`A=LU`. Does not solve the linear system :math:`Ax=B`.

      Doesn't return anything, but creates ``self.solver``.

      .. warning:: Incorrect results could occur if a technosphere matrix was factorized, and then a new technosphere matrix was constructed, as ``self.solver`` would still be the factorized older technosphere matrix. You are responsible for deleting ``self.solver`` when doing these types of advanced calculations.



   .. py:method:: ensure_bw2data_available()

      Raises ``ImportError`` is bw2data not available or version < 4.


   .. py:method:: has(label: str) -> bool

      Shortcut to find out if matrix data for type ``{label}_matrix`` is present in the given data objects.

      Returns a boolean. Will return ``True`` even if data for a zero-dimensional matrix is given.


   .. py:method:: invert_technosphere_matrix()

      Use pardiso to efficiently calculate the inverse of the technosphere matrix.


   .. py:method:: keep_first_iteration()

      Set a flag to use the current values as first element when iterating.

      When creating the class instance, we already use the first index. This method allows us to use the values for the first index.

      Note that the methods ``.lci_calculation()`` and ``.lcia_calculation()`` will be called on the current values, even if these calculations have already been done.


   .. py:method:: lci(demand: Optional[dict] = None, factorize: bool = False) -> None

      Calculate a life cycle inventory.

      #. Load LCI data, and construct the technosphere and biosphere matrices.
      #. Build the demand array
      #. Solve the linear system to get the supply array and life cycle inventory.

      :param \* *factorize*: Factorize the technosphere matrix. Makes additional calculations with the same technosphere matrix much faster. Default is ``False``; not useful is only doing one LCI calculation.
      :type \* *factorize*: bool, optional
      :param \* *builder*: Default is ``bw2calc.matrices.MatrixBuilder``, which is fine for most cases. Custom matrix builders can be used to manipulate data in creative ways before building the matrices.
      :type \* *builder*: ``MatrixBuilder`` object, optional

      Doesn't return anything, but creates ``self.supply_array`` and ``self.inventory``.



   .. py:method:: lci_calculation() -> None

      The actual LCI calculation.

      Separated from ``lci`` to be reusable in cases where the matrices are already built, e.g. ``redo_lci`` and Monte Carlo classes.



   .. py:method:: lcia(demand: Optional[dict] = None) -> None

      Calculate the life cycle impact assessment.

      #. Load and construct the characterization matrix
      #. Multiply the characterization matrix by the life cycle inventory

      Doesn't return anything, but creates ``self.characterized_inventory``.



   .. py:method:: lcia_calculation() -> None

      The actual LCIA calculation.

      Separated from ``lcia`` to be reusable in cases where the matrices are already built, e.g. ``redo_lcia`` and Monte Carlo classes.



   .. py:method:: load_lci_data(nonsquare_ok=False) -> None

      Load inventory data and create technosphere and biosphere matrices.


   .. py:method:: load_lcia_data(data_objs: Optional[Iterable[Union[fs.base.FS, bw_processing.DatapackageBase]]] = None) -> None

      Load data and create characterization matrix.

      This method will filter out regionalized characterization factors.



   .. py:method:: load_normalization_data(data_objs: Optional[Iterable[Union[fs.base.FS, bw_processing.DatapackageBase]]] = None) -> None

      Load normalization data.


   .. py:method:: load_weighting_data(data_objs: Optional[Iterable[Union[fs.base.FS, bw_processing.DatapackageBase]]] = None) -> None

      Load normalization data.


   .. py:method:: normalization_calculation() -> None

      The actual normalization calculation.

      Creates ``self.normalized_inventory``.


   .. py:method:: normalize() -> None

      Multiply characterized inventory by flow-specific normalization factors.


   .. py:method:: redo_lci(demand: Optional[dict] = None) -> None

      Redo LCI with same databases but different demand.

      :param \* *demand*: A demand dictionary.
      :type \* *demand*: dict

      Doesn't return anything, but overwrites ``self.demand_array``, ``self.supply_array``, and ``self.inventory``.

      .. warning:: If you want to redo the LCIA as well, use ``redo_lcia(demand)`` directly.



   .. py:method:: redo_lcia(demand: Optional[dict] = None) -> None

      Redo LCIA, optionally with new demand.

      :param \* *demand*: New demand dictionary. Optional, defaults to ``self.demand``.
      :type \* *demand*: dict, optional

      Doesn't return anything, but overwrites ``self.characterized_inventory``. If ``demand`` is given, also overwrites ``self.demand_array``, ``self.supply_array``, and ``self.inventory``.



   .. py:method:: remap_inventory_dicts() -> None

      Remap ``self.dicts.activity|product|biosphere`` and ``self.demand`` from database integer IDs to keys (``(database name, code)``).

      Uses remapping dictionaries in ``self.remapping_dicts``.


   .. py:method:: reverse_dict()


   .. py:method:: solve_linear_system() -> None

      Master solution function for linear system :math:`Ax=B`.

          To most numerical analysts, matrix inversion is a sin.

          -- Nicolas Higham, Accuracy and Stability of Numerical Algorithms, Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 2002, p. 260.

      We use `UMFpack <http://www.cise.ufl.edu/research/sparse/umfpack/>`_, which is a very fast solver for sparse matrices.

      If the technosphere matrix has already been factorized, then the decomposed technosphere (``self.solver``) is reused. Otherwise the calculation is redone completely.



   .. py:method:: switch_method(method=Union[tuple, Iterable[Union[FS, bwp.DatapackageBase]]]) -> None

      Load a new method and replace ``.characterization_mm`` and ``.characterization_matrix``.

      Does not do any new calculations or change ``.characterized_inventory``.


   .. py:method:: switch_normalization(normalization=Union[tuple, Iterable[Union[FS, bwp.DatapackageBase]]]) -> None

      Load a new normalization and replace ``.normalization_mm`` and ``.normalization_matrix``.

      Does not do any new calculations or change ``.normalized_inventory``.


   .. py:method:: switch_weighting(weighting=Union[tuple, Iterable[Union[FS, bwp.DatapackageBase]]]) -> None

      Load a new weighting and replace ``.weighting_mm`` and ``.weighting_matrix``.

      Does not do any new calculations or change ``.weighted_inventory``.


   .. py:method:: to_dataframe(matrix_label: str = 'characterized_inventory', row_dict: Optional[dict] = None, col_dict: Optional[dict] = None, annotate: bool = True, cutoff: numbers.Number = 200, cutoff_mode: str = 'number') -> pandas.DataFrame

      Return all nonzero elements of the given matrix as a Pandas dataframe.

      The LCA class instance must have the matrix ``matrix_label`` already; common labels are:

      * characterized_inventory
      * inventory
      * technosphere_matrix
      * biosphere_matrix
      * characterization_matrix

      For these common matrices, we already have ``row_dict`` and ``col_dict`` which link row and column indices to database ids. For other matrices, or if you have a custom mapping dictionary, override ``row_dict`` and/or ``col_dict``. They have the form ``{matrix index: identifier}``.

      If ``bw2data`` is installed, this function will try to look up metadata on the row and column objects. To turn this off, set ``annotate`` to ``False``.

      Instead of returning all possible values, you can apply a cutoff. This cutoff can be specified in two ways, controlled by ``cutoff_mode``, which should be either ``fraction`` or ``number``.

      If ``cutoff_mode`` is ``number`` (the default), then ``cutoff`` is the number of rows in the DataFrame. Data values are first sorted by their absolute value, and then the largest ``cutoff`` are taken.

      If ``cutoff_mode`` is ``fraction``, then only values whose absolute value is greater than ``cutoff * total_score`` are taken. ``cutoff`` must be between 0 and 1.

      The returned DataFrame will have the following columns:

      * amount
      * col_index
      * row_index

      If row or columns dictionaries are available, the following columns are added:

      * col_id
      * row_id

      If ``bw2data`` is available, then the following columns are added:

      * col_code
      * col_database
      * col_location
      * col_name
      * col_reference_product
      * col_type
      * col_unit
      * row_categories
      * row_code
      * row_database
      * row_location
      * row_name
      * row_type
      * row_unit
      * source_product

      Returns a pandas ``DataFrame``.



   .. py:method:: weight() -> None

      Multiply characterized inventory by weighting value.

      Can be done with or without normalization.


   .. py:method:: weighting() -> None

      Backwards compatibility. Switching to verb form consistent with ``.normalize``.


   .. py:method:: weighting_calculation() -> None

      The actual weighting calculation.

      Multiples weighting value by normalized inventory, if available, otherwise by characterized inventory.

      Creates ``self.weighted_inventory``.



.. py:data:: get_node

   

.. py:data:: logger

   

