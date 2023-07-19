:py:mod:`bw2io.strategies.lcia`
===============================

.. py:module:: bw2io.strategies.lcia


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.lcia.add_activity_hash_code
   bw2io.strategies.lcia.drop_unlinked_cfs
   bw2io.strategies.lcia.fix_ecoinvent_38_lcia_implementation
   bw2io.strategies.lcia.match_subcategories
   bw2io.strategies.lcia.rationalize_method_names
   bw2io.strategies.lcia.set_biosphere_type



.. py:function:: add_activity_hash_code(data)

   Add 'code' field to characterization factors using 'activity_hash', if 'code' not already present.

   Iterates over the LCIA methods in the given data and adds a 'code' field to each characterization
   factor using the 'activity_hash' function, if the 'code' field is not already present.

   :param data: A list of dictionaries representing LCIA methods with characterization factors.
   :type data: list

   :returns: A list of dictionaries representing the updated LCIA methods with 'code' field added to characterization factors.
   :rtype: list

   .. rubric:: Examples

   >>> data = [
   ...     {
   ...         "exchanges": [
   ...             {
   ...                 "name": "Characterization Factor 1",
   ...                 # Other fields needed for activity_hash function
   ...             },
   ...             {
   ...                 "name": "Characterization Factor 2",
   ...                 "code": "existing_code",
   ...                 # Other fields needed for activity_hash function
   ...             },
   ...         ],
   ...     }
   ... ]
   >>> add_activity_hash_code(data)
   [
       {
           'exchanges': [
               {
                   'name': 'Characterization Factor 1',
                   'code': 'generated_code',
                   # Other fields needed for activity_hash function
               },
               {
                   'name': 'Characterization Factor 2',
                   'code': 'existing_code',
                   # Other fields needed for activity_hash function
               },
           ],
       }
   ]


.. py:function:: drop_unlinked_cfs(data)

   Drop characterization factors (CFs) that don't have an 'input' attribute.

   Iterates over the LCIA methods in the given data and removes any characterization factors that
   don't have an 'input' attribute.

   :param data: A list of dictionaries representing LCIA methods with characterization factors.
   :type data: list

   :returns: A list of dictionaries representing the updated LCIA methods with unlinked characterization factors removed.
   :rtype: list

   .. rubric:: Examples

   >>> data = [
   ...     {
   ...         "exchanges": [
   ...             {"name": "Characterization Factor 1", "input": "input_1"},
   ...             {"name": "Characterization Factor 2"},
   ...         ],
   ...     }
   ... ]
   >>> drop_unlinked_cfs(data)
   [
       {
           'exchanges': [
               {
                   'name': 'Characterization Factor 1',
                   'input': 'input_1',
               },
           ],
       }
   ]


.. py:function:: fix_ecoinvent_38_lcia_implementation(data)

   Update flow names in ecoinvent 3.8 LCIA implementation to correct inconsistencies.

   Ecoinvent 3.8 LCIA implementation uses some flow names from 3.7. Updates these flow names when
   possible and deletes them when not.

   :param data: A list of dictionaries representing LCIA methods with characterization factors.
   :type data: list

   :returns: A list of dictionaries representing the updated LCIA methods with corrected flow names.
   :rtype: list

   .. rubric:: Examples

   >>> data = [
   ...     {
   ...         "name": "Method 1",
   ...         "exchanges": [
   ...             {"name": "Cyfluthrin", "categories": ("soil", "agricultural")},
   ...         ],
   ...     }
   ... ]
   >>> fix_ecoinvent_38_lcia_implementation(data)
   [
       {
           "name": "Method 1",
           "exchanges": [
               {"name": "Beta-cyfluthrin", "categories": ("soil", "agricultural")},
           ],
       }
   ]

   .. rubric:: Notes

   The function includes a hardcoded mapping to fix known inconsistencies in flow names. This may not cover all
   possible inconsistencies and might need to be updated in the future.


.. py:function:: match_subcategories(data, biosphere_db_name, remove=True)

   Add CFs for biosphere flows with the same top-level categories as a given characterization.

   Given a characterization with a top-level category, e.g. ('air',), Finds all biosphere flows with
   the same top-level categories and adds CFs for these flows as well. It doesn't replace CFs for existing flows
   with multi-level categories. If `remove` is set to True, it also deletes the top-level CF, but only if it is
   unlinked.

   :param data: A list of dictionaries representing LCIA methods with characterization factors.
   :type data: list
   :param biosphere_db_name: The name of the biosphere database to look up flows.
   :type biosphere_db_name: str
   :param remove: If True, delete the top-level CF if it is unlinked. Default is True.
   :type remove: bool, optional

   :returns: A list of dictionaries representing the updated LCIA methods with CFs added for biosphere flows with the
             same top-level categories.
   :rtype: list

   .. rubric:: Examples

   >>> data = [
   ...     {
   ...         "name": "Method 1",
   ...         "exchanges": [
   ...             {"categories": ("air",), "name": "Emission", "unit": "kg", "amount": 1.0},
   ...         ],
   ...     }
   ... ]
   >>> biosphere_db_name = "example_biosphere"
   >>> match_subcategories(data, biosphere_db_name)
   [
       {
           'name': 'Method 1',
           'exchanges': [
               {'categories': ('air',), 'name': 'Emission', 'unit': 'kg', 'amount': 1.0},
               # Additional CFs for biosphere flows with the same top-level category ('air',)
           ],
       }
   ]


.. py:function:: rationalize_method_names(data)

   Rationalize LCIA method names by removing redundant parts and unifying naming conventions.

   Iterates over the LCIA methods in the given data and updates the 'name' attribute of each method
   to remove unnecessary information and make the naming conventions more consistent.

   :param data: A list of dictionaries representing LCIA methods with method names.
   :type data: list

   :returns: A list of dictionaries representing the updated LCIA methods with rationalized method names.
   :rtype: list

   .. rubric:: Examples

   >>> data = [
   ...     {"name": ("Method 1 w/o LT", "Total")},
   ...     {"name": ("Method 2 no LT", "Total")},
   ...     {"name": ("Method 3", "Total")},
   ... ]
   >>> rationalize_method_names(data)
   [
       {'name': ('Method 1', 'without long-term')},
       {'name': ('Method 2', 'without long-term')},
       {'name': ('Method 3',)},
   ]


.. py:function:: set_biosphere_type(data)

   Set characterization factor (CF) types to 'biosphere' for compatibility with LCI strategies.

   Iterates over the LCIA methods in the given data and sets the 'type' attribute of each
   characterization factor to 'biosphere'. This will overwrite existing 'type' values.

   :param data: A list of dictionaries representing LCIA methods with characterization factors.
   :type data: list

   :returns: A list of dictionaries representing the updated LCIA methods with 'biosphere' set as the 'type' of
             characterization factors.
   :rtype: list

   .. rubric:: Examples

   >>> data = [
   ...     {
   ...         "exchanges": [
   ...             {"name": "Characterization Factor 1", "type": "original_type"},
   ...             {"name": "Characterization Factor 2"},
   ...         ],
   ...     }
   ... ]
   >>> set_biosphere_type(data)
   [
       {
           'exchanges': [
               {
                   'name': 'Characterization Factor 1',
                   'type': 'biosphere',
               },
               {
                   'name': 'Characterization Factor 2',
                   'type': 'biosphere',
               },
           ],
       }
   ]


