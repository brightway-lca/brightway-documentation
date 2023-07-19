:py:mod:`bw2io.importers.ecospold2_biosphere`
=============================================

.. py:module:: bw2io.importers.ecospold2_biosphere


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.importers.ecospold2_biosphere.Ecospold2BiosphereImporter




Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.importers.ecospold2_biosphere.EMISSIONS_CATEGORIES


.. py:class:: Ecospold2BiosphereImporter(name='biosphere3', version='3.9')

   Bases: :py:obj:`bw2io.importers.base_lci.LCIImporter`

   .. autoapi-inheritance-diagram:: bw2io.importers.ecospold2_biosphere.Ecospold2BiosphereImporter
      :parts: 1
      :private-bases:

   Import elementary flows from ecoinvent xml format.

   .. attribute:: format

      Format of the data: "Ecoinvent XML".

      :type: str

   .. attribute:: db_name

      Name of the database.

      :type: str

   .. attribute:: data

      Extracted data from the xml file.

      :type: list

   .. attribute:: strategies

      List of functions to apply to the extracted data.

      :type: list

   .. seealso::

      :obj:`https`
          //github.com/brightway-lca/brightway2-io/tree/main/bw2io/strategies

   Initialize the importer.

   :param name: Name of the database, by default "biosphere3".
   :type name: str, optional
   :param version: Version of the database, by default "3.9".
   :type version: str, optional

   .. py:attribute:: format
      :value: 'Ecoinvent XML'

      

   .. py:method:: extract(version)

      Extract elementary flows from the xml file.

      :param version: Version of the database.
      :type version: str

      :returns: Extracted data from the xml file.
      :rtype: list



.. py:data:: EMISSIONS_CATEGORIES

   

