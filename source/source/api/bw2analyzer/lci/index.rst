:py:mod:`bw2analyzer.lci`
=========================

.. py:module:: bw2analyzer.lci


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2analyzer.lci.get_labeled_inventory



.. py:function:: get_labeled_inventory(lca: bw2calc.LCA) -> pandas.DataFrame

   Take an LCA's inventory matrix and labels its rows (biosphere) and columns (technosphere) with activity metadata.

   :param \* *lca*: LCA object whose life cycle inventory has been calculated previously.
   :type \* *lca*: bw2calc.LCA

   :returns: pd.DataFrame with activity information as row and column MultiIndices.


