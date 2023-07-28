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

      

   .. py:attribute:: dtype_fields
      :value: [(), (), (), ()]

      

   .. py:attribute:: validator

      

   .. py:method:: add_mappings(data)

      Add objects to ``mapping`` or ``geomapping``, if necessary.

      :param \* *data*: The data
      :type \* *data*: object


   .. py:method:: process_data(row)

      Translate data into correct order


   .. py:method:: write(data, process=True)

      Serialize intermediate data to disk.

      Sets the metadata key ``num_cfs`` automatically.



