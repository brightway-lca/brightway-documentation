:py:mod:`bw2regional.density`
=============================

.. py:module:: bw2regional.density


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2regional.density.get_area
   bw2regional.density.get_column_array
   bw2regional.density.divide_by_area



.. py:function:: get_area(lat1, lat2, width)

   Get area of a spherical quadrangle.

   lat1, lat2, and width should all be in degrees.

   Uses the formula derived and demonstrated in https://gis.stackexchange.com/questions/127165/more-accurate-way-to-calculate-area-of-rasters.


.. py:function:: get_column_array(affine, rows, width)


.. py:function:: divide_by_area(source_fp, destination_fp)

   Create a new raster file at ``destination_fp``, dividing the values in ``source_fp`` by their cell's area.

   Will raise an error is the CRS is not geographic, or the raster is rotated.


