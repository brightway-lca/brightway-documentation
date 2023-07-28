:py:mod:`bw2data.backends.utils`
================================

.. py:module:: bw2data.backends.utils


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.backends.utils.convert_backend



.. py:function:: convert_backend(database_name, backend)

   Convert a Database to another backend.

   bw2data currently supports the `default` and `json` backends.

   :param \* `database_name`: Name of database.
   :type \* `database_name`: unicode
   :param \* `backend`: Type of database. `backend` should be recoginized by `DatabaseChooser`.
   :type \* `backend`: unicode

   Returns `False` if the old and new backend are the same. Otherwise returns an instance of the new Database object.


