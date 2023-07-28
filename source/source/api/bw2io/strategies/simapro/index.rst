:py:mod:`bw2io.strategies.simapro`
==================================

.. py:module:: bw2io.strategies.simapro


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.simapro.change_electricity_unit_mj_to_kwh
   bw2io.strategies.simapro.fix_localized_water_flows
   bw2io.strategies.simapro.fix_zero_allocation_products
   bw2io.strategies.simapro.link_technosphere_based_on_name_unit_location
   bw2io.strategies.simapro.normalize_simapro_biosphere_categories
   bw2io.strategies.simapro.normalize_simapro_biosphere_names
   bw2io.strategies.simapro.normalize_simapro_formulae
   bw2io.strategies.simapro.set_lognormal_loc_value_uncertainty_safe
   bw2io.strategies.simapro.sp_allocate_products
   bw2io.strategies.simapro.split_simapro_name_geo



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.simapro.detoxify_pattern
   bw2io.strategies.simapro.detoxify_re


.. py:function:: change_electricity_unit_mj_to_kwh(db)

   Change datasets with the string ``electricity`` in their name from units of MJ to kilowatt hour.


.. py:function:: fix_localized_water_flows(db)

   Change ``Water, BR`` to ``Water``.

   Biosphere flows can't have locations - locations are defined by the activity dataset.


.. py:function:: fix_zero_allocation_products(db)

   Drop all inputs from allocated products which had zero allocation factors.

   The final production amount is the initial amount times the allocation factor. If this is zero, a singular technosphere matrix is created. We fix this by setting the production amount to one, and deleting all inputs.

   Does not modify datasets with more than one production exchange.


.. py:function:: link_technosphere_based_on_name_unit_location(db, external_db_name=None)

   Link technosphere exchanges based on name, unit, and location. Can't use categories because we can't reliably extract categories from SimaPro exports, only exchanges.

   If ``external_db_name``, link against a different database; otherwise link internally.


.. py:function:: normalize_simapro_biosphere_categories(db)

   Normalize biosphere categories to ecoinvent standard.


.. py:function:: normalize_simapro_biosphere_names(db)

   Normalize biosphere flow names to ecoinvent standard


.. py:function:: normalize_simapro_formulae(formula, settings)

   Convert SimaPro formulae to Python


.. py:function:: set_lognormal_loc_value_uncertainty_safe(db)

   Make sure ``loc`` value is correct for lognormal uncertainty distributions


.. py:function:: sp_allocate_products(db)

   Create a dataset from each product in a raw SimaPro dataset


.. py:function:: split_simapro_name_geo(db)

   Split a name like 'foo/CH U' into name and geo components.

   Sets original name to ``simapro name``.


.. py:data:: detoxify_pattern
   :value: '^(?P<name>.+?)/(?P<geo>[A-Za-z]{2,10})(/I)? [SU]$'

   

.. py:data:: detoxify_re

   

