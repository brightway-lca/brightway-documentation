:py:mod:`bw2io.importers`
=========================

.. py:module:: bw2io.importers


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   base/index.rst
   base_lci/index.rst
   base_lcia/index.rst
   ecoinvent_lcia/index.rst
   ecospold1/index.rst
   ecospold1_lcia/index.rst
   ecospold2/index.rst
   ecospold2_biosphere/index.rst
   excel/index.rst
   excel_lcia/index.rst
   exiobase3_hybrid/index.rst
   exiobase3_monetary/index.rst
   json_ld/index.rst
   json_ld_lcia/index.rst
   simapro_csv/index.rst
   simapro_lcia_csv/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.importers.EcoinventLCIAImporter
   bw2io.importers.MultiOutputEcospold1Importer
   bw2io.importers.NoIntegerCodesEcospold1Importer
   bw2io.importers.SingleOutputEcospold1Importer
   bw2io.importers.Ecospold1LCIAImporter
   bw2io.importers.SingleOutputEcospold2Importer
   bw2io.importers.Ecospold2BiosphereImporter
   bw2io.importers.CSVImporter
   bw2io.importers.ExcelImporter
   bw2io.importers.CSVLCIAImporter
   bw2io.importers.ExcelLCIAImporter
   bw2io.importers.Exiobase3HybridImporter
   bw2io.importers.Exiobase3MonetaryImporter
   bw2io.importers.SimaProCSVImporter
   bw2io.importers.SimaProLCIACSVImporter




.. py:class:: EcoinventLCIAImporter

   Bases: :py:obj:`bw2io.importers.base_lcia.LCIAImporter`

   .. py:method:: add_rationalize_method_names_strategy()


   .. py:method:: separate_methods()

      Separate the list of CFs into distinct methods



.. py:class:: MultiOutputEcospold1Importer(*args, **kwargs)

   Bases: :py:obj:`SingleOutputEcospold1Importer`

   Import and process mutli-output datasets in the ecospold 1 format.

   Works the same as the single-output importer, but first allocates multioutput datasets.


.. py:class:: NoIntegerCodesEcospold1Importer(*args, **kwargs)

   Bases: :py:obj:`SingleOutputEcospold1Importer`

   Import and process single-output datasets in the ecospold 1 format.

   Applies the following strategies:
   #. If only one exchange is a production exchange, that is the reference product
   #. Delete (unreliable) integer codes from extracted data
   #. Drop ``unspecified`` subcategories from biosphere flows
   #. Normalize biosphere flow categories to ecoinvent 3.1 standard
   #. Normalize biosphere flow names to ecoinvent 3.1 standard
   #. Remove locations from biosphere exchanges
   #. Create a ``code`` from the activity hash of the dataset
   #. Link biosphere exchanges to the default biosphere database
   #. Link internal technosphere exchanges

   :param \* *filepath*: Either a file or directory.
   :param \* *db_name*: Name of database to create.


.. py:class:: SingleOutputEcospold1Importer(filepath, db_name, use_mp=True, extractor=Ecospold1DataExtractor)

   Bases: :py:obj:`bw2io.importers.base_lci.LCIImporter`

   Import and process single-output datasets in the ecospold 1 format.

   Applies the following strategies:
   #. If only one exchange is a production exchange, that is the reference product
   #. Delete (unreliable) integer codes from extracted data
   #. Drop ``unspecified`` subcategories from biosphere flows
   #. Normalize biosphere flow categories to ecoinvent 3.1 standard
   #. Normalize biosphere flow names to ecoinvent 3.1 standard
   #. Remove locations from biosphere exchanges
   #. Create a ``code`` from the activity hash of the dataset
   #. Link biosphere exchanges to the default biosphere database
   #. Link internal technosphere exchanges

   :param \* *filepath*: Either a file or directory.
   :param \* *db_name*: Name of database to create.

   .. py:attribute:: format
      :annotation: = Ecospold1

      


.. py:class:: Ecospold1LCIAImporter(filepath, biosphere=None)

   Bases: :py:obj:`bw2io.importers.base_lcia.LCIAImporter`

   .. py:attribute:: format
      :annotation: = Ecospold1 LCIA

      


.. py:class:: SingleOutputEcospold2Importer(dirpath, db_name, extractor=Ecospold2DataExtractor, use_mp=True, signal=None)

   Bases: :py:obj:`bw2io.importers.base_lci.LCIImporter`

   Base class for format-specific importers.

   Defines workflow for applying strategies.

   Takes a database name (string) as initialization parameter.


   .. py:attribute:: format
      :annotation: = Ecospold2

      


.. py:class:: Ecospold2BiosphereImporter(name='biosphere3', version='3.9')

   Bases: :py:obj:`bw2io.importers.base_lci.LCIImporter`

   Base class for format-specific importers.

   Defines workflow for applying strategies.

   Takes a database name (string) as initialization parameter.


   .. py:attribute:: format
      :annotation: = Ecoinvent XML

      

   .. py:method:: extract(version)



.. py:class:: CSVImporter(filepath)

   Bases: :py:obj:`ExcelImporter`

   Generic CSV importer

   .. py:attribute:: format
      :annotation: = CSV

      

   .. py:attribute:: extractor
      

      


.. py:class:: ExcelImporter(filepath)

   Bases: :py:obj:`bw2io.importers.base_lci.LCIImporter`

   Generic Excel importer.

   See the `generic Excel example spreadsheet <https://github.com/brightway-lca/brightway2-io/raw/master/bw2io/data/examples/example.xlsx>`__.

   Excel spreadsheet should follow the following format:

   ::
       Project parameters
       <variable>, <formula>, <amount>, metadata

       Database, <name of database>
       <database field name>, <database field value>

       Parameters
       <variable>, <formula>, <amount>, metadata

       Activity, <name of activity>
       <database field name>, <database field value>
       Exchanges
       <field name>, <field name>, <field name>
       <value>, <value>, <value>
       <value>, <value>, <value>

   Neither project parameters, parameters, nor exchanges for each activity are required.

   An activity is marked as finished with a blank line.

   In general, data is imported without modification. However, the following transformations are applied:

   * Numbers are translated from text into actual numbers.
   * Tuples, separated in the cell by the ``::`` string, are reconstructed.
   * ``True`` and ``False`` are transformed to boolean values.
   * Fields with the value ``(Unknown)`` are dropped.


   .. py:attribute:: format
      :annotation: = Excel

      

   .. py:attribute:: extractor
      

      

   .. py:method:: get_database(data)


   .. py:method:: get_database_parameters(data)


   .. py:method:: get_project_parameters(data)

      Extract project parameters (variables and formulas).

      Project parameters are a section that starts with a line with the string "project parameters" (case-insensitive) in the first cell, and ends with a blank line. There can be multiple project parameter sections.


   .. py:method:: get_labelled_section(sn, ws, index=0, transform=True)

      Turn a list of rows into a list of dictionaries.

      The first line of ``ws`` is the column labels. All subsequent rows are the data values. Missing columns are dropped.

      ``transform`` is a boolean: perform CSV transformation functions like ``csv_restore_tuples``.


   .. py:method:: get_metadata_section(sn, ws, index=0, transform=True)


   .. py:method:: process_activities(data)

      Take list of `(sheet names, raw data)` and process it.


   .. py:method:: write_activity_parameters(data=None, delete_existing=True)


   .. py:method:: write_database_parameters(activate_parameters=True, delete_existing=True)

      Same as base ``write_database_parameters`` method, but ``activate_parameters`` is True by default.


   .. py:method:: write_database(**kwargs)

      Same as base ``write_database`` method, but ``activate_parameters`` is True by default.


   .. py:method:: get_activity(sn, ws)



.. py:class:: CSVLCIAImporter(filepath, name, description, unit, **metadata)

   Bases: :py:obj:`ExcelLCIAImporter`

   Generic CSV LCIA importer

   .. py:attribute:: format
      :annotation: = CSV

      

   .. py:attribute:: extractor
      

      


.. py:class:: ExcelLCIAImporter(filepath, name, description, unit, **metadata)

   Bases: :py:obj:`bw2io.importers.base_lcia.LCIAImporter`

   Generic Excel LCIA importer.

   See the `documentation <https://2.docs.brightway.dev/intro.html#importing-lcia-methods-from-the-standard-excel-template>`__.


   .. py:attribute:: format
      :annotation: = Excel

      

   .. py:attribute:: extractor
      

      


.. py:class:: Exiobase3HybridImporter(dirpath, db_name='EXIOBASE 3.3.17 hybrid')

   Bases: :py:obj:`object`

   .. py:attribute:: format
      :annotation: = Exiobase 3.3.17 hybrid mrio_common_metadata tidy datapackage

      

   .. py:method:: write_database()



.. py:class:: Exiobase3MonetaryImporter(dirpath, db_name, ignore_small_balancing_corrections=True)

   Bases: :py:obj:`bw2io.importers.base_lci.LCIImporter`

   Base class for format-specific importers.

   Defines workflow for applying strategies.

   Takes a database name (string) as initialization parameter.


   .. py:attribute:: format
      :annotation: = Exiobase 3

      

   .. py:method:: apply_strategy(*args, **kwargs)
      :abstractmethod:


   .. py:method:: add_unlinked_flows_to_new_biosphere_database(biosphere_name=None)


   .. py:method:: write_activities_as_database()


   .. py:method:: patch_lcia_methods(new_biosphere)


   .. py:method:: apply_strategies(biosphere=None)


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



.. py:class:: SimaProCSVImporter(filepath, name=None, delimiter=';', encoding='latin-1', normalize_biosphere=True, biosphere_db=None, extractor=SimaProCSVExtractor)

   Bases: :py:obj:`bw2io.importers.base_lci.LCIImporter`

   Base class for format-specific importers.

   Defines workflow for applying strategies.

   Takes a database name (string) as initialization parameter.


   .. py:attribute:: format
      :annotation: = SimaPro CSV

      

   .. py:method:: get_db_name()


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


   .. py:method:: match_ecoinvent2(db_name)



.. py:class:: SimaProLCIACSVImporter(filepath, biosphere=None, delimiter=';', encoding='latin-1', normalize_biosphere=True)

   Bases: :py:obj:`bw2io.importers.base_lcia.LCIAImporter`

   .. py:attribute:: format
      :annotation: = SimaPro CSV LCIA

      


