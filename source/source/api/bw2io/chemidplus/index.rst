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


.. py:exception:: Missing

   Bases: :py:obj:`Exception`

   .. autoapi-inheritance-diagram:: bw2io.chemidplus.Missing
      :parts: 1
      :private-bases:

   404 or other error code returned.

   :param exception: Exception to raise.
   :type exception: Exception
   :param Initialize self.  See help(type(self)) for accurate signature.:


.. py:exception:: Multiple

   Bases: :py:obj:`Exception`

   .. autoapi-inheritance-diagram:: bw2io.chemidplus.Multiple
      :parts: 1
      :private-bases:

   Multiple results for given search query.

   :param exception: Exception to raise.
   :type exception: Exception
   :param Initialize self.  See help(type(self)) for accurate signature.:


.. py:class:: ChemIDPlus

   Use the `ChemIDPlus <https://chem.nlm.nih.gov/api/swagger-ui.html#/SubstanceController>`__ API to lookup synonyms for chemicals, including pesticides.

   Always used to match against a master list. Seeded with names from ecoinvent.

   .. attribute:: api_cache

      Dictionary with raw data from API, key is canonical name.

      :type: dict

   .. attribute:: master_mapping

      Dictionary from synonyms, including canonical names, to master flows.

      :type: dict

   .. attribute:: forbidden_keys

      Identifiers that aren't unique in the ChemIDPlus system.

      :type: set

   .. method:: match(synonym, search=True)

      Match a synonym to a master flow.

   .. method:: match_cas(number)

      Match a CAS number to a master flow.

   .. method:: process_request(request)

      Process a request to the ChemIDPlus API.

   .. method:: load_cache()

      Load the cache of API results.

   .. method:: save_cache()

      Save the cache of API results.


   .. py:attribute:: CAS_TEMPLATE
      :value: 'https://chem.nlm.nih.gov/api/data/search?data=complete&exp=rn%2Feq%2F{cas}'

      

   .. py:attribute:: NAME_TEMPLATE
      :value: 'https://chem.nlm.nih.gov/api/data/search?data=complete&exp=na%2Feq%2F{name}'

      

   .. py:method:: add_master_term(term, CAS)


   .. py:method:: load_cache()


   .. py:method:: match(synonym, search=True)


   .. py:method:: match_cas(number)


   .. py:method:: process_request(response)


   .. py:method:: save_cache()



.. py:function:: canonical_cas(s)

   CAS numbers have up to ten digits; we remove zero padding and add hyphens where needed.

   :param s: CAS number.
   :type s: str

   :returns: Canonical CAS number.
   :rtype: str


.. py:data:: DIRPATH

   

