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

   bw2io.extractors.simapro_csv.replace_with_uppercase
   bw2io.extractors.simapro_csv.to_number



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.extractors.simapro_csv.INTRODUCTION
   bw2io.extractors.simapro_csv.SIMAPRO_END_OF_DATASETS
   bw2io.extractors.simapro_csv.SIMAPRO_PRODUCTS
   bw2io.extractors.simapro_csv.SIMAPRO_TECHNOSPHERE
   bw2io.extractors.simapro_csv.strip_whitespace_and_delete
   bw2io.extractors.simapro_csv.uppercase_expression


.. py:exception:: EndOfDatasets

   Bases: :py:obj:`Exception`

   .. autoapi-inheritance-diagram:: bw2io.extractors.simapro_csv.EndOfDatasets
      :parts: 1
      :private-bases:

   Raise exception when there are no more datasets to iterate.

   Initialize self.  See help(type(self)) for accurate signature.


.. py:class:: SimaProCSVExtractor

   Bases: :py:obj:`object`

   Extract datasets from SimaPro CSV export files.

   The CSV file should be in a specific format, with row 1 containing either the string "SimaPro" or "CSV separator."

   :param filepath: The path to the SimaPro CSV export file.
   :type filepath: str
   :param delimiter: The delimiter in the CSV file. Default is ";".
   :type delimiter: str, optional
   :param name: The name of the project. If the name is not provided, it is extracted from the CSV file.
   :type name: str, optional
   :param encoding: The character encoding in the SimaPro CSV file. Defaults to "cp1252".
   :type encoding: str, optional

   :returns: * **datasets** (*list*) -- The list of extracted datasets from the CSV file.
             * **global_parameters** (*dict*) -- The dictionary of global parameters for the CSV file.
             * **project_metadata** (*dict*) -- The dictionary of project metadata.

   :raises AssertionError:: If the CSV file is not a valid Simapro export file.

   .. py:method:: create_distribution(amount, kind, field1, field2, field3)
      :classmethod:

      Create a distribution based on the given uncertainty data.

      :param amount: The amount of uncertainty.
      :type amount: str
      :param kind: The kind of uncertainty.
      :type kind: str
      :param field1: The first field of uncertainty data.
      :type field1: str
      :param field2: The second field of uncertainty data.
      :type field2: str
      :param field3: The third field of uncertainty data.
      :type field3: str

      :returns: A dictionary representing the distribution.
      :rtype: dict

      :raises ValueError: If the given uncertainty type is unknown.

      .. rubric:: Notes

      This method creates a distribution based on the given uncertainty data.
      The distribution is returned as a dictionary with the following keys:
      - "uncertainty type": the ID of the uncertainty type
      - "loc": the location parameter of the distribution
      - "amount": the amount of uncertainty
      Depending on the kind of uncertainty, other keys may be included:
      - "scale": the scale parameter of the distribution (for "Lognormal" and "Normal" uncertainties)
      - "minimum": the minimum value of the distribution (for "Triangle" and "Uniform" uncertainties)
      - "maximum": the maximum value of the distribution (for "Triangle" and "Uniform" uncertainties)
      - "negative": `True` if the amount of uncertainty is negative, `False` otherwise.
      If the kind of uncertainty is "Undefined", an undefined uncertainty distribution is created.
      If the kind of uncertainty is "Lognormal", a lognormal uncertainty distribution is created.
      If the kind of uncertainty is "Normal", a normal uncertainty distribution is created.
      If the kind of uncertainty is "Triangle", a triangular uncertainty distribution is created.
      If the kind of uncertainty is "Uniform", a uniform uncertainty distribution is created.
      If the kind of uncertainty is unknown, a ValueError is raised.


   .. py:method:: extract(filepath, delimiter=';', name=None, encoding='cp1252')
      :classmethod:

      Extract data from a SimaPro export file (.csv) and returns a list of datasets, global parameters, and project metadata.

      Parameters:
      -----------
      filepath : str
          The file path of the SimaPro export file to extract data from.
      delimiter : str, optional
          The delimiter used in the SimaPro export file. Defaults to ";".
      name : str, optional
          The name of the project. If not provided, the method will attempt to infer it from the SimaPro export file.
      encoding : str, optional
          The character encoding of the SimaPro export file. Defaults to "cp1252".

      Returns:
      --------
      Tuple[List[Dict], Dict, Dict]
          A tuple containing:
              - a list of dictionaries representing each dataset extracted from the SimaPro export file,
              - a dictionary containing global parameters extracted from the SimaPro export file, and
              - a dictionary containing project metadata extracted from the SimaPro export file.


   .. py:method:: get_global_parameters(data, pm)
      :classmethod:

      Extract and return global parameters from a SimaPro export file.

      :param data: A list of lists containing the data read from the SimaPro export file.
      :type data: List[List[str]]
      :param pm: A dictionary containing project metadata extracted from the SimaPro export file.
      :type pm: Dict[str, str]

      :returns:     - parameters (Dict[str, Dict[str, Any]]): A dictionary containing global parameters extracted from the SimaPro export file. Each parameter is represented as a dictionary with keys 'name', 'unit', 'formula', and 'amount'.
                    - global_precompiled (Dict[str, Pattern]): A dictionary containing compiled regular expression patterns used to search for parameter names in the SimaPro export file.
      :rtype: A tuple containing

      :raises ValueError: If an invalid parameter is encountered in the SimaPro export file.


   .. py:method:: get_next_process_index(data, index)
      :classmethod:

      Get the index of the next process in the given data.

      Parameters:
      -----------
      data : List[List[str]]
          The data to search for the next process.
      index : int
          The index to start the search from.

      Returns:
      --------
      int
          The index of the next process in the data.



   .. py:method:: get_project_metadata(data)
      :classmethod:

      Parse metadata from a list of strings and returns a dictionary of metadata key-value pairs.

      :param data: A list of strings containing metadata in the format "{key}: {value}".
      :type data: list

      :returns: A dictionary of metadata key-value pairs extracted from the input `data` list.
      :rtype: dict

      :raises ValueError: If a line of metadata does not contain a colon `:` character, or if it contains multiple colons.
      :raises AssertionError: If a line of metadata does not start and end with curly braces `{}`.

      .. rubric:: Notes

      This method assumes that each line in the input `data` list contains only one metadata key-value pair,
      and that the key and value are separated by a single colon `:` character.

      .. rubric:: Examples

      >>> data = ["{name}: John Smith", "{age}: 25", "", "{country: UK}"]
      >>> meta = get_project_metadata(data)
      >>> print(meta)
      {"name": "John Smith", "age": "25", "country": "UK"}


   .. py:method:: get_project_name(data)
      :classmethod:

      Extract the project name from the given data.

      :param data: A list of data, where each item is a list of strings representing a row of the data.
      :type data: list

      :returns: The project name.
      :rtype: str

      .. rubric:: Notes

      This method searches for a row in the data where the first item starts with "{Project:" or "{Projet:".
      If such a row is found, the project name is extracted from that row and returned. Otherwise, `None` is returned.


   .. py:method:: invalid_uncertainty_data(amount, kind, field1, field2, field3)
      :classmethod:

      Determine if the uncertainty data is invalid.

      :param amount: The amount of uncertainty.
      :type amount: str
      :param kind: The kind of uncertainty.
      :type kind: str
      :param field1: The first field of uncertainty data.
      :type field1: str
      :param field2: The second field of uncertainty data.
      :type field2: str
      :param field3: The third field of uncertainty data.
      :type field3: str

      :returns: `True` if the uncertainty data is invalid, `False` otherwise.
      :rtype: bool

      .. rubric:: Notes

      This method checks if the given uncertainty data is invalid based on the kind of uncertainty.
      If the kind is "Lognormal" and `amount` is empty or `field1` is "0" or "1", the uncertainty data is considered invalid.


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

      Parse a line in the 'Calculated parameters' section of a SimaPro file and return a dictionary of its components.

      :param line: The line to be parsed, with the first string being the name, the second string the formula, and
                   subsequent strings comments associated with the parameter.
      :type line: List[str]
      :param pm: A dictionary mapping variable names to their values in the context of the parameter.
      :type pm: Dict[str, float]

      :returns: * **parsed_parameter** (*Dict[str, Union[str, List[str]]]*)
                * *A dictionary with the following keys*
                * **- 'name'** (*str*) -- The name of the parameter.
                * **- 'formula'** (*str*) -- The formula used in the parameter, with variables replaced by their values according to `pm`.
                * **- 'comment'** (*List[str]*) -- A list of comments on the parameter.

      .. rubric:: Examples

      #TODO


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

      Parse input parameters section of a SimaPro file.

      0. name
      1. value (not formula)
      2. uncertainty type
      3. uncert. param.
      4. uncert. param.
      5. uncert. param.
      6. hidden ("Yes" or "No" - we ignore)
      7. comment

      :rtype: #TODO

      .. rubric:: Examples

      #TODO


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



   .. py:method:: read_data_set(data, index, db_name, filepath, gp, pm, global_precompiled)
      :classmethod:


   .. py:method:: read_dataset_metadata(data, index)
      :classmethod:

      Read metadata from a SIMAPRO dataset.

      :returns: A tuple containing the metadata as a dictionary and the index of the next line
                after the metadata.
      :rtype: Tuple[Dict[str, str], int]

      :raises IndexError: If the index is out of range for the given dataset.



.. py:function:: replace_with_uppercase(string, names, precompiled)

   Replace all occurrences of elements of ``names`` in ``string`` with their uppercase equivalents.

   :param string: String to be modified.
   :type string: str
   :param names: List of variable name strings that should already all be uppercase.
   :type names: list
   :param precompiled: Dictionary #TODO.
   :type precompiled: dict

   :rtype: The modified string.


.. py:function:: to_number(obj)

   Convert a string to a number.

   :param obj: The string to be converted to a number
   :type obj: str

   :returns: converted number as float, or the unchanged string if not successfully converted.
   :rtype: float or str


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

   

.. py:data:: strip_whitespace_and_delete

   

.. py:data:: uppercase_expression
   :value: '(?:^|[^a-zA-Z_])(?P<variable>{})(?:[^a-zA-Z_]|$)'

   

