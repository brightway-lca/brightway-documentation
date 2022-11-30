:py:mod:`bw2data.utils`
=======================

.. py:module:: bw2data.utils


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.utils.safe_filename
   bw2data.utils.maybe_path
   bw2data.utils.natural_sort
   bw2data.utils.random_string
   bw2data.utils.combine_methods
   bw2data.utils.clean_exchanges
   bw2data.utils.as_uncertainty_dict
   bw2data.utils.uncertainify
   bw2data.utils.recursive_str_to_unicode
   bw2data.utils.combine_databases
   bw2data.utils.merge_databases
   bw2data.utils.download_file
   bw2data.utils.web_ui_accessible
   bw2data.utils.open_activity_in_webbrowser
   bw2data.utils.set_data_dir
   bw2data.utils.switch_data_directory
   bw2data.utils.create_in_memory_zipfile_from_directory
   bw2data.utils.get_node
   bw2data.utils.get_activity
   bw2data.utils.get_geocollection



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2data.utils.TYPE_DICTIONARY
   bw2data.utils.DOWNLOAD_URL
   bw2data.utils.POSITIVE_DISTRIBUTIONS


.. py:data:: TYPE_DICTIONARY
   

   

.. py:data:: DOWNLOAD_URL
   :annotation: = https://brightway.dev/data/

   

.. py:function:: safe_filename(*args, **kwargs)


.. py:function:: maybe_path(x)


.. py:function:: natural_sort(l)

   Sort the given list in the way that humans expect, e.g. 9 before 10.


.. py:function:: random_string(length=8)

   Generate a random string of letters and numbers.

   :param \* *length*: Length of string, default is 8
   :type \* *length*: int

   :returns: A string (not unicode)


.. py:function:: combine_methods(name, *ms)

   Combine LCIA methods by adding duplicate characterization factors.

   :param \* *ms*: Any number of method ids, e.g. ``("my method", "wow"), ("another method", "wheee")``.
   :type \* *ms*: one or more method id tuples

   :returns: The new Method instance.


.. py:function:: clean_exchanges(data)

   Make sure all exchange inputs are tuples, not lists.


.. py:data:: POSITIVE_DISTRIBUTIONS
   

   

.. py:function:: as_uncertainty_dict(value)

   Given either a number or a ``stats_arrays`` uncertainty dict, return an uncertainty dict


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


.. py:function:: recursive_str_to_unicode(data, encoding='utf8')

   Convert the strings inside a (possibly nested) python data structure to unicode strings using `encoding`.


.. py:function:: combine_databases(name, *dbs)

   Combine databases into new database called ``name``.


.. py:function:: merge_databases(parent_db, other)

   Merge ``other`` into ``parent_db``, including updating exchanges.

   All databases must be SQLite databases.

   ``parent_db`` and ``other`` should be the names of databases.

   Doesn't return anything.


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


.. py:function:: web_ui_accessible()

   Test if ``bw2-web`` is running and accessible. Returns ``True`` or ``False``.


.. py:function:: open_activity_in_webbrowser(activity)

   Open a dataset document in the Brightway2 web UI. Requires ``bw2-web`` to be running.

   ``activity`` is a dataset key, e.g. ``("foo", "bar")``.


.. py:function:: set_data_dir(dirpath, permanent=True)

   Set the Brightway2 data directory to ``dirpath``.

   If ``permanent`` is ``True``, then set ``dirpath`` as the default data directory.

   Creates ``dirpath`` if needed. Also creates basic directories, and resets metadata.



.. py:function:: switch_data_directory(dirpath)


.. py:function:: create_in_memory_zipfile_from_directory(path)


.. py:function:: get_node(**kwargs)


.. py:function:: get_activity(key=None, **kwargs)

   Support multiple ways to get exactly one activity node.

   ``key`` can be an integer or a key tuple.


.. py:function:: get_geocollection(location, default_global_location=False)

   conservative approach to finding geocollections. Won't guess about ecoinvent or other databases.


