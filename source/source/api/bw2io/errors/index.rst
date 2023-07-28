:py:mod:`bw2io.errors`
======================

.. py:module:: bw2io.errors


Module Contents
---------------

.. py:exception:: InvalidPackage

   Bases: :py:obj:`Exception`

   .. autoapi-inheritance-diagram:: bw2io.errors.InvalidPackage
      :parts: 1
      :private-bases:

   bw2package data doesn't validate

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: MultiprocessingError

   Bases: :py:obj:`Exception`

   .. autoapi-inheritance-diagram:: bw2io.errors.MultiprocessingError
      :parts: 1
      :private-bases:

   Multiprocessing module error or incompatibility

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: NonuniqueCode

   Bases: :py:obj:`Exception`

   .. autoapi-inheritance-diagram:: bw2io.errors.NonuniqueCode
      :parts: 1
      :private-bases:

   Not all provided codes are unique

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: StrategyError

   Bases: :py:obj:`Exception`

   .. autoapi-inheritance-diagram:: bw2io.errors.StrategyError
      :parts: 1
      :private-bases:

   The strategy could not be applied

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: UnsafeData

   Bases: :py:obj:`Exception`

   .. autoapi-inheritance-diagram:: bw2io.errors.UnsafeData
      :parts: 1
      :private-bases:

   bw2package data comes from a class that isn't recognized by Brightway2

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: UnsupportedExchange

   Bases: :py:obj:`Exception`

   .. autoapi-inheritance-diagram:: bw2io.errors.UnsupportedExchange
      :parts: 1
      :private-bases:

   This exchange uncertainty type can't be rescaled automatically

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: WrongDatabase

   Bases: :py:obj:`Exception`

   .. autoapi-inheritance-diagram:: bw2io.errors.WrongDatabase
      :parts: 1
      :private-bases:

   Dataset does not belong to this database

   Initialize self.  See help(type(self)) for accurate signature.


