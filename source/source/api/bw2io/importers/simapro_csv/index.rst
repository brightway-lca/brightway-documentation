:py:mod:`bw2io.importers.simapro_csv`
=====================================

.. py:module:: bw2io.importers.simapro_csv


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.importers.simapro_csv.SimaProCSVImporter




.. py:class:: SimaProCSVImporter(filepath, name=None, delimiter=';', encoding='latin-1', normalize_biosphere=True, biosphere_db=None, extractor=SimaProCSVExtractor)

   Bases: :py:obj:`bw2io.importers.base_lci.LCIImporter`

   .. autoapi-inheritance-diagram:: bw2io.importers.simapro_csv.SimaProCSVImporter
      :parts: 1
      :private-bases:

   Base class for format-specific importers.

   Defines workflow for applying strategies.

   Takes a database name (string) as initialization parameter.


   Initialize the ImportBase object.

   :param \*args: Variable length argument list.
   :param \*\*kwargs: Arbitrary keyword arguments.

   :raises NotImplemented :: This class should be subclassed.

   .. py:attribute:: format
      :value: 'SimaPro CSV'

      

   .. py:method:: get_db_name()


   .. py:method:: match_ecoinvent2(db_name)


   .. py:method:: write_database(data=None, name=None, *args, **kwargs)

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



