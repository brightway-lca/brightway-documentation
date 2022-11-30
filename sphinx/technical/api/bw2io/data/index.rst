:py:mod:`bw2io.data`
====================

.. py:module:: bw2io.data


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   exiopol/index.rst


Package Contents
----------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.data.write_json_file
   bw2io.data.get_csv_example_filepath
   bw2io.data.get_xlsx_example_filepath
   bw2io.data.get_sheet
   bw2io.data.get_biosphere_2_3_category_migration_data
   bw2io.data.get_biosphere_2_3_name_migration_data
   bw2io.data.get_simapro_water_migration_data
   bw2io.data.get_us_lci_migration_data
   bw2io.data.get_exiobase_biosphere_migration_data
   bw2io.data.convert_simapro_ecoinvent_elementary_flows
   bw2io.data.convert_simapro_ecoinvent_3_migration_data
   bw2io.data.get_simapro_ecoinvent_3_migration_data
   bw2io.data.convert_ecoinvent_2_301
   bw2io.data._add_new_ecoinvent_biosphere_flows
   bw2io.data.convert_lcia_methods_data
   bw2io.data.get_valid_geonames
   bw2io.data.get_ecoinvent_pre35_migration_data
   bw2io.data.update_db_ecoinvent_locations
   bw2io.data.add_example_database



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.data.ECOSPOLD_2_3_BIOSPHERE
   bw2io.data.SIMAPRO_BIOSPHERE
   bw2io.data.normalize_units
   bw2io.data.dirpath
   bw2io.data.add_ecoinvent_33_biosphere_flows
   bw2io.data.add_ecoinvent_34_biosphere_flows
   bw2io.data.add_ecoinvent_35_biosphere_flows
   bw2io.data.add_ecoinvent_36_biosphere_flows
   bw2io.data.add_ecoinvent_37_biosphere_flows
   bw2io.data.add_ecoinvent_38_biosphere_flows
   bw2io.data.add_ecoinvent_39_biosphere_flows


.. py:data:: ECOSPOLD_2_3_BIOSPHERE
   

   

.. py:data:: SIMAPRO_BIOSPHERE
   

   

.. py:data:: normalize_units
   

   

.. py:data:: dirpath
   

   

.. py:function:: write_json_file(data, name)


.. py:function:: get_csv_example_filepath()


.. py:function:: get_xlsx_example_filepath()


.. py:function:: get_sheet(path, name)


.. py:function:: get_biosphere_2_3_category_migration_data()

   Get data for 2 -> 3 migration for biosphere flow categories


.. py:function:: get_biosphere_2_3_name_migration_data()

   Get migration data for 2 -> 3 biosphere flow names.

   This migration **must** be applied only after categories have been updated.

   Note that the input data excel sheet is **modified** from the raw data provided by ecoinvent - some biosphere flows which had no equivalent in ecospold2 were mapped using my best judgment. Name changes from 3.1 were also included. Modified cells are marked in **dark orange**.

   Note that not all rows have names in ecoinvent 3. There are a few energy resources that we don't update. For water flows, the categories are updated by a different strategy, and the names don't change, so we just ignore them for now.


.. py:function:: get_simapro_water_migration_data()


.. py:function:: get_us_lci_migration_data()

   Fix US LCI database name inconsistencies


.. py:function:: get_exiobase_biosphere_migration_data()

   Migrate to ecoinvent3 flow names


.. py:function:: convert_simapro_ecoinvent_elementary_flows()

   Write a correspondence list from SimaPro elementary flow names to ecoinvent 3 flow names to a JSON file.

   Uses custom SimaPro specific data. Ecoinvent 2 -> 3 conversion is in a separate JSON file.


.. py:function:: convert_simapro_ecoinvent_3_migration_data()


.. py:function:: get_simapro_ecoinvent_3_migration_data(version)

   Write a migrations data file from SimaPro activity names to ecoinvent 3 processes.

   Correspondence file is processed from Pré, and has the following fields:

       #. SimaPro name
       #. Ecoinvent flow name
       #. Location
       #. Ecoinvent activity name
       #. System model
       #. SimaPro type

   Note that even the official matching data from Pré is incorrect, but works if we cast all strings to lower case.

   SimaPro type is either ``System terminated`` or ``Unit process``. We always match to unit processes regardless of SimaPro type.


.. py:function:: convert_ecoinvent_2_301()

   Write a migrations data file from ecoinvent 2 to 3.1.

   This is not simple, unfortunately. We have to deal with at least the following:
       * Unit changes (e.g. cubic meters to MJ)
       * Some datasets are deleted, and replaced by others



.. py:function:: _add_new_ecoinvent_biosphere_flows(version)


.. py:data:: add_ecoinvent_33_biosphere_flows
   

   

.. py:data:: add_ecoinvent_34_biosphere_flows
   

   

.. py:data:: add_ecoinvent_35_biosphere_flows
   

   

.. py:data:: add_ecoinvent_36_biosphere_flows
   

   

.. py:data:: add_ecoinvent_37_biosphere_flows
   

   

.. py:data:: add_ecoinvent_38_biosphere_flows
   

   

.. py:data:: add_ecoinvent_39_biosphere_flows
   

   

.. py:function:: convert_lcia_methods_data()


.. py:function:: get_valid_geonames()

   Get list of short location names used in ecoinvent 3


.. py:function:: get_ecoinvent_pre35_migration_data()


.. py:function:: update_db_ecoinvent_locations(database_name)

   Update ecoinvent location names for an existing database.

   Returns number of modified datasets.


.. py:function:: add_example_database(overwrite=True)


