:py:mod:`bw2data.backends.utils`
================================

.. py:module:: bw2data.backends.utils


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.backends.utils.get_csv_data_dict
   bw2data.backends.utils.check_exchange_amount
   bw2data.backends.utils.dict_as_activitydataset
   bw2data.backends.utils.dict_as_exchangedataset
   bw2data.backends.utils.replace_cfs
   bw2data.backends.utils.retupleize_geo_strings



.. py:function:: get_csv_data_dict(ds)


.. py:function:: check_exchange_amount(exc)

   Check exchange data validity when processing


.. py:function:: dict_as_activitydataset(ds)


.. py:function:: dict_as_exchangedataset(ds)


.. py:function:: replace_cfs(old_key, new_key)

   Replace ``old_key`` with ``new_key`` in characterization factors.

   Returns list of modified methods.


.. py:function:: retupleize_geo_strings(value)

   Transform data from SQLite representation to Python objects.

   We are using a SQLite3 cursor, which means that the Peewee data conversion code is not called. So ``('foo', 'bar')`` is stored as a string, not a tuple. This code tries to do this conversion correctly.

   TODO: Adapt what Peewee does in this case?


