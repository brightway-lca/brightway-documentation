:py:mod:`bw2io.importers.ecospold1`
===================================

.. py:module:: bw2io.importers.ecospold1


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.importers.ecospold1.MultiOutputEcospold1Importer
   bw2io.importers.ecospold1.NoIntegerCodesEcospold1Importer
   bw2io.importers.ecospold1.SingleOutputEcospold1Importer




.. py:class:: MultiOutputEcospold1Importer(*args, **kwargs)

   Bases: :py:obj:`SingleOutputEcospold1Importer`

   .. autoapi-inheritance-diagram:: bw2io.importers.ecospold1.MultiOutputEcospold1Importer
      :parts: 1
      :private-bases:

   Import and process multi-output datasets in the ecospold 1 format.

   Works the same as the single-output importer, but first allocates multioutput datasets.

   .. attribute:: strategies

      A list of strategies that the importer applies to process the dataset.

      :type: list

   :rtype: None

   Initialize MultiOutputEcospold1Importer.

   :param \*args: Variable length argument list.
   :type \*args: tuple
   :param \*\*kwargs: Arbitrary keyword arguments.
   :type \*\*kwargs: dict

   :rtype: None


.. py:class:: NoIntegerCodesEcospold1Importer(*args, **kwargs)

   Bases: :py:obj:`SingleOutputEcospold1Importer`

   .. autoapi-inheritance-diagram:: bw2io.importers.ecospold1.NoIntegerCodesEcospold1Importer
      :parts: 1
      :private-bases:

   An importer class that deletes integer codes from ecospold1 datasets.

   :param SingleOutputEcospold1Importer: The base importer class.
   :type SingleOutputEcospold1Importer: class

   .. attribute:: strategies

      A list of strategies that the importer applies to process the dataset.

      :type: list

   :rtype: None

   Initialize NoIntegerCodesEcospold1Importer.

   :param \*args: Variable length argument list.
   :type \*args: tuple
   :param \*\*kwargs: Arbitrary keyword arguments.
   :type \*\*kwargs: dict

   :rtype: None


.. py:class:: SingleOutputEcospold1Importer(filepath, db_name, use_mp=True, extractor=Ecospold1DataExtractor)

   Bases: :py:obj:`bw2io.importers.base_lci.LCIImporter`

   .. autoapi-inheritance-diagram:: bw2io.importers.ecospold1.SingleOutputEcospold1Importer
      :parts: 1
      :private-bases:

   Import and process single-output datasets in the ecospold 1 format.

   .. rubric:: Notes

   Applies the following strategies:
   1. If only one exchange is a production exchange, that is the reference product.
   2. Delete (unreliable) integer codes from extracted data.
   3. Drop ``unspecified`` subcategories from biosphere flows.
   4. Normalize biosphere flow categories to ecoinvent 3.1 standard.
   5. Normalize biosphere flow names to ecoinvent 3.1 standard.
   6. Remove locations from biosphere exchanges.
   7. Create a ``code`` from the activity hash of the dataset.
   8. Link biosphere exchanges to the default biosphere database.
   9. Link internal technosphere exchanges.

   :param filepath: File or directory path.
   :type filepath: str or Path
   :param db_name: Name of database to create.
   :type db_name: str
   :param use_mp: Whether to use multiprocessing. Default is True.
   :type use_mp: bool, optional
   :param extractor: Data extractor to use. Default is Ecospold1DataExtractor.
   :type extractor: Type[Ecospold1DataExtractor], optional

   .. py:attribute:: format
      :value: 'Ecospold1'

      


