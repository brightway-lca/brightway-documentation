:py:mod:`bw2io.errors`
======================

.. py:module:: bw2io.errors


Module Contents
---------------

.. py:exception:: InvalidPackage

   Bases: :py:obj:`Exception`

   bw2package data doesn't validate


.. py:exception:: UnsafeData

   Bases: :py:obj:`Exception`

   bw2package data comes from a class that isn't recognized by Brightway2


.. py:exception:: UnsupportedExchange

   Bases: :py:obj:`Exception`

   This exchange uncertainty type can't be rescaled automatically


.. py:exception:: StrategyError

   Bases: :py:obj:`Exception`

   The strategy could not be applied


.. py:exception:: NonuniqueCode

   Bases: :py:obj:`Exception`

   Not all provided codes are unique


.. py:exception:: WrongDatabase

   Bases: :py:obj:`Exception`

   Dataset does not belong to this database


.. py:exception:: MultiprocessingError

   Bases: :py:obj:`Exception`

   Multiprocessing module error or incompatibility


.. py:exception:: UnallocatableDataset

   Bases: :py:obj:`Exception`

   GIven data cannot be sanely or deterministically allocated


.. py:exception:: MissingMigration

   Bases: :py:obj:`Exception`

   Needed migration data is missing


