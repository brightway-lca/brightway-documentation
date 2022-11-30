:py:mod:`bw2io.unlinked_data`
=============================

.. py:module:: bw2io.unlinked_data


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.unlinked_data._UnlinkedData
   bw2io.unlinked_data.UnlinkedData




Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.unlinked_data.unlinked_data


.. py:class:: _UnlinkedData(dirpath=None)

   Bases: :py:obj:`bw2data.serialization.SerializedDict`

   Base class for dictionary that can be `serialized <http://en.wikipedia.org/wiki/Serialization>`_ to or unserialized from disk. Uses JSON as its storage format. Has most of the methods of a dictionary.

   Upon instantiation, the serialized dictionary is read from disk.

   .. py:attribute:: filename
      :annotation: = unlinked_data.json

      


.. py:data:: unlinked_data
   

   

.. py:class:: UnlinkedData(name)

   Bases: :py:obj:`bw2data.data_store.DataStore`

   Base class for all Brightway2 data stores. Subclasses should define:

       * **metadata**: A :ref:`serialized-dict` instance, e.g. ``databases`` or ``methods``. The custom is that each type of data store has a new metadata store, so the data store ``Foo`` would have a metadata store ``foos``.
       * **validator**: A data validator. Optional. See bw2data.validate.


   .. py:attribute:: _metadata
      

      

   .. py:attribute:: _intermediate_dir
      :annotation: = unlinked

      

   .. py:method:: validate(*args, **kwargs)

      Validate data. Must be called manually.



