:py:mod:`bw2regional.lca.extension_tables`
==========================================

.. py:module:: bw2regional.lca.extension_tables


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2regional.lca.extension_tables.ExtensionTablesLCA




.. py:class:: ExtensionTablesLCA(*args, **kwargs)

   Bases: :py:obj:`bw2regional.lca.base_class.RegionalizationBase`

   An LCI or LCIA calculation.

   Compatible with Brightway2 and 2.5 semantics. Can be static, stochastic, or iterative (scenario-based), depending on the ``data_objs`` input data..


   .. py:attribute:: matrix_labels
      :annotation: = ['biosphere_mm', 'distribution_mm', 'geo_transform_mm', 'inv_mapping_mm', 'reg_cf_mm',...

      

   .. py:method:: needed_inv_xtable_intersections()


   .. py:method:: needed_xtable_ia_intersections()


   .. py:method:: check_geocollection_intersections()


   .. py:method:: get_xtable_geodata()


   .. py:method:: create_distribution_matrix()

      Get distribution matrix, **D**, which provides the area of inventory spatial units in each extension table spatial unit. Rows are inventory spatial units and columns are extension table spatial units.


   .. py:method:: create_xtable_matrix()

      Diagonal extension table matrix that indicates the extension table density value in each extension table spatial unit.


   .. py:method:: build_distribution_normalization_matrix()

      Get normalization matrix for inventory-xtable mapping. Normalizes to

      .. math::
          ( \textbf{N}_{dx} )_{i, i} = \left[ \sum_{j} \textbf{DX}_{i, j} \right]^{-1}



   .. py:method:: build_geo_transform_normalization_matrix()

      Get normalization value for areas in each IA spatial unit:

      .. math::
          ( \textbf{N}_{g} )_{i, i} = \left[ \sum_{j} \textbf{G}_{i, j} \right]^{-1}



   .. py:method:: create_geo_transform_matrix()

      Get geographic transform matrix **G**, which gives the intersecting areas of inventory and impact assessment spatial units. Rows are inventory spatial units, and columns are impact assessment spatial units.

      Uses ``self.inv_spatial_dict`` and ``self.ia_spatial_dict``.

      :returns: Parameter array with row/col of inventory and IA locations
                * ``geo_transform_matrix``: The matrix **G**
      :rtype: * ``geo_transform_params``


   .. py:method:: after_matrix_iteration()


   .. py:method:: apply_inv_mappinig_limitations()


   .. py:method:: apply_cf_matrix_limitations()


   .. py:method:: load_lcia_data()

      Load data and create characterization matrix.

      This method will filter out regionalized characterization factors.



   .. py:method:: lcia_calculation()

      Do regionalized LCA calculation.

      Creates ``self.characterized_inventory``.



   .. py:method:: results_ia_spatial_scale()


   .. py:method:: results_inv_spatial_scale()


   .. py:method:: results_xtable_spatial_scale()



