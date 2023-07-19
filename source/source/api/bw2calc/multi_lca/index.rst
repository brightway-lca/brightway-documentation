:py:mod:`bw2calc.multi_lca`
===========================

.. py:module:: bw2calc.multi_lca


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2calc.multi_lca.InventoryMatrices
   bw2calc.multi_lca.MultiLCA




Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2calc.multi_lca.calculation_setups
   bw2calc.multi_lca.logger


.. py:class:: InventoryMatrices(biosphere_matrix, supply_arrays)


.. py:class:: MultiLCA(cs_name, log_config=None)

   Wrapper class for performing LCA calculations with many functional units and LCIA methods.

   Needs to be passed a ``calculation_setup`` name.

   This class does not subclass the `LCA` class, and performs all calculations upon instantiation.

   Initialization creates `self.results`, which is a NumPy array of LCA scores, with rows of functional units and columns of LCIA methods. Ordering is the same as in the `calculation_setup`.


   .. py:property:: all

      Get all possible databases by merging all functional units


.. py:data:: calculation_setups

   

.. py:data:: logger

   

