:py:mod:`bw2data.backends.json`
===============================

.. py:module:: bw2data.backends.json


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   database/index.rst
   mapping/index.rst
   proxies/index.rst
   sync_json_dict/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.backends.json.Activity
   bw2data.backends.json.Exchange
   bw2data.backends.json.JSONDatabase




.. py:class:: Activity(key, data={})

   Bases: :py:obj:`bw2data.proxies.ActivityProxyBase`

   .. autoapi-inheritance-diagram:: bw2data.backends.json.Activity
      :parts: 1
      :private-bases:

   A MutableMapping is a generic container for associating
   key/value pairs.

   This class provides concrete generic implementations of all
   methods except for __getitem__, __setitem__, __delitem__,
   __iter__, and __len__.

   .. py:method:: biosphere(raw=False)


   .. py:method:: exchanges(raw=False)


   .. py:method:: save()


   .. py:method:: technosphere(raw=False)


   .. py:method:: upstream(*args, **kwargs)



.. py:class:: Exchange(data, *args, **kwargs)

   Bases: :py:obj:`bw2data.proxies.ExchangeProxyBase`

   .. autoapi-inheritance-diagram:: bw2data.backends.json.Exchange
      :parts: 1
      :private-bases:

   Simple proxy for an exchange between activity datasets. Makes manipulation and use in command line more convenient.

   .. warning:: This proxy is read only! To save changes to a dataset, you will need to work with the raw database data.

   Usually these proxies are created by the :ref:`activity`, but you can instantiate one with the dictionary of exchange data and an Activity proxy of the consuming activity:

   .. code-block:: python

       exchange = Exchange({"my exchange data": "goes here"})

   Properties:

   * ``input``: Returns :ref:`activity`
   * ``output``: Returns :ref:`activity`
   * ``amount``
   * ``uncertainty``: Returns dictionary of uncertainty data
   * ``uncertainty_type``: Returns ``stats_arrays`` uncertainty type
   * ``unit``



   .. py:method:: save()



.. py:class:: JSONDatabase(name)

   Bases: :py:obj:`bw2data.backends.base.LCIBackend`

   .. autoapi-inheritance-diagram:: bw2data.backends.json.JSONDatabase
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



