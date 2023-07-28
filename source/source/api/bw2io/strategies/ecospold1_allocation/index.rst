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

   :param ds: A dataset that has multiple outputs.
   :type ds: dict

   :returns: A list of allocated datasets.
   :rtype: list of dict

   .. rubric:: Examples

   >>> ds = {'name': 'Dataset A', 'exchanges': [{'name': 'Output 1', 'code': 1, 'type': 'production'},
   ...                                          {'name': 'Output 2', 'code': 2},
   ...                                          {'name': 'Output 3', 'code': 3}],
   ...       'allocations': [{'exchanges': [2], 'fraction': 50.0, 'reference': 1},
   ...                        {'exchanges': [3], 'fraction': 50.0, 'reference': 1}]}
   >>> allocate_exchanges(ds)
   [{'name': 'Dataset A', 'exchanges': [{'name': 'Output 1', 'code': 1, 'type': 'production'},
                                        {'name': 'Output 2', 'code': 2, 'type': 'from'},
                                        {'name': 'Output 3', 'code': 3, 'type': 'from'}]},
    {'name': 'Dataset A: Output 2', 'exchanges': [{'name': 'Output 2', 'code': 2, 'type': 'production'}],
     'allocations': [{'exchanges': [2], 'fraction': 100.0, 'reference': 2}]},
    {'name': 'Dataset A: Output 3', 'exchanges': [{'name': 'Output 3', 'code': 3, 'type': 'production'}],
     'allocations': [{'exchanges': [3], 'fraction': 100.0, 'reference': 3}]}]


.. py:function:: clean_integer_codes(data)

   Convert integer activity codes to strings and delete integer codes from exchanges.

   :param data: List of datasets, where each dataset is a dictionary containing information about the dataset, such as its name,
                description, and exchanges.
   :type data: list of dict

   :returns: The cleaned list of datasets, where integer activity codes have been converted to strings and integer codes
             have been deleted from exchanges.
   :rtype: list of dict

   .. rubric:: Examples

   >>> data = [{'name': 'Dataset A', 'description': '...', 'code': 123},
   ...         {'name': 'Dataset B', 'description': '...', 'exchanges': [{'code': 456, 'amount': 1.0}]}]
   >>> clean_integer_codes(data)
   [{'name': 'Dataset A', 'description': '...', 'code': '123'},
    {'name': 'Dataset B', 'description': '...', 'exchanges': [{'amount': 1.0}]}]


.. py:function:: delete_integer_codes(data)

   Delete integer codes from the input data dictionary.

   :param data: A list of dictionaries, where each dictionary represents a row of data.
                Each dictionary should have a `name` key, and optionally a `code` and or `exchanges` key.
   :type data: list[dict]

   :returns: The updated list of dictionaries with any integer `code` keys removed from
             the dictionaries and their `exchanges` keys
   :rtype: list[dict]

   .. rubric:: Examples

   >>> data = [{'name': 'test', 'code': 1}, {'name': 'test2', 'exchanges': [{'code': 2}]}]
   >>> delete_integer_codes(data)
   >>> data == [{'name': 'test'}, {'name': 'test2', 'exchanges': [{}]}]


.. py:function:: es1_allocate_multioutput(data)

   This strategy allocates multioutput datasets to new datasets.

   This deletes the multioutput dataset, breaking any existing linking. This shouldn't be a concern, as you shouldn't link to a multioutput dataset in any case.

   Note that multiple allocations for the same product and input will result in undefined behavior.

   :param data: List of datasets, where each dataset is a dictionary containing information about the dataset, such as its name,
                description, and exchanges.
   :type data: list of dict

   :returns: The new list of datasets, where multioutput datasets have been allocated to new datasets.
   :rtype: list of dict

   .. rubric:: Examples

   >>> data = [{'name': 'Dataset A', 'exchanges': [{'name': 'Output 1', 'amount': 1.0},
   ...                                             {'name': 'Output 2', 'amount': 2.0}],
   ...          'allocations': [{'name': 'Activity 1', 'product': 'Output 1', 'input': 'Input 1'},
   ...                           {'name': 'Activity 2', 'product': 'Output 2', 'input': 'Input 2'}]},
   ...         {'name': 'Dataset B', 'exchanges': [{'name': 'Output 1', 'amount': 1.0}],
   ...          'allocations': [{'name': 'Activity 3', 'product': 'Output 1', 'input': 'Input 3'}]}]
   >>> es1_allocate_multioutput(data)
   [{'name': 'Dataset A: Output 1', 'exchanges': [{'name': 'Output 1', 'amount': 1.0}],
     'allocations': [{'name': 'Activity 1', 'product': 'Output 1', 'input': 'Input 1'}]},
    {'name': 'Dataset A: Output 2', 'exchanges': [{'name': 'Output 2', 'amount': 2.0}],
     'allocations': [{'name': 'Activity 2', 'product': 'Output 2', 'input': 'Input 2'}]},
    {'name': 'Dataset B', 'exchanges': [{'name': 'Output 1', 'amount': 1.0}],
     'allocations': [{'name': 'Activity 3', 'product': 'Output 1', 'input': 'Input 3'}]}]


.. py:function:: rescale_exchange(exc, scale)

   Rescale an exchange by a given factor.

   :param exc: The exchange to be rescaled.
   :type exc: dict
   :param scale: The factor by which to rescale the exchange.
   :type scale: float

   :returns: The rescaled exchange.
   :rtype: dict

   .. rubric:: Examples

   >>> exc = {'name': 'Output 1', 'amount': 1.0}
   >>> rescale_exchange(exc, 2.0)
   {'name': 'Output 1', 'amount': 2.0}


