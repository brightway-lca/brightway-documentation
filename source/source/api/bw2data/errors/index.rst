:py:mod:`bw2data.errors`
========================

.. py:module:: bw2data.errors


Module Contents
---------------

.. py:exception:: BW2Exception

   Bases: :py:obj:`BaseException`

   .. autoapi-inheritance-diagram:: bw2data.errors.BW2Exception
      :parts: 1
      :private-bases:

   Base class for exceptions in Brightway2

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: Brightway2Project

   Bases: :py:obj:`BW2Exception`

   .. autoapi-inheritance-diagram:: bw2data.errors.Brightway2Project
      :parts: 1
      :private-bases:

   This project is not yet migrated to Brightway 2.5

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: DuplicateNode

   Bases: :py:obj:`BW2Exception`

   .. autoapi-inheritance-diagram:: bw2data.errors.DuplicateNode
      :parts: 1
      :private-bases:

   Can't have nodes with same unique identifiers

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: InvalidDatapackage

   Bases: :py:obj:`BW2Exception`

   .. autoapi-inheritance-diagram:: bw2data.errors.InvalidDatapackage
      :parts: 1
      :private-bases:

   The given datapackage can't be used for the requested task.

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: InvalidExchange

   Bases: :py:obj:`BW2Exception`

   .. autoapi-inheritance-diagram:: bw2data.errors.InvalidExchange
      :parts: 1
      :private-bases:

   Exchange is missing 'amount' or 'input'

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: MissingIntermediateData

   Bases: :py:obj:`BW2Exception`

   .. autoapi-inheritance-diagram:: bw2data.errors.MissingIntermediateData
      :parts: 1
      :private-bases:

   Base class for exceptions in Brightway2

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: MultipleResults

   Bases: :py:obj:`BW2Exception`

   .. autoapi-inheritance-diagram:: bw2data.errors.MultipleResults
      :parts: 1
      :private-bases:

   Base class for exceptions in Brightway2

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: NotAllowed

   Bases: :py:obj:`BW2Exception`

   .. autoapi-inheritance-diagram:: bw2data.errors.NotAllowed
      :parts: 1
      :private-bases:

   This operation is not allowed

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: NotFound

   Bases: :py:obj:`BW2Exception`

   .. autoapi-inheritance-diagram:: bw2data.errors.NotFound
      :parts: 1
      :private-bases:

   Requested web resource not found

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: PickleError

   Bases: :py:obj:`BW2Exception`

   .. autoapi-inheritance-diagram:: bw2data.errors.PickleError
      :parts: 1
      :private-bases:

   Pickle file can't be loaded due to updated library file structure

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: UnknownObject

   Bases: :py:obj:`BW2Exception`

   .. autoapi-inheritance-diagram:: bw2data.errors.UnknownObject
      :parts: 1
      :private-bases:

   Base class for exceptions in Brightway2

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: UntypedExchange

   Bases: :py:obj:`BW2Exception`

   .. autoapi-inheritance-diagram:: bw2data.errors.UntypedExchange
      :parts: 1
      :private-bases:

   Exchange doesn't have 'type' attribute

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: ValidityError

   Bases: :py:obj:`BW2Exception`

   .. autoapi-inheritance-diagram:: bw2data.errors.ValidityError
      :parts: 1
      :private-bases:

   The activity or exchange dataset does not have all the required fields

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: WebUIError

   Bases: :py:obj:`BW2Exception`

   .. autoapi-inheritance-diagram:: bw2data.errors.WebUIError
      :parts: 1
      :private-bases:

   Can't find running instance of bw2-web

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: WrongDatabase

   Bases: :py:obj:`BW2Exception`

   .. autoapi-inheritance-diagram:: bw2data.errors.WrongDatabase
      :parts: 1
      :private-bases:

   Can't save activities from database `x` to database `y`.

   Initialize self.  See help(type(self)) for accurate signature.


