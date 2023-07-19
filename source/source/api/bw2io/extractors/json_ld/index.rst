:py:mod:`bw2io.extractors.json_ld`
==================================

.. py:module:: bw2io.extractors.json_ld


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.extractors.json_ld.JSONLDExtractor




Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.extractors.json_ld.DIRECTORIES_TO_IGNORE
   bw2io.extractors.json_ld.FILES_TO_IGNORE


.. py:class:: JSONLDExtractor

   Bases: :py:obj:`object`

   Extract JSON-LD from a directory.

   .. attribute:: FILES_TO_IGNORE

      Files to ignore when extracting JSON-LD data.

      :type: set

   .. attribute:: DIRECTORIES_TO_IGNORE

      Directories to ignore when extracting JSON-LD data.

      :type: set

   .. py:method:: extract(filepath, add_filename=True)
      :classmethod:

      Extracts JSON-LD data from the filepath.

      :param filepath: The path of the directory from which data will be extracted
      :type filepath: str or Path
      :param add_filename: Add the name to the extracted data. By default, True.
      :type add_filename: bool, optional

      :returns: A dictionary with the extracted JSON-LD data.
      :rtype: dict

      :raises ValueError: If the file is not a zip archive.
      :raises NotImplementedError: If extraction of zip archives is not yet supported.



.. py:data:: DIRECTORIES_TO_IGNORE

   

.. py:data:: FILES_TO_IGNORE

   

