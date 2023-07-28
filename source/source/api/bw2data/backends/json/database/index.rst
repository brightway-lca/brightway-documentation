:py:mod:`bw2data.backends.json.database`
========================================

.. py:module:: bw2data.backends.json.database


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.backends.json.database.JSONDatabase




.. py:class:: JSONDatabase(name)

   Bases: :py:obj:`bw2data.backends.base.LCIBackend`

   .. autoapi-inheritance-diagram:: bw2data.backends.json.database.JSONDatabase
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



