:py:mod:`bw2regional`
=====================

.. py:module:: bw2regional


Subpackages
-----------
.. toctree::
   :titlesonly:
   :maxdepth: 3

   lca/index.rst


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   base_data/index.rst
   databases/index.rst
   density/index.rst
   errors/index.rst
   export/index.rst
   gis_tasks/index.rst
   hashing/index.rst
   intersection/index.rst
   loading/index.rst
   meta/index.rst
   pandarus/index.rst
   pandarus_remote/index.rst
   topography/index.rst
   utils/index.rst
   validate/index.rst
   version/index.rst
   xtables/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   bw2regional.Topography
   bw2regional.Loading
   bw2regional.Intersection
   bw2regional.ExtensionTable
   bw2regional.ExtensionTablesLCA
   bw2regional.OneSpatialScaleLCA
   bw2regional.TwoSpatialScalesLCA
   bw2regional.TwoSpatialScalesWithGenericLoadingLCA
   bw2regional.PandarusRemote



Functions
~~~~~~~~~

.. autoapisummary::

   bw2regional.divide_by_area
   bw2regional.create_ecoinvent_collections
   bw2regional.create_restofworlds_collections
   bw2regional.create_world_collections
   bw2regional.calculate_intersection
   bw2regional.raster_as_extension_table
   bw2regional.sha256
   bw2regional.import_from_pandarus
   bw2regional.create_empty_intersection
   bw2regional.get_spatial_dataset_kind
   bw2regional.hash_collection
   bw2regional.import_regionalized_cfs
   bw2regional.reset_all_geo
   bw2regional.reset_geo_meta



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2regional.cg
   bw2regional.extension_tables
   bw2regional.geocollections
   bw2regional.intersections
   bw2regional.loadings
   bw2regional.topocollections
   bw2regional.remote


.. py:data:: cg
   

   

.. py:class:: Topography(name)

   Bases: :py:obj:`bw2data.DataStore`

   A topographical description of a ``geocollection``.

   A topography must be registered to exactly one geocollection.

   For example, the geocollection 'countries' could have the location 'Ghana', and include a spatial data file which defines 'Ghana'. The `Topography` 'countries-topo' would have two files:

       #. A mapping file that linked each location in the geocollection 'countries' to a set of topographical faces
       #. A spatial dataset which defines the topographical faces

   Topographies can make some calculations much quicker for two reasons:

       #. Large features are split into smaller faces, making GIS calculations easier and spatial index queries more efficient, as bounding boxes are smaller
       #. You only do GIS work on each topographical face once

   The LCA classes in ``bw2regional`` don't work directly with the `Topography` objects; rather, GIS calculations on topographies can be merged to the spatial features of the `geocollection`.

   The usual order of operations with a `geocollection` that has a `Topography` is the following:

       #. Create a `geocollection`, including defining a spatial dataset
       #. Create a new `topocollection` and specify the linked `geocollection`. You can also optionally define another spatial dataset, using the same format as for `geocollections`.
       #. Instantiate the new `Topography` object created in the earlier step, and write mapping data from spatial features in the `geocollection`(s) to face ids in the `Topography` spatial data set.

   The data format for mapping data is ``{feature field value: [list of topo field values (usually id numbers)]}``.

   Here is a code sample for using the test data in `bw2regional`:

   .. code-block:: python

       from bw2regional import Topography, geocollections
       import json

       geocollections['countries'] = {
           'filepath': os.path.join(data_dir, "test_countries.gpkg"),
           'field': 'name'
       }
       topocollections['countries-topo'] = {
           'geocollection': 'countries',
           'filepath': os.path.join(data_dir, "test_provinces.gpkg"),
           'field': 'OBJECTID_1'
       }
       topo = Topography('countries-topo')
       topo.write(json.load(open(os.path.join(data_dir, "test_topo_mapping.json"))))


   .. py:property:: geocollection


   .. py:attribute:: _metadata
      

      

   .. py:method:: add_geomappings(data)


   .. py:method:: write(data)

      Serialize intermediate data to disk.

      :param \* *data*: The data
      :type \* *data*: object



.. py:class:: Loading(name)

   Bases: :py:obj:`bw2data.data_store.ProcessedDataStore`

   .. py:property:: filename

      Remove filesystem-unsafe characters and perform unicode normalization on ``self.name`` using :func:`.filesystem.safe_filename`.

   .. py:attribute:: _metadata
      

      

   .. py:attribute:: validator
      

      

   .. py:attribute:: matrix
      :annotation: = loading_matrix

      

   .. py:method:: add_geomappings(data)

      In theory, this shouldn't do anything, as all spatial units should be in defined by the method.


   .. py:method:: process(**extra_metadata)

      Process intermediate data from a Python dictionary to a `stats_arrays <https://pypi.python.org/pypi/stats_arrays/>`_ array, which is a `NumPy <http://numpy.scipy.org/>`_ `Structured <http://docs.scipy.org/doc/numpy/reference/generated/numpy.recarray.html#numpy.recarray>`_ `Array <http://docs.scipy.org/doc/numpy/user/basics.rec.html>`_. A structured array (also called record array) is a heterogeneous array, where each column has a different label and data type.

      Processed arrays are saved in the ``processed`` directory.

      If the uncertainty type is no uncertainty, undefined, or not specified, then the 'amount' value is used for 'loc' as well. This is needed for the random number generator.

      Doesn't return anything, but writes a file to disk.




.. py:data:: extension_tables
   

   

.. py:data:: geocollections
   

   

.. py:data:: intersections
   

   

.. py:data:: loadings
   

   

.. py:data:: topocollections
   

   

.. py:class:: Intersection(name)

   Bases: :py:obj:`bw2data.ia_data_store.ImpactAssessmentDataStore`

   .. py:attribute:: _metadata
      

      

   .. py:attribute:: validator
      

      

   .. py:attribute:: matrix
      :annotation: = intersection_matrix

      

   .. py:method:: add_geomappings(data)

      Add all geographic units in both geocollections to ``geomapping``, the master location list.

      Called automatically when data is written.


   .. py:method:: create_reversed_intersection()

      Create (B, A) intersection from (A, B).


   .. py:method:: process(**extra_metadata)

      Process intermediate data from a Python dictionary to a `stats_arrays <https://pypi.python.org/pypi/stats_arrays/>`_ array, which is a `NumPy <http://numpy.scipy.org/>`_ `Structured <http://docs.scipy.org/doc/numpy/reference/generated/numpy.recarray.html#numpy.recarray>`_ `Array <http://docs.scipy.org/doc/numpy/user/basics.rec.html>`_. A structured array (also called record array) is a heterogeneous array, where each column has a different label and data type.

      Processed arrays are saved in the ``processed`` directory.

      If the uncertainty type is no uncertainty, undefined, or not specified, then the 'amount' value is used for 'loc' as well. This is needed for the random number generator.

      Doesn't return anything, but writes a file to disk.




.. py:class:: ExtensionTable(name)

   Bases: :py:obj:`bw2regional.loading.Loading`

   .. py:property:: filename

      Remove filesystem-unsafe characters and perform unicode normalization on ``self.name`` using :func:`.filesystem.safe_filename`.

   .. py:attribute:: _metadata
      

      

   .. py:attribute:: validator
      

      

   .. py:attribute:: matrix
      :annotation: = xtable_matrix

      

   .. py:method:: write_to_map(*args, **kwargs)
      :abstractmethod:


   .. py:method:: import_from_map(mask=None)



.. py:function:: divide_by_area(source_fp, destination_fp)

   Create a new raster file at ``destination_fp``, dividing the values in ``source_fp`` by their cell's area.

   Will raise an error is the CRS is not geographic, or the raster is rotated.


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



.. py:class:: TwoSpatialScalesLCA(*args, **kwargs)

   Bases: :py:obj:`bw2regional.lca.base_class.RegionalizationBase`

   An LCI or LCIA calculation.

   Compatible with Brightway2 and 2.5 semantics. Can be static, stochastic, or iterative (scenario-based), depending on the ``data_objs`` input data..


   .. py:attribute:: matrix_labels
      :annotation: = ['biosphere_mm', 'geo_transform_mm', 'inv_mapping_mm', 'reg_cf_mm', 'technosphere_mm']

      

   .. py:method:: load_lcia_data()

      Load data and create characterization matrix.

      This method will filter out regionalized characterization factors.



   .. py:method:: after_matrix_iteration()


   .. py:method:: build_normalization_matrix()

      Get normalization matrix, a diagonal matrix.

      .. math::
          \textbf{N}_{i,i} = \left[ \sum_{j} \left( \textbf{G} \right)_{i,j} \right]^{-1}



   .. py:method:: lcia_calculation()

      Do regionalized LCA calculation.

      Creates ``self.characterized_inventory``.



   .. py:method:: results_ia_spatial_scale()


   .. py:method:: results_inv_spatial_scale()



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



.. py:function:: create_ecoinvent_collections()


.. py:function:: create_restofworlds_collections()


.. py:function:: create_world_collections()


.. py:function:: calculate_intersection(first, second, engine=remote, overwrite=False, cpus=None)

   Calculate and write areal intersections between two vector geocollections


.. py:function:: raster_as_extension_table(vector, raster, name=None, engine=remote, overwrite=False)


.. py:function:: sha256(filepath, blocksize=65536)

   Generate SHA 256 hash for file at `filepath`


.. py:function:: import_from_pandarus(fp)

   Load output file from Pandarus job.

   This function will:

   * Load pandarus output file
   * Locate the appropriate geo- or topocollection
   * Check to make sure that SHA256 hashes and other metadata match
   * If ``first`` is a topocollection, make sure the appropriate ``Topology`` exists, and squash the pandarus results to the linked geocollection(s).



.. py:class:: PandarusRemote(url=None)

   Bases: :py:obj:`object`

   Interaction with `pandarus_remote <https://github.com/cmutel/pandarus_remote>`__ web service.

   Default URL is `https://pandarus.brightway.dev`.

   .. py:property:: alive


   .. py:method:: _download_file(resp)


   .. py:method:: catalog()


   .. py:method:: status(url)


   .. py:method:: upload(collection)


   .. py:method:: intersection(collection_one, collection_two)


   .. py:method:: intersection_as_new_geocollection(collection_one, collection_two, new_name)


   .. py:method:: rasterstats_as_xt(vector, raster, name)


   .. py:method:: calculate_rasterstats(vector, raster)


   .. py:method:: calculate_intersection(collection_one, collection_two)


   .. py:method:: hash_and_upload(collection, catalog=None)


   .. py:method:: handle_errors(response)



.. py:data:: remote
   

   

.. py:function:: create_empty_intersection(name)

   Shortcut to create Intersection object with no data


.. py:function:: get_spatial_dataset_kind(filepath)

   Get kind of spatial dataset at `filepath`.

   Returns one of "vector", "raster", None.



.. py:function:: hash_collection(name)

   Return SHA256 hash for a topo- or geocollection.

   Prefers topocollection if available.


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


.. py:function:: reset_all_geo()

   Reset all bw2regional data and metadata


.. py:function:: reset_geo_meta()


