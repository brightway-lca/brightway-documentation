:py:mod:`bw2regional.errors`
============================

.. py:module:: bw2regional.errors


Module Contents
---------------

.. py:exception:: BW2RegionalizationError

   Bases: :py:obj:`Exception`

   Base class for BW2 regionalization errors


.. py:exception:: UnprocessedDatabase

   Bases: :py:obj:`BW2RegionalizationError`

   A ``Database`` object doesn't have a list of reference geocollections.


.. py:exception:: SiteGenericMethod

   Bases: :py:obj:`BW2RegionalizationError`

   This ``Method`` doesn't have links to ``geocollections``, making it site-generic.


.. py:exception:: MissingIntersection

   Bases: :py:obj:`BW2RegionalizationError`

   Missing an ``Intersection`` object and its data needed for regionalized LCA


.. py:exception:: GeocollectionsMismatch

   Bases: :py:obj:`BW2RegionalizationError`

   Base class for BW2 regionalization errors


.. py:exception:: MissingSpatialSourceData

   Bases: :py:obj:`BW2RegionalizationError`

   Base class for BW2 regionalization errors


.. py:exception:: TopologyError

   Bases: :py:obj:`BW2RegionalizationError`

   Inventory includes locations for which no topology data is available


.. py:exception:: IncompleteSpatialDefinition

   Bases: :py:obj:`BW2RegionalizationError`

   Given metadata is not enough to understand a spatial data source


.. py:exception:: WindowsPathCharacterLimit

   Bases: :py:obj:`BW2RegionalizationError`

   Windows has an absolute limit of 255 characters in a filepath


