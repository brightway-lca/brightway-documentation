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

   .. py:property:: all_linked


   .. py:method:: write_methods(overwrite=False, verbose=True)


   .. py:method:: write_excel(name)


   .. py:method:: drop_unlinked(verbose=True)


   .. py:method:: _reformat_cfs(ds)


   .. py:method:: _format_flow(cf)


   .. py:method:: add_missing_cfs()


   .. py:method:: statistics(print_stats=True)


   .. py:method:: migrate(migration_name)



