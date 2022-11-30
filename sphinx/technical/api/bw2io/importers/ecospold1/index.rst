:py:mod:`bw2io.importers.ecospold1`
===================================

.. py:module:: bw2io.importers.ecospold1


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.importers.ecospold1.SingleOutputEcospold1Importer
   bw2io.importers.ecospold1.NoIntegerCodesEcospold1Importer
   bw2io.importers.ecospold1.MultiOutputEcospold1Importer




.. py:class:: SingleOutputEcospold1Importer(filepath, db_name, use_mp=True, extractor=Ecospold1DataExtractor)

   Bases: :py:obj:`bw2io.importers.base_lci.LCIImporter`

   Import and process single-output datasets in the ecospold 1 format.

   Applies the following strategies:
   #. If only one exchange is a production exchange, that is the reference product
   #. Delete (unreliable) integer codes from extracted data
   #. Drop ``unspecified`` subcategories from biosphere flows
   #. Normalize biosphere flow categories to ecoinvent 3.1 standard
   #. Normalize biosphere flow names to ecoinvent 3.1 standard
   #. Remove locations from biosphere exchanges
   #. Create a ``code`` from the activity hash of the dataset
   #. Link biosphere exchanges to the default biosphere database
   #. Link internal technosphere exchanges

   :param \* *filepath*: Either a file or directory.
   :param \* *db_name*: Name of database to create.

   .. py:attribute:: format
      :annotation: = Ecospold1

      


.. py:class:: NoIntegerCodesEcospold1Importer(*args, **kwargs)

   Bases: :py:obj:`SingleOutputEcospold1Importer`

   Import and process single-output datasets in the ecospold 1 format.

   Applies the following strategies:
   #. If only one exchange is a production exchange, that is the reference product
   #. Delete (unreliable) integer codes from extracted data
   #. Drop ``unspecified`` subcategories from biosphere flows
   #. Normalize biosphere flow categories to ecoinvent 3.1 standard
   #. Normalize biosphere flow names to ecoinvent 3.1 standard
   #. Remove locations from biosphere exchanges
   #. Create a ``code`` from the activity hash of the dataset
   #. Link biosphere exchanges to the default biosphere database
   #. Link internal technosphere exchanges

   :param \* *filepath*: Either a file or directory.
   :param \* *db_name*: Name of database to create.


.. py:class:: MultiOutputEcospold1Importer(*args, **kwargs)

   Bases: :py:obj:`SingleOutputEcospold1Importer`

   Import and process mutli-output datasets in the ecospold 1 format.

   Works the same as the single-output importer, but first allocates multioutput datasets.


