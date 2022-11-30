:py:mod:`tests.data_store`
==========================

.. py:module:: tests.data_store


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   tests.data_store.Metadata
   tests.data_store.MockDS
   tests.data_store.MockPDS



Functions
~~~~~~~~~

.. autoapisummary::

   tests.data_store.reset
   tests.data_store.test_data_store_repr
   tests.data_store.test_data_store_unicode
   tests.data_store.test_data_store_deregister
   tests.data_store.test_data_store_metadata_keyerror
   tests.data_store.test_data_store_metadata_readable_writable
   tests.data_store.test_data_store_write_load
   tests.data_store.test_data_store_copy
   tests.data_store.test_data_store_validation



Attributes
~~~~~~~~~~

.. autoapisummary::

   tests.data_store.metadata


.. py:class:: Metadata

   Bases: :py:obj:`bw2data.serialization.SerializedDict`

   .. py:attribute:: filename
      :annotation: = mock-meta.json

      


.. py:data:: metadata
   

   

.. py:class:: MockDS

   Bases: :py:obj:`bw2data.data_store.DataStore`

   Mock DataStore for testing

   .. py:attribute:: _metadata
      

      

   .. py:attribute:: validator
      

      


.. py:class:: MockPDS

   Bases: :py:obj:`bw2data.data_store.ProcessedDataStore`

   Mock DataStore for testing

   .. py:attribute:: _metadata
      

      

   .. py:attribute:: validator
      

      

   .. py:method:: process_row(row)



.. py:function:: reset()


.. py:function:: test_data_store_repr(reset)


.. py:function:: test_data_store_unicode(reset)


.. py:function:: test_data_store_deregister(reset)


.. py:function:: test_data_store_metadata_keyerror(reset)


.. py:function:: test_data_store_metadata_readable_writable(reset)


.. py:function:: test_data_store_write_load(reset)


.. py:function:: test_data_store_copy(reset)


.. py:function:: test_data_store_validation(reset)


