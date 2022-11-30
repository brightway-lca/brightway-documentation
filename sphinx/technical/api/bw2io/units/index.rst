:py:mod:`bw2io.units`
=====================

.. py:module:: bw2io.units


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.units.get_default_units_migration_data
   bw2io.units.get_unusual_units_migration_data



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.units.UNITS_NORMALIZATION
   bw2io.units.normalize_units
   bw2io.units.DEFAULT_UNITS_CONVERSION
   bw2io.units._USED_IN_ECOINVENT


.. py:data:: UNITS_NORMALIZATION
   

   

.. py:data:: normalize_units
   

   

.. py:data:: DEFAULT_UNITS_CONVERSION
   :annotation: = [['PJ', 'megajoule', 1000000000.0], ['J', 'megajoule', 1e-06], ['Nm3 Europe', 'megajoule',...

   

.. py:function:: get_default_units_migration_data()


.. py:data:: _USED_IN_ECOINVENT
   

   

.. py:function:: get_unusual_units_migration_data()

   Only convert units that are not used in ecoinvent at all


