:py:mod:`bw2io.strategies.csv`
==============================

.. py:module:: bw2io.strategies.csv


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.csv.csv_add_missing_exchanges_section
   bw2io.strategies.csv.csv_drop_unknown
   bw2io.strategies.csv.csv_numerize
   bw2io.strategies.csv.csv_restore_booleans
   bw2io.strategies.csv.csv_restore_tuples



.. py:function:: csv_add_missing_exchanges_section(data)

   Add an empty `exchanges` section to any dictionary in `data` that doesn't already have one.

   :param data: A list of dictionaries, where each dictionary represents a row of data.
   :type data: list of dict

   :returns: The updated list of dictionaries with an empty `exchanges` section added to any dictionary that doesn't already have one.
   :rtype: list[dict]

   .. rubric:: Examples

   >>> data = [
           {"name": "John", "age": 30},
           {"name": "Alice", "age": 25, "exchanges": []},
           {"name": "Bob", "age": 40, "exchanges": [{"name": "NYSE"}]}
       ]
   >>> csv_add_missing_exchanges_section(data)
       [
           {"name": "John", "age": 30, "exchanges": []},
           {"name": "Alice", "age": 25, "exchanges": []},
           {"name": "Bob", "age": 40, "exchanges": [{"name": "NYSE"}]}
       ]


.. py:function:: csv_drop_unknown(data)

   Remove any keys whose values are `(Unknown)`.

   :param data: A list of dictionaries, where each dictionary represents a row of data.
   :type data: list[dict]

   :returns: The updated list of dictionaries with `(Unknown)` values removed from the keys.
   :rtype: list[dict]

   .. rubric:: Examples

   >>> data = [
           {"name": "John", "age": 30, "gender": "(Unknown)"},
           {"name": "Alice", "age": 25, "gender": "Female"},
           {"name": "Bob", "age": 40, "gender": "Male"}
       ]
   >>> csv_drop_unknown(data)
       [
           {"name": "Alice", "age": 25, "gender": "Female"},
           {"name": "Bob", "age": 40, "gender": "Male"}
       ]


.. py:function:: csv_numerize(data)

   Convert string values to float or int where possible

   :param data: A list of datasets.
   :type data: list of dict

   :returns: A list of datasets with string values converted to float or int where possible.
   :rtype: list of dict

   .. rubric:: Examples

   >>> data = [{'amount': '10.0'}, {'exchanges': [{'amount': '20', 'uncertainty type': 'undefined'}]}]
   >>> csv_numerize(data)
   [{'amount': 10.0}, {'exchanges': [{'amount': 20, 'uncertainty type': 'undefined'}]}]


.. py:function:: csv_restore_booleans(data)

   Convert boolean-like strings to booleans where possible.

   :param data: A list of datasets.
   :type data: list of dict

   :returns: A list of datasets with booleans restored.
   :rtype: list of dict

   .. rubric:: Examples

   >>> data = [{'categories': 'category1', 'is_animal': 'true'}, {'exchanges': [{'categories': 'category2', 'amount': '10.0', 'uncertainty type': 'undefined', 'is_biomass': 'False'}]}]
   >>> csv_restore_booleans(data)
   [{'categories': 'category1', 'is_animal': True}, {'exchanges': [{'categories': 'category2', 'amount': '10.0', 'uncertainty type': 'undefined', 'is_biomass': False}]}]


.. py:function:: csv_restore_tuples(data)

   Convert tuple-like strings to actual tuples.

   :param data: A list of datasets.
   :type data: list of dict

   :returns: A list of datasets with tuples restored from string.
   :rtype: list of dict

   .. rubric:: Examples

   >>> data = [{'categories': 'category1::category2'}, {'exchanges': [{'categories': 'category3::category4', 'amount': '10.0'}]}]
   >>> csv_restore_tuples(data)
   [{'categories': ('category1', 'category2')}, {'exchanges': [{'categories': ('category3', 'category4'), 'amount': '10.0'}]}]


