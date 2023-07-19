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

   Class for importing single-output ecospold2 format LCI databases.

   :raises MultiprocessingError: If an error occurs during multiprocessing.

   Initializes the SingleOutputEcospold2Importer class instance.

   :param dirpath: Path to the directory containing the ecospold2 file.
   :type dirpath: str
   :param db_name: Name of the LCI database.
   :type db_name: str
   :param extractor: Class for extracting data from the ecospold2 file, by default Ecospold2DataExtractor.
   :type extractor: class
   :param use_mp: Flag to indicate whether to use multiprocessing, by default True.
   :type use_mp: bool
   :param signal: Object to indicate the status of the import process, by default None.
   :type signal: object

   .. py:attribute:: format
      :value: 'Ecospold2'

      


