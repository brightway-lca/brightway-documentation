:py:mod:`bw2io.modified_database`
=================================

.. py:module:: bw2io.modified_database


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.modified_database.ModifiedDatabase




.. py:class:: ModifiedDatabase(data, ref_database_name, from_simapro=False)

   Bases: :py:obj:`object`

   Find relationships between foreground data ``data`` and background database named ``ref_database_name``.

   Each activity and exchange is summarized in a *hash*, a small set of letters that summarizes all relevant attributes.

   foreground_activities_mapping:
       hash: dataset

   foreground_exchanges_mapping:
       hash: exchange

   foreground_activities:
       activity hash: set of (exchange hash, amount) exchange tuples.

   background_activities_mapping:
       hash: Activity

   background_exchanges_mapping:
       hash: Exchange

   background_activities:
       activity hash: set of (Exchange hash, amount) exchange tuples

   .. py:method:: assert_data_fully_linked()


   .. py:method:: iterate_unmatched()

      Return data on activities in ``data`` which can't be found in ``ref_database_name``.


   .. py:method:: get_reason(exc_tuple, data)

      Get reason why exc_tuple not in data. Reasons are:
      1) Changed amount
      2) Missing


   .. py:method:: iterate_modified()

      Return data on modified activities


   .. py:method:: load_datasets()

      Determine which datasets are modified by comparing the exchanges values.

      Specifically, compare the set of ``(input activity hashes, amount_as_string)`` values.

      If the name or other important attributes changed, then there won't be a correspondence at all, so the dataset is treated as modified in any case.


   .. py:method:: add_to_background_exchanges_mapping(exc)


   .. py:method:: hash_background_exchanges(activity)


   .. py:method:: hash_foreground_exchanges(activity)


   .. py:method:: prune()



