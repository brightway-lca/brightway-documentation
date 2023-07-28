:py:mod:`bw2data.backends.peewee`
=================================

.. py:module:: bw2data.backends.peewee


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   database/index.rst
   proxies/index.rst
   schema/index.rst
   utils/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.backends.peewee.Activity
   bw2data.backends.peewee.ActivityDataset
   bw2data.backends.peewee.Exchange
   bw2data.backends.peewee.ExchangeDataset
   bw2data.backends.peewee.PickleField
   bw2data.backends.peewee.SQLiteBackend
   bw2data.backends.peewee.SubstitutableDatabase




Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2data.backends.peewee.projects
   bw2data.backends.peewee.sqlite3_lci_db


.. py:class:: Activity(document=None, **kwargs)

   Bases: :py:obj:`bw2data.proxies.ActivityProxyBase`

   .. autoapi-inheritance-diagram:: bw2data.backends.peewee.Activity
      :parts: 1
      :private-bases:

   A MutableMapping is a generic container for associating
   key/value pairs.

   This class provides concrete generic implementations of all
   methods except for __getitem__, __setitem__, __delitem__,
   __iter__, and __len__.

   Create an `Activity` proxy object.

   If this is a new activity, can pass `kwargs`.

   If the activity exists in the database, `document` should be an `ActivityDataset`.

   .. py:property:: key


   .. py:method:: _change_code(new_code)


   .. py:method:: _change_database(new_database)


   .. py:method:: biosphere()


   .. py:method:: copy(code=None, **kwargs)

      Copy the activity. Returns a new `Activity`.

      `code` is the new activity code; if not given, a UUID is used.

      `kwargs` are additional new fields and field values, e.g. name='foo'



   .. py:method:: delete()


   .. py:method:: exchanges()


   .. py:method:: new_exchange(**kwargs)

      Create a new exchange linked to this activity


   .. py:method:: production()


   .. py:method:: rp_exchange()

      Return an ``Exchange`` object corresponding to the reference production. Uses the following in order:

      * The ``production`` exchange, if only one is present
      * The ``production`` exchange with the same name as the activity ``reference product``.

      Raises ``ValueError`` if no suitable exchange is found.


   .. py:method:: save()


   .. py:method:: substitution()


   .. py:method:: technosphere(include_substitution=True)


   .. py:method:: upstream(kinds=('technosphere', ))



.. py:class:: ActivityDataset

   Bases: :py:obj:`peewee.Model`

   .. autoapi-inheritance-diagram:: bw2data.backends.peewee.ActivityDataset
      :parts: 1
      :private-bases:

   .. py:attribute:: code

      

   .. py:attribute:: data

      

   .. py:attribute:: database

      

   .. py:attribute:: location

      

   .. py:attribute:: name

      

   .. py:attribute:: product

      

   .. py:attribute:: type

      


.. py:class:: Exchange(document=None, **kwargs)

   Bases: :py:obj:`bw2data.proxies.ExchangeProxyBase`

   .. autoapi-inheritance-diagram:: bw2data.backends.peewee.Exchange
      :parts: 1
      :private-bases:

   A MutableMapping is a generic container for associating
   key/value pairs.

   This class provides concrete generic implementations of all
   methods except for __getitem__, __setitem__, __delitem__,
   __iter__, and __len__.

   Create an `Exchange` proxy object.

   If this is a new exchange, can pass `kwargs`.

   If the exchange exists in the database, `document` should be an `ExchangeDataset`.

   .. py:method:: delete()


   .. py:method:: save()



.. py:class:: ExchangeDataset

   Bases: :py:obj:`peewee.Model`

   .. autoapi-inheritance-diagram:: bw2data.backends.peewee.ExchangeDataset
      :parts: 1
      :private-bases:

   .. py:attribute:: data

      

   .. py:attribute:: input_code

      

   .. py:attribute:: input_database

      

   .. py:attribute:: output_code

      

   .. py:attribute:: output_database

      

   .. py:attribute:: type

      


.. py:class:: PickleField

   Bases: :py:obj:`peewee.BlobField`

   .. autoapi-inheritance-diagram:: bw2data.backends.peewee.PickleField
      :parts: 1
      :private-bases:

   .. py:method:: db_value(value)


   .. py:method:: python_value(value)



.. py:class:: SQLiteBackend(*args, **kwargs)

   Bases: :py:obj:`bw2data.backends.base.LCIBackend`

   .. autoapi-inheritance-diagram:: bw2data.backends.peewee.SQLiteBackend
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



.. py:class:: SubstitutableDatabase(filepath, tables)

   Bases: :py:obj:`object`

   .. py:property:: db


   .. py:method:: _create_database()


   .. py:method:: atomic()


   .. py:method:: change_path(filepath)


   .. py:method:: execute_sql(*args, **kwargs)


   .. py:method:: transaction()


   .. py:method:: vacuum()



.. py:data:: projects

   

.. py:data:: sqlite3_lci_db

   

