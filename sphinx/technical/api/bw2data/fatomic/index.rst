:py:mod:`bw2data.fatomic`
=========================

.. py:module:: bw2data.fatomic


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.fatomic.open
   bw2data.fatomic.writeall
   bw2data.fatomic.transform
   bw2data.fatomic.transformall
   bw2data.fatomic.transformchunks



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2data.fatomic.replace
   bw2data.fatomic.writechunks


.. py:data:: replace
   

   

.. py:function:: open(filename, mode, *args, **kwargs)


.. py:function:: writeall(filename, contents, binary=None)


.. py:data:: writechunks
   

   

.. py:function:: transform(filename, func, binary=False)


.. py:function:: transformall(filename, func, binary=False)


.. py:function:: transformchunks(filename, func, chunksize=None, binary=False)


