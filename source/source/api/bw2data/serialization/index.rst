:py:mod:`bw2data.serialization`
===============================

.. py:module:: bw2data.serialization


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.serialization.CompoundJSONDict
   bw2data.serialization.JsonSanitizer
   bw2data.serialization.JsonWrapper
   bw2data.serialization.PickledDict
   bw2data.serialization.SerializedDict




Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2data.serialization.anyjson


.. py:class:: CompoundJSONDict(dirpath=None)

   Bases: :py:obj:`SerializedDict`

   .. autoapi-inheritance-diagram:: bw2data.serialization.CompoundJSONDict
      :parts: 1
      :private-bases:

   Subclass of ``SerializedDict`` that allows tuples as dictionary keys (not allowed in JSON).

   .. py:method:: pack(data)

      Transform the dictionary to a list because JSON can't handle lists as keys


   .. py:method:: unpack(data)

      Transform data back to a dictionary



.. py:class:: JsonSanitizer

   Bases: :py:obj:`object`

   .. py:method:: load(data)
      :classmethod:


   .. py:method:: sanitize(data)
      :classmethod:



.. py:class:: JsonWrapper

   Bases: :py:obj:`object`

   .. py:method:: dump(data, filepath)
      :classmethod:


   .. py:method:: dump_bz2(data, filepath)
      :classmethod:


   .. py:method:: dumps(data)
      :classmethod:


   .. py:method:: load(file)
      :classmethod:


   .. py:method:: load_bz2(filepath)
      :classmethod:


   .. py:method:: loads(data)
      :classmethod:



.. py:class:: PickledDict(dirpath=None)

   Bases: :py:obj:`SerializedDict`

   .. autoapi-inheritance-diagram:: bw2data.serialization.PickledDict
      :parts: 1
      :private-bases:

   Subclass of ``SerializedDict`` that uses the pickle format instead of JSON.

   .. py:method:: deserialize()

      Load the serialized data. Can be replaced with other serialization formats.


   .. py:method:: serialize()

      Method to do the actual serialization. Can be replaced with other serialization formats.

      :param \* *filepath*: Provide an alternate filepath (e.g. for backup).
      :type \* *filepath*: str, optional



.. py:class:: SerializedDict(dirpath=None)

   Bases: :py:obj:`collections.abc.MutableMapping`

   .. autoapi-inheritance-diagram:: bw2data.serialization.SerializedDict
      :parts: 1
      :private-bases:

   Base class for dictionary that can be `serialized <http://en.wikipedia.org/wiki/Serialization>`_ to or unserialized from disk. Uses JSON as its storage format. Has most of the methods of a dictionary.

   Upon instantiation, the serialized dictionary is read from disk.

   .. py:property:: list

      List the keys of the dictionary. This is a property, and does not need to be called.

   .. py:method:: backup()

      Write a backup version of the data to the ``backups`` directory.


   .. py:method:: deserialize()

      Load the serialized data. Can be replaced with other serialization formats.


   .. py:method:: flush()

      Serialize the current data to disk.


   .. py:method:: keys()

      D.keys() -> a set-like object providing a view on D's keys


   .. py:method:: load()

      Load the serialized data. Creates the file if not yet present.


   .. py:method:: pack(data)

      Transform the data, if necessary. Needed because JSON must have strings as dictionary keys.


   .. py:method:: random()

      Return a random key.


   .. py:method:: serialize(filepath=None)

      Method to do the actual serialization. Can be replaced with other serialization formats.

      :param \* *filepath*: Provide an alternate filepath (e.g. for backup).
      :type \* *filepath*: str, optional


   .. py:method:: unpack(data)

      Return serialized data to true form.


   .. py:method:: values()

      D.values() -> an object providing a view on D's values



.. py:data:: anyjson

   

