:py:mod:`bw2data.search.search`
===============================

.. py:module:: bw2data.search.search


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.search.search.Searcher



Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.search.search.keysplit



.. py:class:: Searcher(database)

   Bases: :py:obj:`object`

   .. py:method:: search(string, limit=25, facet=None, proxy=True, boosts=None, filter=None, mask=None)



.. py:function:: keysplit(strng)

   Split an activity key joined into a single string using the magic sequence `⊡|⊡`


