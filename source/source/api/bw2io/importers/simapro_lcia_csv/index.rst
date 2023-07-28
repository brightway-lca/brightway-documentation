:py:mod:`bw2io.importers.simapro_lcia_csv`
==========================================

.. py:module:: bw2io.importers.simapro_lcia_csv


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.importers.simapro_lcia_csv.SimaProLCIACSVImporter




.. py:class:: SimaProLCIACSVImporter(filepath, biosphere=None, delimiter=';', encoding='latin-1', normalize_biosphere=True)

   Bases: :py:obj:`bw2io.importers.base_lcia.LCIAImporter`

   .. autoapi-inheritance-diagram:: bw2io.importers.simapro_lcia_csv.SimaProLCIACSVImporter
      :parts: 1
      :private-bases:

   Importer for SimaPro CSV LCIA data format.

   :param filepath: Path to the SimaPro CSV LCIA file.
   :type filepath: str
   :param biosphere: Name of the biosphere database to use. Default is None, which uses the current
                     project's default biosphere.
   :type biosphere: str, optional
   :param delimiter: Delimiter used in the CSV file. Default is ';'.
   :type delimiter: str, optional
   :param encoding: Character encoding used in the CSV file. Default is 'latin-1'.
   :type encoding: str, optional
   :param normalize_biosphere: Whether to normalize biosphere flows using the included strategies.
                               Default is True.
   :type normalize_biosphere: bool, optional

   .. rubric:: Notes

   This importer extracts SimaPro CSV LCIA data.

   If ``normalize_biosphere=True``, the following strategies are applied:

   * ``normalize_units``
   * ``set_biosphere_type``
   * ``normalize_simapro_biosphere_categories``
   * ``normalize_simapro_biosphere_names``

   .. py:attribute:: format
      :value: 'SimaPro CSV LCIA'

      


