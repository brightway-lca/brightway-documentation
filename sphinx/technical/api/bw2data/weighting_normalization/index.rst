:py:mod:`bw2data.weighting_normalization`
=========================================

.. py:module:: bw2data.weighting_normalization


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.weighting_normalization.Weighting
   bw2data.weighting_normalization.Normalization




.. py:class:: Weighting

   Bases: :py:obj:`bw2data.ia_data_store.ImpactAssessmentDataStore`

   LCIA weighting data - used to combine or compare different impact categories.

   The data schema for weighting is a one-element list:

   .. code-block:: python

           Schema(All(
               [uncertainty_dict],
               Length(min=1, max=1)
           ))


   .. py:attribute:: _metadata
      

      

   .. py:attribute:: validator
      

      

   .. py:attribute:: matrix
      :annotation: = weighting_matrix

      

   .. py:method:: write(data)

      Because of DataStore assumptions, need a one-element list


   .. py:method:: process_row(row)

      Return an empty tuple (as ``dtype_fields`` is empty), and the weighting uncertainty dictionary.



.. py:class:: Normalization

   Bases: :py:obj:`bw2data.ia_data_store.ImpactAssessmentDataStore`

   LCIA normalization data - used to transform meaningful units, like mass or damage, into "person-equivalents" or some such thing.

   The data schema for IA normalization is:

   .. code-block:: python

           Schema([
               [valid_tuple, maybe_uncertainty]
           ])

   where:
       * ``valid_tuple`` is a dataset identifier, like ``("biosphere", "CO2")``
       * ``maybe_uncertainty`` is either a number or an uncertainty dictionary


   .. py:attribute:: _metadata
      

      

   .. py:attribute:: validator
      

      

   .. py:attribute:: matrix
      :annotation: = normalization_matrix

      

   .. py:method:: process_row(row)

      Given ``(flow key, amount)``, return a dictionary for array insertion.



