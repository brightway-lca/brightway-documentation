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

   A migration is a set of data that can be used to modify a database.

   Migrations are stored in the ``migrations`` directory of the project. They
   are stored as JSON files, and are registered in the ``migrations.json`` file.

   .. method:: write(data, description)

      Write migration data. Requires a description.

   .. method:: load()

      Load migration data.

   .. method:: validate()

      Validate migration data.


   .. py:property:: description


   .. py:attribute:: _metadata

      

   .. py:method:: load()


   .. py:method:: validate(*args, **kwargs)


   .. py:method:: write(data, description)

      Write migration data. Requires a description.

      :param data: Migration data.
      :type data: dict
      :param description: Description of the migration.
      :type description: str



.. py:class:: _Migrations

   Bases: :py:obj:`bw2data.serialization.SerializedDict`

   .. autoapi-inheritance-diagram:: bw2io.migrations._Migrations
      :parts: 1
      :private-bases:

   .. py:attribute:: filename
      :value: 'migrations.json'

      


.. py:function:: create_core_migrations()

   Add pre-defined core migrations data files.


.. py:data:: migrations

   

