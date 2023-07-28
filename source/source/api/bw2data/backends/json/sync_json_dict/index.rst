:py:mod:`bw2data.backends.json.sync_json_dict`
==============================================

.. py:module:: bw2data.backends.json.sync_json_dict


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.backends.json.sync_json_dict.SynchronousJSONDict
   bw2data.backends.json.sync_json_dict.frozendict




.. py:class:: SynchronousJSONDict(dirpath, dirname)

   Bases: :py:obj:`collections.abc.MutableMapping`

   .. autoapi-inheritance-diagram:: bw2data.backends.json.sync_json_dict.SynchronousJSONDict
      :parts: 1
      :private-bases:

   A dictionary which stores each value as a separate file on disk. Values are loaded asynchronously (i.e. only as needed), but saved synchronously (i.e. immediately).

   Dictionary keys are strings, and do not correspond with filenames. The utility function `safe_filename` is used to translate keys into allowable filenames, and a separate mapping dictionary is kept to map dictionary keys to filenames.

   Retrieving a key returns a ``frozendict``, which can't be modified. This is to make sure that all changes get synced to disk. To change a dataset you must replace it completely, i.e. this won't work (it will raise an ``AttributeError``):

   .. code-block:: python

       my_sync_dict['foo']['bar'] = 'baz'

   Instead, you must do:

   .. code-block:: python

       my_sync_dict['foo'] = {'bar': 'baz'}

   After which the 'foo' file would be updated.


   .. py:method:: _delete_file(key)

      Delete the file associated with key ``key``.


   .. py:method:: _load_file(key)

      Load the file for key ``key``.


   .. py:method:: _save_file(key, data)

      Save data ``data`` to file for key ``key``.


   .. py:method:: filepath(key)

      Use :func:`bw2data.utils.safe_filename` to get filename for key ``key``.


   .. py:method:: from_json(data)

      Change exchange `inputs` from lists to tuples (as there is no distinction in JSON, but Python only allows tuples as dictionary keys).


   .. py:method:: keys()

      D.keys() -> a set-like object providing a view on D's keys



.. py:class:: frozendict(*args, **kw)

   Bases: :py:obj:`dict`

   .. autoapi-inheritance-diagram:: bw2data.backends.json.sync_json_dict.frozendict
      :parts: 1
      :private-bases:

   A dictionary that can be created but not modified.

   From http://code.activestate.com/recipes/414283-frozen-dictionaries/

   Initialize self.  See help(type(self)) for accurate signature.

   .. py:attribute:: _blocked_attribute

      

   .. py:method:: _blocked_attribute()



