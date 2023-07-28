:py:mod:`bw2calc.matrices`
==========================

.. py:module:: bw2calc.matrices


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2calc.matrices.MatrixBuilder
   bw2calc.matrices.SingleMatrixBuilder
   bw2calc.matrices.TechnosphereBiosphereMatrixBuilder




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



.. py:class:: SingleMatrixBuilder

   Bases: :py:obj:`MatrixBuilder`

   .. autoapi-inheritance-diagram:: bw2calc.matrices.SingleMatrixBuilder
      :parts: 1
      :private-bases:

   Subclass of ``MatrixBuilder`` that supports consumption (i.e. multiply by -1).

   .. py:method:: build(path)
      :classmethod:

      Build the technosphere and biosphere sparse matrices.


   .. py:method:: build_single_matrix(array, row_dict, col_dict, new_data=None)
      :classmethod:


   .. py:method:: fix_supply_use(array, vector)
      :classmethod:

      Make technosphere inputs negative.



.. py:class:: TechnosphereBiosphereMatrixBuilder

   Bases: :py:obj:`MatrixBuilder`

   .. autoapi-inheritance-diagram:: bw2calc.matrices.TechnosphereBiosphereMatrixBuilder
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



