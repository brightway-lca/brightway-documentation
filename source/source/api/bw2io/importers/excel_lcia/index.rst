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

   Generic CSV LCIA importer

   .. py:attribute:: extractor

      

   .. py:attribute:: format
      :value: 'CSV'

      


.. py:class:: ExcelLCIAImporter(filepath, name, description, unit, **metadata)

   Bases: :py:obj:`bw2io.importers.base_lcia.LCIAImporter`

   .. autoapi-inheritance-diagram:: bw2io.importers.excel_lcia.ExcelLCIAImporter
      :parts: 1
      :private-bases:

   Generic Excel LCIA importer.

   See the `documentation <https://2.docs.brightway.dev/intro.html#importing-lcia-methods-from-the-standard-excel-template>`__.


   .. py:attribute:: extractor

      

   .. py:attribute:: format
      :value: 'Excel'

      


.. py:function:: as_dicts(obj)


