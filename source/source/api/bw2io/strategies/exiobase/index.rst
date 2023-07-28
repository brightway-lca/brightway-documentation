:py:mod:`bw2io.strategies.exiobase`
===================================

.. py:module:: bw2io.strategies.exiobase


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.exiobase.add_biosphere_ids
   bw2io.strategies.exiobase.add_product_ids
   bw2io.strategies.exiobase.add_stam_labels
   bw2io.strategies.exiobase.get_categories
   bw2io.strategies.exiobase.get_exiobase_biosphere_correspondence
   bw2io.strategies.exiobase.normalize_units
   bw2io.strategies.exiobase.remove_numeric_codes
   bw2io.strategies.exiobase.rename_exiobase_co2_eq_flows



.. py:function:: add_biosphere_ids(correspondence, biospheres=None)

   Add 'id' key to each dictionary in the list of correspondence data based on the ecoinvent
   and exiobase names found in the specified biosphere databases.

   :param correspondence: A list of dictionaries containing correspondence data.
   :type correspondence: list of dict
   :param biospheres: A list of biosphere database names. Defaults to the biosphere defined in the
                      configuration file.
   :type biospheres: list, optional

   :returns: The correspondence data with added 'id' keys.
   :rtype: list of dict

   :raises ValueError: If the correspondence data does not have the required keys, or if a specified
       biosphere database does not exist.

   .. rubric:: Examples

   >>> correspondence_data = [{'ecoinvent name': 'CO2', 'exiobase name': 'CO2', 'ecoinvent category': 'air', 'ecoinvent subcategory': ''}]
   >>> add_biosphere_ids(correspondence_data)
   [{'ecoinvent name': 'CO2', 'exiobase name': 'CO2', 'ecoinvent category': 'air', 'ecoinvent subcategory': '', 'id': some_id}]


.. py:function:: add_product_ids(products, db_name)

   Add 'id' key to each dictionary in the list of products based on the name and location
   of the products found in the specified database.

   :param products: A list of dictionaries containing product data.
   :type products: list of dict
   :param db_name: The name of the database to look up the product IDs.
   :type db_name: str

   :returns: The products data with added 'id' keys.
   :rtype: list of dict

   :raises ValueError: If the product data does not have the required keys, or if the specified database
       does not exist.

   .. rubric:: Examples

   >>> products_data = [{'name': 'Electricity', 'location': 'CH'}]
   >>> add_product_ids(products_data, 'ecoinvent 3.7.1')
   [{'name': 'Electricity', 'location': 'CH', 'id': some_id}]


.. py:function:: add_stam_labels(data)

   Adds STAM labels to the input data, which should be a list
   of dictionaries containing a key-value pair for the name. The STAM labels
   are loaded from a JSON file located in the 'lci' directory.

       Parameters
   ----------
   data : list of dict
       A list of dictionaries, where each dictionary contains a key-value pair
       for the name.

   :returns: The updated list of dictionaries with added STAM labels.
   :rtype: list of dict

   :raises TypeError: If data is not a list of dictionaries.

   .. rubric:: Examples

   >>> data = [
   ...     {"name": "element 1"},
   ...     {"name": "element 2"},
   ... ]
   >>> add_stam_labels(data)
   [
       {"name": "element 1", "stam": "STAM 1"},
       {"name": "element 2", "stam": "STAM 2"},
   ]


.. py:function:: get_categories(x)

   Takes a dictionary containing 'ecoinvent category' and
   'ecoinvent subcategory' keys and returns a tuple containing the category
   and subcategory if both are available, or just the category if the
   subcategory is not available.

   :param x: A dictionary containing 'ecoinvent category' and 'ecoinvent subcategory'.
   :type x: dict

   :returns: A tuple containing the ecoinvent category and subcategory if both are available,
             or just the category if the subcategory is not available.
   :rtype: tuple

   .. rubric:: Examples

   >>> data = {'ecoinvent category': 'Energy', 'ecoinvent subcategory': 'Electricity'}
   >>> get_categories(data)
   ('Energy', 'Electricity')


.. py:function:: get_exiobase_biosphere_correspondence()

   Reads the 'EXIOBASE-ecoinvent-biosphere.csv' file and
   returns the correspondence data as a list of dictionaries. The file is
   expected to be in the 'data_directory/lci' directory.

   :returns: A list of dictionaries containing Exiobase biosphere correspondence data.
   :rtype: list of dict

   .. rubric:: Examples

   >>> correspondence_data = get_exiobase_biosphere_correspondence()


.. py:function:: normalize_units(data, label='unit')

   "
   Normalize the units of the given data by replacing them with their equivalent,
   standardized representations.
   The function takes a list of dictionaries where each dictionary contains a key-value
   pair for the specified label (default: "unit"). The function uses a lookup table to
   replace the unit values with their standardized representations.

   :param data: A list of dictionaries where each dictionary contains a key-value pair for the
                specified label.
   :type data: list
   :param label: The label of the key in the dictionaries whose value needs to be normalized
                 (default: "unit").
   :type label: str, optional

   :returns: The updated list of dictionaries with normalized units.
   :rtype: list

   .. rubric:: Examples

   >>> data = [
   ...     {"unit": "M.EUR"},
   ...     {"unit": "1000 p"},
   ...     {"unit": "M.hr"},
   ... ]
   >>> normalize_units(data)
   [
       {"unit": "million €"},
       {"unit": "1000 people"},
       {"unit": "million hour"},
   ]


.. py:function:: remove_numeric_codes(products)

   Removes any numeric codes found at the end of the product names
   in the given list of products.

   :param products: A list of dictionaries, where each dictionary contains a key-value pair
                    for the product name.
   :type products: list of dict

   :returns: The updated list of dictionaries with numeric codes removed from product names.
   :rtype: list of dict

   :raises TypeError: If products is not a list of dictionaries.

   .. rubric:: Examples

   >>> products = [
   ...     {"name": "product A (01)"},
   ...     {"name": "product B (99)"},
   ... ]
   >>> remove_numeric_codes(products)
   [
       {"name": "product A"},
       {"name": "product B"},
   ]


.. py:function:: rename_exiobase_co2_eq_flows(flows)

   Renames CO2 equivalent flows in the input list of flows. The
   input list should contain dictionaries with a key-value pair for the
   'exiobase name'. The function updates the 'exiobase name' for the flows
   that match the provided mapping.

   :param flows: A list of dictionaries, where each dictionary contains a key-value pair
                 for the 'exiobase name'.
   :type flows: list of dict

   :returns: The updated list of flows with renamed CO2 equivalent flows.
   :rtype: list of dict

   .. rubric:: Examples

   >>> flows = [
   ...     {"exiobase name": "PFC - air"},
   ...     {"exiobase name": "HFC - air"},
   ... ]
   >>> rename_exiobase_co2_eq_flows(flows)
   [
       {"exiobase name": "PFC (CO2-eq)"},
       {"exiobase name": "HFC (CO2-eq)"},
   ]


