:py:mod:`bw2calc.single_value_diagonal_matrix`
==============================================

.. py:module:: bw2calc.single_value_diagonal_matrix


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2calc.single_value_diagonal_matrix.SingleValueDiagonalMatrix




.. py:class:: SingleValueDiagonalMatrix(*, packages: Sequence[bw_processing.Datapackage], matrix: str, dimension: int, use_vectors: bool = True, use_arrays: bool = True, use_distributions: bool = False, seed_override: Union[int, None] = None, indexer_override: Any = None, custom_filter: Union[Callable, None] = None)

   Bases: :py:obj:`matrix_utils.MappedMatrix`

   .. autoapi-inheritance-diagram:: bw2calc.single_value_diagonal_matrix.SingleValueDiagonalMatrix
      :parts: 1
      :private-bases:

   A scipy sparse matrix handler which takes in ``bw_processing`` data packages. Row and column ids are mapped to matrix indices, and a matrix is constructed.

   `indexer_override` allows for custom indexer behaviour. Indexers should follow a simple API: they must support `.__next__()`, and have the attribute `.index`, which returns an integer.

   `custom_filter` allows you to remove some data based on their indices. It is applied to all resource groups. If you need more fine-grained control, process the matrix after construction/iteration. `custom_filter` should take the indices array as an input, and return a Numpy boolean array with the same length as the indices array.

   :param \* packages: A list of Ddatapackage objects.
   :param \* matrix: The string identifying the matrix to be built.
   :param \* use_vectors: Flag to use vector data from datapackages
   :param \* use_arrays: Flag to use array data from datapackages
   :param \* use_distributions: Flag to use `stats_arrays` distribution data from datapackages
   :param \* row_mapper: Optional instance of `ArrayMapper`. Used when matrices must align.
   :param \* col_mapper: Optional instance of `ArrayMapper`. Used when matrices must align.
   :param \* seed_override: Optional integer. Overrides the RNG seed given in the datapackage, if any.
   :param \* indexer_override: Parameter for custom indexers. See above.
   :param \* diagonal: If True, only use the `row` indices to build a diagonal matrix.
   :param \* custom_filter: Callable for function to filter data based on `indices` values. See above.
   :param \* empty_ok: If False, raise `AllArraysEmpty` if the matrix would be empty

   .. py:method:: rebuild_matrix()



