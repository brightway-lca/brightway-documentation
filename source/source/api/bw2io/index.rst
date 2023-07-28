:py:mod:`bw2io`
===============

.. py:module:: bw2io


Subpackages
-----------
.. toctree::
   :titlesonly:
   :maxdepth: 3

   export/index.rst
   extractors/index.rst
   importers/index.rst
   strategies/index.rst


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   backup/index.rst
   compatibility/index.rst
   errors/index.rst
   migrations/index.rst
   modified_database/index.rst
   package/index.rst
   units/index.rst
   unlinked_data/index.rst
   utils/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.BW2Package
   bw2io.CSVImporter
   bw2io.CSVLCIAImporter
   bw2io.DatabaseSelectionToGEXF
   bw2io.DatabaseToGEXF
   bw2io.Ecospold1LCIAImporter
   bw2io.ExcelImporter
   bw2io.ExcelLCIAImporter
   bw2io.Migration
   bw2io.MultiOutputEcospold1Importer
   bw2io.SimaProCSVImporter
   bw2io.SimaProLCIACSVImporter
   bw2io.SingleOutputEcospold1Importer
   bw2io.SingleOutputEcospold2Importer
   bw2io.UnlinkedData



Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.backup_data_directory
   bw2io.backup_project_directory
   bw2io.bw2setup
   bw2io.create_core_migrations
   bw2io.create_default_biosphere3
   bw2io.create_default_lcia_methods
   bw2io.es2_activity_hash
   bw2io.lci_matrices_to_excel
   bw2io.lci_matrices_to_matlab
   bw2io.load_json_data_file
   bw2io.restore_project_directory



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.activity_hash
   bw2io.migrations
   bw2io.normalize_units
   bw2io.unlinked_data


.. py:class:: BW2Package

   Bases: :py:obj:`object`

   This is a format for saving objects which implement the :ref:`datastore` API. Data is stored as a BZip2-compressed file of JSON data. This archive format is compatible across Python versions, and is, at least in theory, programming-language agnostic.

   Validation is done with ``bw2data.validate.bw2package_validator``.

   The data format is:

   .. code-block:: python

       {
           'metadata': {},  # Dictionary of metadata to be written to metadata-store.
           'name': basestring,  # Name of object
           'class': {  # Data on the underlying class. A new class is instantiated
                       # based on these strings. See _create_class.
               'module': basestring,  # e.g. "bw2data.database"
               'name': basestring  # e.g. "Database"
           },
           'unrolled_dict': bool,  # Flag indicating if dictionary keys needed to
                                   # be modified for JSON (as JSON keys can't be tuples)
           'data': object  # Object data, e.g. LCIA method or LCI database
       }

   Perfect roundtrips between machines are not guaranteed:
       * All lists are converted to tuples (because JSON does not distinguish between lists and tuples).
       * Absolute filepaths in metadata would be specific to a certain computer and user.

   .. note:: This class does not need to be instantiated, as all its methods are ``classmethods``, i.e. do ``BW2Package.import_obj("foo")`` instead of ``BW2Package().import_obj("foo")``


   .. py:attribute:: APPROVED

      

   .. py:method:: _create_class(metadata, apply_whitelist=True)
      :classmethod:


   .. py:method:: _create_obj(data)
      :classmethod:


   .. py:method:: _get_class_metadata(obj)
      :classmethod:


   .. py:method:: _is_valid_package(data)
      :classmethod:


   .. py:method:: _is_whitelisted(metadata)
      :classmethod:


   .. py:method:: _load_obj(data, whitelist=True)
      :classmethod:


   .. py:method:: _prepare_obj(obj, backwards_compatible=False)
      :classmethod:


   .. py:method:: _write_file(filepath, data)
      :classmethod:


   .. py:method:: export_obj(obj, filename=None, folder='export', backwards_compatible=False)
      :classmethod:

      Export an object.

      :param \* *obj*: Object to export.
      :type \* *obj*: object
      :param \* *filename*: Name of file to create. Default is ``obj.name``.
      :type \* *filename*: str, optional
      :param \* *folder*: Folder to create file in. Default is ``export``.
      :type \* *folder*: str, optional
      :param \* *backwards_compatible*: Create package compatible with bw2data version 1.
      :type \* *backwards_compatible*: bool, optional

      :returns: Filepath of created file.


   .. py:method:: export_objs(objs, filename, folder='export', backwards_compatible=False)
      :classmethod:

      Export a list of objects. Can have heterogeneous types.

      :param \* *objs*: List of objects to export.
      :type \* *objs*: list
      :param \* *filename*: Name of file to create.
      :type \* *filename*: str
      :param \* *folder*: Folder to create file in. Default is ``export``.
      :type \* *folder*: str, optional
      :param \* *backwards_compatible*: Create package compatible with bw2data version 1.
      :type \* *backwards_compatible*: bool, optional

      :returns: Filepath of created file.


   .. py:method:: import_file(filepath, whitelist=True)
      :classmethod:

      Import bw2package file, and create the loaded objects, including registering, writing, and processing the created objects.

      :param \* *filepath*: Path of file to import
      :type \* *filepath*: str
      :param \* *whitelist*: Apply whitelist to allowed types. Default is ``True``.
      :type \* *whitelist*: bool

      :returns: Created object or list of created objects.


   .. py:method:: load_file(filepath, whitelist=True)
      :classmethod:

      Load a bw2package file with one or more objects. Does not create new objects.

      :param \* *filepath*: Path of file to import
      :type \* *filepath*: str
      :param \* *whitelist*: Apply whitelist of approved classes to allowed types. Default is ``True``.
      :type \* *whitelist*: bool

      Returns the loaded data in the bw2package dict data format, with the following changes:
          * ``"class"`` is an actual Python class object (but not instantiated).




.. py:class:: CSVImporter(filepath)

   Bases: :py:obj:`ExcelImporter`

   .. autoapi-inheritance-diagram:: bw2io.CSVImporter
      :parts: 1
      :private-bases:

   Generic CSV importer

   .. py:attribute:: extractor

      

   .. py:attribute:: format
      :value: 'CSV'

      


.. py:class:: CSVLCIAImporter(filepath, name, description, unit, **metadata)

   Bases: :py:obj:`ExcelLCIAImporter`

   .. autoapi-inheritance-diagram:: bw2io.CSVLCIAImporter
      :parts: 1
      :private-bases:

   Generic CSV LCIA importer

   .. py:attribute:: extractor

      

   .. py:attribute:: format
      :value: 'CSV'

      


.. py:class:: DatabaseSelectionToGEXF(database, keys)

   Bases: :py:obj:`DatabaseToGEXF`

   .. autoapi-inheritance-diagram:: bw2io.DatabaseSelectionToGEXF
      :parts: 1
      :private-bases:

   Export a Gephi graph for a selection of activities from a database.

   Also includes all inputs for the filtered activities.

   :param \* *database*: Database name.
   :type \* *database*: str
   :param \* *keys*: The activity keys to export.
   :type \* *keys*: str


.. py:class:: DatabaseToGEXF(database, include_descendants=False)

   Bases: :py:obj:`object`

   Export a Gephi graph for a database.

   Call ``.export()`` to export the file after class instantiation.

   :param \* *database*: Database name.
   :type \* *database*: str
   :param \* *include_descendants*: Include databases which are linked from ``database``.
   :type \* *include_descendants*: bool

   .. warning:: ``include_descendants`` is not yet implemented.


   .. py:method:: export()

      Export the Gephi XML file. Returns the filepath of the created file.


   .. py:method:: get_data(E)

      Get Gephi nodes and edges.



.. py:class:: Ecospold1LCIAImporter(filepath, biosphere=None)

   Bases: :py:obj:`bw2io.importers.base_lcia.LCIAImporter`

   .. autoapi-inheritance-diagram:: bw2io.Ecospold1LCIAImporter
      :parts: 1
      :private-bases:

   .. py:attribute:: format
      :value: 'Ecospold1 LCIA'

      


.. py:class:: ExcelImporter(filepath)

   Bases: :py:obj:`bw2io.importers.base_lci.LCIImporter`

   .. autoapi-inheritance-diagram:: bw2io.ExcelImporter
      :parts: 1
      :private-bases:

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


   .. py:attribute:: extractor

      

   .. py:attribute:: format
      :value: 'Excel'

      

   .. py:method:: get_activity(sn, ws)


   .. py:method:: get_database(data)


   .. py:method:: get_database_parameters(data)


   .. py:method:: get_labelled_section(sn, ws, index=0, transform=True)

      Turn a list of rows into a list of dictionaries.

      The first line of ``ws`` is the column labels. All subsequent rows are the data values. Missing columns are dropped.

      ``transform`` is a boolean: perform CSV transformation functions like ``csv_restore_tuples``.


   .. py:method:: get_metadata_section(sn, ws, index=0, transform=True)


   .. py:method:: get_project_parameters(data)

      Extract project parameters (variables and formulas).

      Project parameters are a section that starts with a line with the string "project parameters" (case-insensitive) in the first cell, and ends with a blank line. There can be multiple project parameter sections.


   .. py:method:: process_activities(data)

      Take list of `(sheet names, raw data)` and process it.


   .. py:method:: write_activity_parameters(data=None, delete_existing=True)


   .. py:method:: write_database(**kwargs)

      Same as base ``write_database`` method, but ``activate_parameters`` is True by default.


   .. py:method:: write_database_parameters(activate_parameters=True, delete_existing=True)

      Same as base ``write_database_parameters`` method, but ``activate_parameters`` is True by default.



.. py:class:: ExcelLCIAImporter(filepath, name, description, unit, **metadata)

   Bases: :py:obj:`bw2io.importers.base_lcia.LCIAImporter`

   .. autoapi-inheritance-diagram:: bw2io.ExcelLCIAImporter
      :parts: 1
      :private-bases:

   Generic Excel LCIA importer.

   See the `documentation <https://2.docs.brightway.dev/intro.html#importing-lcia-methods-from-the-standard-excel-template>`__.


   .. py:attribute:: extractor

      

   .. py:attribute:: format
      :value: 'Excel'

      


.. py:class:: Migration(*args, **kwargs)

   Bases: :py:obj:`bw2data.data_store.DataStore`

   .. autoapi-inheritance-diagram:: bw2io.Migration
      :parts: 1
      :private-bases:

   .. py:property:: description


   .. py:attribute:: _metadata

      

   .. py:method:: load()


   .. py:method:: validate(*args, **kwargs)


   .. py:method:: write(data, description)

      Write migration data. Requires a description.



.. py:class:: MultiOutputEcospold1Importer(*args, **kwargs)

   Bases: :py:obj:`SingleOutputEcospold1Importer`

   .. autoapi-inheritance-diagram:: bw2io.MultiOutputEcospold1Importer
      :parts: 1
      :private-bases:

   Import and process mutli-output datasets in the ecospold 1 format.

   Works the same as the single-output importer, but first allocates multioutput datasets.


.. py:class:: SimaProCSVImporter(filepath, name=None, delimiter=';', encoding='latin-1', normalize_biosphere=True, biosphere_db=None)

   Bases: :py:obj:`bw2io.importers.base_lci.LCIImporter`

   .. autoapi-inheritance-diagram:: bw2io.SimaProCSVImporter
      :parts: 1
      :private-bases:

   Base class for format-specific importers.

   Defines workflow for applying strategies.

   Takes a database name (string) as initialization parameter.


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



.. py:class:: SimaProLCIACSVImporter(filepath, biosphere=None, delimiter=';', encoding='latin-1', normalize_biosphere=True)

   Bases: :py:obj:`bw2io.importers.base_lcia.LCIAImporter`

   .. autoapi-inheritance-diagram:: bw2io.SimaProLCIACSVImporter
      :parts: 1
      :private-bases:

   .. py:attribute:: format
      :value: 'SimaPro CSV LCIA'

      


.. py:class:: SingleOutputEcospold1Importer(filepath, db_name, use_mp=True, extractor=Ecospold1DataExtractor)

   Bases: :py:obj:`bw2io.importers.base_lci.LCIImporter`

   .. autoapi-inheritance-diagram:: bw2io.SingleOutputEcospold1Importer
      :parts: 1
      :private-bases:

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
      :value: 'Ecospold1'

      


.. py:class:: SingleOutputEcospold2Importer(dirpath, db_name, extractor=Ecospold2DataExtractor, use_mp=True, signal=None)

   Bases: :py:obj:`bw2io.importers.base_lci.LCIImporter`

   .. autoapi-inheritance-diagram:: bw2io.SingleOutputEcospold2Importer
      :parts: 1
      :private-bases:

   Base class for format-specific importers.

   Defines workflow for applying strategies.

   Takes a database name (string) as initialization parameter.


   .. py:attribute:: format
      :value: 'Ecospold2'

      


.. py:class:: UnlinkedData

   Bases: :py:obj:`bw2data.data_store.DataStore`

   .. autoapi-inheritance-diagram:: bw2io.UnlinkedData
      :parts: 1
      :private-bases:

   .. py:attribute:: _intermediate_dir
      :value: 'unlinked'

      

   .. py:attribute:: _metadata

      

   .. py:method:: validate(*args, **kwargs)



.. py:function:: backup_data_directory()

   Backup data directory to a ``.tar.gz`` (compressed tar archive).

   Backup archive is saved to the user's home directory.

   Restoration is done manually. Returns the filepath of the backup archive.


.. py:function:: backup_project_directory(project)

   Backup project data directory to a ``.tar.gz`` (compressed tar archive).

   ``project`` is the name of a project.

   Backup archive is saved to the user's home directory.

   Restoration is done using ``restore_project_directory``.

   Returns the filepath of the backup archive.


.. py:function:: bw2setup()


.. py:function:: create_core_migrations()

   Add pre-defined core migrations data files


.. py:function:: create_default_biosphere3(overwrite=False)


.. py:function:: create_default_lcia_methods(overwrite=False, rationalize_method_names=False, shortcut=True)


.. py:function:: es2_activity_hash(activity, flow)

   Generate unique ID for ecoinvent3 dataset.

   Despite using a million UUIDs, there is actually no unique ID in an ecospold2 dataset. Datasets are uniquely identified by the combination of activity and flow UUIDs.


.. py:function:: lci_matrices_to_excel(database_name, include_descendants=True)

   Fake docstring


.. py:function:: lci_matrices_to_matlab(database_name)


.. py:function:: load_json_data_file(filename)


.. py:function:: restore_project_directory(fp)

   Restore backup created using ``backup_project_directory``.

   Raises an error is the project already exists.

   ``fp`` is the filepath of the backup archive.

   Returns the name of the newly created project.


.. py:data:: activity_hash

   

.. py:data:: migrations

   

.. py:data:: normalize_units

   

.. py:data:: unlinked_data

   

