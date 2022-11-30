:py:mod:`bw2regional.intersection`
==================================

.. py:module:: bw2regional.intersection


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2regional.intersection.Intersection




.. py:class:: Intersection(name)

   Bases: :py:obj:`bw2data.ia_data_store.ImpactAssessmentDataStore`

   .. py:attribute:: _metadata
      

      

   .. py:attribute:: validator
      

      

   .. py:attribute:: matrix
      :annotation: = intersection_matrix

      

   .. py:method:: add_geomappings(data)

      Add all geographic units in both geocollections to ``geomapping``, the master location list.

      Called automatically when data is written.


   .. py:method:: create_reversed_intersection()

      Create (B, A) intersection from (A, B).


   .. py:method:: process(**extra_metadata)

      Process intermediate data from a Python dictionary to a `stats_arrays <https://pypi.python.org/pypi/stats_arrays/>`_ array, which is a `NumPy <http://numpy.scipy.org/>`_ `Structured <http://docs.scipy.org/doc/numpy/reference/generated/numpy.recarray.html#numpy.recarray>`_ `Array <http://docs.scipy.org/doc/numpy/user/basics.rec.html>`_. A structured array (also called record array) is a heterogeneous array, where each column has a different label and data type.

      Processed arrays are saved in the ``processed`` directory.

      If the uncertainty type is no uncertainty, undefined, or not specified, then the 'amount' value is used for 'loc' as well. This is needed for the random number generator.

      Doesn't return anything, but writes a file to disk.




