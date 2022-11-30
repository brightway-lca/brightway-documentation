:py:mod:`bw2io.importers.base_lci`
==================================

.. py:module:: bw2io.importers.base_lci


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.importers.base_lci.LCIImporter




.. py:class:: LCIImporter(db_name)

   Bases: :py:obj:`bw2io.importers.base.ImportBase`

   Base class for format-specific importers.

   Defines workflow for applying strategies.

   Takes a database name (string) as initialization parameter.


   .. py:property:: all_linked


   .. py:attribute:: format
      :annotation: = Generic LCIImporter

      

   .. py:attribute:: project_parameters
      

      

   .. py:attribute:: database_parameters
      

      

   .. py:attribute:: metadata
      

      

   .. py:method:: statistics(print_stats=True)


   .. py:method:: write_project_parameters(data=None, delete_existing=True)

      Write global parameters to ``ProjectParameter`` database table.

      ``delete_existing`` controls whether new parameters will delete_existing existing parameters, or just update values. The ``name`` field is used to determine if a parameter exists.

      ``data`` should be a list of dictionaries (``self.project_parameters`` is used by default):

      .. code-block:: python

          [{
              'name': name of variable (unique),
              'amount': numeric value of variable (optional),
              'formula': formula in Python as string (optional),
              optional keys like uncertainty, etc. (no limitations)
          }]



   .. py:method:: write_database_parameters(activate_parameters=False, delete_existing=True)


   .. py:method:: _prepare_activity_parameters(data=None, delete_existing=True)


   .. py:method:: _write_activity_parameters(activity_parameters)


   .. py:method:: write_database(data=None, delete_existing=True, backend=None, activate_parameters=False, db_name=None, **kwargs)

      Write data to a ``Database``.

      All arguments are optional, and are normally not specified.

      ``delete_existing`` effects both the existing database (it will be emptied prior to writing if True, which is the default), and, if ``activate_parameters`` is True, existing database and activity parameters. Database parameters will only be deleted if the import data specifies a new set of database parameters (i.e. ``database_parameters`` is not ``None``) - the same is true for activity parameters. If you need finer-grained control, please use the ``DatabaseParameter``, etc. objects directly.

      :param \* *data*: The data to write to the ``Database``. Default is ``self.data``.
      :type \* *data*: dict, optional
      :param \* *delete_existing*: See above.
      :type \* *delete_existing*: bool, default ``True``
      :param \* *activate_parameters*:
      :type \* *activate_parameters*: bool, default ``False``
      :param \* *backend*: Storage backend to use when creating ``Database``. Default is the default backend.
      :type \* *backend*: string, optional

      :returns: ``Database`` instance.


   .. py:method:: write_excel(only_unlinked=False, only_names=False)

      Write database information to a spreadsheet.

      If ``only_unlinked``, then only write unlinked exchanges.

      If ``only_names``, then write only activity names, no exchange data.

      Returns the filepath to the spreadsheet file.



   .. py:method:: match_database(db_name=None, fields=None, ignore_categories=False, relink=False, kind=None)

      Match current database against itself or another database.

      If ``db_name`` is None, match against current data. Otherwise, ``db_name`` should be the name of an existing ``Database``.

      ``fields`` is a list of fields to use for matching. Field values are case-insensitive, but otherwise must match exactly for a link to be valid. If ``fields`` is ``None``, use the default fields of 'name', 'categories', 'unit', 'reference product', and 'location'.

      If ``ignore_categories``, link based only on name, unit and location. ``ignore_categories`` conflicts with ``fields``.

      If ``relink``, relink exchanges even if a link is already present.

      ``kind`` can be a string or a list of strings. Common values are "technosphere", "biosphere", "production", and "substitution".

      Nothing is returned, but ``self.data`` is changed.



   .. py:method:: create_new_biosphere(biosphere_name, relink=True)

      Create new biosphere database from biosphere flows in ``self.data``.

      Links all biosphere flows to new bio database if ``relink``.


   .. py:method:: add_unlinked_flows_to_biosphere_database(biosphere_name=None)


   .. py:method:: migrate(migration_name)


   .. py:method:: drop_unlinked(i_am_reckless=False)


   .. py:method:: add_unlinked_activities()

      Add technosphere flows to ``self.data``.



