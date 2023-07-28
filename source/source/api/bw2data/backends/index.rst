:py:mod:`bw2data.backends`
==========================

.. py:module:: bw2data.backends


Subpackages
-----------
.. toctree::
   :titlesonly:
   :maxdepth: 3

   iotable/index.rst
   json/index.rst
   peewee/index.rst
   single_file/index.rst


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   base/index.rst
   utils/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.backends.JSONDatabase
   bw2data.backends.LCIBackend
   bw2data.backends.SQLiteBackend
   bw2data.backends.SingleFileDatabase



Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.backends.convert_backend



.. py:class:: JSONDatabase(name)

   Bases: :py:obj:`bw2data.backends.base.LCIBackend`

   .. autoapi-inheritance-diagram:: bw2data.backends.JSONDatabase
      :parts: 1
      :private-bases:

   A data store for LCI databases. Stores each dataset in a separate file, serialized to JSON.

   Instead of loading all the data at once, ``.load()`` creates a :class:`.SynchronousJSONDict`, which loads values on demand.

   Use this backend by setting ``"backend":"json"`` in the database metadata. This is done automatically if you call ``.register()`` from this class.

   .. py:attribute:: backend
      :value: 'json'

      

   .. py:method:: filepath_intermediate()


   .. py:method:: get(code)

      Get Activity proxy for this dataset


   .. py:method:: load(as_dict=False, *args, **kwargs)

      Instantiate :class:`.SynchronousJSONDict` for this database.


   .. py:method:: register(**kwargs)

      Register a database with the metadata store, using the correct value for ``backend``, and creates database directory.


   .. py:method:: write(data, process=True)

      Serialize data to disk. Most of the time, this data has already been saved to disk, so this is a no-op. The only exception is if ``data`` is a new database dictionary.

      Normalizes units when found.

      :param \* *data*: Inventory data
      :type \* *data*: dict



.. py:class:: LCIBackend(name)

   Bases: :py:obj:`bw2data.data_store.ProcessedDataStore`

   .. autoapi-inheritance-diagram:: bw2data.backends.LCIBackend
      :parts: 1
      :private-bases:

   A base class for LCI backends.

   Subclasses must support at least the following calls:

   * ``load()``
   * ``write(data)``

   In addition, they should specify their backend with the ``backend`` attribute (a unicode string).

   ``LCIBackend`` provides the following, which should not need to be modified:

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

   .. py:property:: filename

      Remove filesystem-unsafe characters and perform unicode normalization on ``self.name`` using :func:`.utils.safe_filename`.

   .. py:attribute:: _metadata

      

   .. py:attribute:: dtype_fields
      :value: [(), (), (), (), ()]

      

   .. py:attribute:: dtype_fields_geomapping
      :value: [(), (), (), ()]

      

   .. py:attribute:: validator

      

   .. py:method:: copy(name)

      Make a copy of the database.

      Internal links within the database will be updated to match the new database name, i.e. ``("old name", "some id")`` will be converted to ``("new name", "some id")`` for all exchanges.

      :param \* *name*: Name of the new database. Must not already exist.
      :type \* *name*: str


   .. py:method:: delete(**kwargs)

      Delete data from this instance. For the base class, only clears cached data.


   .. py:method:: filepath_geomapping()


   .. py:method:: filepath_intermediate()
      :abstractmethod:


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


   .. py:method:: load(*args, **kwargs)
      :abstractmethod:

      Load the intermediate data for this database.

      If ``load()`` does not return a dictionary, then the returned object must have at least the following dictionary-like methods:

      * ``__iter__``
      * ``__contains__``
      * ``__getitem__``
      * ``__setitem__``
      * ``__delitem__``
      * ``__len__``
      * ``keys()``
      * ``values()``
      * ``items()``
      * ``items()``

      However, this method **must** support the keyword argument ``as_dict``, and ``.load(as_dict=True)`` must return a normal dictionary with all Database data. This is necessary for JSON serialization.

      It is recommended to subclass ``collections.{abc.}MutableMapping`` (see ``SynchronousJSONDict`` for an example of data loaded on demand).



   .. py:method:: process(*args, **kwargs)

      Process inventory documents.

      Creates both a parameter array for exchanges, and a geomapping parameter array linking inventory activities to locations.

      If the uncertainty type is no uncertainty, undefined, or not specified, then the 'amount' value is used for 'loc' as well. This is needed for the random number generator.

      :param \* *version*: The version of the database to process
      :type \* *version*: int, optional

      Doesn't return anything, but writes two files to disk.




   .. py:method:: query(*queries)

      Search through the database.


   .. py:method:: random()

      Return a random activity key.

      Returns a random activity key, or ``None`` (and issues a warning) if the current database is empty.


   .. py:method:: register(**kwargs)

      Register a database with the metadata store.

      Databases must be registered before data can be written.

      Writing data automatically sets the following metadata:
          * *depends*: Names of the databases that this database references, e.g. "biosphere"
          * *number*: Number of processes in this database.

      :param \* *format*: Format that the database was converted from, e.g. "Ecospold"
      :type \* *format*: str, optional


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

      Rename a database. Modifies exchanges to link to new name. Deregisters old database.

      :param \* *name*: New name.
      :type \* *name*: str

      :returns: New ``Database`` object.


   .. py:method:: write(data)
      :abstractmethod:

      Serialize data to disk.

      ``data`` must be a dictionary of the form::

          {
              ('database name', 'dataset code'): {dataset}
          }




.. py:class:: SQLiteBackend(*args, **kwargs)

   Bases: :py:obj:`bw2data.backends.base.LCIBackend`

   .. autoapi-inheritance-diagram:: bw2data.backends.SQLiteBackend
      :parts: 1
      :private-bases:

   A base class for LCI backends.

   Subclasses must support at least the following calls:

   * ``load()``
   * ``write(data)``

   In addition, they should specify their backend with the ``backend`` attribute (a unicode string).

   ``LCIBackend`` provides the following, which should not need to be modified:

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

   .. py:property:: _searchable


   .. py:attribute:: backend
      :value: 'sqlite'

      

   .. py:attribute:: filters

      

   .. py:attribute:: order_by

      

   .. py:method:: _add_indices()


   .. py:method:: _drop_indices()


   .. py:method:: _efficient_write_dataset(index, key, ds, exchanges, activities)


   .. py:method:: _efficient_write_many_data(data, indices=True)


   .. py:method:: _get_filters()


   .. py:method:: _get_order_by()


   .. py:method:: _get_queryset(random=False, filters=True)


   .. py:method:: _set_filters(filters)


   .. py:method:: _set_order_by(field)


   .. py:method:: delete(keep_params=False, warn=True)

      Delete all data from SQLite database and Whoosh index


   .. py:method:: get(code)


   .. py:method:: graph_technosphere(filename=None, **kwargs)


   .. py:method:: load(*args, **kwargs)

      Load the intermediate data for this database.

      If ``load()`` does not return a dictionary, then the returned object must have at least the following dictionary-like methods:

      * ``__iter__``
      * ``__contains__``
      * ``__getitem__``
      * ``__setitem__``
      * ``__delitem__``
      * ``__len__``
      * ``keys()``
      * ``values()``
      * ``items()``
      * ``items()``

      However, this method **must** support the keyword argument ``as_dict``, and ``.load(as_dict=True)`` must return a normal dictionary with all Database data. This is necessary for JSON serialization.

      It is recommended to subclass ``collections.{abc.}MutableMapping`` (see ``SynchronousJSONDict`` for an example of data loaded on demand).



   .. py:method:: make_searchable(reset=False)


   .. py:method:: make_unsearchable()


   .. py:method:: new_activity(code, **kwargs)


   .. py:method:: process()

      Process inventory documents to NumPy structured arrays.

      Use a raw SQLite3 cursor instead of Peewee for a ~2 times speed advantage.




   .. py:method:: random(filters=True, true_random=False)

      True random requires loading and sorting data in SQLite, and can be resource-intensive.


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


   .. py:method:: write(data, process=True)

      Write ``data`` to database.

      ``data`` must be a dictionary of the form::

          {
              ('database name', 'dataset code'): {dataset}
          }

      Writing a database will first deletes all existing data.



.. py:class:: SingleFileDatabase(name)

   Bases: :py:obj:`bw2data.backends.base.LCIBackend`

   .. autoapi-inheritance-diagram:: bw2data.backends.SingleFileDatabase
      :parts: 1
      :private-bases:

   A data store for LCI databases where each database is stored as a ``pickle`` file.

   Databases are automatically versioned. See below for reversion, etc. methods

   :param \*name*: Name of the database to manage.
   :type \*name*: str

   .. py:property:: filename

      Remove filesystem-unsafe characters and perform unicode normalization on ``self.name`` using :func:`.utils.safe_filename`.

   .. py:property:: version

      The current version number (integer) of this database.

      :returns: Version number

   .. py:attribute:: backend
      :value: 'singlefile'

      

   .. py:attribute:: validator

      

   .. py:method:: filename_for_version(version=None)

      Filename for given version; Default is current version.

      :returns: Filename (not path)


   .. py:method:: filepath_intermediate(version=None)


   .. py:method:: get(code)

      Get Activity proxy for this dataset


   .. py:method:: load(version=None, **kwargs)

      Load the intermediate data for this database.

      Can also load previous versions of this database's intermediate data.

      :param \* *version*: Version of the database to load. Default ``version`` is the latest version.
      :type \* *version*: int

      :returns: The intermediate data, a dictionary.


   .. py:method:: make_latest_version()

      Make the current version the latest version.

      Requires loading data because a new intermediate data file is created.


   .. py:method:: register(**kwargs)

      Register a database with the metadata store.

      Databases must be registered before data can be written.



   .. py:method:: revert(version)

      Return data to a previous state.

      .. warning:: Reverting can lead to data loss, e.g. if you revert from version 3 to version 1, and then save your database, you will overwrite version 2. Use :meth:`.make_latest_version` before saving, which will set the current version to 4.

      :param \* *version*: Number of the version to revert to.
      :type \* *version*: int


   .. py:method:: versions()

      Get a list of available versions of this database.

      :returns: List of (version, datetime created) tuples.


   .. py:method:: write(data, process=True)

      Serialize data to disk.

      :param \* *data*: Inventory data
      :type \* *data*: dict



.. py:function:: convert_backend(database_name, backend)

   Convert a Database to another backend.

   bw2data currently supports the `default` and `json` backends.

   :param \* `database_name`: Name of database.
   :type \* `database_name`: unicode
   :param \* `backend`: Type of database. `backend` should be recoginized by `DatabaseChooser`.
   :type \* `backend`: unicode

   Returns `False` if the old and new backend are the same. Otherwise returns an instance of the new Database object.


