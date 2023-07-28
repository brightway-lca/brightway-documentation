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
   bw2io.extractors.ecospold2.monitor


.. py:class:: Ecospold2DataExtractor

   Bases: :py:obj:`object`

   .. py:method:: abort_exchange(exc, comment=None)
      :classmethod:

      Set the uncertainty type of the input exchange to UndefinedUncertainty.id. Remove the keys "scale", "shape", "minimum", and "maximum" from the dictionary.
      Update the "loc" key to "amount". Append "comment" to "exc['comment']" if "comment" is not None,
      otherwise append "Invalid parameters - set to undefined uncertainty." to "exc['comment']".

      :param exc: The input exchange.
      :type exc: dict
      :param comment: A string to append to "exc['comment']". Defaults to None.
      :type comment: str, optional

      :returns: None


   .. py:method:: condense_multiline_comment(element)
      :classmethod:

      Concatenate the text of all child elements with the tag
      "{http://www.EcoInvent.org/EcoSpold02}text" and the text of all child
      elements with the tag "{http://www.EcoInvent.org/EcoSpold02}imageUrl"
      in the given `element` XML element.

       Args
       ----
          cls (type): The class object.
          element (lxml.etree.Element): The XML element.

      :returns: * **str** (*The concatenated text of all child elements with the tag*)
                * **"{http** (*//www.EcoInvent.org/EcoSpold02}text" and the text of all child*)
                * **elements with the tag "{http** (*//www.EcoInvent.org/EcoSpold02}imageUrl".*)
                * *If an error occurs, an empty string is returned.*


   .. py:method:: extract(dirpath, db_name, use_mp=True)
      :classmethod:

      Extract data from all ecospold2 files in a directory.

      :param dirpath: The path to the directory containing the ecospold2 files.
      :type dirpath: str
      :param db_name: The name of the database to create.
      :type db_name: str
      :param use_mp: Whether to use multiprocessing to extract the data (default is True).
      :type use_mp: bool, optional

      :returns: A list of the extracted data from the ecospold2 files.
      :rtype: list

      :raises FileNotFoundError: If no .spold files are found in the directory.


   .. py:method:: extract_activity(dirpath, filename, db_name)
      :classmethod:

      Extract and return the data of an activity from an XML file with the given
      `filename` in the directory with the path `dirpath`.

       Args
       ----
          cls (type): The class object.
          dirpath (str): The path of the directory containing the XML file.
          filename (str): The name of the XML file.
          db_name (str): The name of the database.

      :returns: **dict** --

                follows:
                    - "comment": str. The condensed multiline comment.
                    - "classifications": list of tuples. The classification systems and
                      values of the activity.
                    - "activity type": str. The type of the activity.
                    - "activity": str. The ID of the activity.
                    - "database": str. The name of the database.
                    - "exchanges": list of dicts. The exchanges of the activity.
                    - "filename": str. The name of the XML file.
                    - "location": str. The short name of the location of the activity.
                    - "name": str. The name of the activity.
                    - "synonyms": list of str. The synonyms of the activity.
                    - "parameters": dict. The parameters of the activity.
                    - "authors": dict of dicts. The authors of the activity. The keys and
                      values of the inner dicts are as follows:
                        - "name": str. The name of the author.
                        - "email": str. The email of the author.
                    - "type": str. The type of the activity.
      :rtype: The dictionary of data for the activity. The keys and values are as


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

      Extract parameter information from "exc" and return it as a tuple.

      :param exc: The input exchange.
      :type exc: dict

      :returns: A tuple containing the parameter name and a dictionary containing the parameter information.
      :rtype: tuple


   .. py:method:: extract_properties(exc)
      :classmethod:

      Extract the properties of an exchange.

      :param exc: An XML element representing an exchange.
      :type exc: lxml.etree.Element

      :returns: A dictionary of the properties of the exchange. Each key in the dictionary
                is a string representing the name of a property, and the corresponding value
                is a dictionary with the following keys:

                - "amount" (float): The numerical value of the property.
                - "comment" (str, optional): A comment describing the property, if available.
                - "unit" (str, optional): The unit of the property, if available.
                - "variable name" (str, optional): The name of the variable associated with
                the property, if available.
      :rtype: dict


   .. py:method:: extract_technosphere_metadata(dirpath)
      :classmethod:

      Extract technosphere metadata from ecospold2 directory.

      :param dirpath: The path to the ecospold2 directory.
      :type dirpath: str

      :returns: List of names, units, and IDs
      :rtype: List of dict


   .. py:method:: extract_uncertainty_dict(obj)
      :classmethod:

      Extract uncertainty information from "obj" and return it as a dictionary.

      :param obj: The input object.

      :returns: The extracted uncertainty information.
      :rtype: dict



.. py:function:: getattr2(obj, attr)

   Get attribute of an object; return empty dict if AttributeError occurs.

   :param obj: The object to get attribute from.
   :type obj: object
   :param attr: The name of the attribute to get.
   :type attr: str

   :returns: The attribute value if it exists, else an empty dict.
   :rtype: dict


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

   

.. py:data:: monitor
   :value: True

   

