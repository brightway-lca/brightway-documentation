:py:mod:`bw2io.importers.exiobase3_monetary`
============================================

.. py:module:: bw2io.importers.exiobase3_monetary


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.importers.exiobase3_monetary.Exiobase3MonetaryImporter




.. py:class:: Exiobase3MonetaryImporter(dirpath, db_name, ignore_small_balancing_corrections=True)

   Bases: :py:obj:`bw2io.importers.base_lci.LCIImporter`

   .. autoapi-inheritance-diagram:: bw2io.importers.exiobase3_monetary.Exiobase3MonetaryImporter
      :parts: 1
      :private-bases:

   Base class for format-specific importers.

   Defines workflow for applying strategies.

   Takes a database name (string) as initialization parameter.


   .. py:attribute:: format
      :value: 'Exiobase 3'

      

   .. py:method:: add_unlinked_flows_to_new_biosphere_database(biosphere_name=None)


   .. py:method:: apply_strategies(biosphere=None)


   .. py:method:: apply_strategy(*args, **kwargs)
      :abstractmethod:


   .. py:method:: patch_lcia_methods(new_biosphere)


   .. py:method:: write_activities_as_database()


   .. py:method:: write_database(biosphere=None)

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



