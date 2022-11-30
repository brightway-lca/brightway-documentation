:py:mod:`bw2data.serialization`
===============================

.. py:module:: bw2data.serialization


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.serialization.JsonWrapper
   bw2data.serialization.JsonSanitizer
   bw2data.serialization.SerializedDict
   bw2data.serialization.PickledDict
   bw2data.serialization.CompoundJSONDict




Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2data.serialization.anyjson


.. py:data:: anyjson
   

   

.. py:class:: JsonWrapper

   .. py:method:: dump(data, filepath)
      :classmethod:


   .. py:method:: dump_bz2(data, filepath)
      :classmethod:


   .. py:method:: load(file)
      :classmethod:


   .. py:method:: load_bz2(filepath)
      :classmethod:


   .. py:method:: dumps(data)
      :classmethod:


   .. py:method:: loads(data)
      :classmethod:



.. py:class:: JsonSanitizer

   .. py:method:: sanitize(data)
      :classmethod:


   .. py:method:: load(data)
      :classmethod:



.. py:class:: SerializedDict(dirpath=None)

   Bases: :py:obj:`collections.abc.MutableMapping`

   Base class for dictionary that can be `serialized <http://en.wikipedia.org/wiki/Serialization>`_ to or unserialized from disk. Uses JSON as its storage format. Has most of the methods of a dictionary.

   Upon instantiation, the serialized dictionary is read from disk.

   .. py:property:: list

      List the keys of the dictionary. This is a property, and does not need to be called.

   .. py:attribute:: __repr__
      

      

   .. py:method:: load()

      Load the serialized data. Creates the file if not yet present.


   .. py:method:: flush()

      Serialize the current data to disk.


   .. py:method:: __getitem__(key)


   .. py:method:: __setitem__(key, value)


   .. py:method:: __contains__(key)


   .. py:method:: __str__()

      Return str(self).


   .. py:method:: __delitem__(name)


   .. py:method:: __len__()


   .. py:method:: __iter__()


   .. py:method:: __hash__()

      Return hash(self).


   .. py:method:: keys()

      D.keys() -> a set-like object providing a view on D's keys


   .. py:method:: values()

      D.values() -> an object providing a view on D's values


   .. py:method:: serialize(filepath=None)

      Method to do the actual serialization. Can be replaced with other serialization formats.

      :param \* *filepath*: Provide an alternate filepath (e.g. for backup).
      :type \* *filepath*: str, optional


   .. py:method:: deserialize()

      Load the serialized data. Can be replaced with other serialization formats.


   .. py:method:: pack(data)

      Transform the data, if necessary. Needed because JSON must have strings as dictionary keys.


   .. py:method:: unpack(data)

      Return serialized data to true form.


   .. py:method:: random()

      Return a random key.


   .. py:method:: backup()

      Write a backup version of the data to the ``backups`` directory.



.. py:class:: PickledDict(dirpath=None)

   Bases: :py:obj:`SerializedDict`

   Subclass of ``SerializedDict`` that uses the pickle format instead of JSON.

   .. py:method:: serialize()

      Method to do the actual serialization. Can be replaced with other serialization formats.

      :param \* *filepath*: Provide an alternate filepath (e.g. for backup).
      :type \* *filepath*: str, optional


   .. py:method:: deserialize()

      Load the serialized data. Can be replaced with other serialization formats.



.. py:class:: CompoundJSONDict(dirpath=None)

   Bases: :py:obj:`SerializedDict`

   Subclass of ``SerializedDict`` that allows tuples as dictionary keys (not allowed in JSON).

   .. py:method:: pack(data)

      Transform the dictionary to a list because JSON can't handle lists as keys


   .. py:method:: unpack(data)

      Transform data back to a dictionary



