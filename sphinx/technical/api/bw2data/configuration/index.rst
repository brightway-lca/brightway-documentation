:py:mod:`bw2data.configuration`
===============================

.. py:module:: bw2data.configuration


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.configuration.Config




Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2data.configuration.config


.. py:class:: Config

   A singleton that stores configuration settings

   .. py:property:: biosphere

      Get name for ``biosphere`` database from user preferences.

      Default name is ``biosphere3``; change this by changing ``config.p["biosphere_database"]``.

   .. py:property:: global_location

      Get name for global location from user preferences.

      Default name is ``GLO``; change this by changing ``config.p["global_location"]``.

   .. py:attribute:: version
      :annotation: = 3

      

   .. py:attribute:: backends
      

      

   .. py:attribute:: cache
      

      

   .. py:attribute:: metadata
      :annotation: = []

      

   .. py:attribute:: sqlite3_databases
      :annotation: = []

      

   .. py:attribute:: _windows
      

      


.. py:data:: config
   

   

