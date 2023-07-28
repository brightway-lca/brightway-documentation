:py:mod:`bw2io.strategies`
==========================

.. py:module:: bw2io.strategies


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   biosphere/index.rst
   csv/index.rst
   ecospold1/index.rst
   ecospold1_allocation/index.rst
   ecospold2/index.rst
   generic/index.rst
   lcia/index.rst
   locations/index.rst
   migrations/index.rst
   simapro/index.rst
   special/index.rst


Package Contents
----------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.add_activity_hash_code
   bw2io.strategies.add_cpc_classification_from_single_reference_product
   bw2io.strategies.add_database_name
   bw2io.strategies.assign_only_product_as_production
   bw2io.strategies.assign_single_product_as_activity
   bw2io.strategies.change_electricity_unit_mj_to_kwh
   bw2io.strategies.clean_integer_codes
   bw2io.strategies.convert_activity_parameters_to_list
   bw2io.strategies.convert_uncertainty_types_to_integers
   bw2io.strategies.create_composite_code
   bw2io.strategies.csv_add_missing_exchanges_section
   bw2io.strategies.csv_drop_unknown
   bw2io.strategies.csv_numerize
   bw2io.strategies.csv_restore_booleans
   bw2io.strategies.csv_restore_tuples
   bw2io.strategies.delete_exchanges_missing_activity
   bw2io.strategies.delete_ghost_exchanges
   bw2io.strategies.delete_integer_codes
   bw2io.strategies.delete_none_synonyms
   bw2io.strategies.drop_falsey_uncertainty_fields_but_keep_zeros
   bw2io.strategies.drop_temporary_outdated_biosphere_flows
   bw2io.strategies.drop_unlinked
   bw2io.strategies.drop_unlinked_cfs
   bw2io.strategies.drop_unspecified_subcategories
   bw2io.strategies.ensure_categories_are_tuples
   bw2io.strategies.es1_allocate_multioutput
   bw2io.strategies.es2_assign_only_product_with_amount_as_reference_product
   bw2io.strategies.fix_ecoinvent_flows_pre35
   bw2io.strategies.fix_localized_water_flows
   bw2io.strategies.fix_unreasonably_high_lognormal_uncertainties
   bw2io.strategies.fix_zero_allocation_products
   bw2io.strategies.link_biosphere_by_flow_uuid
   bw2io.strategies.link_internal_technosphere_by_composite_code
   bw2io.strategies.link_technosphere_based_on_name_unit_location
   bw2io.strategies.link_technosphere_by_activity_hash
   bw2io.strategies.match_subcategories
   bw2io.strategies.migrate_datasets
   bw2io.strategies.migrate_exchanges
   bw2io.strategies.normalize_biosphere_categories
   bw2io.strategies.normalize_biosphere_names
   bw2io.strategies.normalize_simapro_biosphere_categories
   bw2io.strategies.normalize_simapro_biosphere_names
   bw2io.strategies.normalize_units
   bw2io.strategies.remove_uncertainty_from_negative_loss_exchanges
   bw2io.strategies.remove_unnamed_parameters
   bw2io.strategies.remove_zero_amount_coproducts
   bw2io.strategies.remove_zero_amount_inputs_with_no_activity
   bw2io.strategies.set_biosphere_type
   bw2io.strategies.set_code_by_activity_hash
   bw2io.strategies.set_lognormal_loc_value
   bw2io.strategies.sp_allocate_products
   bw2io.strategies.split_exchanges
   bw2io.strategies.split_simapro_name_geo
   bw2io.strategies.strip_biosphere_exc_locations
   bw2io.strategies.tupleize_categories
   bw2io.strategies.update_ecoinvent_locations



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.link_iterable_by_fields


.. py:function:: add_activity_hash_code(data)

   Add ``code`` field to characterization factors using ``activity_hash``, if ``code`` not already present.


.. py:function:: add_cpc_classification_from_single_reference_product(db)


.. py:function:: add_database_name(db, name)

   Add database name to datasets


.. py:function:: assign_only_product_as_production(db)

   Assign only product as reference product.

   Skips datasets that already have a reference product or no production exchanges. Production exchanges must have a ``name`` and an amount.

   Will replace the following activity fields, if not already specified:

   * 'name' - name of reference product
   * 'unit' - unit of reference product
   * 'production amount' - amount of reference product



.. py:function:: assign_single_product_as_activity(db)


.. py:function:: change_electricity_unit_mj_to_kwh(db)

   Change datasets with the string ``electricity`` in their name from units of MJ to kilowatt hour.


.. py:function:: clean_integer_codes(data)

   Convert integer activity codes to strings and delete integer codes from exchanges (they can't be believed).


.. py:function:: convert_activity_parameters_to_list(data)

   Convert activity parameters from dictionary to list of dictionaries


.. py:function:: convert_uncertainty_types_to_integers(db)

   Generic number conversion function convert to floats. Return to integers.


.. py:function:: create_composite_code(db)

   Create composite code from activity and flow names


.. py:function:: csv_add_missing_exchanges_section(data)


.. py:function:: csv_drop_unknown(data)

   Drop keys whose values are `(Unknown)`.


.. py:function:: csv_numerize(data)

   Turns strings into numbers where possible


.. py:function:: csv_restore_booleans(data)

   Turn `True` and `False` into proper booleans, where possible


.. py:function:: csv_restore_tuples(data)

   Restore tuples separated by `::` string


.. py:function:: delete_exchanges_missing_activity(db)

   Delete exchanges that weren't linked correctly by ecoinvent.

   These exchanges are missing the "activityLinkId" attribute, and the flow they want to consume is not produced as the reference product of any activity. See the `known data issues <http://www.ecoinvent.org/database/ecoinvent-version-3/reports-of-changes/known-data-issues/>`__ report.



.. py:function:: delete_ghost_exchanges(db)

   Delete technosphere which can't be linked due to ecoinvent errors.

   A ghost exchange is one which links to a combination of *activity* and *flow* which aren't provided in the database.


.. py:function:: delete_integer_codes(data)

   Delete integer codes completely from extracted ecospold1 datasets


.. py:function:: delete_none_synonyms(db)


.. py:function:: drop_falsey_uncertainty_fields_but_keep_zeros(db)

   Drop fields like '' but keep zero and NaN.

   Note that this doesn't strip `False`, which behaves *exactly* like 0.



.. py:function:: drop_temporary_outdated_biosphere_flows(db)

   Drop biosphere exchanges which aren't used and are outdated


.. py:function:: drop_unlinked(db)

   This is the nuclear option - use at your own risk!


.. py:function:: drop_unlinked_cfs(data)

   Drop CFs which don't have ``input`` attribute


.. py:function:: drop_unspecified_subcategories(db)

   Drop subcategories if they are in the following:
   * ``unspecified``
   * ``(unspecified)``
   * ``''`` (empty string)
   * ``None``



.. py:function:: ensure_categories_are_tuples(db)


.. py:function:: es1_allocate_multioutput(data)

   This strategy allocates multioutput datasets to new datasets.

   This deletes the multioutput dataset, breaking any existing linking. This shouldn't be a concern, as you shouldn't link to a multioutput dataset in any case.

   Note that multiple allocations for the same product and input will result in undefined behavior.



.. py:function:: es2_assign_only_product_with_amount_as_reference_product(db)

   If a multioutput process has one product with a non-zero amount, assign that product as reference product.

   This is by default called after ``remove_zero_amount_coproducts``, which will delete the zero-amount coproducts in any case. However, we still keep the zero-amount logic in case people want to keep all coproducts.


.. py:function:: fix_ecoinvent_flows_pre35(db)


.. py:function:: fix_localized_water_flows(db)

   Change ``Water, BR`` to ``Water``.

   Biosphere flows can't have locations - locations are defined by the activity dataset.


.. py:function:: fix_unreasonably_high_lognormal_uncertainties(db, cutoff=2.5, replacement=0.25)

   Fix unreasonably high uncertainty values.

   With the default cutoff value of 2.5 and a median of 1, the 95% confidence
   interval has a high to low ratio of 20.000.


.. py:function:: fix_zero_allocation_products(db)

   Drop all inputs from allocated products which had zero allocation factors.

   The final production amount is the initial amount times the allocation factor. If this is zero, a singular technosphere matrix is created. We fix this by setting the production amount to one, and deleting all inputs.

   Does not modify datasets with more than one production exchange.


.. py:function:: link_biosphere_by_flow_uuid(db, biosphere='biosphere3')


.. py:function:: link_internal_technosphere_by_composite_code(db)

   Link internal technosphere inputs by ``code``.

   Only links to process datasets actually in the database document.


.. py:function:: link_technosphere_based_on_name_unit_location(db, external_db_name=None)

   Link technosphere exchanges based on name, unit, and location. Can't use categories because we can't reliably extract categories from SimaPro exports, only exchanges.

   If ``external_db_name``, link against a different database; otherwise link internally.


.. py:function:: link_technosphere_by_activity_hash(db, external_db_name=None, fields=None)

   Link technosphere exchanges using ``activity_hash`` function.

   If ``external_db_name``, link against a different database; otherwise link internally.

   If ``fields``, link using only certain fields.


.. py:function:: match_subcategories(data, biosphere_db_name, remove=True)

   Given a characterization with a top-level category, e.g. ``('air',)``, find all biosphere flows with the same top-level categories, and add CFs for these flows as well. Doesn't replace CFs for existing flows with multi-level categories. If ``remove``, also delete the top-level CF, but only if it is unlinked.


.. py:function:: migrate_datasets(db, migration)


.. py:function:: migrate_exchanges(db, migration)


.. py:function:: normalize_biosphere_categories(db, lcia=False)

   Normalize biosphere categories to ecoinvent 3.1 standard


.. py:function:: normalize_biosphere_names(db, lcia=False)

   Normalize biosphere flow names to ecoinvent 3.1 standard.

   Assumes that each dataset and each exchange have a ``name``. Will change names even if exchange is already linked.


.. py:function:: normalize_simapro_biosphere_categories(db)

   Normalize biosphere categories to ecoinvent standard.


.. py:function:: normalize_simapro_biosphere_names(db)

   Normalize biosphere flow names to ecoinvent standard


.. py:function:: normalize_units(db)

   Normalize units in datasets and their exchanges


.. py:function:: remove_uncertainty_from_negative_loss_exchanges(db)

   Remove uncertainty from negative lognormal exchanges.

   There are 15699 of these in ecoinvent 3.3 cutoff.

   The basic uncertainty and pedigree matrix are applied rather blindly,
   and the can produce strange net production values. It makes much more
   sense to assume that these loss factors are static.

   Only applies to exchanges which decrease net production.



.. py:function:: remove_unnamed_parameters(db)

   Remove parameters which have no name. They can't be used in formulas or referenced.


.. py:function:: remove_zero_amount_coproducts(db)

   Remove coproducts with zero production amounts from ``exchanges``


.. py:function:: remove_zero_amount_inputs_with_no_activity(db)

   Remove technosphere exchanges with amount of zero and no uncertainty.

   Input exchanges with zero amounts are the result of the ecoinvent linking algorithm, and can be safely discarded.


.. py:function:: set_biosphere_type(data)

   Set CF types to 'biosphere', to keep compatibility with LCI strategies.

   This will overwrite existing ``type`` values.


.. py:function:: set_code_by_activity_hash(db, overwrite=False)

   Use ``activity_hash`` to set dataset code.

   By default, won't overwrite existing codes, but will if ``overwrite`` is ``True``.


.. py:function:: set_lognormal_loc_value(db)

   Make sure ``loc`` value is correct for lognormal uncertainty distributions


.. py:function:: sp_allocate_products(db)

   Create a dataset from each product in a raw SimaPro dataset


.. py:function:: split_exchanges(data, filter_params, changed_attributes, allocation_factors=None)

   Split unlinked exchanges in ``data`` which satisfy ``filter_params`` into new exchanges with changed attributes.

   ``changed_attributes`` is a list of dictionaries with the attributes that should be changed.

   ``allocation_factors`` is an optional list of floats to allocate the original exchange amount to the respective copies defined in ``changed_attributes``. They don't have to sum to one. If ``allocation_factors`` are not defined, then exchanges are split equally.

   Resets uncertainty to ``UndefinedUncertainty`` (0).

   To use this function as a strategy, you will need to curry it first using ``functools.partial``.

   Example usage::

       split_exchanges(
           [
               {'exchanges': [{
                   'name': 'foo',
                   'location': 'bar',
                   'amount': 20
               }, {
                   'name': 'food',
                   'location': 'bar',
                   'amount': 12
               }]}
           ],
           {'name': 'foo'},
           [{'location': 'A'}, {'location': 'B', 'cat': 'dog'}
       ]
       >>> [
           {'exchanges': [{
               'name': 'food',
               'location': 'bar',
               'amount': 12
           }, {
               'name': 'foo',
               'location': 'A',
               'amount': 12.,
               'uncertainty_type': 0
           }, {
               'name': 'foo',
               'location': 'B',
               'amount': 8.,
               'uncertainty_type': 0,
               'cat': 'dog',
           }]}
       ]



.. py:function:: split_simapro_name_geo(db)

   Split a name like 'foo/CH U' into name and geo components.

   Sets original name to ``simapro name``.


.. py:function:: strip_biosphere_exc_locations(db)

   Biosphere flows don't have locations - if any are included they can confuse linking


.. py:function:: tupleize_categories(db)


.. py:function:: update_ecoinvent_locations(db)

   Update old ecoinvent location codes


.. py:data:: link_iterable_by_fields

   

