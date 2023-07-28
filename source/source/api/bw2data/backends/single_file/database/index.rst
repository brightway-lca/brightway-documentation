:py:mod:`bw2data.backends.single_file.database`
===============================================

.. py:module:: bw2data.backends.single_file.database


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.backends.single_file.database.SingleFileDatabase




.. py:class:: SingleFileDatabase(name)

   Bases: :py:obj:`bw2data.backends.base.LCIBackend`

   .. autoapi-inheritance-diagram:: bw2data.backends.single_file.database.SingleFileDatabase
      :parts: 1
      :private-bases:

   A data store for LCI databases where each database is stored as a ``pickle`` file.

   Databases are automatically versioned. See below for reversion, etc. methods

   :param \*name*: Name of the database to manage.
   :type \*name*: str

   .. py:property:: filename

      Remove filesystem-unsafe characters and perform unicode normalization on ``self.name`` using :func:`.utils.safe_filename`.

   .. py:property:: version

      The current version number (integer) of this database.

      :returns: Version number

   .. py:attribute:: backend
      :value: 'singlefile'

      

   .. py:attribute:: validator

      

   .. py:method:: filename_for_version(version=None)

      Filename for given version; Default is current version.

      :returns: Filename (not path)


   .. py:method:: filepath_intermediate(version=None)


   .. py:method:: get(code)

      Get Activity proxy for this dataset


   .. py:method:: load(version=None, **kwargs)

      Load the intermediate data for this database.

      Can also load previous versions of this database's intermediate data.

      :param \* *version*: Version of the database to load. Default ``version`` is the latest version.
      :type \* *version*: int

      :returns: The intermediate data, a dictionary.


   .. py:method:: make_latest_version()

      Make the current version the latest version.

      Requires loading data because a new intermediate data file is created.


   .. py:method:: register(**kwargs)

      Register a database with the metadata store.

      Databases must be registered before data can be written.



   .. py:method:: revert(version)

      Return data to a previous state.

      .. warning:: Reverting can lead to data loss, e.g. if you revert from version 3 to version 1, and then save your database, you will overwrite version 2. Use :meth:`.make_latest_version` before saving, which will set the current version to 4.

      :param \* *version*: Number of the version to revert to.
      :type \* *version*: int


   .. py:method:: versions()

      Get a list of available versions of this database.

      :returns: List of (version, datetime created) tuples.


   .. py:method:: write(data, process=True)

      Serialize data to disk.

      :param \* *data*: Inventory data
      :type \* *data*: dict



