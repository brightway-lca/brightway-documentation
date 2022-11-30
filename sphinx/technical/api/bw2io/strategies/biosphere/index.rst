:py:mod:`bw2io.strategies.biosphere`
====================================

.. py:module:: bw2io.strategies.biosphere


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.biosphere.drop_unspecified_subcategories
   bw2io.strategies.biosphere.normalize_biosphere_names
   bw2io.strategies.biosphere.normalize_biosphere_categories
   bw2io.strategies.biosphere.strip_biosphere_exc_locations
   bw2io.strategies.biosphere.ensure_categories_are_tuples



.. py:function:: drop_unspecified_subcategories(db)

   Drop subcategories if they are in the following:
   * ``unspecified``
   * ``(unspecified)``
   * ``''`` (empty string)
   * ``None``



.. py:function:: normalize_biosphere_names(db, lcia=False)

   Normalize biosphere flow names to ecoinvent 3.1 standard.

   Assumes that each dataset and each exchange have a ``name``. Will change names even if exchange is already linked.


.. py:function:: normalize_biosphere_categories(db, lcia=False)

   Normalize biosphere categories to ecoinvent 3.1 standard


.. py:function:: strip_biosphere_exc_locations(db)

   Biosphere flows don't have locations - if any are included they can confuse linking


.. py:function:: ensure_categories_are_tuples(db)


