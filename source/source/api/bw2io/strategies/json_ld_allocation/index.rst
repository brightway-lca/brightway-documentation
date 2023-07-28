:py:mod:`bw2io.strategies.json_ld_allocation`
=============================================

.. py:module:: bw2io.strategies.json_ld_allocation


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.json_ld_allocation.allocatable_exchanges
   bw2io.strategies.json_ld_allocation.allocation_needed
   bw2io.strategies.json_ld_allocation.causal_allocation
   bw2io.strategies.json_ld_allocation.get_allocation_dict
   bw2io.strategies.json_ld_allocation.get_production_exchange
   bw2io.strategies.json_ld_allocation.get_production_exchanges
   bw2io.strategies.json_ld_allocation.json_ld_allocate_datasets



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.json_ld_allocation.VALID_METHODS


.. py:function:: allocatable_exchanges(exchanges)

   Filter a list of exchanges to retain only those that are allocatable.

   Filters the input list of exchanges, retaining only those that meet
   at least one of the following conditions:
   1. Their 'flowType' attribute in the 'flow' dictionary is 'ELEMENTARY_FLOW'.
   2. Their 'flowType' attribute in the 'flow' dictionary is 'WASTE_FLOW'.
   3. They have an 'avoidedProduct' key.
   4. They have an 'input' key.

   :param exchanges: A list of dictionaries representing exchanges, each containing keys such as
                     'flow', 'avoidedProduct', and 'input'.
   :type exchanges: list of dict

   :returns: A list of allocatable exchanges, filtered based on the specified conditions.
   :rtype: list of dict

   .. rubric:: Examples

   >>> exchanges = [
   ...     {"flow": {"flowType": "ELEMENTARY_FLOW"}},
   ...     {"flow": {"flowType": "WASTE_FLOW"}},
   ...     {"avoidedProduct": True},
   ...     {"input": "some_input"},
   ...     {"flow": {"flowType": "OTHER_FLOW"}},
   ... ]
   >>> allocatable_exchanges(exchanges)
   [
       {"flow": {"flowType": "ELEMENTARY_FLOW"}},
       {"flow": {"flowType": "WASTE_FLOW"}},
       {"avoidedProduct": True},
       {"input": "some_input"},
   ]


.. py:function:: allocation_needed(ds)

   Determine if allocation is needed for the given dataset.

   Checks if the input dataset requires allocation by examining its
   'allocationFactors' attribute and verifying that its '@type' is neither 'product'
   nor 'emission'. Allocation is typically necessary for datasets that represent
   shared processes or resources that need to be divided among multiple consumers.

   :param ds: A dictionary representing a dataset, containing keys such as
              'allocationFactors' and '@type'.
   :type ds: dict

   :returns: True if the dataset requires allocation, False otherwise.
   :rtype: bool

   .. rubric:: Examples

   >>> ds_product = {"@type": "product", "allocationFactors": {"A": 0.5, "B": 0.5}}
   >>> allocation_needed(ds_product)
   False

   >>> ds_emission = {"@type": "emission", "allocationFactors": {"A": 0.5, "B": 0.5}}
   >>> allocation_needed(ds_emission)
   False

   >>> ds_shared = {"@type": "shared_process", "allocationFactors": {"A": 0.3, "B": 0.7}}
   >>> allocation_needed(ds_shared)
   True


.. py:function:: causal_allocation(exchanges, ad)

   Allocate causal factors to exchanges in a list, applying a rescaling factor based on a given dictionary.

   Iterates over a list of exchanges and applies the corresponding causal allocation factor
   provided in the `ad` dictionary. It raises an UnallocatableDataset exception if the causal allocation
   factor for a given exchange is missing in the `ad` dictionary.

   :param exchanges: A list of dictionaries representing exchanges, where each dictionary contains a flow with an @id key.
   :type exchanges: list
   :param ad: A dictionary containing causal allocation factors for each exchange, indexed by the exchange flow @id.
   :type ad: dict

   :returns: A list of processed exchanges with the causal allocation factors applied.
   :rtype: list

   :raises UnallocatableDataset: If the causal allocation factor for an exchange is missing in the `ad` dictionary.

   .. rubric:: Examples

   >>> exchanges = [{'flow': {'@id': 1}, 'amount': 10}, {'flow': {'@id': 2}, 'amount': 20}]
   >>> ad = {1: 0.5, 2: 0.25}
   >>> causal_allocation(exchanges, ad)
   [{'flow': {'@id': 1}, 'amount': 5.0}, {'flow': {'@id': 2}, 'amount': 5.0}]


.. py:function:: get_allocation_dict(factors)

   Create a nested dictionary for the given allocation factors.

   Processes a list of allocation factors and organizes them into a
   nested dictionary structure. The outer dictionary has keys corresponding to the
   allocation types ('CAUSAL_ALLOCATION' or other types), while the inner
   dictionaries have keys corresponding to product IDs and, for 'CAUSAL_ALLOCATION',
   also flow IDs.

   :param factors: A list of dictionaries representing allocation factors, each containing keys
                   such as 'allocationType', 'product', 'exchange', and 'value'.
   :type factors: list of dict

   :returns: A nested dictionary containing the allocation factors organized by allocation
             type, product ID, and, for 'CAUSAL_ALLOCATION', flow ID.
   :rtype: defaultdict(dict)

   :raises UnallocatableDataset: If a 'CAUSAL_ALLOCATION' factor is missing either the 'product' or 'flow' keys.

   .. rubric:: Examples

   >>> factors = [
   ...     {
   ...         "allocationType": "CAUSAL_ALLOCATION",
   ...         "product": {"@id": "P1"},
   ...         "exchange": {"flow": {"@id": "F1"}},
   ...         "value": 0.7,
   ...     },
   ...     {
   ...         "allocationType": "ECONOMIC_ALLOCATION",
   ...         "product": {"@id": "P2"},
   ...         "value": 0.6,
   ...     },
   ... ]
   >>> get_allocation_dict(factors)
   defaultdict(
       dict,
       {
           'CAUSAL_ALLOCATION': {'P1': {'F1': 0.7}},
           'ECONOMIC_ALLOCATION': {'P2': 0.6},
       },
   )


.. py:function:: get_production_exchange(exchanges, flow_id)

   Find the production exchange with the specified flow ID.

   Searches the input list of exchanges for the production exchange
   with the specified flow ID. It raises an UnallocatableDataset exception if more
   than one candidate is found or a ValueError if no candidate is found.

   :param exchanges: A list of dictionaries representing exchanges, each containing keys such as
                     'flow' and 'input'.
   :type exchanges: list of dict
   :param flow_id: The flow ID to search for in the production exchanges.
   :type flow_id: str

   :returns: The production exchange with the specified flow ID.
   :rtype: dict

   :raises UnallocatableDataset: If more than one production exchange with the specified flow ID is found.
   :raises ValueError: If no production exchange with the specified flow ID is found.

   .. rubric:: Examples

   >>> exchanges = [
   ...     {"flow": {"flowType": "PRODUCT_FLOW", "@id": "F1"}},
   ...     {"flow": {"flowType": "PRODUCT_FLOW", "@id": "F2"}},
   ...     {"flow": {"flowType": "ELEMENTARY_FLOW", "@id": "F3"}},
   ... ]
   >>> get_production_exchange(exchanges, "F1")
   {"flow": {"flowType": "PRODUCT_FLOW", "@id": "F1"}}


.. py:function:: get_production_exchanges(exchanges)

   Filter a list of exchanges to retain only those representing production flows.

   Filters the input list of exchanges, retaining only those that have
   a 'flowType' attribute of 'PRODUCT_FLOW' in the 'flow' dictionary and do not have
   an 'input' key. Production flows typically represent the output of a process or
   system.

   :param exchanges: A list of dictionaries representing exchanges, each containing keys such as
                     'flow' and 'input'.
   :type exchanges: list of dict

   :returns: A list of production exchanges, filtered based on the specified conditions.
   :rtype: list of dict

   .. rubric:: Examples

   >>> exchanges = [
   ...     {"flow": {"flowType": "PRODUCT_FLOW"}},
   ...     {"flow": {"flowType": "PRODUCT_FLOW"}, "input": "some_input"},
   ...     {"flow": {"flowType": "ELEMENTARY_FLOW"}},
   ... ]
   >>> get_production_exchanges(exchanges)
   [{"flow": {"flowType": "PRODUCT_FLOW"}}]


.. py:function:: json_ld_allocate_datasets(db, preferred_allocation=None)

   Perform allocation on multifunctional datasets in a given database according to the specified allocation method.

   Uses the preferred_allocation method if available; otherwise, it uses the default method.
   The allocation is performed according to the JSON-LD specification which lists the following methods:

   * PHYSICAL_ALLOCATION
   * ECONOMIC_ALLOCATION
   * CAUSAL_ALLOCATION (Can be exchange-specific)
   * USE_DEFAULT_ALLOCATION
   * NO_ALLOCATION

   :param db: A dictionary representing a database containing processes and their exchanges.
   :type db: dict
   :param preferred_allocation: The preferred allocation method to use, if available. Defaults to None.
   :type preferred_allocation: str, optional

   :returns: A dictionary representing the modified database with allocated datasets.
   :rtype: dict

   :raises AssertionError: If an invalid allocation method is provided.
   :raises UnallocatableDataset: If the default allocation is chosen, but allocation factors for this method are not provided.

   .. rubric:: Examples

   >>> db = {
   ...     "processes": {
   ...         # Add processes with exchanges and allocation factors here
   ...     }
   ... }
   >>> preferred_allocation = "ECONOMIC_ALLOCATION"
   >>> json_ld_allocate_datasets(db, preferred_allocation)
   # Returns the modified database with allocated datasets


.. py:data:: VALID_METHODS

   

