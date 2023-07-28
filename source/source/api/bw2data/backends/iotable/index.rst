:py:mod:`bw2data.backends.iotable`
==================================

.. py:module:: bw2data.backends.iotable


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.backends.iotable.ActivityDataset
   bw2data.backends.iotable.ExchangeDataset
   bw2data.backends.iotable.IOTableBackend
   bw2data.backends.iotable.SQLiteBackend



Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.backends.iotable.dict_as_activitydataset



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2data.backends.iotable.MAX_INT_32
   bw2data.backends.iotable.TYPE_DICTIONARY


.. py:exception:: UnknownObject

   Bases: :py:obj:`BW2Exception`

   .. autoapi-inheritance-diagram:: bw2data.backends.iotable.UnknownObject
      :parts: 1
      :private-bases:

   Base class for exceptions in Brightway2

   Initialize self.  See help(type(self)) for accurate signature.


.. py:class:: ActivityDataset

   Bases: :py:obj:`peewee.Model`

   .. autoapi-inheritance-diagram:: bw2data.backends.iotable.ActivityDataset
      :parts: 1
      :private-bases:

   .. py:attribute:: code

      

   .. py:attribute:: data

      

   .. py:attribute:: database

      

   .. py:attribute:: location

      

   .. py:attribute:: name

      

   .. py:attribute:: product

      

   .. py:attribute:: type

      


.. py:class:: ExchangeDataset

   Bases: :py:obj:`peewee.Model`

   .. autoapi-inheritance-diagram:: bw2data.backends.iotable.ExchangeDataset
      :parts: 1
      :private-bases:

   .. py:attribute:: data

      

   .. py:attribute:: input_code

      

   .. py:attribute:: input_database

      

   .. py:attribute:: output_code

      

   .. py:attribute:: output_database

      

   .. py:attribute:: type

      


.. py:class:: IOTableBackend(*args, **kwargs)

   Bases: :py:obj:`bw2data.backends.peewee.SQLiteBackend`

   .. autoapi-inheritance-diagram:: bw2data.backends.iotable.IOTableBackend
      :parts: 1
      :private-bases:

   IO tables have too much data to store each value in a database; instead, we only store the processed data in NumPy arrays.

   Activities will not seem to have any activities.

   .. py:attribute:: backend
      :value: 'iotable'

      

   .. py:method:: process()

      No-op; no intermediate data to process


   .. py:method:: write(products, exchanges, includes_production=False, **kwargs)

      Write IO data to disk in two different formats.

      Product data is stored in SQLite as normal activities.
      Exchange data is written directly to NumPy structured arrays.

      ``products`` is a dictionary of product datasets in the normal format.

      ``exchanges`` is a list of exchanges with the format ``(input code, output code, type, value)``.




.. py:class:: SQLiteBackend(*args, **kwargs)

   Bases: :py:obj:`bw2data.backends.base.LCIBackend`

   .. autoapi-inheritance-diagram:: bw2data.backends.iotable.SQLiteBackend
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



.. py:function:: dict_as_activitydataset(ds)


.. py:data:: MAX_INT_32
   :value: 4294967295

   

.. py:data:: TYPE_DICTIONARY

   

