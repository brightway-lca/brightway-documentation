:py:mod:`bw2io.strategies.json_ld_lcia`
=======================================

.. py:module:: bw2io.strategies.json_ld_lcia


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.json_ld_lcia.json_ld_lcia_add_method_metadata
   bw2io.strategies.json_ld_lcia.json_ld_lcia_convert_to_list
   bw2io.strategies.json_ld_lcia.json_ld_lcia_reformat_cfs_as_exchanges
   bw2io.strategies.json_ld_lcia.json_ld_lcia_set_method_metadata



.. py:function:: json_ld_lcia_add_method_metadata(data)

   Add metadata of the Life Cycle Impact Assessment (LCIA) method to the corresponding impact categories.

   Iterates over the LCIA methods and adds metadata from the method to each of its impact
   categories. The metadata includes the method's name, description, version, and lastChange.

   :param data: A dictionary containing LCIA methods and their impact categories.
   :type data: dict

   :returns: A dictionary with the updated LCIA impact categories containing the parent method metadata.
   :rtype: dict

   .. rubric:: Examples

   >>> data = {

   ...     "lcia_methods": {
   ...         "method_1": {
   ...             "name": "LCIA Method 1",
   ...             "description": "Sample LCIA Method 1",
   ...             "version": "1.0",
   ...             "lastChange": "2021-01-01",
   ...             "impactCategories": [
   ...                 {"@id": "category_1"},
   ...                 {"@id": "category_2"},
   ...             ],
   ...         },
   ...     },
   ...     "lcia_categories": {
   ...         "category_1": {},
   ...         "category_2": {},
   ...     },
   ... }
   >>> json_ld_lcia_add_method_metadata(data)
   {
       'lcia_methods': {
           'method_1': {
               'name': 'LCIA Method 1',
               'description': 'Sample LCIA Method 1',
               'version': '1.0',
               'lastChange': '2021-01-01',
               'impactCategories': [
                   {'@id': 'category_1'},
                   {'@id': 'category_2'},
               ],
           },
       },
       'lcia_categories': {
           'category_1': {
               'parent': {
                   'name': 'LCIA Method 1',
                   'description': 'Sample LCIA Method 1',
                   'version': '1.0',
                   'lastChange': '2021-01-01',
               },
           },
           'category_2': {
               'parent': {
                   'name': 'LCIA Method 1',
                   'description': 'Sample LCIA Method 1',
                   'version': '1.0',
                   'lastChange': '2021-01-01',
               },
           },
       },
   }


.. py:function:: json_ld_lcia_convert_to_list(data)

   Convert the Life Cycle Impact Assessment (LCIA) categories in the given data to a list.

   Takes the LCIA categories from the input data dictionary and returns them as a list.

   :param data: A dictionary containing the LCIA categories with their respective keys.
   :type data: dict

   :returns: A list of dictionaries representing the LCIA categories.
   :rtype: list

   .. rubric:: Examples

   >>> data = {
   ...     "lcia_categories": {
   ...         "category_1": {"name": "LCIA Category 1"},
   ...         "category_2": {"name": "LCIA Category 2"},
   ...     }
   ... }
   >>> json_ld_lcia_convert_to_list(data)
   [{'name': 'LCIA Category 1'}, {'name': 'LCIA Category 2'}]


.. py:function:: json_ld_lcia_reformat_cfs_as_exchanges(data)

   Reformat the impact factors of Life Cycle Impact Assessment (LCIA) methods as exchanges.

   Modifies the given LCIA methods data by renaming the 'impactFactors' field to 'exchanges' and
   updating the fields within each exchange.

   :param data: A list of dictionaries representing LCIA methods with impact factors.
   :type data: list

   :returns: A list of dictionaries representing the updated LCIA methods with reformatted exchanges.
   :rtype: list

   .. rubric:: Examples

   >>> data = [
   ...     {
   ...         "impactFactors": [
   ...             {
   ...                 "value": 1.0,
   ...                 "unit": {"name": "kg"},
   ...             }
   ...         ],
   ...     }
   ... ]
   >>> json_ld_lcia_reformat_cfs_as_exchanges(data)
   [
       {
           'exchanges': [
               {
                   'amount': 1.0,
                   'unit': 'kg',
               }
           ],
       }
   ]


.. py:function:: json_ld_lcia_set_method_metadata(data)

       Update the metadata of Life Cycle Impact Assessment (LCIA) methods in the given data.

       Processes the metadata of the LCIA methods in the given data, removing unnecessary fields,
       renaming fields, setting units, and updating the name and description.

       Parameters
       ----------
       data : list
           A list of dictionaries representing LCIA methods with metadata.

       Returns
       -------
       list
           A list of dictionaries representing the updated LCIA methods with modified metadata.

       Examples
       --------
       >>> data = [
       ...     {
       ...         "@context": "http://www.example.com",
       ...         "@type": "LCIA",
       ...         "referenceUnitName": "kg",
       ...         "@id": "method_1",
       ...         "name": "LCIA Method 1",
       ...         "description": "Sample LCIA Method 1",
       ...         "parent": {
       ...             "name": "Parent Method",
       ...             "description": "Sample parent method",
       ...         },
       ...     }
       ... ]
       >>> json_ld_lcia_set_method_metadata(data)
       [
           {
               'unit': 'kg',
               'id': 'method_1',
               'name': ('Parent Method', 'LCIA Method 1'),
               'description': 'Sample LCIA Method 1
   Sample parent method',
               'parent': {
                   'name': 'Parent Method',
                   'description': 'Sample parent method',
               },
           }
       ]



