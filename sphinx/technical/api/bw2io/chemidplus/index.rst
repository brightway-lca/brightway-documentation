:py:mod:`bw2io.chemidplus`
==========================

.. py:module:: bw2io.chemidplus


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.chemidplus.ChemIDPlus



Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.chemidplus.canonical_cas



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.chemidplus.DIRPATH


.. py:data:: DIRPATH
   

   

.. py:function:: canonical_cas(s)

   CAS numbers have up to ten digits; we remove zero padding and add hyphens where needed.


.. py:exception:: Multiple

   Bases: :py:obj:`Exception`

   Multiple results for given search query.


.. py:exception:: Missing

   Bases: :py:obj:`Exception`

   404 or other error code returned


.. py:class:: ChemIDPlus

   Use the `ChemIDPlus <https://chem.nlm.nih.gov/api/swagger-ui.html#/SubstanceController>`__ API to lookup synonyms for chemicals, including pesticides.

   Always used to match against a master list. Seeded with names from ecoinvent.

   .. py:attribute:: CAS_TEMPLATE
      :annotation: = https://chem.nlm.nih.gov/api/data/search?data=complete&exp=rn%2Feq%2F{cas}

      

   .. py:attribute:: NAME_TEMPLATE
      :annotation: = https://chem.nlm.nih.gov/api/data/search?data=complete&exp=na%2Feq%2F{name}

      

   .. py:method:: match(synonym, search=True)


   .. py:method:: match_cas(number)


   .. py:method:: add_master_term(term, CAS)


   .. py:method:: save_cache()


   .. py:method:: load_cache()


   .. py:method:: process_request(response)



