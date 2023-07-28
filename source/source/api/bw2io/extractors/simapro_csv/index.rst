:py:mod:`bw2io.extractors.simapro_csv`
======================================

.. py:module:: bw2io.extractors.simapro_csv


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.extractors.simapro_csv.SimaProCSVExtractor



Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.extractors.simapro_csv.replace_with_lowercase
   bw2io.extractors.simapro_csv.to_number



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.extractors.simapro_csv.INTRODUCTION
   bw2io.extractors.simapro_csv.SIMAPRO_END_OF_DATASETS
   bw2io.extractors.simapro_csv.SIMAPRO_PRODUCTS
   bw2io.extractors.simapro_csv.SIMAPRO_TECHNOSPHERE
   bw2io.extractors.simapro_csv.lowercase_expression
   bw2io.extractors.simapro_csv.strip_whitespace_and_delete


.. py:exception:: EndOfDatasets

   Bases: :py:obj:`Exception`

   .. autoapi-inheritance-diagram:: bw2io.extractors.simapro_csv.EndOfDatasets
      :parts: 1
      :private-bases:

   Common base class for all non-exit exceptions.

   Initialize self.  See help(type(self)) for accurate signature.


.. py:class:: SimaProCSVExtractor

   Bases: :py:obj:`object`

   .. py:method:: create_distribution(amount, kind, field1, field2, field3)
      :classmethod:


   .. py:method:: extract(filepath, delimiter=';', name=None, encoding='cp1252')
      :classmethod:


   .. py:method:: get_global_parameters(data, pm)
      :classmethod:


   .. py:method:: get_next_process_index(data, index)
      :classmethod:


   .. py:method:: get_project_metadata(data)
      :classmethod:


   .. py:method:: get_project_name(data)
      :classmethod:


   .. py:method:: invalid_uncertainty_data(amount, kind, field1, field2, field3)
      :classmethod:


   .. py:method:: parse_biosphere_flow(line, category, pm)
      :classmethod:

      Parse biosphere flow line.

      0. name
      1. subcategory
      2. unit
      3. value or formula
      4. uncertainty type
      5. uncert. param.
      6. uncert. param.
      7. uncert. param.
      8. comment

      However, sometimes the value is in index 2, and the unit in index 3. Because why not! We assume default ordering unless we find a number in index 2.



   .. py:method:: parse_calculated_parameter(line, pm)
      :classmethod:

      Parse line in `Calculated parameters` section.

      0. name
      1. formula
      2. comment

      Can include multiline comment in TSV.


   .. py:method:: parse_final_waste_flow(line, pm)
      :classmethod:

      Parse final wate flow line.

      0: name
      1: subcategory?
      2: unit
      3. value or formula
      4. uncertainty type
      5. uncert. param.
      6. uncert. param.
      7. uncert. param.

      However, sometimes the value is in index 2, and the unit in index 3. Because why not! We assume default ordering unless we find a number in index 2.



   .. py:method:: parse_input_line(line, category, pm)
      :classmethod:

      Parse technosphere input line.

      0. name
      1. unit
      2. value or formula
      3. uncertainty type
      4. uncert. param.
      5. uncert. param.
      6. uncert. param.
      7. comment

      However, sometimes the value is in index 1, and the unit in index 2. Because why not! We assume default ordering unless we find a number in index 1.



   .. py:method:: parse_input_parameter(line)
      :classmethod:

      Parse line in `Input parameters` section.

      0. name
      1. value (not formula)
      2. uncertainty type
      3. uncert. param.
      4. uncert. param.
      5. uncert. param.
      6. hidden ("Yes" or "No" - we ignore)
      7. comment



   .. py:method:: parse_reference_product(line, pm)
      :classmethod:

      Parse reference product line.

      0. name
      1. unit
      2. value or formula
      3. allocation
      4. waste type
      5. category (separated by \)
      6. comment

      However, sometimes the value is in index 1, and the unit in index 2. Because why not! We assume default ordering unless we find a number in index 1.



   .. py:method:: parse_waste_treatment(line, pm)
      :classmethod:

      Parse reference product line.

      0. name
      1. unit
      2. value or formula
      3. waste type
      4. category (separated by \)
      5. comment



   .. py:method:: read_data_set(data, index, db_name, filepath, gp, pm)
      :classmethod:


   .. py:method:: read_dataset_metadata(data, index)
      :classmethod:



.. py:function:: replace_with_lowercase(string, names)

   Replace all occurrences of elements of ``names`` in ``string`` with their lowercase equivalents.

   ``names`` is a list of variable name strings that should already all be lowercase.

   Returns a modified ``string``.


.. py:function:: to_number(obj)


.. py:data:: INTRODUCTION
   :value: Multiline-String

    .. raw:: html

        <details><summary>Show Value</summary>

    .. code-block:: python

        """Starting SimaPro import:
        	Filepath: %s
        	Delimiter: %s
        	Name: %s
        """

    .. raw:: html

        </details>

   

.. py:data:: SIMAPRO_END_OF_DATASETS

   

.. py:data:: SIMAPRO_PRODUCTS

   

.. py:data:: SIMAPRO_TECHNOSPHERE

   

.. py:data:: lowercase_expression
   :value: '(?:^|[^a-zA-Z_])(?P<variable>{})(?:[^a-zA-Z_]|$)'

   

.. py:data:: strip_whitespace_and_delete

   

