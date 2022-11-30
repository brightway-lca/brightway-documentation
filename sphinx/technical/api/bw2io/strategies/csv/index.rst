:py:mod:`bw2io.strategies.csv`
==============================

.. py:module:: bw2io.strategies.csv


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.csv.csv_restore_tuples
   bw2io.strategies.csv.csv_restore_booleans
   bw2io.strategies.csv.csv_numerize
   bw2io.strategies.csv.csv_drop_unknown
   bw2io.strategies.csv.csv_add_missing_exchanges_section



.. py:function:: csv_restore_tuples(data)

   Restore tuples separated by `::` string


.. py:function:: csv_restore_booleans(data)

   Turn `True` and `False` into proper booleans, where possible


.. py:function:: csv_numerize(data)

   Turns strings into numbers where possible


.. py:function:: csv_drop_unknown(data)

   Drop keys whose values are `(Unknown)`.


.. py:function:: csv_add_missing_exchanges_section(data)


