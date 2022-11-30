:py:mod:`bw2regional.loading`
=============================

.. py:module:: bw2regional.loading


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2regional.loading.Loading




.. py:class:: Loading(name)

   Bases: :py:obj:`bw2data.data_store.ProcessedDataStore`

   .. py:property:: filename

      Remove filesystem-unsafe characters and perform unicode normalization on ``self.name`` using :func:`.filesystem.safe_filename`.

   .. py:attribute:: _metadata
      

      

   .. py:attribute:: validator
      

      

   .. py:attribute:: matrix
      :annotation: = loading_matrix

      

   .. py:method:: add_geomappings(data)

      In theory, this shouldn't do anything, as all spatial units should be in defined by the method.


   .. py:method:: process(**extra_metadata)

      Process intermediate data from a Python dictionary to a `stats_arrays <https://pypi.python.org/pypi/stats_arrays/>`_ array, which is a `NumPy <http://numpy.scipy.org/>`_ `Structured <http://docs.scipy.org/doc/numpy/reference/generated/numpy.recarray.html#numpy.recarray>`_ `Array <http://docs.scipy.org/doc/numpy/user/basics.rec.html>`_. A structured array (also called record array) is a heterogeneous array, where each column has a different label and data type.

      Processed arrays are saved in the ``processed`` directory.

      If the uncertainty type is no uncertainty, undefined, or not specified, then the 'amount' value is used for 'loc' as well. This is needed for the random number generator.

      Doesn't return anything, but writes a file to disk.




