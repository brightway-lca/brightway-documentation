:py:mod:`bw2calc.indexing`
==========================

.. py:module:: bw2calc.indexing


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2calc.indexing.index_with_arrays
   bw2calc.indexing.index_with_searchsorted



.. py:function:: index_with_arrays(array_from, array_to, mapping)

   Map ``array_from`` keys to ``array_to`` values using the dictionary ``mapping``.

   Turns the keys and values of mapping into index arrays.

   This is needed to take the ``flow``, ``input``, and ``output`` columns, which can be arbitrarily large integers, and transform them to matrix indices, which start from zero.

   Here is an example:

   .. code-block:: python

       import numpy as np
       a_f = np.array((1, 2, 3, 4))
       a_t = np.zeros(4)
       mapping = {1: 5, 2: 6, 3: 7, 4: 8}
       index_with_arrays(a_f, a_t, mapping)
       # => a_t is now [5, 6, 7, 8]

   :param \* *array_from*: 1-dimensional integer numpy array.
   :type \* *array_from*: array
   :param \* *array_to*: 1-dimensional integer numpy array.
   :type \* *array_to*: array
   :param \* *mapping*: Dictionary that links ``mapping`` indices to ``row`` or ``col`` indices, e.g. ``{34: 3}``.
   :type \* *mapping*: dict

   Operates in place. Doesn't return anything.


.. py:function:: index_with_searchsorted(array_from, array_to)

   Build a dictionary from the sorted, unique elements of an array, and map this dictionary from ``array_from`` to ``array_to``.

   Adapted from http://stackoverflow.com/questions/3403973/fast-replacement-of-values-in-a-numpy-array.

   Here is an example:

   .. code-block:: python

       import numpy as np
       array = np.array((4, 8, 6, 2, 4))
       output = np.zeros(5)
       index_with_searchsorted(array, output)
       # => returns {2: 0, 4: 1, 6: 2, 8: 3}
       # and `output` is [1, 3, 2, 0, 1]

   ``array_from`` and ``array_to`` are arrays of integers.

   Returns a dictionary that maps the sorted, unique elements of ``array_from`` to integers starting with zero.


