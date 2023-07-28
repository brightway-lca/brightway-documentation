:py:mod:`bw2data.utils`
=======================

.. py:module:: bw2data.utils


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.utils.clean_exchanges
   bw2data.utils.combine_databases
   bw2data.utils.combine_methods
   bw2data.utils.create_in_memory_zipfile_from_directory
   bw2data.utils.download_file
   bw2data.utils.get_activity
   bw2data.utils.merge_databases
   bw2data.utils.natural_sort
   bw2data.utils.open_activity_in_webbrowser
   bw2data.utils.python_2_unicode_compatible
   bw2data.utils.random_string
   bw2data.utils.recursive_str_to_unicode
   bw2data.utils.set_data_dir
   bw2data.utils.uncertainify
   bw2data.utils.web_ui_accessible



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2data.utils.DOWNLOAD_URL
   bw2data.utils.MAX_INT_32
   bw2data.utils.TYPE_DICTIONARY
   bw2data.utils.numpy_string


.. py:function:: clean_exchanges(data)

   Make sure all exchange inputs are tuples, not lists.


.. py:function:: combine_databases(name, *dbs)

   Combine databases into new database called ``name``.


.. py:function:: combine_methods(name, *ms)

   Combine LCIA methods by adding duplicate characterization factors.

   :param \* *ms*: Any number of method ids, e.g. ``("my method", "wow"), ("another method", "wheee")``.
   :type \* *ms*: one or more method id tuples

   :returns: The new Method instance.


.. py:function:: create_in_memory_zipfile_from_directory(path)


.. py:function:: download_file(filename, directory='downloads', url=None)

   Download a file and write it to disk in ``downloads`` directory.

   If ``url`` is None, uses the Brightway2 data base URL. ``url`` should everything up to the filename, such that ``url`` + ``filename`` is the valid complete URL to download from.

   Streams download to reduce memory usage.

   :param \* *filename*: The filename to download.
   :type \* *filename*: str
   :param \* *directory*: Directory to save the file. Created if it doesn't already exist.
   :type \* *directory*: str, optional
   :param \* *url*: URL where the file is located, if not the default Brightway data URL.
   :type \* *url*: str, optional

   :returns: The path of the created file.


.. py:function:: get_activity(key)


.. py:function:: merge_databases(parent_db, other)

   Merge ``other`` into ``parent_db``, including updating exchanges.

   All databases must be SQLite databases.

   ``parent_db`` and ``other`` should be the names of databases.

   Doesn't return anything.


.. py:function:: natural_sort(l)

   Sort the given list in the way that humans expect, e.g. 9 before 10.


.. py:function:: open_activity_in_webbrowser(activity)

   Open a dataset document in the Brightway2 web UI. Requires ``bw2-web`` to be running.

   ``activity`` is a dataset key, e.g. ``("foo", "bar")``.


.. py:function:: python_2_unicode_compatible(cls)

   Adaptation of function in future library which was causing recursion.

   We check and define __unicode__ only if it doesn't exist already.

   A decorator that defines __unicode__ and __str__ methods under Python
   2. Under Python 3, this decorator is a no-op.



.. py:function:: random_string(length=8)

   Generate a random string of letters and numbers.

   :param \* *length*: Length of string, default is 8
   :type \* *length*: int

   :returns: A string (not unicode)


.. py:function:: recursive_str_to_unicode(data, encoding='utf8')

   Convert the strings inside a (possibly nested) python data structure to unicode strings using `encoding`.


.. py:function:: set_data_dir(dirpath, permanent=True)

   Set the Brightway2 data directory to ``dirpath``.

   If ``permanent`` is ``True``, then set ``dirpath`` as the default data directory.

   Creates ``dirpath`` if needed. Also creates basic directories, and resets metadata.



.. py:function:: uncertainify(data, distribution=None, bounds_factor=0.1, sd_factor=0.1)

   Add some rough uncertainty to exchanges.

   .. warning:: This function only changes exchanges with no uncertainty type or uncertainty type ``UndefinedUncertainty``, and does not change production exchanges!

   Can only apply normal or uniform uncertainty distributions; default is uniform. Distribution, if specified, must be a ``stats_array`` uncertainty object.

   ``data`` is a LCI data dictionary.

   If using the normal distribution:

   * ``sd_factor`` will be multiplied by the mean to calculate the standard deviation.
   * If no bounds are desired, set ``bounds_factor`` to ``None``.
   * Otherwise, the bounds will be ``[(1 - bounds_factor) * mean, (1 + bounds_factor) * mean]``.

   If using the uniform distribution, then the bounds are ``[(1 - bounds_factor) * mean, (1 + bounds_factor) * mean]``.

   Returns the modified data.



.. py:function:: web_ui_accessible()

   Test if ``bw2-web`` is running and accessible. Returns ``True`` or ``False``.


.. py:data:: DOWNLOAD_URL
   :value: 'https://brightwaylca.org/data/'

   

.. py:data:: MAX_INT_32
   :value: 4294967295

   

.. py:data:: TYPE_DICTIONARY

   

.. py:data:: numpy_string

   

