:py:mod:`bw2data.data_store`
============================

.. py:module:: bw2data.data_store


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.data_store.DataStore
   bw2data.data_store.ProcessedDataStore




.. py:class:: DataStore(name)

   Bases: :py:obj:`object`

   Base class for all Brightway2 data stores. Subclasses should define:

       * **metadata**: A :ref:`serialized-dict` instance, e.g. ``databases`` or ``methods``. The custom is that each type of data store has a new metadata store, so the data store ``Foo`` would have a metadata store ``foos``.
       * **validator**: A data validator. Optional. See bw2data.validate.



   .. py:property:: filename

      Remove filesystem-unsafe characters and perform unicode normalization on ``self.name`` using :func:`.utils.safe_filename`.

   .. py:property:: registered


   .. py:attribute:: _intermediate_dir
      :value: 'intermediate'

      

   .. py:attribute:: _metadata

      

   .. py:attribute:: metadata

      

   .. py:attribute:: validator

      

   .. py:method:: _get_metadata()


   .. py:method:: _set_metadata(value)


   .. py:method:: backup()

      Save a backup to ``backups`` folder.

      :returns: File path of backup.


   .. py:method:: copy(name)

      Make a copy of this object with a new ``name``.

      This method only changes the name, but not any of the data or metadata.

      :param \* *name*: Name of the new object.
      :type \* *name*: object

      :returns: The new object.


   .. py:method:: deregister()

      Remove an object from the metadata store. Does not delete any files.


   .. py:method:: load()

      Load the intermediate data for this object.

      :returns: The intermediate data.


   .. py:method:: register(**kwargs)

      Register an object with the metadata store. Takes any number of keyword arguments.


   .. py:method:: validate(data)

      Validate data. Must be called manually.


   .. py:method:: write(data)

      Serialize intermediate data to disk.

      :param \* *data*: The data
      :type \* *data*: object



.. py:class:: ProcessedDataStore(name)

   Bases: :py:obj:`DataStore`

   .. autoapi-inheritance-diagram:: bw2data.data_store.ProcessedDataStore
      :parts: 1
      :private-bases:

   Brightway2 data stores that can be processed to NumPy arrays. In addition to ``metadata`` and (optionally) ``validator``, subclasses should define:

       * **dtype_fields**: A list of fields to construct a NumPy structured array, e.g. ``[('foo', np.int), ('bar', np.float)]``. Fields names **must** be bytestrings, not unicode (i.e. ``b"foo"`` instead of ``"foo"``). Uncertainty fields (``base_uncertainty_fields``) are added automatically.

   In order to use ``dtype_fields``, subclasses should override the method ``process_data``. This function takes rows of data, and returns the correct values for the custom dtype fields (as a tuple), **and** the ``amount`` field with its associated uncertainty. This second part is a little flexible - if there is no uncertainty, a number can be returned; otherwise, an uncertainty dictionary should be returned.

   Subclasses should also override ``add_mappings``. This method takes the entire dataset, and loads objects to :ref:`mapping` or :ref:`geomapping` as needed.



   .. py:property:: dtype

      Returns both the generic ``base_uncertainty_fields`` plus class-specific ``dtype_fields``. ``dtype`` determines the columns of the :ref:`processed array <processing-data>`.

   .. py:attribute:: base_uncertainty_fields
      :value: [(), (), (), (), (), (), (), ()]

      

   .. py:attribute:: dtype_fields

      

   .. py:method:: add_mappings(data)

      Add objects to ``mapping`` or ``geomapping``, if necessary.

      :param \* *data*: The data
      :type \* *data*: object


   .. py:method:: as_uncertainty_dict(value)

      Convert floats to ``stats_arrays`` uncertainty dict, if necessary


   .. py:method:: dtype_field_order(dtype=None)


   .. py:method:: filepath_processed()


   .. py:method:: process()

      Process intermediate data from a Python dictionary to a `stats_arrays <https://pypi.python.org/pypi/stats_arrays/>`_ array, which is a `NumPy <http://numpy.scipy.org/>`_ `Structured <http://docs.scipy.org/doc/numpy/reference/generated/numpy.recarray.html#numpy.recarray>`_ `Array <http://docs.scipy.org/doc/numpy/user/basics.rec.html>`_. A structured array (also called record array) is a heterogeneous array, where each column has a different label and data type.

      Processed arrays are saved in the ``processed`` directory.

      If the uncertainty type is no uncertainty, undefined, or not specified, then the 'amount' value is used for 'loc' as well. This is needed for the random number generator.

      Doesn't return anything, but writes a file to disk.




   .. py:method:: process_data(row)
      :abstractmethod:

      Translate data into correct order


   .. py:method:: validate(data)

      Validate data. Must be called manually.


   .. py:method:: write(data, process=True)

      Serialize intermediate data to disk.

      :param \* *data*: The data
      :type \* *data*: object



