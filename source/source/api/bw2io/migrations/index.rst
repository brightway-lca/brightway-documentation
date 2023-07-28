:py:mod:`bw2io.migrations`
==========================

.. py:module:: bw2io.migrations


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.migrations.Migration
   bw2io.migrations._Migrations



Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.migrations.create_core_migrations



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.migrations.migrations


.. py:class:: Migration(*args, **kwargs)

   Bases: :py:obj:`bw2data.data_store.DataStore`

   .. autoapi-inheritance-diagram:: bw2io.migrations.Migration
      :parts: 1
      :private-bases:

   .. py:property:: description


   .. py:attribute:: _metadata

      

   .. py:method:: load()


   .. py:method:: validate(*args, **kwargs)


   .. py:method:: write(data, description)

      Write migration data. Requires a description.



.. py:class:: _Migrations

   Bases: :py:obj:`bw2data.serialization.SerializedDict`

   .. autoapi-inheritance-diagram:: bw2io.migrations._Migrations
      :parts: 1
      :private-bases:

   .. py:attribute:: filename
      :value: 'migrations.json'

      


.. py:function:: create_core_migrations()

   Add pre-defined core migrations data files


.. py:data:: migrations

   

