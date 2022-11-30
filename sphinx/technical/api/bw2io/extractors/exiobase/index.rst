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



.. py:function:: remove_numerics(string)

   Transform names like 'Tobacco products (16)' into 'Tobacco products'


.. py:class:: Exiobase3MonetaryDataExtractor

   Bases: :py:obj:`object`

   .. py:method:: _get_path(dirpath)
      :classmethod:


   .. py:method:: _get_production_volumes(dirpath)
      :classmethod:


   .. py:method:: _get_unit_data(dirpath)
      :classmethod:


   .. py:method:: get_flows(dirpath)
      :classmethod:


   .. py:method:: get_products(dirpath)
      :classmethod:


   .. py:method:: get_technosphere_iterator(dirpath, num_products, ignore_small_balancing_corrections=True)
      :classmethod:


   .. py:method:: get_biosphere_iterator(dirpath, ignore_small_balancing_corrections=True)
      :classmethod:



