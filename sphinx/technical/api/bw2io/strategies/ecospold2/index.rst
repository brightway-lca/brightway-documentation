:py:mod:`bw2io.strategies.ecospold2`
====================================

.. py:module:: bw2io.strategies.ecospold2


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.ecospold2.link_biosphere_by_flow_uuid
   bw2io.strategies.ecospold2.remove_zero_amount_coproducts
   bw2io.strategies.ecospold2.remove_zero_amount_inputs_with_no_activity
   bw2io.strategies.ecospold2.remove_unnamed_parameters
   bw2io.strategies.ecospold2.es2_assign_only_product_with_amount_as_reference_product
   bw2io.strategies.ecospold2.assign_single_product_as_activity
   bw2io.strategies.ecospold2.create_composite_code
   bw2io.strategies.ecospold2.link_internal_technosphere_by_composite_code
   bw2io.strategies.ecospold2.delete_exchanges_missing_activity
   bw2io.strategies.ecospold2.delete_ghost_exchanges
   bw2io.strategies.ecospold2.remove_uncertainty_from_negative_loss_exchanges
   bw2io.strategies.ecospold2.set_lognormal_loc_value
   bw2io.strategies.ecospold2.fix_unreasonably_high_lognormal_uncertainties
   bw2io.strategies.ecospold2.fix_ecoinvent_flows_pre35
   bw2io.strategies.ecospold2.drop_temporary_outdated_biosphere_flows
   bw2io.strategies.ecospold2.add_cpc_classification_from_single_reference_product
   bw2io.strategies.ecospold2.delete_none_synonyms
   bw2io.strategies.ecospold2.update_social_flows_in_older_consequential



.. py:function:: link_biosphere_by_flow_uuid(db, biosphere='biosphere3')


.. py:function:: remove_zero_amount_coproducts(db)

   Remove coproducts with zero production amounts from ``exchanges``


.. py:function:: remove_zero_amount_inputs_with_no_activity(db)

   Remove technosphere exchanges with amount of zero and no uncertainty.

   Input exchanges with zero amounts are the result of the ecoinvent linking algorithm, and can be safely discarded.


.. py:function:: remove_unnamed_parameters(db)

   Remove parameters which have no name. They can't be used in formulas or referenced.


.. py:function:: es2_assign_only_product_with_amount_as_reference_product(db)

   If a multioutput process has one product with a non-zero amount, assign that product as reference product.

   This is by default called after ``remove_zero_amount_coproducts``, which will delete the zero-amount coproducts in any case. However, we still keep the zero-amount logic in case people want to keep all coproducts.


.. py:function:: assign_single_product_as_activity(db)


.. py:function:: create_composite_code(db)

   Create composite code from activity and flow names


.. py:function:: link_internal_technosphere_by_composite_code(db)

   Link internal technosphere inputs by ``code``.

   Only links to process datasets actually in the database document.


.. py:function:: delete_exchanges_missing_activity(db)

   Delete exchanges that weren't linked correctly by ecoinvent.

   These exchanges are missing the "activityLinkId" attribute, and the flow they want to consume is not produced as the reference product of any activity. See the `known data issues <http://www.ecoinvent.org/database/ecoinvent-version-3/reports-of-changes/known-data-issues/>`__ report.



.. py:function:: delete_ghost_exchanges(db)

   Delete technosphere which can't be linked due to ecoinvent errors.

   A ghost exchange is one which links to a combination of *activity* and *flow* which aren't provided in the database.


.. py:function:: remove_uncertainty_from_negative_loss_exchanges(db)

   Remove uncertainty from negative lognormal exchanges.

   There are 15699 of these in ecoinvent 3.3 cutoff.

   The basic uncertainty and pedigree matrix are applied rather blindly,
   and the can produce strange net production values. It makes much more
   sense to assume that these loss factors are static.

   Only applies to exchanges which decrease net production.



.. py:function:: set_lognormal_loc_value(db)

   Make sure ``loc`` value is correct for lognormal uncertainty distributions


.. py:function:: fix_unreasonably_high_lognormal_uncertainties(db, cutoff=2.5, replacement=0.25)

   Fix unreasonably high uncertainty values.

   With the default cutoff value of 2.5 and a median of 1, the 95% confidence
   interval has a high to low ratio of 20.000.


.. py:function:: fix_ecoinvent_flows_pre35(db)


.. py:function:: drop_temporary_outdated_biosphere_flows(db)

   Drop biosphere exchanges which aren't used and are outdated


.. py:function:: add_cpc_classification_from_single_reference_product(db)


.. py:function:: delete_none_synonyms(db)


.. py:function:: update_social_flows_in_older_consequential(db, biosphere_db)

   The consequential system model automatically generates new biosphere flows with the category ``social`` (even though they aren't social flows) which are not really used and definitely not characterized, and whose UUID seems to change with each release. They are:

   * residual wood, dry
   * venting of argon, crude, liquid
   * venting of nitrogen, liquid

   The ecoinvent centre `recommends that they be dropped <https://ecoinvent.org/the-ecoinvent-database/data-releases/ecoinvent-3-7-1/#!/known-issues>`__:

   Consequential system model issues
   Three elementary exchanges are found in the compartment “social”. These exchanges can be ignored, both at the unit process and the inventory level, as ecoinvent does not yet account for social impacts.

   However, we can just look up the new UUIDs.



