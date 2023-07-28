:py:mod:`bw2io.extractors.simapro_lcia_csv`
===========================================

.. py:module:: bw2io.extractors.simapro_lcia_csv


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.extractors.simapro_lcia_csv.SimaProLCIACSVExtractor




Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.extractors.simapro_lcia_csv.INTRODUCTION
   bw2io.extractors.simapro_lcia_csv.SKIPPABLE_SECTIONS
   bw2io.extractors.simapro_lcia_csv.strip_delete


.. py:exception:: EndOfDatasets

   Bases: :py:obj:`Exception`

   .. autoapi-inheritance-diagram:: bw2io.extractors.simapro_lcia_csv.EndOfDatasets
      :parts: 1
      :private-bases:

   Common base class for all non-exit exceptions.

   Initialize self.  See help(type(self)) for accurate signature.


.. py:class:: SimaProLCIACSVExtractor

   Bases: :py:obj:`object`

   .. py:method:: extract(filepath, delimiter=';', encoding='cp1252')
      :classmethod:


   .. py:method:: get_all_cfs(nw_data, category_data)
      :classmethod:


   .. py:method:: get_category_data(data, index)
      :classmethod:


   .. py:method:: get_damage_category_data(data, index)
      :classmethod:


   .. py:method:: get_damage_exchanges(damage_data, category_data)
      :classmethod:


   .. py:method:: get_next_method_index(data, index)
      :classmethod:


   .. py:method:: get_normalization_weighting_data(data, index)
      :classmethod:


   .. py:method:: parse_cf(line)
      :classmethod:

      Parse line in `Substances` section.

      0. category
      1. subcategory
      2. flow
      3. CAS number
      4. CF
      5. unit



   .. py:method:: read_metadata(data, index)
      :classmethod:


   .. py:method:: read_method_data_set(data, index, filepath)
      :classmethod:


   .. py:method:: skip_to_section_end(data, index)
      :classmethod:



.. py:data:: INTRODUCTION
   :value: Multiline-String

    .. raw:: html

        <details><summary>Show Value</summary>

    .. code-block:: python

        """Starting SimaPro import:
        	Filepath: %s
        	Delimiter: %s
        """

    .. raw:: html

        </details>

   

.. py:data:: SKIPPABLE_SECTIONS

   

.. py:data:: strip_delete

   

