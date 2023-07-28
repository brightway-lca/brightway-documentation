:py:mod:`bw2data.backends.peewee.schema`
========================================

.. py:module:: bw2data.backends.peewee.schema


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.backends.peewee.schema.ActivityDataset
   bw2data.backends.peewee.schema.ExchangeDataset




.. py:class:: ActivityDataset

   Bases: :py:obj:`peewee.Model`

   .. autoapi-inheritance-diagram:: bw2data.backends.peewee.schema.ActivityDataset
      :parts: 1
      :private-bases:

   .. py:attribute:: code

      

   .. py:attribute:: data

      

   .. py:attribute:: database

      

   .. py:attribute:: location

      

   .. py:attribute:: name

      

   .. py:attribute:: product

      

   .. py:attribute:: type

      


.. py:class:: ExchangeDataset

   Bases: :py:obj:`peewee.Model`

   .. autoapi-inheritance-diagram:: bw2data.backends.peewee.schema.ExchangeDataset
      :parts: 1
      :private-bases:

   .. py:attribute:: data

      

   .. py:attribute:: input_code

      

   .. py:attribute:: input_database

      

   .. py:attribute:: output_code

      

   .. py:attribute:: output_database

      

   .. py:attribute:: type

      


