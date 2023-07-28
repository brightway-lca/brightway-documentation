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
   chemidplus/index.rst
   compatibility/index.rst
   download_utils/index.rst
   errors/index.rst
   migrations/index.rst
   modified_database/index.rst
   package/index.rst
   remote/index.rst
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
   bw2io.ChemIDPlus
   bw2io.DatabaseSelectionToGEXF
   bw2io.DatabaseToGEXF
   bw2io.Ecospold1LCIAImporter
   bw2io.ExcelImporter
   bw2io.ExcelLCIAImporter
   bw2io.Exiobase3MonetaryImporter
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

   bw2io.activity_hash
   bw2io.backup_data_directory
   bw2io.backup_project_directory
   bw2io.bw2setup
   bw2io.create_core_migrations
   bw2io.create_default_biosphere3
   bw2io.create_default_lcia_methods
   bw2io.es2_activity_hash
   bw2io.exiobase_monetary
   bw2io.install_project
   bw2io.lci_matrices_to_excel
   bw2io.lci_matrices_to_matlab
   bw2io.load_json_data_file
   bw2io.restore_project_directory
   bw2io.useeio11



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.migrations
   bw2io.normalize_units
   bw2io.unlinked_data






















.. py:function:: bw2setup()



.. py:function:: create_default_biosphere3(overwrite=False)


.. py:function:: create_default_lcia_methods(overwrite=False, rationalize_method_names=False, shortcut=True)



.. py:function:: exiobase_monetary(version=(3, 8, 1), year=2017, products=False, name=None, ignore_small_balancing_corrections=True)







.. py:function:: useeio11(name='USEEIO-1.1', collapse_products=False, prune=False)





