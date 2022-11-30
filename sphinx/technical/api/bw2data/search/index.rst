:py:mod:`bw2data.search`
========================

.. py:module:: bw2data.search


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   indices/index.rst
   schema/index.rst
   search/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.search.IndexManager
   bw2data.search.Searcher




.. py:class:: IndexManager(database_path, dir_name='whoosh')

   .. py:method:: get()


   .. py:method:: create()


   .. py:method:: _format_dataset(ds)


   .. py:method:: add_dataset(ds)


   .. py:method:: add_datasets(datasets)


   .. py:method:: update_dataset(ds)


   .. py:method:: delete_dataset(ds)


   .. py:method:: delete_database()



.. py:class:: Searcher(database)

   .. py:method:: __enter__()


   .. py:method:: __exit__(type, value, traceback)


   .. py:method:: search(string, limit=25, facet=None, proxy=True, boosts=None, filter=None, mask=None, node_class=None)



