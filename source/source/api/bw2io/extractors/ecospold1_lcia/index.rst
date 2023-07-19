:py:mod:`bw2io.extractors.ecospold1_lcia`
=========================================

.. py:module:: bw2io.extractors.ecospold1_lcia


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.extractors.ecospold1_lcia.Ecospold1LCIAExtractor



Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.extractors.ecospold1_lcia._to_unicode



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.extractors.ecospold1_lcia.monitor


.. py:class:: Ecospold1LCIAExtractor

   Bases: :py:obj:`object`

   Extract impact assessment methods and weightings data from ecospold XML format.

   .. attribute:: None

      

   .. method:: extract

      Extracts data from an ecospold XML file.

   .. method:: parse_method

      Parses the ecospold XML dataset to extract information.

   .. method:: parse_cf

      Parses an ecospold XML data element to extract characterization factor information.
      

   .. py:method:: extract(path)
      :classmethod:

      Extracts ecospold XML file data.

      :param path: The path to the ecospold XML file or directory.
      :type path: str

      :returns: A list of dictionaries with the extracted information.
      :rtype: list


   .. py:method:: parse_cf(cf)
      :classmethod:

      Parse a cf object and extract relevant data.

      :param cf: A dictionary of cf data.
      :type cf: dict

      :returns: A dictionary of parsed cf data.
      :rtype: dict

      :raises TypeError: If 'cf' is not a dictionary.

      .. rubric:: Notes

      This method expects 'cf' to contain the following keys:
      - meanValue (float): the amount
      - category (str): the category
      - subCategory (str, optional): the subcategory, if any
      - name (str): the name
      - unit (str): the unit of the amount

      If `subCategory` is not provided, it will default to `None`.


   .. py:method:: parse_method(ds, filepath)
      :classmethod:

      Parse and extract information from an ecospold XML dataset.

      :param ds: The XML dataset.
      :type ds: object
      :param filepath: The path to the XML file.
      :type filepath: str

      :returns: A dictionary of the information extracted from the ecospold XML dataset.
      :rtype: dict



.. py:function:: _to_unicode(data)


.. py:data:: monitor
   :value: True

   

