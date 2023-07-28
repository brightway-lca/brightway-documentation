:py:mod:`bw2io.importers.ecospold2`
===================================

.. py:module:: bw2io.importers.ecospold2


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.importers.ecospold2.SingleOutputEcospold2Importer




.. py:class:: SingleOutputEcospold2Importer(dirpath, db_name, extractor=Ecospold2DataExtractor, use_mp=True, signal=None)

   Bases: :py:obj:`bw2io.importers.base_lci.LCIImporter`

   .. autoapi-inheritance-diagram:: bw2io.importers.ecospold2.SingleOutputEcospold2Importer
      :parts: 1
      :private-bases:

   Base class for format-specific importers.

   Defines workflow for applying strategies.

   Takes a database name (string) as initialization parameter.


   .. py:attribute:: format
      :value: 'Ecospold2'

      


