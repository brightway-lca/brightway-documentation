:py:mod:`bw2data.backends.schema`
=================================

.. py:module:: bw2data.backends.schema


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.backends.schema.ActivityDataset
   bw2data.backends.schema.ExchangeDataset



Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.backends.schema.get_id



.. py:class:: ActivityDataset

   Bases: :py:obj:`peewee.Model`

   .. autoapi-inheritance-diagram:: bw2data.backends.schema.ActivityDataset
      :parts: 1
      :private-bases:

   .. py:property:: key


   .. py:attribute:: code

      

   .. py:attribute:: data

      

   .. py:attribute:: database

      

   .. py:attribute:: location

      

   .. py:attribute:: name

      

   .. py:attribute:: product

      

   .. py:attribute:: type

      


.. py:class:: ExchangeDataset

   Bases: :py:obj:`peewee.Model`

   .. autoapi-inheritance-diagram:: bw2data.backends.schema.ExchangeDataset
      :parts: 1
      :private-bases:

   .. py:attribute:: data

      

   .. py:attribute:: input_code

      

   .. py:attribute:: input_database

      

   .. py:attribute:: output_code

      

   .. py:attribute:: output_database

      

   .. py:attribute:: type

      


.. py:function:: get_id(key)


