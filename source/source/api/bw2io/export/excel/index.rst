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

   :param string: String to convert to a valid worksheet name.
   :type string: str

   :returns: **string** -- Valid worksheet name.
   :rtype: str

   .. rubric:: Notes

   Data from http://www.accountingweb.com/technology/excel/seven-characters-you-cant-use-in-worksheet-names.


.. py:function:: lci_matrices_to_excel(database_name, include_descendants=True)

   Export LCI matrices to Excel.

   :param database_name: Name of database to export.
   :type database_name: str
   :param include_descendants: Include databases which are linked from ``database_name``. (default True)
   :type include_descendants: bool

   :returns: **filepath** -- Path to created Excel file.
   :rtype: str

   .. rubric:: Examples

   >>> lci_matrices_to_excel(database_name='example_db', include_descendants=True)
   '/path/to/example_db.xlsx'


.. py:function:: write_lci_excel(database_name, objs=None, sections=None, dirpath=None)

   Export database `database_name` to an Excel spreadsheet.

   .. rubric:: Notes

   Not all data can be exported. The following constraints apply:

   * Nested data, e.g. `{'foo': {'bar': 'baz'}}` are excluded.
   * Spreadsheets are not a great format for nested data. However, *tuples* are exported, and the characters `::` are used to join elements of the tuple.
   * The only well-supported data types are strings, numbers, and booleans.

   Default directory is ``projects.output_dir``, set ``dirpath`` to have save the file somewhere else.

   :param database_name: Name of the database to export.
   :type database_name: str
   :param objs: List of objects to export. If not provided, all objects in the database will be exported.
   :type objs: list, optional
   :param sections: List of sections to export. If not provided, all sections will be exported.
   :type sections: list, optional
   :param dirpath: Directory to save the file to. Default is ``projects.output_dir``.
   :type dirpath: str, optional

   :returns: Filepath of the exported file.
   :rtype: str


.. py:function:: write_lci_matching(db, database_name, only_unlinked=False, only_activity_names=False)

   Write matched and unmatched exchanges to Excel file

   :param db: Database to write.
   :type db: :class:`bw2data.Database`
   :param database_name: Name of the database to write.
   :type database_name: str
   :param only_unlinked: Only write unlinked exchanges. Default is ``False``.
   :type only_unlinked: bool, optional
   :param only_activity_names: Only write activity names. Default is ``False``.
   :type only_activity_names: bool, optional

   :returns: Filepath of the exported file.
   :rtype: str


.. py:function:: write_lcia_matching(db, name)

   Write matched and unmatched CFs to Excel file

   :param db: Database to write.
   :type db: :class:`bw2data.Database`
   :param name: Name of the database to write.
   :type name: str

   :returns: Filepath of the exported file.
   :rtype: str


