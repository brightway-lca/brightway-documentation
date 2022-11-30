:py:mod:`bw2io.export`
======================

.. py:module:: bw2io.export


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   csv/index.rst
   excel/index.rst
   gexf/index.rst
   matlab/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.export.DatabaseSelectionToGEXF
   bw2io.export.DatabaseToGEXF



Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.export.write_lci_csv
   bw2io.export.lci_matrices_to_excel
   bw2io.export.write_lci_excel
   bw2io.export.keyword_to_gephi_graph
   bw2io.export.lci_matrices_to_matlab



.. py:function:: write_lci_csv(database_name, objs=None, sections=None, dirpath=None)

   Export database `database_name` to a CSV file.

   Not all data can be exported. The following constraints apply:

   * Nested data, e.g. `{'foo': {'bar': 'baz'}}` are excluded. CSV is not a great format for nested data. However, *tuples* are exported, and the characters `::` are used to join elements of the tuple.
   * The only well-supported data types are strings, numbers, and booleans.

   Default directory is ``projects.output_dir``, set ``dirpath`` to have save the file somewhere else.

   Returns the filepath of the exported file.



.. py:function:: lci_matrices_to_excel(database_name, include_descendants=True)

   Fake docstring


.. py:function:: write_lci_excel(database_name, objs=None, sections=None, dirpath=None)

   Export database `database_name` to an Excel spreadsheet.

   Not all data can be exported. The following constraints apply:

   * Nested data, e.g. `{'foo': {'bar': 'baz'}}` are excluded. Spreadsheets are not a great format for nested data. However, *tuples* are exported, and the characters `::` are used to join elements of the tuple.
   * The only well-supported data types are strings, numbers, and booleans.

   Default directory is ``projects.output_dir``, set ``dirpath`` to have save the file somewhere else.

   Returns the filepath of the exported file.



.. py:class:: DatabaseSelectionToGEXF(database, keys)

   Bases: :py:obj:`DatabaseToGEXF`

   Export a Gephi graph for a selection of activities from a database.

   Also includes all inputs for the filtered activities.

   :param \* *database*: Database name.
   :type \* *database*: str
   :param \* *keys*: The activity keys to export.
   :type \* *keys*: str


.. py:class:: DatabaseToGEXF(database, include_descendants=False)

   Bases: :py:obj:`object`

   Export a Gephi graph for a database.

   Call ``.export()`` to export the file after class instantiation.

   :param \* *database*: Database name.
   :type \* *database*: str
   :param \* *include_descendants*: Include databases which are linked from ``database``.
   :type \* *include_descendants*: bool

   .. warning:: ``include_descendants`` is not yet implemented.


   .. py:method:: export()

      Export the Gephi XML file. Returns the filepath of the created file.


   .. py:method:: get_data(E)

      Get Gephi nodes and edges.



.. py:function:: keyword_to_gephi_graph(database, keyword)

   Export a Gephi graph for a database for all activities whose names include the string ``keyword``.

   :param \* *database*: Database name.
   :type \* *database*: str
   :param \* *keyword*: Keyword to search for.
   :type \* *keyword*: str

   :returns: The filepath of the exported file.


.. py:function:: lci_matrices_to_matlab(database_name)


