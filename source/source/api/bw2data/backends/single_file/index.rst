:py:mod:`bw2data.backends.single_file`
======================================

.. py:module:: bw2data.backends.single_file


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   database/index.rst
   proxies/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.backends.single_file.Activity
   bw2data.backends.single_file.Exchange
   bw2data.backends.single_file.SingleFileDatabase




.. py:class:: Activity(key, data={})

   Bases: :py:obj:`bw2data.proxies.ActivityProxyBase`

   .. autoapi-inheritance-diagram:: bw2data.backends.single_file.Activity
      :parts: 1
      :private-bases:

   A MutableMapping is a generic container for associating
   key/value pairs.

   This class provides concrete generic implementations of all
   methods except for __getitem__, __setitem__, __delitem__,
   __iter__, and __len__.

   .. py:method:: biosphere()


   .. py:method:: exchanges()


   .. py:method:: save()


   .. py:method:: technosphere()


   .. py:method:: upstream(*args, **kwargs)



.. py:class:: Exchange(data, *args, **kwargs)

   Bases: :py:obj:`bw2data.proxies.ExchangeProxyBase`

   .. autoapi-inheritance-diagram:: bw2data.backends.single_file.Exchange
      :parts: 1
      :private-bases:

   Simple proxy for an exchange between activity datasets. Makes manipulation and use in command line more convenient.

   .. warning:: This proxy is read only! To save changes to a dataset, you will need to work with the raw database data.

   Usually these proxies are created by the :ref:`activity`, but you can instantiate one with the dictionary of exchange data and an Activity proxy of the consuming activity:

   .. code-block:: python

       exchange = Exchange({"my exchange data": "goes here"})

   Properties:

   * ``input``: Returns :ref:`activity`
   * ``output``: Returns :ref:`activity`
   * ``amount``
   * ``uncertainty``: Returns dictionary of uncertainty data
   * ``uncertainty_type``: Returns ``stats_arrays`` uncertainty type
   * ``unit``



   .. py:method:: save()



.. py:class:: SingleFileDatabase(name)

   Bases: :py:obj:`bw2data.backends.base.LCIBackend`

   .. autoapi-inheritance-diagram:: bw2data.backends.single_file.SingleFileDatabase
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



