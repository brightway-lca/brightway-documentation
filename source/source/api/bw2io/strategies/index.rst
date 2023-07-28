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
   exiobase/index.rst
   generic/index.rst
   json_ld/index.rst
   json_ld_allocation/index.rst
   json_ld_lcia/index.rst
   lcia/index.rst
   locations/index.rst
   migrations/index.rst
   parameterization/index.rst
   simapro/index.rst
   special/index.rst
   useeio/index.rst


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
   bw2io.strategies.json_ld_add_activity_unit
   bw2io.strategies.json_ld_add_products_as_activities
   bw2io.strategies.json_ld_allocate_datasets
   bw2io.strategies.json_ld_convert_unit_to_reference_unit
   bw2io.strategies.json_ld_fix_process_type
   bw2io.strategies.json_ld_get_activities_list_from_rawdata
   bw2io.strategies.json_ld_get_normalized_exchange_locations
   bw2io.strategies.json_ld_get_normalized_exchange_units
   bw2io.strategies.json_ld_label_exchange_type
   bw2io.strategies.json_ld_lcia_add_method_metadata
   bw2io.strategies.json_ld_lcia_convert_to_list
   bw2io.strategies.json_ld_lcia_reformat_cfs_as_exchanges
   bw2io.strategies.json_ld_lcia_set_method_metadata
   bw2io.strategies.json_ld_location_name
   bw2io.strategies.json_ld_prepare_exchange_fields_for_linking
   bw2io.strategies.json_ld_remove_fields
   bw2io.strategies.json_ld_rename_metadata_fields
   bw2io.strategies.link_biosphere_by_flow_uuid
   bw2io.strategies.link_internal_technosphere_by_composite_code
   bw2io.strategies.link_iterable_by_fields
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
   bw2io.strategies.remove_random_exchanges
   bw2io.strategies.remove_uncertainty_from_negative_loss_exchanges
   bw2io.strategies.remove_unnamed_parameters
   bw2io.strategies.remove_useeio_products
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
   bw2io.strategies.update_social_flows_in_older_consequential
















































































