:py:mod:`bw2io.strategies.json_ld_allocation`
=============================================

.. py:module:: bw2io.strategies.json_ld_allocation


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.json_ld_allocation.allocation_needed
   bw2io.strategies.json_ld_allocation.allocatable_exchanges
   bw2io.strategies.json_ld_allocation.get_allocation_dict
   bw2io.strategies.json_ld_allocation.get_production_exchanges
   bw2io.strategies.json_ld_allocation.get_production_exchange
   bw2io.strategies.json_ld_allocation.causal_allocation
   bw2io.strategies.json_ld_allocation.json_ld_allocate_datasets



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.json_ld_allocation.VALID_METHODS


.. py:data:: VALID_METHODS
   

   

.. py:function:: allocation_needed(ds)


.. py:function:: allocatable_exchanges(exchanges)


.. py:function:: get_allocation_dict(factors)


.. py:function:: get_production_exchanges(exchanges)


.. py:function:: get_production_exchange(exchanges, flow_id)


.. py:function:: causal_allocation(exchanges, ad)


.. py:function:: json_ld_allocate_datasets(db, preferred_allocation=None)

   Perform allocation on multifunctional datasets.

   Uses the ``preferred_allocation`` method if available; otherwise, the default method.

   Here are the allocation methods listed in the JSON-LD spec:

   * PHYSICAL_ALLOCATION
   * ECONOMIC_ALLOCATION
   * CAUSAL_ALLOCATION (Can be exchange-specific)
   * USE_DEFAULT_ALLOCATION
   * NO_ALLOCATION

   We can't use ``@id`` values as codes after allocation, so we combine the process id and the flow id for the allocated dataset.



