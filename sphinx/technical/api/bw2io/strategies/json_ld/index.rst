:py:mod:`bw2io.strategies.json_ld`
==================================

.. py:module:: bw2io.strategies.json_ld


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.json_ld.json_ld_get_normalized_exchange_locations
   bw2io.strategies.json_ld.json_ld_add_products_as_activities
   bw2io.strategies.json_ld.json_ld_convert_unit_to_reference_unit
   bw2io.strategies.json_ld.json_ld_get_normalized_exchange_units
   bw2io.strategies.json_ld.json_ld_add_activity_unit
   bw2io.strategies.json_ld.json_ld_get_activities_list_from_rawdata
   bw2io.strategies.json_ld.json_ld_rename_metadata_fields
   bw2io.strategies.json_ld.json_ld_remove_fields
   bw2io.strategies.json_ld.json_ld_location_name
   bw2io.strategies.json_ld.json_ld_fix_process_type
   bw2io.strategies.json_ld.json_ld_prepare_exchange_fields_for_linking
   bw2io.strategies.json_ld.json_ld_label_exchange_type



.. py:function:: json_ld_get_normalized_exchange_locations(data)

   The exchanges location strings are not necessarily the same as those given in the process or the master metadata. Fix this inconsistency.

   This has to happen before we transform the input data from a dictionary to a list of activities, as it uses the ``locations`` data.


.. py:function:: json_ld_add_products_as_activities(db, products)


.. py:function:: json_ld_convert_unit_to_reference_unit(db)

   Convert the units to their reference unit. Also changes the format to eliminate unnecessary complexity.

   Changes:

       {
           'flow': {'refUnit': 'MJ', ...},
           'unit': {
               '@type': 'Unit',
               '@id': '86ad2244-1f0e-4912-af53-7865283103e4',
               'name': 'kWh'
       }

   To:

       {
           'flow': {...},
           'unit': 'MJ'
       }




.. py:function:: json_ld_get_normalized_exchange_units(data)

   The exchanges unit strings are not necessarily the same as BW units. Fix this inconsistency.


.. py:function:: json_ld_add_activity_unit(db)

   Add units to activities from their reference products.


.. py:function:: json_ld_get_activities_list_from_rawdata(data)

   Return list of processes from raw data.


.. py:function:: json_ld_rename_metadata_fields(db)

   Change metadata field names from the JSON-LD `processes` to BW schema.

   BW schema: https://wurst.readthedocs.io/#internal-data-format



.. py:function:: json_ld_remove_fields(db)


.. py:function:: json_ld_location_name(db)


.. py:function:: json_ld_fix_process_type(db)


.. py:function:: json_ld_prepare_exchange_fields_for_linking(db)


.. py:function:: json_ld_label_exchange_type(db)


