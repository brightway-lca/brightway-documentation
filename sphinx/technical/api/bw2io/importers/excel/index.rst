:py:mod:`bw2io.importers.excel`
===============================

.. py:module:: bw2io.importers.excel


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.importers.excel.ExcelImporter
   bw2io.importers.excel.CSVImporter



Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.importers.excel.valid_first_cell



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.importers.excel.is_empty_line
   bw2io.importers.excel.remove_empty


.. py:data:: is_empty_line
   

   

.. py:data:: remove_empty
   

   

.. py:function:: valid_first_cell(sheet, data)

   Return boolean if first cell in worksheet is not ``skip``.


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



.. py:class:: CSVImporter(filepath)

   Bases: :py:obj:`ExcelImporter`

   Generic CSV importer

   .. py:attribute:: format
      :annotation: = CSV

      

   .. py:attribute:: extractor
      

      


