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

   Extract data from SimaPro LCIACSV file format.

   :param filepath: Filepath of the SimaPro LCIACSV file.
   :type filepath: str
   :param delimiter: Delimiter used in the SimaPro LCIACSV file.
   :type delimiter: str, optional (default: ";")
   :param encoding: Encoding of the SimaPro LCIACSV file.
   :type encoding: str, optional (default: "cp1252")

   :raises AssertionError: If the filepath does not exist or the file is not a valid SimaPro export file.

   :returns: List of datasets extracted from the SimaPro LCIACSV file.
   :rtype: list

   .. py:method:: extract(filepath, delimiter=';', encoding='cp1252')
      :classmethod:


   .. py:method:: get_all_cfs(nw_data, category_data)
      :classmethod:

      Get all CFs from `nw_data` and `category_data`.

      :param nw_data: A list of tuples containing normalization-weighting (NW) set names and scales.
      :type nw_data: list
      :param category_data: A list of tuples containing impact category names, units, and CF data.
      :type category_data: list

      :returns: A list of all CFs.
      :rtype: list


   .. py:method:: get_category_data(data, index)
      :classmethod:

      Parse impact category data and return its name, unit, and data.

      :param data: A list of lists with the data for all categories
      :type data: list of lists
      :param index: The index of the current impact category in the list
      :type index: int

      :returns: A tuple with the name, unit, and data for the impact category
      :rtype: tuple


   .. py:method:: get_damage_category_data(data, index)
      :classmethod:

      Parse damage category data and return the name, unit, and data of the category.

      :param data: A list of lists with the data of the damage categories
      :type data: list of lists
      :param index: The index of the current damage category in the list
      :type index: int

      :returns: A tuple with the name, unit, and data for the damage category
      :rtype: tuple


   .. py:method:: get_damage_exchanges(damage_data, category_data)
      :classmethod:

      Calculate the damage exchanges based on damage data and category data.

      :param damage_data: A list of tuples containing the name and scale of the damage
      :type damage_data: list of tuples
      :param category_data: A list of tuples containing the name, unit, and data of each impact category
      :type category_data: list of tuples

      :returns: A list of dictionaries with the calculated damage exchanges of each impact category
      :rtype: list of dictionaries


   .. py:method:: get_next_method_index(data, index)
      :classmethod:

      Find the index of the next "Method" in the given data starting from the
      specified index, skipping any sections specified in SKIPPABLE_SECTIONS.

      :param data: The nested list containing the data.
      :type data: list of lists
      :param index: The starting index to search for the next "Method".
      :type index: int

      :returns: The index of the next "Method" in the data.
      :rtype: int

      :raises EndOfDatasets: If the file ends without extra metadata.


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

      Read metadata from `data` starting at `index`.

      :param data: A list of lists containing the data to be processed.
      :type data: list
      :param index: The starting index to read metadata from.
      :type index: int

      :returns: A tuple containing a dictionary of metadata and the index where the metadata reading ended.
      :rtype: tuple


   .. py:method:: read_method_data_set(data, index, filepath)
      :classmethod:

      Read method data set from `data` starting at `index`.

      :param data: A list of lists containing the data to be processed.
      :type data: list
      :param index: The starting index to read method data set from.
      :type index: int
      :param filepath: The file path of the method data set.
      :type filepath: str

      :returns: * *list* -- A list of completed method data sets.
                * *int* -- The index where the method data set reading ended.

      :raises ValueError:


   .. py:method:: skip_to_section_end(data, index)
      :classmethod:

      Skip to the end of the current section in the data starting from the
      specified index.

      :param data: The nested list containing the data.
      :type data: list of lists
      :param index: The starting index to skip from.
      :type index: int

      :returns: The index of the end of the current section in the data.
      :rtype: int



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

   

