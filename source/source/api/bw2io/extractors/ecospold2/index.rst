:py:mod:`bw2io.extractors.ecospold2`
====================================

.. py:module:: bw2io.extractors.ecospold2


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.extractors.ecospold2.Ecospold2DataExtractor



Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.extractors.ecospold2.getattr2



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.extractors.ecospold2.ACTIVITY_TYPES
   bw2io.extractors.ecospold2.PM_MAPPING
   bw2io.extractors.ecospold2.TOO_HIGH
   bw2io.extractors.ecospold2.TOO_LOW


.. py:class:: Ecospold2DataExtractor

   Bases: :py:obj:`object`

   .. py:method:: abort_exchange(exc, comment=None)
      :classmethod:


   .. py:method:: condense_multiline_comment(element)
      :classmethod:


   .. py:method:: extract(dirpath, db_name, use_mp=True)
      :classmethod:


   .. py:method:: extract_activity(dirpath, filename, db_name)
      :classmethod:


   .. py:method:: extract_exchange(exc)
      :classmethod:

      Process exchange.

      Input groups are:

          1. Materials/fuels
          2. Electricity/Heat
          3. Services
          4. From environment (elementary exchange only)
          5. FromTechnosphere

      Output groups are:

          0. ReferenceProduct
          2. By-product
          3. MaterialForTreatment
          4. To environment (elementary exchange only)
          5. Stock addition



   .. py:method:: extract_parameter(exc)
      :classmethod:


   .. py:method:: extract_properties(exc)
      :classmethod:


   .. py:method:: extract_technosphere_metadata(dirpath)
      :classmethod:


   .. py:method:: extract_uncertainty_dict(obj)
      :classmethod:



.. py:function:: getattr2(obj, attr)


.. py:data:: ACTIVITY_TYPES

   

.. py:data:: PM_MAPPING

   

.. py:data:: TOO_HIGH
   :value: Multiline-String

    .. raw:: html

        <details><summary>Show Value</summary>

    .. code-block:: python

        """Lognormal scale value impossibly high: {}.
        Reverting to undefined uncertainty."""

    .. raw:: html

        </details>

   

.. py:data:: TOO_LOW
   :value: Multiline-String

    .. raw:: html

        <details><summary>Show Value</summary>

    .. code-block:: python

        """Lognormal scale value at or below zero: {}.
        Reverting to undefined uncertainty."""

    .. raw:: html

        </details>

   

