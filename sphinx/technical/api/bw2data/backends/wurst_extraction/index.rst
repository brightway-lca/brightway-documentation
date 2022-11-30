:py:mod:`bw2data.backends.wurst_extraction`
===========================================

.. py:module:: bw2data.backends.wurst_extraction


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.backends.wurst_extraction._list_or_dict
   bw2data.backends.wurst_extraction.extract_activity
   bw2data.backends.wurst_extraction.extract_exchange
   bw2data.backends.wurst_extraction.add_exchanges_to_consumers
   bw2data.backends.wurst_extraction.add_input_info_for_indigenous_exchanges
   bw2data.backends.wurst_extraction.add_input_info_for_external_exchanges
   bw2data.backends.wurst_extraction.extract_brightway_databases



.. py:function:: _list_or_dict(obj)


.. py:function:: extract_activity(proxy, add_identifiers=False)

   Get data in Wurst internal format for an ``ActivityDataset``


.. py:function:: extract_exchange(proxy, add_properties=False)

   Get data in Wurst internal format for an ``ExchangeDataset``


.. py:function:: add_exchanges_to_consumers(activities, exchange_qs, add_properties=False, add_identifiers=False)

   Retrieve exchanges from database, and add to activities.

   Assumes that activities are single output, and that the exchange code is the same as the activity code. This assumption is valid for ecoinvent 3.3 cutoff imported into Brightway2.


.. py:function:: add_input_info_for_indigenous_exchanges(activities, names, add_identifiers=False)

   Add details on exchange inputs if these activities are already available


.. py:function:: add_input_info_for_external_exchanges(activities, names, add_identifiers=False)

   Add details on exchange inputs from other databases


.. py:function:: extract_brightway_databases(database_names, add_properties=False, add_identifiers=False)

   Extract a Brightway2 SQLiteBackend database to the Wurst internal format.

   ``database_names`` is a list of database names. You should already be in the correct project.

   Returns a list of dataset documents.


