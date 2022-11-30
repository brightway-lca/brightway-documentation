:py:mod:`bw2regional.meta`
==========================

.. py:module:: bw2regional.meta


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2regional.meta.Loadings
   bw2regional.meta.Intersections
   bw2regional.meta.Geocollections
   bw2regional.meta.Topocollections
   bw2regional.meta.ExtensionTables




Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2regional.meta.extension_tables
   bw2regional.meta.geocollections
   bw2regional.meta.intersections
   bw2regional.meta.loadings
   bw2regional.meta.topocollections


.. py:class:: Loadings(dirpath=None)

   Bases: :py:obj:`bw2data.serialization.SerializedDict`

   Metadata on regionalized LCIA weightings.

   .. py:attribute:: filename
      :annotation: = loadings.json

      


.. py:class:: Intersections(dirpath=None)

   Bases: :py:obj:`bw2data.serialization.CompoundJSONDict`

   Areal intersections between the elements of two geo- or topocollections

   .. py:attribute:: filename
      :annotation: = intersections.json

      


.. py:class:: Geocollections(dirpath=None)

   Bases: :py:obj:`bw2data.serialization.SerializedDict`

   Metadata for spatial data sets.

   .. py:attribute:: filename
      :annotation: = geocollections.json

      

   .. py:method:: __setitem__(key, value)



.. py:class:: Topocollections(dirpath=None)

   Bases: :py:obj:`Geocollections`

   Mappings from geocollections to a set of topographical face ids.

   .. py:attribute:: filename
      :annotation: = topocollections.json

      

   .. py:method:: __setitem__(key, value)



.. py:class:: ExtensionTables(dirpath=None)

   Bases: :py:obj:`bw2data.serialization.SerializedDict`

   Metadata for extension tables that give loadings on a third spatial scale.

   .. py:attribute:: filename
      :annotation: = extension-tables.json

      


.. py:data:: extension_tables
   

   

.. py:data:: geocollections
   

   

.. py:data:: intersections
   

   

.. py:data:: loadings
   

   

.. py:data:: topocollections
   

   

