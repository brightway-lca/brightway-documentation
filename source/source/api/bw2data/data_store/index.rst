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

   Base class for all Brightway2 data stores. Subclasses should define:

       * **metadata**: A :ref:`serialized-dict` instance, e.g. ``databases`` or ``methods``. The custom is that each type of data store has a new metadata store, so the data store ``Foo`` would have a metadata store ``foos``.
       * **validator**: A data validator. Optional. See bw2data.validate.


   .. py:property:: filename

      Remove filesystem-unsafe characters and perform unicode normalization on ``self.name`` using :func:`.filesystem.safe_filename`.

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

   Brightway2 data stores that can be processed to NumPy arrays.

   In addition to ``metadata`` and (optionally) ``validator``, subclasses should override ``add_geomappings``. This method takes the entire dataset, and loads objects to :ref:`geomapping` as needed.


   .. py:attribute:: matrix
      :value: 'unknown'

      

   .. py:method:: add_geomappings(data)

      Add objects to ``geomapping``, if necessary.

      :param \* *data*: The data
      :type \* *data*: object


   .. py:method:: datapackage()


   .. py:method:: dirpath_processed()


   .. py:method:: filename_processed()


   .. py:method:: filepath_processed()


   .. py:method:: process(**extra_metadata)

      Process intermediate data from a Python dictionary to a `stats_arrays <https://pypi.python.org/pypi/stats_arrays/>`_ array, which is a `NumPy <http://numpy.scipy.org/>`_ `Structured <http://docs.scipy.org/doc/numpy/reference/generated/numpy.recarray.html#numpy.recarray>`_ `Array <http://docs.scipy.org/doc/numpy/user/basics.rec.html>`_. A structured array (also called record array) is a heterogeneous array, where each column has a different label and data type.

      Processed arrays are saved in the ``processed`` directory.

      If the uncertainty type is no uncertainty, undefined, or not specified, then the 'amount' value is used for 'loc' as well. This is needed for the random number generator.

      Doesn't return anything, but writes a file to disk.



   .. py:method:: process_row(row)
      :abstractmethod:

      Translate data into a dictionary suitable for array inputs.

      See `bw_processing documentation <https://github.com/brightway-lca/bw_processing>`__.


   .. py:method:: validate(data)

      Validate data. Must be called manually.


   .. py:method:: write(data, process=True)

      Serialize intermediate data to disk.

      :param \* *data*: The data
      :type \* *data*: object



