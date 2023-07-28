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



.. py:class:: Ecospold1LCIAExtractor

   Bases: :py:obj:`object`

   Extract impact assessment methods and weightings data from ecospold XML format.

   .. py:method:: extract(path)
      :classmethod:


   .. py:method:: parse_cf(cf)
      :classmethod:


   .. py:method:: parse_method(ds, filepath)
      :classmethod:



.. py:function:: _to_unicode(data)


