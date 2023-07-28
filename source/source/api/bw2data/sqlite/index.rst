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




.. py:class:: PickleField

   Bases: :py:obj:`peewee.BlobField`

   .. autoapi-inheritance-diagram:: bw2data.sqlite.PickleField
      :parts: 1
      :private-bases:

   .. py:method:: db_value(value)


   .. py:method:: python_value(value)



.. py:class:: SubstitutableDatabase(filepath, tables)

   Bases: :py:obj:`object`

   .. py:property:: db


   .. py:method:: _create_database()


   .. py:method:: atomic()


   .. py:method:: change_path(filepath)


   .. py:method:: execute_sql(*args, **kwargs)


   .. py:method:: transaction()


   .. py:method:: vacuum()



