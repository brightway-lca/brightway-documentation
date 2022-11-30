:py:mod:`bw2io.importers.excel_lcia`
====================================

.. py:module:: bw2io.importers.excel_lcia


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.importers.excel_lcia.ExcelLCIAImporter
   bw2io.importers.excel_lcia.CSVLCIAImporter



Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.importers.excel_lcia.as_dicts



.. py:function:: as_dicts(obj)


.. py:class:: ExcelLCIAImporter(filepath, name, description, unit, **metadata)

   Bases: :py:obj:`bw2io.importers.base_lcia.LCIAImporter`

   Generic Excel LCIA importer.

   See the `documentation <https://2.docs.brightway.dev/intro.html#importing-lcia-methods-from-the-standard-excel-template>`__.


   .. py:attribute:: format
      :annotation: = Excel

      

   .. py:attribute:: extractor
      

      


.. py:class:: CSVLCIAImporter(filepath, name, description, unit, **metadata)

   Bases: :py:obj:`ExcelLCIAImporter`

   Generic CSV LCIA importer

   .. py:attribute:: format
      :annotation: = CSV

      

   .. py:attribute:: extractor
      

      


