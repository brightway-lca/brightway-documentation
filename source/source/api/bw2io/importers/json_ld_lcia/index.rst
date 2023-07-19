:py:mod:`bw2io.importers.json_ld_lcia`
======================================

.. py:module:: bw2io.importers.json_ld_lcia


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.importers.json_ld_lcia.JSONLDLCIAImporter




.. py:class:: JSONLDLCIAImporter(dirpath)

   Bases: :py:obj:`bw2io.importers.base_lcia.LCIAImporter`

   .. autoapi-inheritance-diagram:: bw2io.importers.json_ld_lcia.JSONLDLCIAImporter
      :parts: 1
      :private-bases:

   Importer for the `OLCD JSON-LD LCIA data format <https://github.com/GreenDelta/olca-schema>`__.

   :param dirpath: Directory path for the JSON-LD data.
   :type dirpath: str

   .. attribute:: format

      Data format description.

      :type: str

   .. attribute:: extractor

      Extractor class for the JSON-LD data.

      :type: :class:`JSONLDExtractor`

   .. attribute:: data

      Extracted LCIA data.

      :type: dict

   .. attribute:: strategies

      List of strategies to apply to the LCIA data.

      :type: list

   .. method:: match_biosphere_by_id(database_name)

      Matches biosphere flows to a specified database by ID.

   Initialize the JSONLDLCIAImporter object.

   :param dirpath: Directory path for the JSON-LD data.
   :type dirpath: str

   :rtype: None

   .. py:attribute:: extractor

      

   .. py:attribute:: format
      :value: 'OLCA JSON-LD'

      

   .. py:method:: match_biosphere_by_id(database_name)

      Matches biosphere flows to a specified database by ID.

      :param database_name: Name of the biosphere database.
      :type database_name: str

      :rtype: None



