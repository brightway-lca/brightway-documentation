:py:mod:`bw2calc.speed_test`
============================

.. py:module:: bw2calc.speed_test


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2calc.speed_test.SpeedTest




.. py:class:: SpeedTest

   Bases: :py:obj:`object`

   Compare speed of sparse matrix operations on this machine compared to a reference machine.

   .. py:attribute:: density
      :value: 0.02

      

   .. py:attribute:: seed
      :value: 42

      

   .. py:attribute:: size
      :value: 1000

      

   .. py:method:: get_demand_vector()


   .. py:method:: get_sparse_matrix()

      Adapted from scipy to use seeded RNG


   .. py:method:: ratio()

      On the reference machine, this takes about 5.85 seconds


   .. py:method:: test()



