:py:mod:`bw2data.method`
========================

.. py:module:: bw2data.method


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.method.Method




.. py:class:: Method(name)

   Bases: :py:obj:`bw2data.ia_data_store.ImpactAssessmentDataStore`

   .. autoapi-inheritance-diagram:: bw2data.method.Method
      :parts: 1
      :private-bases:

   A manager for an impact assessment method. This class can register or deregister methods, write intermediate data, process data to parameter arrays, validate, and copy methods.

   The Method class never holds intermediate data, but it can load or write intermediate data. The only attribute is *name*, which is the name of the method being managed.

   Instantiation does not load any data. If this method is not yet registered in the metadata store, a warning is written to ``stdout``.

   Methods are hierarchally structured, and this structure is preserved in the method name. It is a tuple of strings, like ``('ecological scarcity 2006', 'total', 'natural resources')``.

   The data schema for IA methods is:

   .. code-block:: python

           Schema([Any(
               [valid_tuple, maybe_uncertainty],         # site-generic
               [valid_tuple, maybe_uncertainty, object]  # regionalized
           )])

   where:
       * *valid_tuple* (tuple): A dataset identifier, like ``("biosphere", "CO2")``.
       * *maybe_uncertainty* (uncertainty dict or number): Either a number or an uncertainty dictionary.
       * *object* (object, optional) is a location identifier, used only for regionalized LCIA.

   :param \* *name*: Name of impact assessment method to manage.
   :type \* *name*: tuple

   .. py:attribute:: _metadata

      

   .. py:attribute:: matrix
      :value: 'characterization_matrix'

      

   .. py:attribute:: validator

      

   .. py:method:: add_geomappings(data)

      Add objects to ``geomapping``, if necessary.

      :param \* *data*: The data
      :type \* *data*: object


   .. py:method:: process(**extra_metadata)

      Process intermediate data from a Python dictionary to a `stats_arrays <https://pypi.python.org/pypi/stats_arrays/>`_ array, which is a `NumPy <http://numpy.scipy.org/>`_ `Structured <http://docs.scipy.org/doc/numpy/reference/generated/numpy.recarray.html#numpy.recarray>`_ `Array <http://docs.scipy.org/doc/numpy/user/basics.rec.html>`_. A structured array (also called record array) is a heterogeneous array, where each column has a different label and data type.

      Processed arrays are saved in the ``processed`` directory.

      If the uncertainty type is no uncertainty, undefined, or not specified, then the 'amount' value is used for 'loc' as well. This is needed for the random number generator.

      Doesn't return anything, but writes a file to disk.



   .. py:method:: process_row(row)

      Given ``(flow, amount, maybe location)``, return a dictionary for array insertion.


   .. py:method:: write(data, process=True)

      Serialize intermediate data to disk.

      Sets the metadata key ``num_cfs`` automatically.



