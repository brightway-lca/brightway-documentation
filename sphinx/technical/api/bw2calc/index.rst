:py:mod:`bw2calc`
=================

.. py:module:: bw2calc


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   dense_lca/index.rst
   dictionary_manager/index.rst
   errors/index.rst
   graph_traversal/index.rst
   lca/index.rst
   least_squares/index.rst
   log_utils/index.rst
   monte_carlo/index.rst
   multi_lca/index.rst
   single_value_diagonal_matrix/index.rst
   utils/index.rst
   version/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   bw2calc.DenseLCA
   bw2calc.GraphTraversal
   bw2calc.MultifunctionalGraphTraversal
   bw2calc.LeastSquaresLCA
   bw2calc.MultiLCA




.. py:class:: DenseLCA(demand: dict, method: Optional[tuple] = None, weighting: Optional[str] = None, normalization: Optional[str] = None, data_objs: Optional[Iterable[Union[pathlib.Path, fs.base.FS, bw_processing.DatapackageBase]]] = None, remapping_dicts: Optional[Iterable[dict]] = None, log_config: Optional[dict] = None, seed_override: Optional[int] = None, use_arrays: bool = False, use_distributions: bool = False)

   Bases: :py:obj:`bw2calc.lca.LCA`

   An LCI or LCIA calculation.

   Compatible with Brightway2 and 2.5 semantics. Can be static, stochastic, or iterative (scenario-based), depending on the ``data_objs`` input data..


   .. py:method:: solve_linear_system()

      Master solution function for linear system :math:`Ax=B`.

          To most numerical analysts, matrix inversion is a sin.

          -- Nicolas Higham, Accuracy and Stability of Numerical Algorithms, Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 2002, p. 260.

      We use `UMFpack <http://www.cise.ufl.edu/research/sparse/umfpack/>`_, which is a very fast solver for sparse matrices.

      If the technosphere matrix has already been factorized, then the decomposed technosphere (``self.solver``) is reused. Otherwise the calculation is redone completely.




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



.. py:class:: LeastSquaresLCA(demand: dict, method: Optional[tuple] = None, weighting: Optional[str] = None, normalization: Optional[str] = None, data_objs: Optional[Iterable[Union[pathlib.Path, fs.base.FS, bw_processing.DatapackageBase]]] = None, remapping_dicts: Optional[Iterable[dict]] = None, log_config: Optional[dict] = None, seed_override: Optional[int] = None, use_arrays: bool = False, use_distributions: bool = False)

   Bases: :py:obj:`bw2calc.lca.LCA`

   Solve overdetermined technosphere matrix with more products than activities using least-squares approximation.

   See also:

   * `Multioutput processes in LCA <http://chris.mutel.org/multioutput.html>`_
   * `LSMR in SciPy <http://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.lsmr.html#scipy.sparse.linalg.lsmr>`_
   * `Another least-squares algorithm in SciPy <http://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.lsqr.html#scipy.sparse.linalg.lsqr>`_


   .. py:method:: load_lci_data() -> None

      Load inventory data and create technosphere and biosphere matrices.


   .. py:method:: solve_linear_system(solver=lsmr) -> numpy.ndarray

      Master solution function for linear system :math:`Ax=B`.

          To most numerical analysts, matrix inversion is a sin.

          -- Nicolas Higham, Accuracy and Stability of Numerical Algorithms, Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 2002, p. 260.

      We use `UMFpack <http://www.cise.ufl.edu/research/sparse/umfpack/>`_, which is a very fast solver for sparse matrices.

      If the technosphere matrix has already been factorized, then the decomposed technosphere (``self.solver``) is reused. Otherwise the calculation is redone completely.



   .. py:method:: decompose_technosphere() -> None
      :abstractmethod:

      Factorize the technosphere matrix into lower and upper triangular matrices, :math:`A=LU`. Does not solve the linear system :math:`Ax=B`.

      Doesn't return anything, but creates ``self.solver``.

      .. warning:: Incorrect results could occur if a technosphere matrix was factorized, and then a new technosphere matrix was constructed, as ``self.solver`` would still be the factorized older technosphere matrix. You are responsible for deleting ``self.solver`` when doing these types of advanced calculations.




.. py:class:: MultiLCA(cs_name, log_config=None)

   Wrapper class for performing LCA calculations with many functional units and LCIA methods.

   Needs to be passed a ``calculation_setup`` name.

   This class does not subclass the `LCA` class, and performs all calculations upon instantiation.

   Initialization creates `self.results`, which is a NumPy array of LCA scores, with rows of functional units and columns of LCIA methods. Ordering is the same as in the `calculation_setup`.


   .. py:property:: all

      Get all possible databases by merging all functional units


