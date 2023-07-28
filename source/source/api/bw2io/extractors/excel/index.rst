:py:mod:`bw2io.extractors.excel`
================================

.. py:module:: bw2io.extractors.excel


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.extractors.excel.ExcelExtractor



Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.extractors.excel.get_cell_value_handle_error



.. py:class:: ExcelExtractor

   Bases: :py:obj:`object`

   A class used to extract data from an Excel file.

   :param object: The parent object for the ExcelExtractor class.
   :type object: type

   :returns: An instance of the class.
   :rtype: object

   .. seealso::

      :obj:`openpyxl.load_workbook`
          Load a workbook from a file.

   .. rubric:: Notes

   This class requires the openpyxl package to be installed.

   :raises AssertionError: If the file at 'filepath' does not exist.

   :param filepath: The path to the Excel file.
   :type filepath: str

   :returns: A list of tuples containing the name of each sheet in the file and the data from each sheet.
   :rtype: list

   .. rubric:: Examples

   >>> extractor = ExcelExtractor()
   >>> filepath = 'example.xlsx'
   >>> data = extractor.extract(filepath)

   .. py:method:: extract(filepath)
      :classmethod:

      Extract data from an Excel file.

      :param filepath: The path to the Excel file.
      :type filepath: str

      :returns: A list of tuples containing the name of each sheet in the file and the data from each sheet.
      :rtype: list

      :raises AssertionError: If the file at 'filepath' does not exist.


   .. py:method:: extract_sheet(wb, name, strip=True)
      :classmethod:

      Extract data from a single sheet in an Excel workbook.

      :param wb: The workbook object with the sheet to extract data from.
      :type wb: openpyxl.workbook.Workbook
      :param name: The name of the sheet to extract data from.
      :type name: str
      :param strip: If True, strip whitespace from cell values, by default True.
      :type strip: bool, optional

      :returns: A list of lists containing the data from the sheet.
      :rtype: list

      .. rubric:: Notes

      This method is called by the 'extract' method to extract the data from each sheet in the workbook.

      .. rubric:: Examples

      >>> wb = openpyxl.load_workbook('example.xlsx')
      >>> name = 'Sheet1'
      >>> data = ExcelExtractor.extract_sheet(wb, sheetname)



.. py:function:: get_cell_value_handle_error(cell)

   Retrieve the value of a given cell and handle error types.

   :param cell: The cell to get the value from.
   :type cell: openpyxl.cell.cell.Cell

   :returns: The value of the cell, or None if the cell has an error type.
   :rtype: object

   .. rubric:: Examples

   >>> from openpyxl import Workbook
   >>> wb = Workbook()
   >>> ws = wb.active
   >>> ws["A1"] = "hello"
   >>> assert get_cell_value_handle_error(ws["A1"]) == "hello"
   >>> ws["B1"] = "=1/0"
   >>> assert get_cell_value_handle_error(ws["B1"]) == None


