:py:mod:`bw2io.importers.base_lcia`
===================================

.. py:module:: bw2io.importers.base_lcia


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.importers.base_lcia.LCIAImporter




.. py:class:: LCIAImporter(filepath, biosphere=None)

   Bases: :py:obj:`bw2io.importers.base.ImportBase`

   .. autoapi-inheritance-diagram:: bw2io.importers.base_lcia.LCIAImporter
      :parts: 1
      :private-bases:

   .. py:property:: all_linked


   .. py:method:: _format_flow(cf)


   .. py:method:: _reformat_cfs(ds)


   .. py:method:: add_missing_cfs()


   .. py:method:: drop_unlinked(verbose=True)


   .. py:method:: migrate(migration_name)


   .. py:method:: statistics(print_stats=True)


   .. py:method:: write_excel(name)


   .. py:method:: write_methods(overwrite=False, verbose=True)



