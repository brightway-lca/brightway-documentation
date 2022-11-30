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


.. py:data:: EMISSIONS_CATEGORIES
   

   

.. py:class:: Ecospold2BiosphereImporter(name='biosphere3', version='3.9')

   Bases: :py:obj:`bw2io.importers.base_lci.LCIImporter`

   Base class for format-specific importers.

   Defines workflow for applying strategies.

   Takes a database name (string) as initialization parameter.


   .. py:attribute:: format
      :annotation: = Ecoinvent XML

      

   .. py:method:: extract(version)



