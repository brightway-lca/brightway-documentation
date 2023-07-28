:py:mod:`bw2data.compat`
========================

.. py:module:: bw2data.compat


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.compat.Mapping
   bw2data.compat._Databases



Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.compat.get_database_filepath
   bw2data.compat.prepare_lca_inputs
   bw2data.compat.translate_key
   bw2data.compat.unpack



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2data.compat.databases


.. py:class:: Mapping

   A dictionary that maps object ids, like ``("Ecoinvent 2.2", 42)``, to integers.

   Used only for backwards compatibility; preferred method is now to look up the ids of activities directly in the SQlite database.

   .. py:method:: add(keys)


   .. py:method:: delete(keys)



.. py:class:: _Databases

   .. py:method:: clean()


   .. py:method:: flush()


   .. py:method:: set_dirty(name)



.. py:function:: get_database_filepath(functional_unit)

   Get filepaths for all databases in supply chain of `functional_unit`


.. py:function:: prepare_lca_inputs(demand=None, method=None, weighting=None, normalization=None, demands=None, remapping=True, demand_database_last=True)

   Prepare LCA input arguments in Brightway 2.5 style.


.. py:function:: translate_key(key)


.. py:function:: unpack(dct)


.. py:data:: databases

   

