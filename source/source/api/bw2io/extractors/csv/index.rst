:py:mod:`bw2io.extractors.csv`
==============================

.. py:module:: bw2io.extractors.csv


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.extractors.csv.CSVExtractor




.. py:class:: CSVExtractor

   Bases: :py:obj:`object`

   Extracts data from CSV files.

   See Also:
   ---------
   - :class:`.ExcelExtractor`: Extracts data from Excel files.

   References:
   -----------
   - https://docs.python.org/3/library/csv.html: Official documentation for the csv module in Python.


   .. py:method:: extract(filepath, encoding='utf-8-sig')
      :classmethod:

      Extracts CSV file data from the filepath.

      Parameters:
      ----------
      filepath : str
          The path to the CSV file.
      encoding : str, optional
          The encoding of the CSV file, with default being "utf-8-sig".

      Returns:
      -------
      list
          A list containing the filename and the contents of the CSV file.

      Raises:
      ------
      AssertionError
          If the file does not exist.

      Examples:
      --------
      >>> CSVExtractor.extract("example.csv")
      ["example.csv", [["1", "2", "3"], ["4", "5", "6"]]]



