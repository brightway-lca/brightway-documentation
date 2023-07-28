:py:mod:`bw2calc.dictionary_manager`
====================================

.. py:module:: bw2calc.dictionary_manager


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2calc.dictionary_manager.DictionaryManager
   bw2calc.dictionary_manager.ReversibleRemappableDictionary



Functions
~~~~~~~~~

.. autoapisummary::

   bw2calc.dictionary_manager.resolved



.. py:class:: DictionaryManager

   Class that handles dictionaries which can be remapped or reverse.

   Usage::

       dm = DictionaryManager()
       dm.foo = {1: 2}
       dm.foo[1]
       >> 2



.. py:class:: ReversibleRemappableDictionary(obj)

   Bases: :py:obj:`collections.abc.Mapping`

   .. autoapi-inheritance-diagram:: bw2calc.dictionary_manager.ReversibleRemappableDictionary
      :parts: 1
      :private-bases:

   A dictionary that can be easily remapped or reversed.

   Perhaps  overkill, but at the time it was easier than creating many dictionaries on the LCA object itself.

   Example usage::

       In [1]: from bw2calc.dictionary_manager import ReversibleRemappableDictionary

       In [2]: d = ReversibleRemappableDictionary({1: 2})

       In [3]: d.reverse
       Out[3]: {2: 1}

       In [4]: d.remap({1: "foo"})

       In [5]: d['foo']
       Out[5]: 2

       In [6]: d.original
       Out[6]: {1: 2}

       In [7]: d.reverse
       Out[7]: {2: 'foo'}

       In [8]: d.unmap()

       In [9]: d[1]
       Out[9]: 2


   .. py:property:: original


   .. py:property:: reversed


   .. py:method:: remap(mapping)

      Transform the keys based on the mapping dict ``mapping``.

      ``mapping`` doesn't need to cover every key in the original.

      Example usage:

      {1: 2}.remap({1: "foo"} >> {"foo": 2}



   .. py:method:: unmap()

      Restore dict to original state.



.. py:function:: resolved(f)

   Decorator that resolves a ``partial`` function before it can be used


