:py:mod:`bw2io.importers.ecospold1_lcia`
========================================

.. py:module:: bw2io.importers.ecospold1_lcia


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.importers.ecospold1_lcia.Ecospold1LCIAImporter




.. py:class:: Ecospold1LCIAImporter(filepath, biosphere=None)

   Bases: :py:obj:`bw2io.importers.base_lcia.LCIAImporter`

   .. autoapi-inheritance-diagram:: bw2io.importers.ecospold1_lcia.Ecospold1LCIAImporter
      :parts: 1
      :private-bases:

   Importer for Ecospold1 LCIA format.

   .. attribute:: format

      The format of the LCIA data, which is "Ecospold1 LCIA".

      :type: str

   .. attribute:: data

      The LCIA data extracted from the Ecospold1 LCIA file.

      :type: dict

   Initialize the Ecospold1LCIAImporter instance.

   :param filepath: Path to the Ecospold1 LCIA file.
   :type filepath: str
   :param biosphere: Biosphere database to use. If None, the default biosphere database will be used.
   :type biosphere: bw2data.BiosphereDatabase, optional

   .. py:attribute:: format
      :value: 'Ecospold1 LCIA'

      


