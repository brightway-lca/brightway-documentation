:py:mod:`bw2io.extractors.ecospold1`
====================================

.. py:module:: bw2io.extractors.ecospold1


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.extractors.ecospold1.Ecospold1DataExtractor



Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.extractors.ecospold1.getattr2



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.extractors.ecospold1.monitor


.. py:class:: Ecospold1DataExtractor

   Bases: :py:obj:`object`

   .. py:method:: extract(path, db_name, use_mp=True)
      :classmethod:

      Extract data from ecospold1 files.

      :param path: Path to the directory containing the ecospold1 files or path to a single file.
      :type path: str
      :param db_name: Name of the database.
      :type db_name: str
      :param use_mp: If True, uses multiprocessing to parallelize extraction of data from multiple files, by default True.
      :type use_mp: bool, optional

      :returns: List of dictionaries containing data from the ecospold1 files.
      :rtype: list


   .. py:method:: is_valid_ecospold1(dataset)
      :classmethod:

      Check if a dataset is a valid ecospold1 file.

      :param dataset: A dataset from an ecospold1 file.
      :type dataset: lxml.objectify.ObjectifiedElement

      :returns: True if the dataset is a valid ecospold1 file, False otherwise.
      :rtype: bool


   .. py:method:: process_allocation(exc, dataset)
      :classmethod:


   .. py:method:: process_dataset(dataset, filename, db_name)
      :classmethod:


   .. py:method:: process_exchange(exc, dataset)
      :classmethod:

      Process exchange.

      Input groups are:

          1. Materials/fuels
          2. Electricity/Heat
          3. Services
          4. FromNature
          5. FromTechnosphere

      Output groups are:

          0. Reference product
          1. Include avoided product system
          2. Allocated byproduct
          3. Waste to treatment
          4. ToNature

      A single-output process will have one output group 0; A MO process will have multiple output group 2s. Output groups 1 and 3 are not used in ecoinvent.



   .. py:method:: process_exchanges(dataset)
      :classmethod:


   .. py:method:: process_file(filepath, db_name)
      :classmethod:

      Process a single ecospold1 file.

      :param filepath: Path to the ecospold1 file.
      :type filepath: str
      :param db_name: Name of the database.
      :type db_name: str

      :returns: List of dictionaries containing data from the ecospold1 file.
      :rtype: list


   .. py:method:: process_uncertainty_fields(exc, data)
      :classmethod:



.. py:function:: getattr2(obj, attr)


.. py:data:: monitor
   :value: True

   

