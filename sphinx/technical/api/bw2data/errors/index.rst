:py:mod:`bw2data.errors`
========================

.. py:module:: bw2data.errors


Module Contents
---------------

.. py:exception:: BW2Exception

   Bases: :py:obj:`BaseException`

   Base class for exceptions in Brightway2


.. py:exception:: InvalidExchange

   Bases: :py:obj:`BW2Exception`

   Exchange is missing 'amount' or 'input'


.. py:exception:: DuplicateNode

   Bases: :py:obj:`BW2Exception`

   Can't have nodes with same unique identifiers


.. py:exception:: MissingIntermediateData

   Bases: :py:obj:`BW2Exception`

   Base class for exceptions in Brightway2


.. py:exception:: UnknownObject

   Bases: :py:obj:`BW2Exception`

   Base class for exceptions in Brightway2


.. py:exception:: MultipleResults

   Bases: :py:obj:`BW2Exception`

   Base class for exceptions in Brightway2


.. py:exception:: UntypedExchange

   Bases: :py:obj:`BW2Exception`

   Exchange doesn't have 'type' attribute


.. py:exception:: WebUIError

   Bases: :py:obj:`BW2Exception`

   Can't find running instance of bw2-web


.. py:exception:: ValidityError

   Bases: :py:obj:`BW2Exception`

   The activity or exchange dataset does not have all the required fields


.. py:exception:: NotAllowed

   Bases: :py:obj:`BW2Exception`

   This operation is not allowed


.. py:exception:: WrongDatabase

   Bases: :py:obj:`BW2Exception`

   Can't save activities from database `x` to database `y`.


.. py:exception:: NotFound

   Bases: :py:obj:`BW2Exception`

   Requested web resource not found


.. py:exception:: PickleError

   Bases: :py:obj:`BW2Exception`

   Pickle file can't be loaded due to updated library file structure


.. py:exception:: Brightway2Project

   Bases: :py:obj:`BW2Exception`

   This project is not yet migrated to Brightway 2.5


.. py:exception:: InvalidDatapackage

   Bases: :py:obj:`BW2Exception`

   The given datapackage can't be used for the requested task.


