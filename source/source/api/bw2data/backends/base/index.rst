:py:mod:`bw2data.backends.base`
===============================

.. py:module:: bw2data.backends.base


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.backends.base.LCIBackend




.. py:class:: LCIBackend(name)

   Bases: :py:obj:`bw2data.data_store.ProcessedDataStore`

   .. autoapi-inheritance-diagram:: bw2data.backends.base.LCIBackend
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




