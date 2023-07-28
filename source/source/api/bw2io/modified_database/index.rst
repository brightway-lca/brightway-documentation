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

   .. attribute:: foreground_activities_mapping

      hash: dataset

      :type: dict

   .. attribute:: foreground_exchanges_mapping

      hash: exchange

      :type: dict

   .. attribute:: foreground_activities

      activity hash: set of (exchange hash, amount) exchange tuples.

      :type: dict

   .. attribute:: background_activities_mapping

      hash: Activity

      :type: dict

   .. attribute:: background_exchanges_mapping

      hash: Exchange

      :type: dict

   .. attribute:: background_activities

      activity hash: set of (Exchange hash, amount) exchange tuples

      :type: dict

   .. method:: assert_data_fully_linked()

      Assert that all exchanges in ``data`` have an ``input`` key.

   .. method:: iterate_unmatched()

      Return data on activities in ``data`` which can't be found in ``ref_database_name``.

   .. method:: get_reason(exc_tuple, data)

      Get reason why exc_tuple not in data. Reasons are: 1) Changed amount 2) Missing

   .. method:: iterate_modified()

      Return data on modified activities

   .. method:: load_datasets()

      Determine which datasets are modified by comparing the exchanges values.

   .. method:: add_to_background_exchanges_mapping(exc)

      Add exchange to ``background_exchanges_mapping``.

   .. method:: hash_background_exchanges(activity)

      Hash exchanges in ``activity`` and add to ``background_exchanges_mapping``.

   .. method:: hash_foreground_exchanges(activity)

      Hash exchanges in ``activity`` and add to ``foreground_exchanges_mapping``.

   .. method:: prune()

      Remove activities from ``data`` that are not in ``ref_database_name``.

   .. py:method:: add_to_background_exchanges_mapping(exc)


   .. py:method:: assert_data_fully_linked()


   .. py:method:: get_reason(exc_tuple, data)

      Get reason why exc_tuple not in data. Reasons are:
      1) Changed amount
      2) Missing

      :param exc_tuple: (exchange hash, amount)
      :type exc_tuple: tuple
      :param data: set of (exchange hash, amount) exchange tuples
      :type data: set

      :returns: Reason why exc_tuple not in data
      :rtype: str


   .. py:method:: hash_background_exchanges(activity)


   .. py:method:: hash_foreground_exchanges(activity)


   .. py:method:: iterate_modified()

      Return data on modified activities

      :returns: (key, value)
      :rtype: tuple


   .. py:method:: iterate_unmatched()

      Return data on activities in ``data`` which can't be found in ``ref_database_name``.

      :returns: (key, value)
      :rtype: tuple


   .. py:method:: load_datasets()

      Determine which datasets are modified by comparing the exchanges values.

      Specifically, compare the set of ``(input activity hashes, amount_as_string)`` values.

      If the name or other important attributes changed, then there won't be a correspondence at all, so the dataset is treated as modified in any case.


   .. py:method:: prune()



