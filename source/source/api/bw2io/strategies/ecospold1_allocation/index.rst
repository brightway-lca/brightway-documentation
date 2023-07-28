:py:mod:`bw2io.strategies.ecospold1_allocation`
===============================================

.. py:module:: bw2io.strategies.ecospold1_allocation


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.ecospold1_allocation.allocate_exchanges
   bw2io.strategies.ecospold1_allocation.clean_integer_codes
   bw2io.strategies.ecospold1_allocation.delete_integer_codes
   bw2io.strategies.ecospold1_allocation.es1_allocate_multioutput
   bw2io.strategies.ecospold1_allocation.rescale_exchange



.. py:function:: allocate_exchanges(ds)

   Take a dataset, which has multiple outputs, and return a list of allocated datasets.

   The allocation data structure looks like:

   .. code-block:: python

       {
           'exchanges': [integer codes for biosphere flows, ...],
           'fraction': out of 100,
           'reference': integer codes
       }

   We assume that the allocation factor for each coproduct is always 100 percent.




.. py:function:: clean_integer_codes(data)

   Convert integer activity codes to strings and delete integer codes from exchanges (they can't be believed).


.. py:function:: delete_integer_codes(data)

   Delete integer codes completely from extracted ecospold1 datasets


.. py:function:: es1_allocate_multioutput(data)

   This strategy allocates multioutput datasets to new datasets.

   This deletes the multioutput dataset, breaking any existing linking. This shouldn't be a concern, as you shouldn't link to a multioutput dataset in any case.

   Note that multiple allocations for the same product and input will result in undefined behavior.



.. py:function:: rescale_exchange(exc, scale)


