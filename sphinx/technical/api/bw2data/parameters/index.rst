:py:mod:`bw2data.parameters`
============================

.. py:module:: bw2data.parameters


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.parameters.ParameterBase
   bw2data.parameters.ProjectParameter
   bw2data.parameters.DatabaseParameter
   bw2data.parameters.ActivityParameter
   bw2data.parameters.ParameterizedExchange
   bw2data.parameters.Group
   bw2data.parameters.GroupDependency
   bw2data.parameters.ParameterManager



Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.parameters.get_new_symbols
   bw2data.parameters.alter_parameter_formula



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2data.parameters.clean
   bw2data.parameters.nonempty
   bw2data.parameters.AUTOUPDATE_TRIGGER
   bw2data.parameters._CROSSDATABASE_TEMPLATE
   bw2data.parameters.CROSSDATASE_INSERT_TRIGGER
   bw2data.parameters.CROSSDATASE_UPDATE_TRIGGER
   bw2data.parameters._CROSSGROUP_TEMPLATE
   bw2data.parameters.CROSSGROUP_INSERT_TRIGGER
   bw2data.parameters.CROSSGROUP_UPDATE_TRIGGER
   bw2data.parameters._CLOSURE_TEMPLATE
   bw2data.parameters.GD_INSERT_TRIGGER
   bw2data.parameters.GD_UPDATE_TRIGGER
   bw2data.parameters._PE_GROUP_TEMPLATE
   bw2data.parameters.PE_INSERT_TRIGGER
   bw2data.parameters.PE_UPDATE_TRIGGER
   bw2data.parameters.parameters


.. py:data:: clean
   

   

.. py:data:: nonempty
   

   Autoupdate `updated` field in Group when parameters change

.. py:data:: AUTOUPDATE_TRIGGER
   :annotation: = Multiline-String

    .. raw:: html

        <details><summary>Show Value</summary>

    .. code-block:: text
        :linenos:

        CREATE TRIGGER IF NOT EXISTS {table}_{action}_trigger AFTER {action} ON {table} BEGIN
            UPDATE group_table SET updated = datetime('now') WHERE name = {name};
        END;

    .. raw:: html

        </details>

   Activity parameter groups can't cross databases

.. py:data:: _CROSSDATABASE_TEMPLATE
   :annotation: = Multiline-String

    .. raw:: html

        <details><summary>Show Value</summary>

    .. code-block:: text
        :linenos:

        CREATE TRIGGER IF NOT EXISTS ap_crossdatabase_{action} BEFORE {action} ON activityparameter BEGIN
            SELECT CASE WHEN
                ((SELECT COUNT(*) FROM activityparameter WHERE "group" = NEW."group") > 0)
            AND (NEW.database NOT IN (SELECT DISTINCT "database" FROM activityparameter where "group" = NEW."group"))
            THEN RAISE(ABORT,'Cross database group')
            END;
        END;

    .. raw:: html

        </details>

   

.. py:data:: CROSSDATASE_INSERT_TRIGGER
   

   

.. py:data:: CROSSDATASE_UPDATE_TRIGGER
   

   Activities can't be in multiple activity parameter groups

.. py:data:: _CROSSGROUP_TEMPLATE
   :annotation: = Multiline-String

    .. raw:: html

        <details><summary>Show Value</summary>

    .. code-block:: text
        :linenos:

        CREATE TRIGGER IF NOT EXISTS ap_crossgroup_{action} BEFORE {action} ON activityparameter BEGIN
            SELECT CASE WHEN EXISTS (SELECT * FROM activityparameter AS a WHERE
                    a.database = NEW.database AND
                    a.code = NEW.code AND
                    a."group" != NEW."group")
            THEN RAISE(ABORT,'Cross group activity')
            END;
        END;

    .. raw:: html

        </details>

   

.. py:data:: CROSSGROUP_INSERT_TRIGGER
   

   

.. py:data:: CROSSGROUP_UPDATE_TRIGGER
   

   No circular dependences in activity parameter group dependencies

.. py:data:: _CLOSURE_TEMPLATE
   :annotation: = Multiline-String

    .. raw:: html

        <details><summary>Show Value</summary>

    .. code-block:: text
        :linenos:

        CREATE TRIGGER IF NOT EXISTS gd_circular_{action} BEFORE {action} ON groupdependency BEGIN
            SELECT CASE WHEN EXISTS (SELECT * FROM groupdependency AS g WHERE g."group" = NEW.depends AND g.depends = NEW."group")
            THEN RAISE(ABORT,'Circular dependency')
            END;
        END;


    .. raw:: html

        </details>

   

.. py:data:: GD_INSERT_TRIGGER
   

   

.. py:data:: GD_UPDATE_TRIGGER
   

   Parameterized exchange groups must be in activityparameters table

.. py:data:: _PE_GROUP_TEMPLATE
   :annotation: = Multiline-String

    .. raw:: html

        <details><summary>Show Value</summary>

    .. code-block:: text
        :linenos:

        CREATE TRIGGER IF NOT EXISTS pe_group_{action} BEFORE {action} ON parameterizedexchange BEGIN
            SELECT CASE WHEN
                ((SELECT COUNT(*) FROM activityparameter WHERE "group" = NEW."group") < 1)
            THEN RAISE(ABORT,'Missing activity parameter group')
            END;
        END;


    .. raw:: html

        </details>

   

.. py:data:: PE_INSERT_TRIGGER
   

   

.. py:data:: PE_UPDATE_TRIGGER
   

   

.. py:class:: ParameterBase

   Bases: :py:obj:`peewee.Model`

   .. py:attribute:: __repr__
      

      

   .. py:method:: __lt__(other)


   .. py:method:: create_table()
      :classmethod:


   .. py:method:: expire_downstream(group)
      :staticmethod:

      Expire any activity parameters that depend on this group



.. py:class:: ProjectParameter

   Bases: :py:obj:`ParameterBase`

   Parameter set for a project. Group name is 'project'.

   Columns:

       * name: str, unique
       * formula: str, optional
       * amount: float, optional
       * data: object, optional. Used for any other metadata.

   Note that there is no magic for reading and writing to ``data`` (unlike ``Activity`` objects) - it must be used directly.


   .. py:property:: dict

      Parameter data as a standardized dictionary

   .. py:attribute:: name
      

      

   .. py:attribute:: formula
      

      

   .. py:attribute:: amount
      

      

   .. py:attribute:: data
      

      

   .. py:attribute:: _old_name
      :annotation: = 'project'

      

   .. py:attribute:: _new_name
      :annotation: = 'project'

      

   .. py:attribute:: _db_table
      :annotation: = projectparameter

      

   .. py:method:: __str__()


   .. py:method:: save(*args, **kwargs)


   .. py:method:: load(group=None)
      :staticmethod:

      Return dictionary of parameter data with names as keys and ``.dict()`` as values.


   .. py:method:: static(ignored='project', only=None)
      :staticmethod:

      Get dictionary of ``{name: amount}`` for all project parameters.

      ``only`` restricts returned names to ones found in ``only``. ``ignored`` included for API compatibility with other ``recalculate`` methods.


   .. py:method:: expired()
      :staticmethod:

      Return boolean - is this group expired?


   .. py:method:: recalculate(ignored=None)
      :staticmethod:

      Recalculate all parameters.

      ``ignored`` included for API compatibility with other ``recalculate`` methods - it will really be ignored.


   .. py:method:: dependency_chain()
      :staticmethod:

      Determine if ```ProjectParameter`` parameters have dependencies
      within the group.

      Returns:

      .. code-block:: python

          [
              {
                  'kind': 'project',
                  'group': 'project',
                  'names': set of variables names
              }
          ]



   .. py:method:: is_dependency_within_group(name)
      :staticmethod:


   .. py:method:: is_deletable()

      Perform a test to see if the current parameter can be deleted.


   .. py:method:: update_formula_parameter_name(old, new)
      :classmethod:

      Performs an update of the formula of relevant parameters.

      NOTE: Make sure to wrap this in an .atomic() statement!



.. py:class:: DatabaseParameter

   Bases: :py:obj:`ParameterBase`

   Parameter set for a database. Group name is the name of the database.

   Columns:

       * database: str
       * name: str, unique within a database
       * formula: str, optional
       * amount: float, optional
       * data: object, optional. Used for any other metadata.

   Note that there is no magic for reading and writing to ``data`` (unlike ``Activity`` objects) - it must be used directly.


   .. py:class:: Meta

      .. py:attribute:: indexes
         :annotation: = [[['database', 'name'], True]]

         

      .. py:attribute:: constraints
         

         


   .. py:property:: dict

      Parameter data as a standardized dictionary

   .. py:attribute:: database
      

      

   .. py:attribute:: name
      

      

   .. py:attribute:: formula
      

      

   .. py:attribute:: amount
      

      

   .. py:attribute:: data
      

      

   .. py:attribute:: _old_name
      :annotation: = OLD.database

      

   .. py:attribute:: _new_name
      :annotation: = NEW.database

      

   .. py:attribute:: _db_table
      :annotation: = databaseparameter

      

   .. py:method:: __str__()


   .. py:method:: load(database)
      :staticmethod:

      Return dictionary of parameter data with names as keys and ``.dict()`` as values.


   .. py:method:: expired(database)
      :staticmethod:

      Return boolean - is this group expired?


   .. py:method:: static(database, only=None)
      :staticmethod:

      Return dictionary of {name: amount} for database group.


   .. py:method:: recalculate(database)
      :staticmethod:

      Recalculate all database parameters for ``database``, if expired.


   .. py:method:: dependency_chain(group, include_self=False)
      :staticmethod:

      Find where each missing variable is defined in dependency chain.

      If ``include_self`` is True will include parameters within the group as possible dependencies

      Returns:

      .. code-block:: python

          [
              {
                  'kind': one of 'project', 'database', 'activity',
                  'group': group name,
                  'names': set of variables names
              }
          ]



   .. py:method:: is_dependency_within_group(name, database)
      :staticmethod:


   .. py:method:: save(*args, **kwargs)

      Save this model instance


   .. py:method:: is_deletable()

      Perform a test to see if the current parameter can be deleted.


   .. py:method:: is_dependent_on(name)
      :staticmethod:

      Test if any database parameters are dependent on the given
      project parameter name.


   .. py:method:: update_formula_project_parameter_name(old, new)
      :classmethod:

      Performs an update of the formula of relevant parameters.

      This method specifically targets project parameters used in database
      formulas


   .. py:method:: update_formula_database_parameter_name(old, new)
      :classmethod:

      Performs an update of the formula of relevant parameters.

      This method specifically targets database parameters used in database
      formulas



.. py:class:: ActivityParameter

   Bases: :py:obj:`ParameterBase`

   Parameter set for a group of activities.

   Columns:

       * group: str
       * database: str
       * code: str. Code and database define the linked activity for this parameter.
       * name: str, unique within a group
       * formula: str, optional
       * amount: float, optional
       * data: object, optional. Used for any other metadata.

   Activities can only have parameters in one group. Group names cannot be 'project' or the name of any existing database.

   Activity parameter groups can depend on other activity parameter groups, so that a formula in group "a" can depend on a variable in group "b". This dependency information is stored in ``Group.order`` - in our small example, we could define the following:

   .. code-block:: python

       a = Group.get(name="a")
       a.order = ["b", "c"]
       a.save()

   In this case, a variable not found in "a" would be searched for in "b" and then "c", in that order. Database and then project parameters are also implicitly included at the end of ``Group.order``.

   Note that there is no magic for reading and writing to ``data`` (unlike ``Activity`` objects) - it must be used directly.


   .. py:class:: Meta

      .. py:attribute:: indexes
         :annotation: = [[['group', 'name'], True]]

         

      .. py:attribute:: constraints
         

         


   .. py:property:: dict

      Parameter data as a standardized dictionary

   .. py:attribute:: group
      

      

   .. py:attribute:: database
      

      

   .. py:attribute:: code
      

      

   .. py:attribute:: name
      

      

   .. py:attribute:: formula
      

      

   .. py:attribute:: amount
      

      

   .. py:attribute:: data
      

      

   .. py:attribute:: _old_name
      :annotation: = OLD."group"

      

   .. py:attribute:: _new_name
      :annotation: = NEW."group"

      

   .. py:attribute:: _db_table
      :annotation: = activityparameter

      

   .. py:method:: __str__()


   .. py:method:: load(group)
      :staticmethod:

      Return dictionary of parameter data with names as keys and ``.dict()`` as values.


   .. py:method:: static(group, only=None, full=False)
      :staticmethod:

      Get dictionary of ``{name: amount}`` for parameters defined in ``group``.

      ``only`` restricts returned names to ones found in ``only``. ``full`` returns all names, including those found in the dependency chain.


   .. py:method:: _static_dependencies(group)
      :staticmethod:

      Get dictionary of ``{name: amount}`` for all variables defined in dependency chain.

      Be careful! This could have variables which overlap with local variable names. Designed for internal use.


   .. py:method:: insert_dummy(group, activity)
      :staticmethod:


   .. py:method:: expired(group)
      :staticmethod:

      Return boolean - is this group expired?


   .. py:method:: dependency_chain(group, include_self=False)
      :staticmethod:

      Find where each missing variable is defined in dependency chain.

      Will also load in all parameters needed to resolve the ``ParameterizedExchanges`` for this group.

      If ``include_self`` is True will include parameters within the group as possible dependencies

      Returns:

      .. code-block:: python

          [
              {
                  'kind': one of 'project', 'database', 'activity',
                  'group': group name,
                  'names': set of variables names
              }
          ]



   .. py:method:: is_dependency_within_group(name, group, include_order=False)
      :staticmethod:

      Determine if the given parameter `name` is a dependency within
      the given activity `group`.

      The optional ``include_order`` parameter will include dependencies
      from groups found in the the ``Group``.`order` field.


   .. py:method:: recalculate(group)
      :staticmethod:

      Recalculate all values for activity parameters in this group, and update their underlying `Activity` and `Exchange` values.


   .. py:method:: recalculate_exchanges(group)
      :staticmethod:

      Recalculate formulas for all parameterized exchanges in group ``group``.


   .. py:method:: save(*args, **kwargs)

      Save this model instance


   .. py:method:: is_deletable()

      Perform a test to see if the current parameter can be deleted.


   .. py:method:: is_dependent_on(name, group)
      :staticmethod:

      Test if any activity parameters are dependent on the given
      parameter name from the given group.


   .. py:method:: update_formula_project_parameter_name(old, new)
      :classmethod:

      Performs an update of the formula of relevant parameters.

      This method specifically targets project parameters used in activity
      formulas


   .. py:method:: update_formula_database_parameter_name(old, new)
      :classmethod:

      Performs an update of the formula of relevant parameters.

      This method specifically targets database parameters used in activity
      formulas


   .. py:method:: update_formula_activity_parameter_name(old, new, include_order=False)
      :classmethod:

      Performs an update of the formula of relevant parameters.

      This method specifically targets activity parameters used in activity
      formulas


   .. py:method:: create_table()
      :classmethod:



.. py:class:: ParameterizedExchange

   Bases: :py:obj:`peewee.Model`

   .. py:attribute:: group
      

      

   .. py:attribute:: exchange
      

      

   .. py:attribute:: formula
      

      

   .. py:method:: create_table()
      :classmethod:


   .. py:method:: save(*args, **kwargs)


   .. py:method:: load(group)
      :staticmethod:

      Return dictionary of parameter data with names as keys and ``.dict()`` as values.


   .. py:method:: recalculate(group)
      :staticmethod:

      Shortcut for ``ActivityParameter.recalculate_exchanges``.



.. py:class:: Group

   Bases: :py:obj:`peewee.Model`

   .. py:class:: Meta

      .. py:attribute:: table_name
         :annotation: = group_table

         


   .. py:attribute:: name
      

      

   .. py:attribute:: fresh
      

      

   .. py:attribute:: updated
      

      

   .. py:attribute:: order
      

      

   .. py:method:: expire()

      Set ``fresh`` to ``False``


   .. py:method:: freshen()

      Set ``fresh`` to ``True``


   .. py:method:: save(*args, **kwargs)

      Save this model instance. Will remove 'project' and database names from ``order``.


   .. py:method:: purge_order()



.. py:class:: GroupDependency

   Bases: :py:obj:`peewee.Model`

   .. py:class:: Meta

      .. py:attribute:: indexes
         :annotation: = [[['group', 'depends'], True]]

         

      .. py:attribute:: constraints
         

         


   .. py:attribute:: group
      

      

   .. py:attribute:: depends
      

      

   .. py:method:: save(*args, **kwargs)


   .. py:method:: create_table()
      :classmethod:



.. py:class:: ParameterManager

   .. py:method:: add_to_group(group, activity)

      Add `activity` to group.

      Creates ``group`` if needed.

      Will delete any existing ``ActivityParameter`` for this activity.

      Deletes `parameters` key from `Activity`.


   .. py:method:: remove_from_group(group, activity, restore_amounts=True)

      Remove `activity` from `group`.

      Will delete any existing ``ActivityParameter`` and ``ParameterizedExchange`` for this activity.

      Restores `parameters` key to this `Activity`.
      By default, restores `amount` value of each parameterized exchange
      of the `Activity` to the original value. This can be avoided by using
      the ``restore_amounts`` parameter.



   .. py:method:: add_exchanges_to_group(group, activity)

      Add exchanges with formulas from ``activity`` to ``group``.

      Every exchange with a formula field will have its original `amount`
      value stored as `original_amount`. This original value can be
      restored when parameterization is removed from the activity with
      `remove_from_group`.



   .. py:method:: remove_exchanges_from_group(group, activity, restore_original=True)

      Takes a group and activity and removes all ``ParameterizedExchange``
      objects from the group.

      The ``restore_original`` parameter determines if the original amount
      values will be restored to those exchanges where a formula was used
      to alter the amount.



   .. py:method:: new_project_parameters(data, overwrite=True)

      Efficiently and correctly enter multiple parameters.

      Will overwrite existing project parameters with the same name, unless ``overwrite`` is false, in which case a ``ValueError`` is raised.

      ``data`` should be a list of dictionaries:

      .. code-block:: python

          [{
              'name': name of variable (unique),
              'amount': numeric value of variable (optional),
              'formula': formula in Python as string (optional),
              optional keys like uncertainty, etc. (no limitations)
          }]



   .. py:method:: new_database_parameters(data, database, overwrite=True)

      Efficiently and correctly enter multiple parameters. Deletes **all** existing database parameters for this database.

      Will overwrite existing database parameters with the same name, unless ``overwrite`` is false, in which case a ``ValueError`` is raised.

      ``database`` should be an existing database. ``data`` should be a list of dictionaries:

      .. code-block:: python

          [{
              'name': name of variable (unique),
              'amount': numeric value of variable (optional),
              'formula': formula in Python as string (optional),
              optional keys like uncertainty, etc. (no limitations)
          }]



   .. py:method:: new_activity_parameters(data, group, overwrite=True)

      Efficiently and correctly enter multiple parameters. Deletes **all** existing activity parameters for this group.

      Will overwrite existing parameters in the same group with the same name, unless ``overwrite`` is false, in which case a ``ValueError`` is raised.

      Input parameters must refer to a single, existing database.

      ``group`` is the group name; will be autocreated if necessary. ``data`` should be a list of dictionaries:

      .. code-block:: python

          [{
              'name': name of variable (unique),
              'database': activity database,
              'code': activity code,
              'amount': numeric value of variable (optional),
              'formula': formula in Python as string (optional),
              optional keys like uncertainty, etc. (no limitations)
          }]



   .. py:method:: rename_project_parameter(parameter, new_name, update_dependencies=False)

      Given a parameter and a new name, safely update the parameter.

      Will raise a TypeError if the given parameter is of the incorrect type.
      Will raise a ValueError if other parameters depend on the given one
      and ``update_dependencies`` is False.



   .. py:method:: rename_database_parameter(parameter, new_name, update_dependencies=False)

      Given a parameter and a new name, safely update the parameter.

      Will raise a TypeError if the given parameter is of the incorrect type.
      Will raise a ValueError if other parameters depend on the given one
      and ``update_dependencies`` is False.



   .. py:method:: rename_activity_parameter(parameter, new_name, update_dependencies=False)

      Given a parameter and a new name, safely update the parameter.

      Will raise a TypeError if the given parameter is of the incorrect type.
      Will raise a ValueError if other parameters depend on the given one
      and ``update_dependencies`` is False.



   .. py:method:: recalculate()

      Recalculate all expired project, database, and activity parameters, as well as exchanges.


   .. py:method:: __len__()


   .. py:method:: __repr__()

      Return repr(self).



.. py:data:: parameters
   

   

.. py:function:: get_new_symbols(data, context=None)


.. py:function:: alter_parameter_formula(parameter, old, new)

   Replace the `old` part with `new` in the formula field and return
   the parameter itself.


