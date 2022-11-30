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



.. py:function:: getattr2(obj, attr)


.. py:class:: Ecospold1DataExtractor

   Bases: :py:obj:`object`

   .. py:method:: extract(path, db_name, use_mp=True)
      :classmethod:


   .. py:method:: process_file(filepath, db_name)
      :classmethod:


   .. py:method:: is_valid_ecospold1(dataset)
      :classmethod:


   .. py:method:: process_dataset(dataset, filename, db_name)
      :classmethod:


   .. py:method:: process_exchanges(dataset)
      :classmethod:


   .. py:method:: process_allocation(exc, dataset)
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


   .. py:method:: process_uncertainty_fields(exc, data)
      :classmethod:



