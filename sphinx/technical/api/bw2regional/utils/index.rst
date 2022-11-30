:py:mod:`bw2regional.utils`
===========================

.. py:module:: bw2regional.utils


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2regional.utils.filter_fiona_metadata
   bw2regional.utils.import_regionalized_cfs
   bw2regional.utils.get_pandarus_map
   bw2regional.utils.get_pandarus_map_for_method
   bw2regional.utils.hash_collection
   bw2regional.utils.create_empty_intersection
   bw2regional.utils.get_spatial_dataset_kind
   bw2regional.utils.reset_all_geo
   bw2regional.utils.reset_geo_meta
   bw2regional.utils.filter_rows
   bw2regional.utils.filter_columns
   bw2regional.utils.create_certain_datapackage
   bw2regional.utils.dp



.. py:function:: filter_fiona_metadata(dct)

   Include only valid Fiona keywords for opening a feature collection


.. py:function:: import_regionalized_cfs(geocollection, method_tuple, mapping, scaling_factor=1, global_cfs=None, nan_value=None)

   Import data from a vector geospatial dataset into a ``Method``.

   A ``Method`` can have both site-generic and regionalized characterization factors.

   The ``mapping`` defines which field (vector) maps to which biosphere flows. Some geocollections may only define regionalized chracterization factors for a single biosphere flow, but it is much more common to have each field or band map to multiple biosphere flows. Therefore, mapping should be defined as:

   .. code-block:: python

       {
           field name (str): [list of biosphere flows (tuples)]
       }

   :param \* *geocollection*: A ``geocollection`` name.
   :param \* *method_tuple*: A method tuple.
   :param \* *mapping*: Mapping from fields or bands to biosphere flows. See above.
   :param \* *scaling_factor*: Optional. Rescale the values in the spatial data source.
   :param \* *global_cfs*: An optional list of CFs to add when writing the method.
   :param \* *nan_value*: Sentinel value for missing values if ``NaN`` is not used directly.


.. py:function:: get_pandarus_map(geocollection)


.. py:function:: get_pandarus_map_for_method(method, geocollection=None)


.. py:function:: hash_collection(name)

   Return SHA256 hash for a topo- or geocollection.

   Prefers topocollection if available.


.. py:function:: create_empty_intersection(name)

   Shortcut to create Intersection object with no data


.. py:function:: get_spatial_dataset_kind(filepath)

   Get kind of spatial dataset at `filepath`.

   Returns one of "vector", "raster", None.



.. py:function:: reset_all_geo()

   Reset all bw2regional data and metadata


.. py:function:: reset_geo_meta()


.. py:function:: filter_rows(matrix, row_indices, exclude=True)

   Filter a sparse matrix, either excluding or taking only the rows in ``row_indices``.

   * ``matrix``: A Scipy sparse matrix.
   * ``row_indices``: An iterable of integer row indices
   * ``exclude``: Boolean. If true, exclude rows in ``row_indices``. Otherwise, include only rows in ``row_indices``.

   Returns a sparse matrix.


.. py:function:: filter_columns(matrix, col_indices, exclude=True)

   Filter a sparse matrix, either excluding or taking only the columns in ``col_indices``.

   * ``matrix``: A Scipy sparse matrix.
   * ``col_indices``: An iterable of integer column indices
   * ``exclude``: Boolean. If true, exclude rows in ``row_indices``. Otherwise, include only rows in ``row_indices``.

   Returns a sparse matrix.


.. py:function:: create_certain_datapackage(indices, data, data_store, **extra_metadata)


.. py:function:: dp(fp)


