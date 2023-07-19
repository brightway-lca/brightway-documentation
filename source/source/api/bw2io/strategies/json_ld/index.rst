:py:mod:`bw2io.strategies.json_ld`
==================================

.. py:module:: bw2io.strategies.json_ld


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.json_ld.json_ld_add_activity_unit
   bw2io.strategies.json_ld.json_ld_add_products_as_activities
   bw2io.strategies.json_ld.json_ld_convert_unit_to_reference_unit
   bw2io.strategies.json_ld.json_ld_fix_process_type
   bw2io.strategies.json_ld.json_ld_get_activities_list_from_rawdata
   bw2io.strategies.json_ld.json_ld_get_normalized_exchange_locations
   bw2io.strategies.json_ld.json_ld_get_normalized_exchange_units
   bw2io.strategies.json_ld.json_ld_label_exchange_type
   bw2io.strategies.json_ld.json_ld_location_name
   bw2io.strategies.json_ld.json_ld_prepare_exchange_fields_for_linking
   bw2io.strategies.json_ld.json_ld_remove_fields
   bw2io.strategies.json_ld.json_ld_rename_metadata_fields



.. py:function:: json_ld_add_activity_unit(db)

   Add units to activities in the given database from their reference products.

   Takes a database represented as a list of dictionaries and adds units to activities in the database based
   on their reference products. This is done by looking at the production exchanges of each activity and taking the unit of
   the reference product as the unit of the activity.

   :param db: A list of dictionaries representing a database containing information about processes and exchanges.
   :type db: list

   :returns: A list of dictionaries representing the updated database with units added to activities.
   :rtype: list

   :raises AssertionError: If there is more than one production exchange for an activity.

   .. rubric:: Examples

   >>> db = [
               {"name": "Activity 1", "exchanges": [{"flow": {"name": "Flow 1"}, "unit": "kg"}]},
               {"name": "Activity 2", "exchanges": [{"flow": {"name": "Flow 2"}, "unit": "tonnes"}]}
           ]
   >>> json_ld_add_activity_unit(db)
   [{'name': 'Activity 1', 'exchanges': [{'flow': {'name': 'Flow 1'}, 'unit': 'kg'}, {'flowType': 'PRODUCT_FLOW',
       'input': False, 'unit': 'kg'}], 'unit': 'kg'},
    {'name': 'Activity 2', 'exchanges': [{'flow': {'name': 'Flow 2'}, 'unit': 'tonnes'}, {'flowType': 'PRODUCT_FLOW',
       'input': False, 'unit': 'ton'}}]


.. py:function:: json_ld_add_products_as_activities(db, products)

   "
   Add products as activities to the given database.
   Takes a database and a list of products, and adds the products to the database as activities.
   The products are added to the end of the database, after the existing activities.

   :param db: A list of activities representing a database.
   :type db: list
   :param products: A list of products to be added to the database as activities.
   :type products: list

   :returns: A list of activities representing the updated database.
   :rtype: list

   .. rubric:: Examples

   >>> db = [{'name': 'Activity 1'}, {'name': 'Activity 2'}]
   >>> products = [{'name': 'Product 1'}, {'name': 'Product 2'}]
   >>> json_ld_add_products_as_activities(db, products)
   [{'name': 'Activity 1'}, {'name': 'Activity 2'}, {'name': 'Product 1'}, {'name': 'Product 2'}]


.. py:function:: json_ld_convert_unit_to_reference_unit(db)

   Convert the units in the given database to their reference units and simplify the format.

   Takes a database represented as a dictionary and converts the units in the exchanges to their reference
   units. It also simplifies the format of the exchanges to eliminate unnecessary complexity.

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

   :param db: A dictionary representing a database containing information about processes and exchanges.
   :type db: dict

   :returns: A dictionary representing the updated database with units converted to reference units and exchanges simplified.
   :rtype: dict

   .. rubric:: Examples

   >>> db = {
               "unit_groups": {
                   "group1": {
                       "id": "group1",
                       "name": "Group 1",
                       "units": [
                           {
                               "@type": "Unit",
                               "@id": "unit1",
                               "name": "kWh",
                               "conversionFactor": 3.6
                           }
                       ]
                   }
               },
               "processes": {
                   "P1": {
                       "exchanges": [
                           {
                               "flow": {"refUnit": "MJ"},
                               "amount": 10.0,
                               "unit": {"@type": "Unit", "@id": "unit1", "name": "kWh"}
                           }
                       ]
                   }
               }
           }
   >>> json_ld_convert_unit_to_reference_unit(db)
   {'unit_groups': {'group1': {'id': 'group1', 'name': 'Group 1', 'units': [{'@type': 'Unit', '@id': 'unit1',
       'name': 'kWh', 'conversionFactor': 3.6}]}}, 'processes': {'P1': {'exchanges': [{'flow': {'refUnit': 'MJ'},
       'amount': 36.0, 'unit': 'MJ'}]}}}


.. py:function:: json_ld_fix_process_type(db)

   Fix process type information in the given database.

   Takes a database represented as a list of dictionaries and updates the process type information in the
   'processes' to match the format of the Brightway schema. This is done by changing the value of the 'type' key from
   'Process' to 'process'.

   :param db: A list of dictionaries representing a database containing information about processes and exchanges.
   :type db: list

   :returns: A list of dictionaries representing the updated database with process type information in the Brightway schema
             format.
   :rtype: list

   .. rubric:: Examples

   >>> db = [
               {"name": "Activity 1", "type": "Process"},
               {"name": "Activity 2", "type": "Product"}
           ]
   >>> json_ld_fix_process_type(db)
   [{'name': 'Activity 1', 'type': 'process'}, {'name': 'Activity 2', 'type': 'Product'}]


.. py:function:: json_ld_get_activities_list_from_rawdata(data)

   Return a list of processes from raw data.

   Takes raw data in the form of a dictionary and returns a list of processes from the 'processes' key of the
   dictionary.

   :param data: A dictionary containing raw data.
   :type data: dict

   :returns: A list of dictionaries representing the processes.
   :rtype: list

   .. rubric:: Examples

   >>> data = {"processes": {"P1": {"name": "Process 1"}, "P2": {"name": "Process 2"}}}
   >>> json_ld_get_activities_list_from_rawdata(data)
   [{'name': 'Process 1'}, {'name': 'Process 2'}]


.. py:function:: json_ld_get_normalized_exchange_locations(data)

   Normalize exchange location strings to match those given in the process or the master metadata.
   The function takes a dictionary ``data`` as input and replaces exchange location strings with their corresponding names
   if they do not match the names given in the process or the master metadata. Uses the 'locations' data
   to create a mapping between location codes and location names.

   :param data: A dictionary containing information about processes, exchanges, and locations.
   :type data: dict

   :returns: A dictionary containing normalized location strings in the exchanges.
   :rtype: dict

   .. rubric:: Examples

   >>> data = {"locations": {"L1": {"code": "L1", "name": "Location 1"}},
               "processes": {"P1": {"exchanges": [{"flow": {"location": "L1"}}]}}}
   >>> json_ld_get_normalized_exchange_locations(data)
   {'locations': {'L1': {'code': 'L1', 'name': 'Location 1'}},
   'processes': {'P1': {'exchanges': [{'flow': {'location': 'Location 1'}}]}}}


.. py:function:: json_ld_get_normalized_exchange_units(data)

   Normalize the unit strings in the exchanges to match the Brightway units.

   Takes a list of activities represented as a dictionary and normalizes the unit strings in the exchanges
   to match the Brightway units. Uses a normalization function 'normalize_units_function' to convert
   non-Brightway units to their corresponding Brightway units.

   :param data: A list of activities represented as dictionaries containing information about processes and exchanges.
   :type data: list

   :returns: A list of activities represented as dictionaries containing normalized unit strings in the exchanges.
   :rtype: list

   .. seealso::

      :obj:`normalize_units_function`
          A function used to convert non-Brightway units to their corresponding Brightway units.

   .. rubric:: Examples

   >>> data = [
               {"name": "Activity 1", "exchanges": [{"flow": {"name": "Flow 1"}, "unit": "kg"}]},
               {"name": "Activity 2", "exchanges": [{"flow": {"name": "Flow 2"}, "unit": "tonnes"}]}
           ]
   >>> json_ld_get_normalized_exchange_units(data)
   [{'name': 'Activity 1', 'exchanges': [{'flow': {'name': 'Flow 1'}, 'unit': 'kilogram'}]},
    {'name': 'Activity 2', 'exchanges': [{'flow': {'name': 'Flow 2'}, 'unit': 'ton'}}]]


.. py:function:: json_ld_label_exchange_type(db)

   Add exchange type labels to each exchange in a given life cycle inventory represented as a list of activities and their exchanges.

   Parameters:
   -----------
   db : list
       A list of activities and their exchanges in a life cycle inventory.

   Raises:
   -------
   ValueError
       If an avoided product is considered as an input or if an input exchange is not a product, or if an output exchange is not a product or waste flow.

   Returns:
   --------
   list
       A modified list of activities and their exchanges with the addition of exchange type labels.

   Examples:
   ---------
   >>> db = [{'exchanges': [{'flow': {'flowType': 'PRODUCT_FLOW'}}, {'flow': {'flowType': 'ELEMENTARY_FLOW'}}]},
   ...       {'exchanges': [{'avoidedProduct': True}]},
   ...       {'exchanges': [{'input': True, 'flow': {'flowType': 'WASTE_FLOW'}}]},
   ...       {'exchanges': [{'flow': {'flowType': 'WASTE_FLOW'}}]}]
   >>> json_ld_label_exchange_type(db)
   [{'exchanges': [{'flow': {'flowType': 'PRODUCT_FLOW'}, 'type': 'technosphere'}, {'flow': {'flowType': 'ELEMENTARY_FLOW'}, 'type': 'biosphere'}]},
    {'exchanges': [{'avoidedProduct': True, 'type': 'substitution'}]},
    {'exchanges': [{'input': True, 'flow': {'flowType': 'WASTE_FLOW'}, 'type': 'production'}}],
    {'exchanges': [{'flow': {'flowType': 'WASTE_FLOW'}, 'type': 'production'}]}]


.. py:function:: json_ld_location_name(db)

   Update location information in the given database.

   Takes a database represented as a list of dictionaries and updates the location information in the
   'processes' to match the format of the Brightway schema. This is done by taking the name of the location from the
   'name' key of the location information and replacing the entire location information with just the location name.

   :param db: A list of dictionaries representing a database containing information about processes and exchanges.
   :type db: list

   :returns: A list of dictionaries representing the updated database with location information in the Brightway schema format.
   :rtype: list

   .. rubric:: Examples

   >>> db = [
               {"name": "Activity 1", "location": {"name": "Location 1"}},
               {"name": "Activity 2", "location": {"name": "Location 2"}}
           ]
   >>> json_ld_location_name(db)
   [{'name': 'Activity 1', 'location': 'Location 1'}, {'name': 'Activity 2', 'location': 'Location 2'}]


.. py:function:: json_ld_prepare_exchange_fields_for_linking(db)

   Update exchange information in the given database to prepare for linking.

   Takes a database represented as a list of dictionaries and updates the exchange information in the
   'processes' to prepare for linking. This is done by deleting unnecessary fields from the exchange dictionary and moving
   the 'name' and '@id' fields from the 'flow' dictionary to the exchange dictionary as 'name' and 'code' fields.

   :param db: A list of dictionaries representing a database containing information about processes and exchanges.
   :type db: list

   :returns: A list of dictionaries representing the updated database with exchange information prepared for linking.
   :rtype: list

   .. rubric:: Examples

   >>> db = [
               {"name": "Activity 1", "exchanges": [
                   {"flow": {"@id": "F1", "name": "Flow 1", "flowType": "PRODUCT_FLOW", "unit": "kg"},
                    "amount": 10, "input": False, "type": "technosphere", "uncertainty": {"amount": 0.1}}
               ]},
               {"name": "Activity 2", "exchanges": [
                   {"flow": {"@id": "F2", "name": "Flow 2", "flowType": "PRODUCT_FLOW", "unit": "kg"},
                    "amount": 20, "input": True, "type": "biosphere", "uncertainty": {"amount": 0.2}}
               ]}
           ]
   >>> json_ld_prepare_exchange_fields_for_linking(db)
   [{'name': 'Activity 1', 'exchanges': [
       {'amount': 10, 'type': 'technosphere', 'uncertainty': {'amount': 0.1}, 'name': 'Flow 1', 'code': 'F1'}
   ]}, {'name': 'Activity 2', 'exchanges': [
       {'amount': 20, 'type': 'biosphere', 'uncertainty': {'amount': 0.2}, 'name': 'Flow 2', 'code': 'F2'}
   ]}]


.. py:function:: json_ld_remove_fields(db)

   Remove specified fields from the given database.

   Takes a database represented as a list of dictionaries and removes specified fields from the dictionary.
   The fields to be removed are specified in the FIELDS set.

   :param db: A list of dictionaries representing a database containing information about processes and exchanges.
   :type db: list

   :returns: A list of dictionaries representing the updated database with specified fields removed.
   :rtype: list

   .. rubric:: Examples

   >>> db = [
           {"name": "Activity 1", "@context": "http://example.com", "processType": "type1", "infrastructureProcess": True},
           {"name": "Activity 2", "@context": "http://example.com", "processType": "type2", "infrastructureProcess": False}
       ]
   >>> json_ld_remove_fields(db)
   [{'name': 'Activity 1'}, {'name': 'Activity 2'}]


.. py:function:: json_ld_rename_metadata_fields(db)

   Change metadata field names in the given database to match the Brightway schema.

   Takes a database represented as a list of dictionaries and changes the metadata field names in the
   'processes' to match the Brightway schema. This is done by using a mapping between the old and new field names.

   Brightway schema: https://documentation.brightway.dev/en/latest/source/introduction/introduction.html#activity-data-format

   :param db: A list of dictionaries representing a database containing information about processes and exchanges.
   :type db: list

   :returns: A list of dictionaries representing the updated database with metadata field names changed to match the Brightway
             schema.
   :rtype: list

   .. rubric:: Examples

   >>> db = [                {"@id": "P1", "category": "Class 1", "@type": "Process", "lastChange": "2022-02-01"},                {"@id": "P2", "category": "Class 2", "@type": "Process", "lastChange": "2022-03-01"}            ]
   >>> json_ld_rename_metadata_fields(db)
   [{'code': 'P1', 'classifications': 'Class 1', 'type': 'Process', 'modified': '2022-02-01'},     {'code': 'P2', 'classifications': 'Class 2', 'type': 'Process', 'modified': '2022-03-01'}]


