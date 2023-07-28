:py:mod:`bw2io.importers.excel_lcia`
====================================

.. py:module:: bw2io.importers.excel_lcia


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.importers.excel_lcia.CSVLCIAImporter
   bw2io.importers.excel_lcia.ExcelLCIAImporter



Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.importers.excel_lcia.as_dicts



.. py:class:: CSVLCIAImporter(filepath, name, description, unit, **metadata)

   Bases: :py:obj:`ExcelLCIAImporter`

   .. autoapi-inheritance-diagram:: bw2io.importers.excel_lcia.CSVLCIAImporter
      :parts: 1
      :private-bases:

   Generic CSV LCIA importer.

   .. attribute:: format

      The file format.

      :type: str

   .. attribute:: extractor

      The file extractor class.

      :type: class

   Initializes the ExcelLCIAImporter object.

   :param filepath: The path to the Excel file.
   :type filepath: str
   :param name: The name of the LCIA method.
   :type name: tuple
   :param description: The description of the LCIA method.
   :type description: str
   :param unit: The unit of the LCIA method.
   :type unit: str
   :param \*\*metadata: The metadata associated with the LCIA method.

   .. py:attribute:: extractor

      

   .. py:attribute:: format
      :value: 'CSV'

      


.. py:class:: ExcelLCIAImporter(filepath, name, description, unit, **metadata)

   Bases: :py:obj:`bw2io.importers.base_lcia.LCIAImporter`

   .. autoapi-inheritance-diagram:: bw2io.importers.excel_lcia.ExcelLCIAImporter
      :parts: 1
      :private-bases:

   Generic Excel LCIA importer.

   .. attribute:: format

      The file format. The default format is CSV.

      :type: str

   .. attribute:: extractor

      The file extractor class.

      :type: class

   Initializes the ExcelLCIAImporter object.

   :param filepath: The path to the Excel file.
   :type filepath: str
   :param name: The name of the LCIA method.
   :type name: tuple
   :param description: The description of the LCIA method.
   :type description: str
   :param unit: The unit of the LCIA method.
   :type unit: str
   :param \*\*metadata: The metadata associated with the LCIA method.

   .. py:attribute:: extractor

      

   .. py:attribute:: format
      :value: 'Excel'

      


.. py:function:: as_dicts(obj)

   Converts a 2D list to a list of dictionaries.

   :param obj: The 2D list to be converted.
   :type obj: list

   :returns: The list of dictionaries.
   :rtype: list


