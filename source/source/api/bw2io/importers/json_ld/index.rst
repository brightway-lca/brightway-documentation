:py:mod:`bw2io.importers.json_ld`
=================================

.. py:module:: bw2io.importers.json_ld


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.importers.json_ld.JSONLDImporter




.. py:class:: JSONLDImporter(dirpath, database_name, preferred_allocation=None)

   Bases: :py:obj:`bw2io.importers.base_lci.LCIImporter`

   .. autoapi-inheritance-diagram:: bw2io.importers.json_ld.JSONLDImporter
      :parts: 1
      :private-bases:

   Importer for the `OLCD JSON-LD data format <https://github.com/GreenDelta/olca-schema>`__.

   See `discussion with linked issues here <https://github.com/brightway-lca/brightway2-io/issues/15>`__.


   .. py:attribute:: extractor

      

   .. py:attribute:: format
      :value: 'OLCA JSON-LD'

      

   .. py:method:: apply_strategies(*args, **kwargs)


   .. py:method:: flows_as_biosphere_database(data, database_name, suffix=' biosphere')


   .. py:method:: flows_as_products(data)


   .. py:method:: merge_biosphere_flows()

      Add flows in ``self.biosphere_database`` to ``self.data``.


   .. py:method:: write_separate_biosphere_database()



