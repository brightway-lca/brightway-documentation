:py:mod:`bw2regional.lca.base_class`
====================================

.. py:module:: bw2regional.lca.base_class


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2regional.lca.base_class.RegionalizationBase



Functions
~~~~~~~~~

.. autoapisummary::

   bw2regional.lca.base_class.get_dependent_databases
   bw2regional.lca.base_class.annotate_flow



.. py:function:: get_dependent_databases(demand_dict)

   Demand can be activitiy ids or tuple keys.


.. py:function:: annotate_flow(flow_id, _)


.. py:class:: RegionalizationBase(demand, *args, **kwargs)

   Bases: :py:obj:`bw2calc.lca.LCA`

   An LCI or LCIA calculation.

   Compatible with Brightway2 and 2.5 semantics. Can be static, stochastic, or iterative (scenario-based), depending on the ``data_objs`` input data..


   .. py:method:: get_inventory_geocollections()

      Get the set of all needed inventory geocollections.

      Raise UnprocessedDatabase if any database is missing the required metadata.


   .. py:method:: get_ia_geocollections()

      Retrieve the geocollections linked to the impact assessment method


   .. py:method:: create_inventory_mapping_matrix()

      Get inventory mapping matrix, **M**, which maps inventory activities to inventory locations. Rows are inventory activities and columns are inventory spatial units.

      Uses ``self.technosphere_mm.row_mapper`` and ``self.databases``.

      Creates ``self.inv_mapping_mm``, ``self.inv_mapping_matrix``, and ``self.dicts.inv_spatial``/



   .. py:method:: needed_intersections()

      Figure out which ``Intersection`` objects are needed bsed on ``self.inventory_geocollections`` and ``self.ia_geocollections``.

      Raise ``MissingIntersection`` if an intersection is required, but not available.


   .. py:method:: create_geo_transform_matrix()

      Get geographic transform matrix **G**, which gives the intersecting areas of inventory and impact assessment spatial units. Rows are inventory spatial units, and columns are impact assessment spatial units.

      Uses ``self.inv_spatial_dict`` and ``self.ia_spatial_dict``.

      :returns: Parameter array with row/col of inventory and IA locations
                * ``geo_transform_matrix``: The matrix **G**
      :rtype: * ``geo_transform_params``


   .. py:method:: create_regionalized_characterization_matrix(row_mapper=None)

      Get regionalized characterization matrix, **R**, which gives location- and biosphere flow-specific characterization factors.

      Rows are impact assessment spatial units, and columns are biosphere flows. However, we build it transverse and transpose it, as the characterization matrix indices are provided that way.

      Uses ``self._biosphere_dict`` and ``self.method``.

      :returns: Parameter array with row/col of IA locations/biosphere flows
                * ``ia_spatial_dict``: Dictionary linking impact assessment locations to matrix rows
                * ``reg_cf_matrix``: The matrix **R**
      :rtype: * ``reg_cf_params``


   .. py:method:: create_loading_matrix()

      Get diagonal regionalized loading matrix, **L**, which gives location-specific background loading factors. Dimensions are impact assessment spatial units.

      Uses ``self.dicts.ia_spatial``.



   .. py:method:: _results_new_scale(matrix, flow)


   .. py:method:: results_ia_spatial_scale()
      :abstractmethod:


   .. py:method:: results_inv_spatial_scale()
      :abstractmethod:


   .. py:method:: __geodataframe(matrix, sum_flows, annotate_flows, col_dict, used_geocollections, cutoff)


   .. py:method:: geodataframe_xtable_spatial_scale(sum_flows=True, annotate_flows=None, cutoff=None)


   .. py:method:: geodataframe_ia_spatial_scale(sum_flows=True, annotate_flows=None, cutoff=None)


   .. py:method:: geodataframe_inv_spatial_scale(sum_flows=True, annotate_flows=None, cutoff=None)



