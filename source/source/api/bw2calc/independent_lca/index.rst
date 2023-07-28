:py:mod:`bw2calc.independent_lca`
=================================

.. py:module:: bw2calc.independent_lca


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2calc.independent_lca.IndependentLCAMixin




.. py:class:: IndependentLCAMixin

   Bases: :py:obj:`object`

   Mixin that allows `method`, etc. to be filepaths or ``np.ndarray`` instead of DataStore object names.

   Removes dependency on `bw2data`.

   .. py:method:: fix_dictionaries()

      Don't adjust dictionaries even if ``bw2data`` is present, as functional unit is an integer.


   .. py:method:: get_array_filepaths()

      Pass through already correct values



