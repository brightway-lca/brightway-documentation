:py:mod:`bw2calc.utils`
=======================

.. py:module:: bw2calc.utils


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2calc.utils.extract_uncertainty_fields
   bw2calc.utils.get_seed
   bw2calc.utils.load_arrays
   bw2calc.utils.load_calculation_package
   bw2calc.utils.md5
   bw2calc.utils.wrap_functional_unit



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2calc.utils.MAX_INT_32
   bw2calc.utils.MAX_SIGNED_INT_32
   bw2calc.utils.global_index


.. py:function:: extract_uncertainty_fields(array)

   Extract the core set of fields needed for uncertainty analysis from a parameter array


.. py:function:: get_seed(seed=None)

   Get valid Numpy random seed value


.. py:function:: load_arrays(objs)

   Load the numpy arrays from list of objects ``objs``.

   Currently accepts ``str`` filepaths, ``BytesIO``,
    ``numpy.ndarray`` arrays. Creates copies of objects


.. py:function:: load_calculation_package(fp)

   Load a calculation package created by ``save_calculation_package``.

   NumPy arrays are saved to a temporary directory, and file paths are adjusted.

   ``fp`` is the absolute file path of a calculation package file.

   Returns a dictionary suitable for passing to an LCA object, e.g. ``LCA(**load_calculation_package(fp))``.



.. py:function:: md5(filepath, blocksize=65536)

   Generate MD5 hash for file at `filepath`


.. py:function:: wrap_functional_unit(dct)

   Transform functional units for effective logging.

   Turns ``Activity`` objects into their keys.


.. py:data:: MAX_INT_32
   :value: 4294967295

   

.. py:data:: MAX_SIGNED_INT_32
   :value: 2147483647

   

.. py:data:: global_index

   

