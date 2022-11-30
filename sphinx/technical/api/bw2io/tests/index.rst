:py:mod:`bw2io.tests`
=====================

.. py:module:: bw2io.tests


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.tests.MockMetadata
   bw2io.tests.MockDS




Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.tests.mocks


.. py:class:: MockMetadata(dirpath=None)

   Bases: :py:obj:`bw2data.serialization.SerializedDict`

   Base class for dictionary that can be `serialized <http://en.wikipedia.org/wiki/Serialization>`_ to or unserialized from disk. Uses JSON as its storage format. Has most of the methods of a dictionary.

   Upon instantiation, the serialized dictionary is read from disk.

   .. py:attribute:: filename
      :annotation: = mock-meta.json

      


.. py:data:: mocks
   

   

.. py:class:: MockDS(name)

   Bases: :py:obj:`bw2data.data_store.DataStore`

   Mock DataStore for testing

   .. py:attribute:: _metadata
      

      

   .. py:attribute:: validator
      

      

   .. py:attribute:: dtype_fields
      :annotation: = []

      

   .. py:method:: process_data(row)



