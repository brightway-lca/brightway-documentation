:py:mod:`bw2io.importers.ecoinvent_lcia`
========================================

.. py:module:: bw2io.importers.ecoinvent_lcia


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.importers.ecoinvent_lcia.EcoinventLCIAImporter




.. py:class:: EcoinventLCIAImporter

   Bases: :py:obj:`bw2io.importers.base_lcia.LCIAImporter`

   .. autoapi-inheritance-diagram:: bw2io.importers.ecoinvent_lcia.EcoinventLCIAImporter
      :parts: 1
      :private-bases:

   A class for importing ecoinvent-compatible LCIA methods


   Initialize an instance of EcoinventLCIAImporter.

   Defines strategies in ``__init__`` because ``config.biosphere`` is dynamic.

   .. py:method:: add_rationalize_method_names_strategy()

      Add the `rationalize_method_names` strategy to the list of strategies


   .. py:method:: separate_methods()

      Separate the list of CFs into distinct methods



