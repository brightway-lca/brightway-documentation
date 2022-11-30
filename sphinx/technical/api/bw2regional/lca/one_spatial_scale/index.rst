:py:mod:`bw2regional.lca.one_spatial_scale`
===========================================

.. py:module:: bw2regional.lca.one_spatial_scale


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2regional.lca.one_spatial_scale.OneSpatialScaleLCA




.. py:class:: OneSpatialScaleLCA(*args, **kwargs)

   Bases: :py:obj:`bw2regional.lca.base_class.RegionalizationBase`

   An LCI or LCIA calculation.

   Compatible with Brightway2 and 2.5 semantics. Can be static, stochastic, or iterative (scenario-based), depending on the ``data_objs`` input data..


   .. py:attribute:: matrix_labels
      :annotation: = ['biosphere_mm', 'inv_mapping_mm', 'reg_cf_mm', 'technosphere_mm']

      

   .. py:method:: load_lcia_data()

      Load data and create characterization matrix.

      This method will filter out regionalized characterization factors.



   .. py:method:: lcia_calculation()

      Do regionalized LCA calculation.

      Creates ``self.characterized_inventory``.



   .. py:method:: results_ia_spatial_scale()
      :abstractmethod:


   .. py:method:: results_inv_spatial_scale()



