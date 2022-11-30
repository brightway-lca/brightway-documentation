:py:mod:`bw2regional.lca.two_spatial_scales_weighting`
======================================================

.. py:module:: bw2regional.lca.two_spatial_scales_weighting


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2regional.lca.two_spatial_scales_weighting.TwoSpatialScalesWithGenericLoadingLCA




.. py:class:: TwoSpatialScalesWithGenericLoadingLCA(*args, **kwargs)

   Bases: :py:obj:`bw2regional.lca.base_class.RegionalizationBase`

   An LCI or LCIA calculation.

   Compatible with Brightway2 and 2.5 semantics. Can be static, stochastic, or iterative (scenario-based), depending on the ``data_objs`` input data..


   .. py:attribute:: matrix_labels
      :annotation: = ['biosphere_mm', 'geo_transform_mm', 'inv_mapping_mm', 'reg_cf_mm', 'technosphere_mm', 'loading_mm']

      

   .. py:method:: load_lcia_data()

      Load data and create characterization matrix.

      This method will filter out regionalized characterization factors.



   .. py:method:: after_matrix_iteration()


   .. py:method:: build_normalization_matrix()

      Get normalization matrix, a diagonal matrix.

      .. math::
          \textbf{N}_{i,i} = \left[ \sum_{j} \left( \textbf{GL} \right)_{i,j} \right]^{-1}



   .. py:method:: lcia_calculation()

      Do regionalized LCA calculation.

      Creates ``self.characterized_inventory``.



   .. py:method:: results_ia_spatial_scale()


   .. py:method:: results_inv_spatial_scale()



