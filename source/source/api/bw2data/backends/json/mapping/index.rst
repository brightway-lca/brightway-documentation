:py:mod:`bw2data.backends.json.mapping`
=======================================

.. py:module:: bw2data.backends.json.mapping


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.backends.json.mapping.KeyMapping



Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.backends.json.mapping.get_mapping



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2data.backends.json.mapping.cache


.. py:class:: KeyMapping(dirpath=None)

   Bases: :py:obj:`bw2data.serialization.PickledDict`

   .. autoapi-inheritance-diagram:: bw2data.backends.json.mapping.KeyMapping
      :parts: 1
      :private-bases:

   Subclass of ``SerializedDict`` that uses the pickle format instead of JSON.

   .. py:attribute:: filename
      :value: 'keys-filenames.mapping'

      


.. py:function:: get_mapping(filepath)


.. py:data:: cache

   

