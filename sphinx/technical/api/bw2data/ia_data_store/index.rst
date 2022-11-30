:py:mod:`bw2data.ia_data_store`
===============================

.. py:module:: bw2data.ia_data_store


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.ia_data_store.ImpactAssessmentDataStore



Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.ia_data_store.abbreviate



.. py:function:: abbreviate(names, length=8)

   Take a tuple or list, and construct a string, doing the following:

   First, apply :func:`.filesystem.safe_filename` to each element in ``names``.

   Next, take the following, in order:
       * The first word of the first element in names, lower-cased, where word is defined as everything up to the first empty space character.
       * Join the rest of the first element (i.e. after the first word) with all other elements. Use the empty space character to join.
       * In this long string separated by spaces, take the lowercase first character of each word. Add the first word to this new string.
       * Finally, add a dash, and then the MD5 hash of the entire identifier, where each element is joined by a dash character.

   ``('ReCiPe Endpoint (E,A)', 'human health', 'ionising radiation')`` becomes ``'recipee(hhir-70eeef20a20deb6347ad428e3f6c5f3c'``.

   The MD5 hash is needed because taking the first characters doesn't guarantee unique strings.



.. py:class:: ImpactAssessmentDataStore(name)

   Bases: :py:obj:`bw2data.data_store.ProcessedDataStore`

   A subclass of ``DataStore`` for impact assessment methods.

   IA objects are hierarchically structured, and their identifier uses this structure, like ``('ecological scarcity 2006', 'total', 'natural resources')``. The identifier must be a ``tuple``, i.e. ``()``, not a ``list``, i.e. ``[]``. The identifier should only contain unicode strings, and can be of any length >= 1.

   Because impact assessment methods are identified by a tuple of strings, e.g. ``('ReCiPe Endpoint (E,A)', 'human health', 'ionising radiation')``, we need to transform this identifier before it can be used e.g. as a filename. We do this using the :func:`.abbreviate` function, which returns a single unicode string.

   :param \* *name*: Name of the IA object to manage. Must be a tuple of unicode strings.
   :type \* *name*: tuple

   .. py:property:: filename

      Remove filesystem-unsafe characters and perform unicode normalization on ``self.name`` using :func:`.filesystem.safe_filename`.

   .. py:method:: __str__()

      Return str(self).


   .. py:method:: get_abbreviation()

      Retrieve the abbreviation of the method identifier from the metadata store. See class documentation.


   .. py:method:: copy(name=None)

      Make a copy of the method, including its CFs and metadata.

      If ``name`` is not provided, add "Copy of" to the last element of the original name, e.g. ``("foo", "bar")`` becomes ``("foo", "Copy of bar")``

      :param \* *name*: Name of the new method.
      :type \* *name*: tuple, optional

      :returns: The new object.


   .. py:method:: register(**kwargs)

      Register an object with the metadata store.

      The metadata key ``abbreviation`` is set automatically.

      Objects must be registered before data can be written. If this object is not yet registered in the metadata store, a warning is written to **stdout**.

      Takes any number of keyword arguments.




