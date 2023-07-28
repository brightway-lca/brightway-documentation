:py:mod:`bw2data.filesystem`
============================

.. py:module:: bw2data.filesystem


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.filesystem.check_dir
   bw2data.filesystem.create_dir
   bw2data.filesystem.md5
   bw2data.filesystem.safe_filename



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2data.filesystem.re_slugify


.. py:function:: check_dir(directory)

   Returns ``True`` if given path is a directory and writeable, ``False`` otherwise.


.. py:function:: create_dir(dirpath)

   Create directory tree to `dirpath`; ignore if already exists


.. py:function:: md5(filepath, blocksize=65536)

   Generate MD5 hash for file at `filepath`


.. py:function:: safe_filename(string, add_hash=True)

   Convert arbitrary strings to make them safe for filenames. Substitutes strange characters, and uses unicode normalization.

   if `add_hash`, appends hash of `string` to avoid name collisions.

   From http://stackoverflow.com/questions/295135/turn-a-string-into-a-valid-filename-in-python


.. py:data:: re_slugify

   

