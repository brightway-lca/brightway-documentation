:py:mod:`bw2io.strategies.lcia`
===============================

.. py:module:: bw2io.strategies.lcia


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.lcia.add_activity_hash_code
   bw2io.strategies.lcia.drop_unlinked_cfs
   bw2io.strategies.lcia.fix_ecoinvent_38_lcia_implementation
   bw2io.strategies.lcia.match_subcategories
   bw2io.strategies.lcia.rationalize_method_names
   bw2io.strategies.lcia.set_biosphere_type



.. py:function:: add_activity_hash_code(data)

   Add ``code`` field to characterization factors using ``activity_hash``, if ``code`` not already present.


.. py:function:: drop_unlinked_cfs(data)

   Drop CFs which don't have ``input`` attribute


.. py:function:: fix_ecoinvent_38_lcia_implementation(data)

   Ecoinvent 3.8 LCIA implmentation uses some flow names from 3.7.

   Update these when possible, delete when not.


.. py:function:: match_subcategories(data, biosphere_db_name, remove=True)

   Given a characterization with a top-level category, e.g. ``('air',)``, find all biosphere flows with the same top-level categories, and add CFs for these flows as well. Doesn't replace CFs for existing flows with multi-level categories. If ``remove``, also delete the top-level CF, but only if it is unlinked.


.. py:function:: rationalize_method_names(data)


.. py:function:: set_biosphere_type(data)

   Set CF types to 'biosphere', to keep compatibility with LCI strategies.

   This will overwrite existing ``type`` values.


