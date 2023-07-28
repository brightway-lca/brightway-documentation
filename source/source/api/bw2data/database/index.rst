:py:mod:`bw2data.database`
==========================

.. py:module:: bw2data.database


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.database.DatabaseChooser



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2data.database.Database


.. py:function:: DatabaseChooser(name, backend=None)

   A method that returns a database class instance. The default database type is `SingleFileDatabase`. `JSONDatabase` stores each process dataset in indented JSON in a separate file. Database types are specified in `databases[database_name]['backend']`.

   New database types can be registered with the config object:

   .. code-block:: python

       config.backends['backend type string'] = MyNewBackendClass

   .. warning:: Registering new backends must be done each time you start the Python interpreter.

   To test whether an object is a database subclass, do:

   .. code-block:: python

       from bw2data.backends import LCIBackend
       isinstance(my_database, LCIBackend)



.. py:data:: Database

   

