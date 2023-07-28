:py:mod:`bw2calc.least_squares`
===============================

.. py:module:: bw2calc.least_squares


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2calc.least_squares.LeastSquaresLCA




.. py:class:: LeastSquaresLCA(demand: dict, method: Optional[tuple] = None, weighting: Optional[str] = None, normalization: Optional[str] = None, data_objs: Optional[Iterable[Union[pathlib.Path, fs.base.FS, bw_processing.DatapackageBase]]] = None, remapping_dicts: Optional[Iterable[dict]] = None, log_config: Optional[dict] = None, seed_override: Optional[int] = None, use_arrays: bool = False, use_distributions: bool = False)

   Bases: :py:obj:`bw2calc.lca.LCA`

   .. autoapi-inheritance-diagram:: bw2calc.least_squares.LeastSquaresLCA
      :parts: 1
      :private-bases:

   Solve overdetermined technosphere matrix with more products than activities using least-squares approximation.

   See also:

   * `Multioutput processes in LCA <http://chris.mutel.org/multioutput.html>`_
   * `LSMR in SciPy <http://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.lsmr.html#scipy.sparse.linalg.lsmr>`_
   * `Another least-squares algorithm in SciPy <http://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.lsqr.html#scipy.sparse.linalg.lsqr>`_


   Create a new LCA calculation.

   :param \* *demand*: The demand or functional unit. Needs to be a dictionary to indicate amounts, e.g. ``{7: 2.5}``.
   :type \* *demand*: dict
   :param \* *method*: LCIA Method tuple, e.g. ``("My", "great", "LCIA", "method")``. Can be omitted if only interested in calculating the life cycle inventory.
   :type \* *method*: tuple, optional

   :returns: A new LCA object

   .. py:method:: decompose_technosphere() -> None
      :abstractmethod:

      Factorize the technosphere matrix into lower and upper triangular matrices, :math:`A=LU`. Does not solve the linear system :math:`Ax=B`.

      Doesn't return anything, but creates ``self.solver``.

      .. warning:: Incorrect results could occur if a technosphere matrix was factorized, and then a new technosphere matrix was constructed, as ``self.solver`` would still be the factorized older technosphere matrix. You are responsible for deleting ``self.solver`` when doing these types of advanced calculations.



   .. py:method:: load_lci_data() -> None

      Load inventory data and create technosphere and biosphere matrices.


   .. py:method:: solve_linear_system(solver=lsmr) -> numpy.ndarray

      Master solution function for linear system :math:`Ax=B`.

          To most numerical analysts, matrix inversion is a sin.

          -- Nicolas Higham, Accuracy and Stability of Numerical Algorithms, Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 2002, p. 260.

      We use `UMFpack <http://www.cise.ufl.edu/research/sparse/umfpack/>`_, which is a very fast solver for sparse matrices.

      If the technosphere matrix has already been factorized, then the decomposed technosphere (``self.solver``) is reused. Otherwise the calculation is redone completely.




