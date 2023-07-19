:py:mod:`bw2io.extractors.exiobase`
===================================

.. py:module:: bw2io.extractors.exiobase


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.extractors.exiobase.Exiobase3MonetaryDataExtractor



Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.extractors.exiobase.remove_numerics



.. py:class:: Exiobase3MonetaryDataExtractor

   Bases: :py:obj:`object`

   .. py:method:: _get_path(dirpath)
      :classmethod:

      Get the directory path of the EXIOBASE data file.

      :param dirpath: The path of the EXIOBASE data file or directory.
      :type dirpath: str

      :returns: The directory path of the EXIOBASE data file.
      :rtype: Path


   .. py:method:: _get_production_volumes(dirpath)
      :classmethod:

      Extract production volumes from the EXIOBASE data file.

      :param dirpath: The path of the EXIOBASE data file or directory.
      :type dirpath: str

      :returns: A dictionary for the production volume.
      :rtype: dict


   .. py:method:: _get_unit_data(dirpath)
      :classmethod:

      Extract unit data from the EXIOBASE data file.

      :param dirpath: The path to the EXIOBASE data file or directory.
      :type dirpath: str

      :returns: A dctionary of unit data from the EXIOBase data file.
      :rtype: dict


   .. py:method:: get_biosphere_iterator(dirpath, ignore_small_balancing_corrections=True)
      :classmethod:

      Returns an iterator that yields tuples of flow names, locations, and amounts.

      :param dirpath: The path to the directory.
      :type dirpath: str
      :param ignore_small_balancing_corrections: Ignore small balancing corrections. By default True.
      :type ignore_small_balancing_corrections: bool, optional


   .. py:method:: get_flows(dirpath)
      :classmethod:

      Extract flows from an EXIOBASE data file.

      :param dirpath: The path of the EXIOBASE data file or directory.
      :type dirpath: str

      :returns: A dictionary of flows from the EXIOBASE data file.
      :rtype: dict


   .. py:method:: get_products(dirpath)
      :classmethod:

      Get product information from a given directory.

      :param dirpath: The path to the directory with the product information.
      :type dirpath: str

      :returns: A list of dictionaries with the following keys:
                - 'name': str
                The product name.
                - 'location': str
                The product location.
                - 'unit': str
                The product's unit of measure.
                - 'production volume': float
                The total production volume for the product.
      :rtype: list


   .. py:method:: get_technosphere_iterator(dirpath, num_products, ignore_small_balancing_corrections=True)
      :classmethod:

      Get an iterator in a given directory.

      :param dirpath: The path to the directory with the data.
      :type dirpath: str
      :param num_products: The number of products.
      :type num_products: int
      :param ignore_small_balancing_corrections: Ignore small balancing corrections. By default True.
      :type ignore_small_balancing_corrections: bool, optional



.. py:function:: remove_numerics(string)

   Remove numeric values enclosed in parentheses from a given string, e.g. 'Tobacco products (16)' into 'Tobacco products'.

   :param string: The string to be processed
   :type string: str

   :returns: The processed string without numeric values enclosed in parentheses.
   :rtype: str


