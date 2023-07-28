:py:mod:`bw2io.export.excel`
============================

.. py:module:: bw2io.export.excel


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.export.excel.create_valid_worksheet_name
   bw2io.export.excel.lci_matrices_to_excel
   bw2io.export.excel.write_lci_excel
   bw2io.export.excel.write_lci_matching
   bw2io.export.excel.write_lcia_matching



.. py:function:: create_valid_worksheet_name(string)

   Exclude invalid characters and names.

   Data from http://www.accountingweb.com/technology/excel/seven-characters-you-cant-use-in-worksheet-names.


.. py:function:: lci_matrices_to_excel(database_name, include_descendants=True)

   Fake docstring


.. py:function:: write_lci_excel(database_name, objs=None, sections=None)

   Export database `database_name` to an Excel spreadsheet.

   Not all data can be exported. The following constraints apply:

   * Nested data, e.g. `{'foo': {'bar': 'baz'}}` are excluded. Spreadsheets are not a great format for nested data. However, *tuples* are exported, and the characters `::` are used to join elements of the tuple.
   * The only well-supported data types are strings, numbers, and booleans.

   Returns the filepath of the exported file.



.. py:function:: write_lci_matching(db, database_name, only_unlinked=False, only_activity_names=False)

   Write matched and unmatched exchanges to Excel file


.. py:function:: write_lcia_matching(db, name)

   Write matched and unmatched CFs to Excel file


