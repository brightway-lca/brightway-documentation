:py:mod:`bw2data.filesystem`
============================

.. py:module:: bw2data.filesystem


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.filesystem.create_dir
   bw2data.filesystem.check_dir
   bw2data.filesystem.md5



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2data.filesystem.re_slugify


.. py:data:: re_slugify
   

   

.. py:function:: create_dir(dirpath)

   Create directory tree to `dirpath`; ignore if already exists


.. py:function:: check_dir(directory)

   Returns ``True`` if given path is a directory and writeable, ``False`` otherwise.


.. py:function:: md5(filepath, blocksize=65536)

   Generate MD5 hash for file at `filepath`


