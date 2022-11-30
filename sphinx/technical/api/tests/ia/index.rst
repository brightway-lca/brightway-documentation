:py:mod:`tests.ia`
==================

.. py:module:: tests.ia


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   tests.ia.Metadata
   tests.ia.MockIADS



Functions
~~~~~~~~~

.. autoapisummary::

   tests.ia.reset
   tests.ia.test_unicode
   tests.ia.test_abbreviate
   tests.ia.test_copy_no_name
   tests.ia.test_copy_with_name
   tests.ia.test_register_adds_abbreviation
   tests.ia.test_method_write_adds_num_cfs_to_metadata
   tests.ia.test_method_processed_array
   tests.ia.test_method_missing_reference
   tests.ia.test_method_missing_location
   tests.ia.test_method_missing_global_location
   tests.ia.test_method_base_class
   tests.ia.test_method_validator
   tests.ia.test_weighting_write_good_data
   tests.ia.test_weighting_write_invalid_data
   tests.ia.test_weighting_process
   tests.ia.test_weighting_base_class
   tests.ia.test_weighting_validator
   tests.ia.test_base_normalization_class
   tests.ia.test_normalization_process_row
   tests.ia.test_method_geocollection
   tests.ia.test_method_geocollection_missing_ok
   tests.ia.test_method_geocollection_warning



Attributes
~~~~~~~~~~

.. autoapisummary::

   tests.ia.metadata


.. py:class:: Metadata

   Bases: :py:obj:`bw2data.serialization.CompoundJSONDict`

   .. py:attribute:: filename
      :annotation: = mock-meta.json

      


.. py:data:: metadata
   

   

.. py:class:: MockIADS

   Bases: :py:obj:`bw2data.ia_data_store.ImpactAssessmentDataStore`

   Mock IADS for testing

   .. py:attribute:: _metadata
      

      

   .. py:attribute:: validator
      

      

   .. py:method:: process_row(row)



.. py:function:: reset()


.. py:function:: test_unicode(reset)


.. py:function:: test_abbreviate(reset)


.. py:function:: test_copy_no_name(reset)


.. py:function:: test_copy_with_name(reset)


.. py:function:: test_register_adds_abbreviation(reset)


.. py:function:: test_method_write_adds_num_cfs_to_metadata(reset)


.. py:function:: test_method_processed_array(reset)


.. py:function:: test_method_missing_reference()


.. py:function:: test_method_missing_location()


.. py:function:: test_method_missing_global_location()


.. py:function:: test_method_base_class(reset)


.. py:function:: test_method_validator(reset)


.. py:function:: test_weighting_write_good_data(reset)


.. py:function:: test_weighting_write_invalid_data(reset)


.. py:function:: test_weighting_process(reset)


.. py:function:: test_weighting_base_class(reset)


.. py:function:: test_weighting_validator(reset)


.. py:function:: test_base_normalization_class(reset)


.. py:function:: test_normalization_process_row(reset)


.. py:function:: test_method_geocollection()


.. py:function:: test_method_geocollection_missing_ok()


.. py:function:: test_method_geocollection_warning()


