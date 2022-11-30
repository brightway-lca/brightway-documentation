:py:mod:`tests.parameters`
==========================

.. py:module:: tests.parameters


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   tests.parameters.test_project_parameters
   tests.parameters.test_project_parameter_autocreate_group
   tests.parameters.test_expire_downstream
   tests.parameters.test_project_parameters_ordering
   tests.parameters.test_project_parameters_dict
   tests.parameters.test_project_parameters_load
   tests.parameters.test_project_parameters_static
   tests.parameters.test_project_parameters_expired
   tests.parameters.test_project_parameters_recalculate
   tests.parameters.test_project_parameters_expire_downstream
   tests.parameters.test_project_autoupdate_triggers
   tests.parameters.test_project_name_uniqueness
   tests.parameters.test_project_parameter_dependency_chain
   tests.parameters.test_project_parameter_dependency_chain_missing
   tests.parameters.test_project_parameter_depend_within_group
   tests.parameters.test_project_parameter_is_deletable
   tests.parameters.test_project_parameter_is_not_deletable_project
   tests.parameters.test_project_parameter_is_not_deletable_database
   tests.parameters.test_project_parameter_is_not_deletable_activity
   tests.parameters.test_project_parameter_formula_update
   tests.parameters.test_create_database_parameters
   tests.parameters.test_database_parameters_group_autocreated
   tests.parameters.test_database_parameters_expired
   tests.parameters.test_database_parameters_dict
   tests.parameters.test_database_parameters_load
   tests.parameters.test_database_parameters_static
   tests.parameters.test_database_parameters_check
   tests.parameters.test_database_autoupdate_triggers
   tests.parameters.test_database_uniqueness_constraint
   tests.parameters.test_database_parameter_cross_database_constraint
   tests.parameters.test_update_database_parameters
   tests.parameters.test_database_parameter_dependency_chain
   tests.parameters.test_database_parameter_dependency_chain_missing
   tests.parameters.test_database_parameter_dependency_chain_include_self
   tests.parameters.test_database_parameter_depend_within_group
   tests.parameters.test_database_parameter_is_deletable
   tests.parameters.test_database_parameter_is_not_deletable_database
   tests.parameters.test_database_parameter_is_not_deletable_activity
   tests.parameters.test_database_parameter_is_dependent_on
   tests.parameters.test_database_parameter_formula_update_project
   tests.parameters.test_database_parameter_formula_update_database
   tests.parameters.test_create_parameterized_exchange_missing_group
   tests.parameters.test_create_parameterized_exchange
   tests.parameters.test_create_parameterized_exchange_nonunique
   tests.parameters.chain
   tests.parameters.test_create_activity_parameter
   tests.parameters.test_activity_parameters_group_autocreated
   tests.parameters.test_activity_parameter_expired
   tests.parameters.test_activity_parameter_dict
   tests.parameters.test_activity_parameter_load
   tests.parameters.test_activity_parameter_static
   tests.parameters.test_activity_parameter_recalculate_shortcut
   tests.parameters.test_activity_parameter_dependency_chain
   tests.parameters.test_activity_parameter_dependency_chain_missing
   tests.parameters.test_activity_parameter_dependency_chain_includes_exchanges
   tests.parameters.test_activity_parameter_dependency_chain_include_self
   tests.parameters.test_activity_parameter_dependency_chain_include_self_exchanges
   tests.parameters.test_activity_parameter_depend_within_group
   tests.parameters.test_activity_parameter_depend_within_group_include
   tests.parameters.test_activity_parameter_dummy
   tests.parameters.test_activity_parameter_multiple_dummies
   tests.parameters.test_activity_parameter_static_dependencies
   tests.parameters.test_activity_parameter_recalculate_exchanges
   tests.parameters.test_pe_no_activities_parameter_group_error
   tests.parameters.test_recalculate_exchanges_no_activities_parameters
   tests.parameters.test_activity_parameter_recalculate
   tests.parameters.test_activity_parameter_is_deletable
   tests.parameters.test_activity_parameter_is_dependent_on
   tests.parameters.test_activity_parameter_formula_update_project
   tests.parameters.test_activity_parameter_formula_update_database
   tests.parameters.test_activity_parameter_formula_update_activity
   tests.parameters.test_activity_parameter_formula_update_activity_include
   tests.parameters.test_activity_parameter_crossdatabase_triggers
   tests.parameters.test_activity_parameter_crossgroup_triggers
   tests.parameters.test_activity_parameter_autoupdate_triggers
   tests.parameters.test_activity_parameter_checks_uniqueness_constraints
   tests.parameters.test_activity_parameter_checks
   tests.parameters.test_group
   tests.parameters.test_group_purging
   tests.parameters.test_group_dependency
   tests.parameters.test_group_dependency_save_checks
   tests.parameters.test_group_dependency_constraints
   tests.parameters.test_group_dependency_circular
   tests.parameters.test_group_dependency_override
   tests.parameters.test_parameters_new_project_parameters_uniqueness
   tests.parameters.test_parameters_new_project_parameters
   tests.parameters.test_parameters_new_project_parameters_no_overwrite
   tests.parameters.test_parameters_repr
   tests.parameters.test_parameters_recalculate
   tests.parameters.test_parameters_new_database_parameters
   tests.parameters.test_parameters_new_database_parameters_no_overwrite
   tests.parameters.test_parameters_new_activity_parameters_errors
   tests.parameters.test_parameters_new_activity_parameters
   tests.parameters.test_parameters_new_activity_parameters_no_overlap
   tests.parameters.test_parameters_rename_project_parameter
   tests.parameters.test_parameters_rename_project_parameter_incorrect_type
   tests.parameters.test_parameters_rename_project_parameter_dependencies
   tests.parameters.test_parameters_rename_project_parameter_dependencies_fail
   tests.parameters.test_parameters_rename_project_parameter_dependencies_full
   tests.parameters.test_parameters_rename_database_parameter
   tests.parameters.test_parameters_rename_database_parameter_dependencies
   tests.parameters.test_parameters_rename_activity_parameter
   tests.parameters.test_parameters_rename_activity_parameter_dependencies
   tests.parameters.test_parameters_rename_activity_parameter_group_exchange
   tests.parameters.test_parameters_rename_activity_parameter_order_exchange
   tests.parameters.test_parameters_add_to_group_empty
   tests.parameters.test_parameters_add_to_group
   tests.parameters.test_parameters_remove_from_group
   tests.parameters.test_parameters_save_restore_exchange_amount
   tests.parameters.test_parameters_save_keep_changed_exchange_amount



Attributes
~~~~~~~~~~

.. autoapisummary::

   tests.parameters.uuid4hex


.. py:data:: uuid4hex
   

   

.. py:function:: test_project_parameters()


.. py:function:: test_project_parameter_autocreate_group()


.. py:function:: test_expire_downstream()


.. py:function:: test_project_parameters_ordering()


.. py:function:: test_project_parameters_dict()


.. py:function:: test_project_parameters_load()


.. py:function:: test_project_parameters_static()


.. py:function:: test_project_parameters_expired()


.. py:function:: test_project_parameters_recalculate()


.. py:function:: test_project_parameters_expire_downstream()


.. py:function:: test_project_autoupdate_triggers()


.. py:function:: test_project_name_uniqueness()


.. py:function:: test_project_parameter_dependency_chain()


.. py:function:: test_project_parameter_dependency_chain_missing()


.. py:function:: test_project_parameter_depend_within_group()


.. py:function:: test_project_parameter_is_deletable()

   Project parameters can be deleted if they are no dependencies.


.. py:function:: test_project_parameter_is_not_deletable_project()


.. py:function:: test_project_parameter_is_not_deletable_database()


.. py:function:: test_project_parameter_is_not_deletable_activity()


.. py:function:: test_project_parameter_formula_update()

   Update formulas only where the name of the parameter is an exact match.


.. py:function:: test_create_database_parameters()


.. py:function:: test_database_parameters_group_autocreated()


.. py:function:: test_database_parameters_expired()


.. py:function:: test_database_parameters_dict()


.. py:function:: test_database_parameters_load()


.. py:function:: test_database_parameters_static()


.. py:function:: test_database_parameters_check()


.. py:function:: test_database_autoupdate_triggers()


.. py:function:: test_database_uniqueness_constraint()


.. py:function:: test_database_parameter_cross_database_constraint()

   Database parameters cannot use parameters on other databases.


.. py:function:: test_update_database_parameters()


.. py:function:: test_database_parameter_dependency_chain()


.. py:function:: test_database_parameter_dependency_chain_missing()


.. py:function:: test_database_parameter_dependency_chain_include_self()


.. py:function:: test_database_parameter_depend_within_group()


.. py:function:: test_database_parameter_is_deletable()

   Database parameters can be deleted if they are no dependencies.


.. py:function:: test_database_parameter_is_not_deletable_database()


.. py:function:: test_database_parameter_is_not_deletable_activity()


.. py:function:: test_database_parameter_is_dependent_on()

   Databases parameters can be dependent on project parameters.


.. py:function:: test_database_parameter_formula_update_project()

   Update formulas of database parameters, only update the formulas
   where the actual ProjectParameter is referenced.


.. py:function:: test_database_parameter_formula_update_database()

   Update formulas of database parameters, only update the formulas
   where the actual DatabaseParameter is referenced.


.. py:function:: test_create_parameterized_exchange_missing_group()


.. py:function:: test_create_parameterized_exchange()


.. py:function:: test_create_parameterized_exchange_nonunique()


.. py:function:: chain()


.. py:function:: test_create_activity_parameter()


.. py:function:: test_activity_parameters_group_autocreated()


.. py:function:: test_activity_parameter_expired()


.. py:function:: test_activity_parameter_dict()


.. py:function:: test_activity_parameter_load()


.. py:function:: test_activity_parameter_static(chain)


.. py:function:: test_activity_parameter_recalculate_shortcut()


.. py:function:: test_activity_parameter_dependency_chain(chain)


.. py:function:: test_activity_parameter_dependency_chain_missing(chain)

   Use unknown parameter 'K' in formula to test for MissingName error.


.. py:function:: test_activity_parameter_dependency_chain_includes_exchanges(chain)


.. py:function:: test_activity_parameter_dependency_chain_include_self(chain)

   Out of the parameters 'D' and 'F' in group 'A', only 'D' counts
   as a dependency for group 'A'.

   This means that 'F' can be freely deleted, after which 'D' is no longer
   a dependency for group 'A' (as 'D' was a dependency of 'F') and can now
   also be deleted.


.. py:function:: test_activity_parameter_dependency_chain_include_self_exchanges(chain)

   Out of the parameters 'J' and 'H' in group 'G', only 'H' counts
   as a dependency as 'J' is not used by either 'H' or by any exchanges.


.. py:function:: test_activity_parameter_depend_within_group(chain)

   When considering only dependencies within the given group. 'D' is
   a dependency within the group 'A', while 'F' is not.


.. py:function:: test_activity_parameter_depend_within_group_include(chain)

   The 'J' parameter in group 'G' depends on the 'F' parameter in group
   'A'. 'F' doesn't exist within the 'G' group but is instead linked to the
   'J' parameter through the 'G' group order.


.. py:function:: test_activity_parameter_dummy()


.. py:function:: test_activity_parameter_multiple_dummies()


.. py:function:: test_activity_parameter_static_dependencies(chain)


.. py:function:: test_activity_parameter_recalculate_exchanges()


.. py:function:: test_pe_no_activities_parameter_group_error()


.. py:function:: test_recalculate_exchanges_no_activities_parameters()


.. py:function:: test_activity_parameter_recalculate()


.. py:function:: test_activity_parameter_is_deletable(chain)

   An activity parameter is deletable if it is not a dependency of another
   activity parameter.


.. py:function:: test_activity_parameter_is_dependent_on(chain)

   An activity parameter can be dependent on any other type of parameter.


.. py:function:: test_activity_parameter_formula_update_project(chain)


.. py:function:: test_activity_parameter_formula_update_database(chain)


.. py:function:: test_activity_parameter_formula_update_activity(chain)


.. py:function:: test_activity_parameter_formula_update_activity_include(chain)


.. py:function:: test_activity_parameter_crossdatabase_triggers()


.. py:function:: test_activity_parameter_crossgroup_triggers()


.. py:function:: test_activity_parameter_autoupdate_triggers()


.. py:function:: test_activity_parameter_checks_uniqueness_constraints()


.. py:function:: test_activity_parameter_checks()


.. py:function:: test_group()


.. py:function:: test_group_purging()


.. py:function:: test_group_dependency()


.. py:function:: test_group_dependency_save_checks()


.. py:function:: test_group_dependency_constraints()


.. py:function:: test_group_dependency_circular()


.. py:function:: test_group_dependency_override()

   GroupDependency can be overridden by having a parameter with the same
   name within the group.


.. py:function:: test_parameters_new_project_parameters_uniqueness()


.. py:function:: test_parameters_new_project_parameters()


.. py:function:: test_parameters_new_project_parameters_no_overwrite()


.. py:function:: test_parameters_repr()


.. py:function:: test_parameters_recalculate()


.. py:function:: test_parameters_new_database_parameters()


.. py:function:: test_parameters_new_database_parameters_no_overwrite()


.. py:function:: test_parameters_new_activity_parameters_errors()


.. py:function:: test_parameters_new_activity_parameters()


.. py:function:: test_parameters_new_activity_parameters_no_overlap()


.. py:function:: test_parameters_rename_project_parameter()

   Project parameters can be renamed.


.. py:function:: test_parameters_rename_project_parameter_incorrect_type()


.. py:function:: test_parameters_rename_project_parameter_dependencies()

   Updating downstream parameters will update all relevant formulas
   to use the new name for the parameter.


.. py:function:: test_parameters_rename_project_parameter_dependencies_fail()

   An exception is raised if rename is attempted without updating
   downstream if other parameters depend on that parameter.


.. py:function:: test_parameters_rename_project_parameter_dependencies_full(chain)

   Updating downstream parameters will update all relevant formulas
   to use the new name for the parameter.

   Parameter amounts do no change as only the name is altered.


.. py:function:: test_parameters_rename_database_parameter()


.. py:function:: test_parameters_rename_database_parameter_dependencies(chain)


.. py:function:: test_parameters_rename_activity_parameter(chain)


.. py:function:: test_parameters_rename_activity_parameter_dependencies(chain)


.. py:function:: test_parameters_rename_activity_parameter_group_exchange()

   Rename 'D' from group 'A' updates ParameterizedExchange and
   underlying exchange.


.. py:function:: test_parameters_rename_activity_parameter_order_exchange()

   Rename 'D' from group 'A' updates ParameterizedExchange and
   underlying exchange in group 'G'


.. py:function:: test_parameters_add_to_group_empty()


.. py:function:: test_parameters_add_to_group()


.. py:function:: test_parameters_remove_from_group()


.. py:function:: test_parameters_save_restore_exchange_amount()

   The original amount of the exchange is restored when it is no
   longer parameterized.


.. py:function:: test_parameters_save_keep_changed_exchange_amount()


