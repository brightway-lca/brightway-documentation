:py:mod:`bw2regional.export`
============================

.. py:module:: bw2regional.export


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2regional.export.add_attributes
   bw2regional.export.unplottable
   bw2regional.export.create_geodataframe
   bw2regional.export._generic_exporter
   bw2regional.export._hash_feature
   bw2regional.export.add_two_geojson_results



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2regional.export.as_inv_spatial_scale
   bw2regional.export.as_ia_spatial_scale
   bw2regional.export.as_xt_spatial_scale


.. py:function:: add_attributes(dct, func, row_index, col_index)


.. py:function:: unplottable(key)


.. py:function:: create_geodataframe(matrix, used_geocollections, row_dict, col_dict, spatial_dim='col', attribute_adder=None, cutoff=None)


.. py:function:: _generic_exporter(lca, geocollection, filepath, spatial_dict, spatial_func, score_column_absolute='score_abs', score_column_relative='score_rel', cutoff=0.001)


.. py:data:: as_inv_spatial_scale
   

   

.. py:data:: as_ia_spatial_scale
   

   

.. py:data:: as_xt_spatial_scale
   

   

.. py:function:: _hash_feature(feature)

   Calculate SHA256 hash of feature geometry as WKT


.. py:function:: add_two_geojson_results(first, second, output_filepath, first_column_name='score_abs', second_column_name='score_abs', score_column_absolute='score_abs', score_column_relative='score_rel', cutoff=0.0001)

   Sum results from two regionalized LCA calculations on the same spatial scale.


