:py:mod:`bw2regional.gis_tasks`
===============================

.. py:module:: bw2regional.gis_tasks


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2regional.gis_tasks.raster_as_extension_table
   bw2regional.gis_tasks.calculate_intersection



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2regional.gis_tasks.pandarus
   bw2regional.gis_tasks.CPU_COUNT


.. py:data:: pandarus
   

   

.. py:data:: CPU_COUNT
   

   

.. py:function:: raster_as_extension_table(vector, raster, name=None, engine=remote, overwrite=False)


.. py:function:: calculate_intersection(first, second, engine=remote, overwrite=False, cpus=None)

   Calculate and write areal intersections between two vector geocollections


