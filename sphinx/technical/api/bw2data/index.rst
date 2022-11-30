:py:mod:`bw2data`
=================

.. py:module:: bw2data


Subpackages
-----------
.. toctree::
   :titlesonly:
   :maxdepth: 3

   backends/index.rst
   bin/index.rst
   search/index.rst


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   compat/index.rst
   configuration/index.rst
   data_store/index.rst
   database/index.rst
   errors/index.rst
   fatomic/index.rst
   filesystem/index.rst
   ia_data_store/index.rst
   logs/index.rst
   meta/index.rst
   method/index.rst
   parameters/index.rst
   project/index.rst
   proxies/index.rst
   query/index.rst
   serialization/index.rst
   sqlite/index.rst
   tests/index.rst
   updates/index.rst
   utils/index.rst
   validate/index.rst
   version/index.rst
   weighting_normalization/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.JsonWrapper
   bw2data.Database
   bw2data.Method
   bw2data.Searcher
   bw2data.IndexManager
   bw2data.Weighting
   bw2data.Normalization



Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.set_data_dir
   bw2data.get_activity
   bw2data.get_node
   bw2data.get_id
   bw2data.prepare_lca_inputs
   bw2data.extract_brightway_databases



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2data.config
   bw2data.projects
   bw2data.dynamic_calculation_setups
   bw2data.calculation_setups
   bw2data.geomapping
   bw2data.methods
   bw2data.normalizations
   bw2data.preferences
   bw2data.weightings
   bw2data.Node
   bw2data.Edge
   bw2data.databases
   bw2data.mapping
   bw2data.parameters


.. py:data:: config
   

   

.. py:data:: projects
   

   

.. py:function:: set_data_dir(dirpath, permanent=True)

   Set the Brightway2 data directory to ``dirpath``.

   If ``permanent`` is ``True``, then set ``dirpath`` as the default data directory.

   Creates ``dirpath`` if needed. Also creates basic directories, and resets metadata.



.. py:data:: dynamic_calculation_setups
   

   

.. py:data:: calculation_setups
   

   

.. py:data:: geomapping
   

   

.. py:data:: methods
   

   

.. py:data:: normalizations
   

   

.. py:data:: preferences
   

   

.. py:data:: weightings
   

   

.. py:class:: JsonWrapper

   .. py:method:: dump(data, filepath)
      :classmethod:


   .. py:method:: dump_bz2(data, filepath)
      :classmethod:


   .. py:method:: load(file)
      :classmethod:


   .. py:method:: load_bz2(filepath)
      :classmethod:


   .. py:method:: dumps(data)
      :classmethod:


   .. py:method:: loads(data)
      :classmethod:



.. py:class:: Database(name=None, *args, **kwargs)

   Bases: :py:obj:`peewee.Model`

   A base class for SQLite backends.

   Subclasses must support at least the following calls:

   * ``load()``
   * ``write(data)``

   In addition, they should specify their backend with the ``backend`` attribute (a unicode string).

   * ``rename``
   * ``copy``
   * ``find_dependents``
   * ``random``
   * ``process``

   For new classes to be recognized by the ``DatabaseChooser``, they need to be registered with the ``config`` object, e.g.:

   .. code-block:: python

       config.backends['backend type string'] = BackendClass

   Instantiation does not load any data. If this database is not yet registered in the metadata store, a warning is written to ``stdout``.

   The data schema for databases in voluptuous is:

   .. code-block:: python

       exchange = {
               Required("input"): valid_tuple,
               Required("type"): basestring,
               }
       exchange.update(uncertainty_dict)
       lci_dataset = {
           Optional("categories"): Any(list, tuple),
           Optional("location"): object,
           Optional("unit"): basestring,
           Optional("name"): basestring,
           Optional("type"): basestring,
           Optional("exchanges"): [exchange]
       }
       db_validator = Schema({valid_tuple: lci_dataset}, extra=True)

   where:
       * ``valid_tuple`` is a :ref:`dataset identifier <dataset-codes>`, like ``("ecoinvent", "super strong steel")``
       * ``uncertainty_fields`` are fields from an :ref:`uncertainty dictionary <uncertainty-type>`.

   Processing a Database actually produces two parameter arrays: one for the exchanges, which make up the technosphere and biosphere matrices, and a geomapping array which links activities to locations.

   :param \*name*: Name of the database to manage.
   :type \*name*: unicode string

   .. py:property:: node_class


   .. py:property:: filename

      Remove filesystem-unsafe characters and perform unicode normalization on ``self.name`` using :func:`.filesystem.safe_filename`.

   .. py:property:: metadata


   .. py:property:: registered


   .. py:property:: _metadata


   .. py:attribute:: name
      

      

   .. py:attribute:: backend
      

      

   .. py:attribute:: depends
      

      

   .. py:attribute:: geocollections
      

      

   .. py:attribute:: dirty
      

      

   .. py:attribute:: searchable
      

      

   .. py:attribute:: extra
      

      

   .. py:attribute:: validator
      

      

   .. py:attribute:: __repr__
      

      

   .. py:attribute:: filters
      

      

   .. py:attribute:: order_by
      

      

   .. py:method:: __str__()


   .. py:method:: __lt__(other)


   .. py:method:: exists(name)
      :classmethod:


   .. py:method:: set_dirty(name)
      :classmethod:


   .. py:method:: copy(name)

      Make a copy of the database.

      Internal links within the database will be updated to match the new database name, i.e. ``("old name", "some id")`` will be converted to ``("new name", "some id")`` for all exchanges.

      :param \* *name*: Name of the new database. Must not already exist.
      :type \* *name*: str


   .. py:method:: dirpath_processed()


   .. py:method:: filepath_intermediate()


   .. py:method:: filename_processed()


   .. py:method:: filepath_processed(clean=True)


   .. py:method:: datapackage()


   .. py:method:: find_dependents(data=None, ignore=None)

      Get sorted list of direct dependent databases (databases linked from exchanges).

      :param \* *data*: Inventory data
      :type \* *data*: dict, optional
      :param \* *ignore*: List of database names to ignore
      :type \* *ignore*: list

      :returns: List of database names


   .. py:method:: find_graph_dependents()

      Recursively get list of all dependent databases.

      :returns: A set of database names


   .. py:method:: query(*queries)

      Search through the database.


   .. py:method:: relabel_data(data, new_name)

      Relabel database keys and exchanges.

      In a database which internally refer to the same database, update to new database name ``new_name``.

      Needed to copy a database completely or cut out a section of a database.

      For example:

      .. code-block:: python

          data = {
              ("old and boring", 1):
                  {"exchanges": [
                      {"input": ("old and boring", 42),
                      "amount": 1.0},
                      ]
                  },
              ("old and boring", 2):
                  {"exchanges": [
                      {"input": ("old and boring", 1),
                      "amount": 4.0}
                      ]
                  }
              }
          print(relabel_database(data, "shiny new"))
          >> {
              ("shiny new", 1):
                  {"exchanges": [
                      {"input": ("old and boring", 42),
                      "amount": 1.0},
                      ]
                  },
              ("shiny new", 2):
                  {"exchanges": [
                      {"input": ("shiny new", 1),
                      "amount": 4.0}
                      ]
                  }
              }

      In the example, the exchange to ``("old and boring", 42)`` does not change, as this is not part of the updated data.

      :param \* *data*: The data to modify
      :type \* *data*: dict
      :param \* *new_name*: The name of the modified database
      :type \* *new_name*: str

      :returns: The modified data


   .. py:method:: rename(name)

      Rename a database. Modifies exchanges to link to new name.

      :param \* *name*: New name.
      :type \* *name*: str

      :returns: self  # Backwards compatibility


   .. py:method:: __iter__()


   .. py:method:: __len__()


   .. py:method:: __contains__(obj)


   .. py:method:: _get_queryset(random=False, filters=True)


   .. py:method:: _get_filters()


   .. py:method:: _set_filters(filters)


   .. py:method:: _get_order_by()


   .. py:method:: _set_order_by(field)


   .. py:method:: random(filters=True, true_random=False)

      True random requires loading and sorting data in SQLite, and can be resource-intensive.


   .. py:method:: get_node(code=None, **kwargs)


   .. py:method:: _drop_indices()


   .. py:method:: _add_indices()


   .. py:method:: _efficient_write_dataset(index, key, ds, exchanges, activities)


   .. py:method:: _efficient_write_many_data(data, indices=True)


   .. py:method:: write(data, process=True)

      Write ``data`` to database.

      ``data`` must be a dictionary of the form::

          {
              ('database name', 'dataset code'): {dataset}
          }

      Writing a database will first deletes all existing data.


   .. py:method:: write_exchanges(technosphere, biosphere, dependents)

      Write IO data directly to processed arrays.

      Product data is stored in SQLite as normal activities.
      Exchange data is written directly to NumPy structured arrays.

      Technosphere and biosphere data has format ``(row id, col id, value, flip)``.



   .. py:method:: load(*args, **kwargs)


   .. py:method:: new_activity(code, **kwargs)


   .. py:method:: new_node(code=None, **kwargs)


   .. py:method:: make_searchable(reset=False)


   .. py:method:: make_unsearchable()


   .. py:method:: delete_instance()


   .. py:method:: delete_data(keep_params=False, warn=True)

      Delete all data from SQLite database and Whoosh index


   .. py:method:: exchange_data_iterator(sql, dependents, flip=False)

      Iterate over exchanges and format for ``bw_processing`` arrays.

      ``dependents`` is a set of dependent database names.

      ``flip`` means flip the numeric sign; see ``bw_processing`` docs.

      Uses raw sqlite3 to retrieve data for ~2x speed boost.


   .. py:method:: clean_all()
      :classmethod:


   .. py:method:: process(csv=False)

      Create structured arrays for the technosphere and biosphere matrices.

      Uses ``bw_processing`` for array creation and metadata serialization.

      Also creates a ``geomapping`` array, linking activities to locations. Used for regionalized calculations.

      Use a raw SQLite3 cursor instead of Peewee for a ~2 times speed advantage.



   .. py:method:: search(string, **kwargs)

      Search this database for ``string``.

      The searcher include the following fields:

      * name
      * comment
      * categories
      * location
      * reference product

      ``string`` can include wild cards, e.g. ``"trans*"``.

      By default, the ``name`` field is given the most weight. The full weighting set is called the ``boost`` dictionary, and the default weights are::

          {
              "name": 5,
              "comment": 1,
              "product": 3,
              "categories": 2,
              "location": 3
          }

      Optional keyword arguments:

      * ``limit``: Number of results to return.
      * ``boosts``: Dictionary of field names and numeric boosts - see default boost values above. New values must be in the same format, but with different weights.
      * ``filter``: Dictionary of criteria that search results must meet, e.g. ``{'categories': 'air'}``. Keys must be one of the above fields.
      * ``mask``: Dictionary of criteria that exclude search results. Same format as ``filter``.
      * ``facet``: Field to facet results. Must be one of ``name``, ``product``, ``categories``, ``location``, or ``database``.
      * ``proxy``: Return ``Activity`` proxies instead of raw Whoosh documents. Default is ``True``.

      Returns a list of ``Activity`` datasets.


   .. py:method:: set_geocollections()

      Set ``geocollections`` attribute for databases which don't currently have it.


   .. py:method:: graph_technosphere(filename=None, **kwargs)


   .. py:method:: delete_duplicate_exchanges(fields=['amount', 'type'])

      Delete exchanges which are exact duplicates. Useful if you accidentally ran your input data notebook twice.

      To determine uniqueness, we look at the exchange input and output nodes, and at the exchanges values for fields ``fields``.


   .. py:method:: backup()

      Save a backup to ``backups`` folder.

      :returns: File path of backup.


   .. py:method:: nodes_to_dataframe(columns: Optional[List[str]] = None, return_sorted: bool = True) -> pandas.DataFrame

      Return a pandas DataFrame with all database nodes. Uses the provided node attributes by default,  such as name, unit, location.

      By default, returns a DataFrame sorted by name, reference product, location, and unit. Set ``return_sorted`` to ``False`` to skip sorting.

      Specify ``columns`` to get custom columns. You will need to write your own function to get more customization, there are endless possibilities here.

      Returns a pandas ``DataFrame``.



   .. py:method:: edges_to_dataframe(categorical: bool = True, formatters: Optional[List[Callable]] = None) -> pandas.DataFrame

      Return a pandas DataFrame with all database exchanges. Standard DataFrame columns are:

          target_id: int,
          target_database: str,
          target_code: str,
          target_name: Optional[str],
          target_reference_product: Optional[str],
          target_location: Optional[str],
          target_unit: Optional[str],
          target_type: Optional[str]
          source_id: int,
          source_database: str,
          source_code: str,
          source_name: Optional[str],
          source_product: Optional[str],  # Note different label
          source_location: Optional[str],
          source_unit: Optional[str],
          source_categories: Optional[str]  # Tuple concatenated with "::" as in `bw2io`
          edge_amount: float,
          edge_type: str,

      Target is the node consuming the edge, source is the node or flow being consumed. The terms target and source were chosen because they also work well for biosphere edges.

      Args:

      ``categorical`` will turn each string column in a `pandas Categorical Series <https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html>`__. This takes 1-2 extra seconds, but saves around 50% of the memory consumption.

      ``formatters`` is a list of callables that modify each row. These functions must take the following keyword arguments, and use the `Wurst internal data format <https://wurst.readthedocs.io/#internal-data-format>`__:

          * ``node``: The target node, as a dict
          * ``edge``: The edge, including attributes of the source node
          * ``row``: The current row dict being modified.

      The functions in ``formatters`` don't need to return anything, they modify ``row`` in place.

      Returns a pandas ``DataFrame``.



   .. py:method:: _iotable_edges_to_dataframe() -> pandas.DataFrame

      Return a pandas DataFrame with all database exchanges. DataFrame columns are:

          target_id: int,
          target_database: str,
          target_code: str,
          target_name: Optional[str],
          target_reference_product: Optional[str],
          target_location: Optional[str],
          target_unit: Optional[str],
          target_type: Optional[str]
          source_id: int,
          source_database: str,
          source_code: str,
          source_name: Optional[str],
          source_product: Optional[str],  # Note different label
          source_location: Optional[str],
          source_unit: Optional[str],
          source_categories: Optional[str]  # Tuple concatenated with "::" as in `bw2io`
          edge_amount: float,
          edge_type: str,

      Target is the node consuming the edge, source is the node or flow being consumed. The terms target and source were chosen because they also work well for biosphere edges.

      As IO Tables are normally quite large, the DataFrame building will operate directly on Numpy arrays, and therefore special formatters are not supported in this function.

      Returns a pandas ``DataFrame``.



   .. py:method:: _sqlite_edges_to_dataframe(categorical: bool = True, formatters: Optional[List[Callable]] = None) -> pandas.DataFrame


   .. py:method:: validate(data)


   .. py:method:: add_geomappings(data)


   .. py:method:: register(write_empty=True, **kwargs)

      Legacy method to register a database with the metadata store.
      Writing data automatically sets the following metadata:
          * *depends*: Names of the databases that this database references, e.g. "biosphere"
          * *number*: Number of processes in this database.


   .. py:method:: deregister()

      Legacy method to remove an object from the metadata store. Does not delete any data.



.. py:function:: get_activity(key=None, **kwargs)

   Support multiple ways to get exactly one activity node.

   ``key`` can be an integer or a key tuple.


.. py:function:: get_node(**kwargs)


.. py:class:: Method(name)

   Bases: :py:obj:`bw2data.ia_data_store.ImpactAssessmentDataStore`

   A manager for an impact assessment method. This class can register or deregister methods, write intermediate data, process data to parameter arrays, validate, and copy methods.

   The Method class never holds intermediate data, but it can load or write intermediate data. The only attribute is *name*, which is the name of the method being managed.

   Instantiation does not load any data. If this method is not yet registered in the metadata store, a warning is written to ``stdout``.

   Methods are hierarchally structured, and this structure is preserved in the method name. It is a tuple of strings, like ``('ecological scarcity 2006', 'total', 'natural resources')``.

   The data schema for IA methods is:

   .. code-block:: python

           Schema([Any(
               [valid_tuple, maybe_uncertainty],         # site-generic
               [valid_tuple, maybe_uncertainty, object]  # regionalized
           )])

   where:
       * *valid_tuple* (tuple): A dataset identifier, like ``("biosphere", "CO2")``.
       * *maybe_uncertainty* (uncertainty dict or number): Either a number or an uncertainty dictionary.
       * *object* (object, optional) is a location identifier, used only for regionalized LCIA.

   :param \* *name*: Name of impact assessment method to manage.
   :type \* *name*: tuple

   .. py:attribute:: _metadata
      

      

   .. py:attribute:: validator
      

      

   .. py:attribute:: matrix
      :annotation: = characterization_matrix

      

   .. py:method:: add_geomappings(data)

      Add objects to ``geomapping``, if necessary.

      :param \* *data*: The data
      :type \* *data*: object


   .. py:method:: process_row(row)

      Given ``(flow, amount, maybe location)``, return a dictionary for array insertion.


   .. py:method:: write(data, process=True)

      Serialize intermediate data to disk.

      Sets the metadata key ``num_cfs`` automatically.


   .. py:method:: process(**extra_metadata)

      Process intermediate data from a Python dictionary to a `stats_arrays <https://pypi.python.org/pypi/stats_arrays/>`_ array, which is a `NumPy <http://numpy.scipy.org/>`_ `Structured <http://docs.scipy.org/doc/numpy/reference/generated/numpy.recarray.html#numpy.recarray>`_ `Array <http://docs.scipy.org/doc/numpy/user/basics.rec.html>`_. A structured array (also called record array) is a heterogeneous array, where each column has a different label and data type.

      Processed arrays are saved in the ``processed`` directory.

      If the uncertainty type is no uncertainty, undefined, or not specified, then the 'amount' value is used for 'loc' as well. This is needed for the random number generator.

      Doesn't return anything, but writes a file to disk.




.. py:class:: Searcher(database)

   .. py:method:: __enter__()


   .. py:method:: __exit__(type, value, traceback)


   .. py:method:: search(string, limit=25, facet=None, proxy=True, boosts=None, filter=None, mask=None, node_class=None)



.. py:class:: IndexManager(database_path, dir_name='whoosh')

   .. py:method:: get()


   .. py:method:: create()


   .. py:method:: _format_dataset(ds)


   .. py:method:: add_dataset(ds)


   .. py:method:: add_datasets(datasets)


   .. py:method:: update_dataset(ds)


   .. py:method:: delete_dataset(ds)


   .. py:method:: delete_database()



.. py:class:: Weighting

   Bases: :py:obj:`bw2data.ia_data_store.ImpactAssessmentDataStore`

   LCIA weighting data - used to combine or compare different impact categories.

   The data schema for weighting is a one-element list:

   .. code-block:: python

           Schema(All(
               [uncertainty_dict],
               Length(min=1, max=1)
           ))


   .. py:attribute:: _metadata
      

      

   .. py:attribute:: validator
      

      

   .. py:attribute:: matrix
      :annotation: = weighting_matrix

      

   .. py:method:: write(data)

      Because of DataStore assumptions, need a one-element list


   .. py:method:: process_row(row)

      Return an empty tuple (as ``dtype_fields`` is empty), and the weighting uncertainty dictionary.



.. py:class:: Normalization

   Bases: :py:obj:`bw2data.ia_data_store.ImpactAssessmentDataStore`

   LCIA normalization data - used to transform meaningful units, like mass or damage, into "person-equivalents" or some such thing.

   The data schema for IA normalization is:

   .. code-block:: python

           Schema([
               [valid_tuple, maybe_uncertainty]
           ])

   where:
       * ``valid_tuple`` is a dataset identifier, like ``("biosphere", "CO2")``
       * ``maybe_uncertainty`` is either a number or an uncertainty dictionary


   .. py:attribute:: _metadata
      

      

   .. py:attribute:: validator
      

      

   .. py:attribute:: matrix
      :annotation: = normalization_matrix

      

   .. py:method:: process_row(row)

      Given ``(flow key, amount)``, return a dictionary for array insertion.



.. py:function:: get_id(key)


.. py:data:: Node
   

   

.. py:data:: Edge
   

   

.. py:function:: prepare_lca_inputs(demand=None, method=None, weighting=None, normalization=None, demands=None, remapping=True, demand_database_last=True)

   Prepare LCA input arguments in Brightway 2.5 style.


.. py:data:: databases
   

   

.. py:function:: extract_brightway_databases(database_names, add_properties=False, add_identifiers=False)

   Extract a Brightway2 SQLiteBackend database to the Wurst internal format.

   ``database_names`` is a list of database names. You should already be in the correct project.

   Returns a list of dataset documents.


.. py:data:: mapping
   

   

.. py:data:: parameters
   

   

