:py:mod:`bw2analyzer.report`
============================

.. py:module:: bw2analyzer.report


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2analyzer.report.SerializedLCAReport




.. py:class:: SerializedLCAReport(activity, method, iterations=10000, cpus=None, outliers=0.025)

   A complete LCA report (i.e. LCA score, Monte Carlo uncertainty analysis, contribution analysis) that can be serialized to a defined standard.

   .. py:attribute:: version
      :value: 2

      

   .. py:method:: calculate()

      Calculate LCA report data


   .. py:method:: get_force_directed(nodes, edges, lca)

      Get graph traversal results


   .. py:method:: get_monte_carlo()

      Get Monte Carlo results


   .. py:method:: get_treemap(nodes, edges, lca, unroll_cutoff=0.01, simplify_limit=0.1)


   .. py:method:: upload()

      Upload report data if allowed


   .. py:method:: write()

      Write report data to file



