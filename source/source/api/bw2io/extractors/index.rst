:py:mod:`bw2io.extractors`
==========================

.. py:module:: bw2io.extractors


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   csv/index.rst
   ecospold1/index.rst
   ecospold1_lcia/index.rst
   ecospold2/index.rst
   excel/index.rst
   exiobase/index.rst
   json_ld/index.rst
   simapro_csv/index.rst
   simapro_lcia_csv/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.extractors.CSVExtractor
   bw2io.extractors.Ecospold1DataExtractor
   bw2io.extractors.Ecospold1LCIAExtractor
   bw2io.extractors.Ecospold2DataExtractor
   bw2io.extractors.ExcelExtractor
   bw2io.extractors.ExiobaseDataExtractor
   bw2io.extractors.SimaProCSVExtractor
   bw2io.extractors.SimaProLCIACSVExtractor




.. py:class:: CSVExtractor

   Bases: :py:obj:`object`

   .. py:method:: extract(filepath, encoding='utf-8-sig')
      :classmethod:



.. py:class:: Ecospold1DataExtractor

   Bases: :py:obj:`object`

   .. py:method:: extract(path, db_name, use_mp=True)
      :classmethod:


   .. py:method:: is_valid_ecospold1(dataset)
      :classmethod:


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


   .. py:method:: process_uncertainty_fields(exc, data)
      :classmethod:



.. py:class:: Ecospold1LCIAExtractor

   Bases: :py:obj:`object`

   Extract impact assessment methods and weightings data from ecospold XML format.

   .. py:method:: extract(path)
      :classmethod:


   .. py:method:: parse_cf(cf)
      :classmethod:


   .. py:method:: parse_method(ds, filepath)
      :classmethod:



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



.. py:class:: ExcelExtractor

   Bases: :py:obj:`object`

   .. py:method:: extract(filepath)
      :classmethod:


   .. py:method:: extract_sheet(wb, name, strip=True)
      :classmethod:



.. py:class:: ExiobaseDataExtractor

   Bases: :py:obj:`object`

   .. py:method:: _check_dir(path)
      :classmethod:


   .. py:method:: _extract_csv(path, filename, materials=False)
      :classmethod:


   .. py:method:: _extract_metadata(path)
      :classmethod:


   .. py:method:: _generate_csv(path, filename)
      :classmethod:


   .. py:method:: extract(path)
      :classmethod:



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



