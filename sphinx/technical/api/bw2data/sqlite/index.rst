:py:mod:`bw2data.sqlite`
========================

.. py:module:: bw2data.sqlite


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.sqlite.PickleField
   bw2data.sqlite.SubstitutableDatabase
   bw2data.sqlite.JSONField
   bw2data.sqlite.TupleJSONField




.. py:class:: PickleField

   Bases: :py:obj:`peewee.BlobField`

   .. py:method:: db_value(value)


   .. py:method:: python_value(value)



.. py:class:: SubstitutableDatabase(filepath, tables)

   .. py:property:: db


   .. py:method:: _create_database()


   .. py:method:: change_path(filepath)


   .. py:method:: atomic()


   .. py:method:: execute_sql(*args, **kwargs)


   .. py:method:: transaction()


   .. py:method:: vacuum()



.. py:class:: JSONField

   Bases: :py:obj:`peewee.TextField`

   Simpler JSON field that doesn't support advanced querying and is human-readable

   .. py:method:: db_value(value)


   .. py:method:: python_value(value)



.. py:class:: TupleJSONField

   Bases: :py:obj:`JSONField`

   Simpler JSON field that doesn't support advanced querying and is human-readable

   .. py:method:: python_value(value)



