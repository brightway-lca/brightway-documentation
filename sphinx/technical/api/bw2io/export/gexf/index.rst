:py:mod:`bw2io.export.gexf`
===========================

.. py:module:: bw2io.export.gexf


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.export.gexf.DatabaseToGEXF
   bw2io.export.gexf.DatabaseSelectionToGEXF



Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.export.gexf.keyword_to_gephi_graph



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



.. py:class:: DatabaseSelectionToGEXF(database, keys)

   Bases: :py:obj:`DatabaseToGEXF`

   Export a Gephi graph for a selection of activities from a database.

   Also includes all inputs for the filtered activities.

   :param \* *database*: Database name.
   :type \* *database*: str
   :param \* *keys*: The activity keys to export.
   :type \* *keys*: str


.. py:function:: keyword_to_gephi_graph(database, keyword)

   Export a Gephi graph for a database for all activities whose names include the string ``keyword``.

   :param \* *database*: Database name.
   :type \* *database*: str
   :param \* *keyword*: Keyword to search for.
   :type \* *keyword*: str

   :returns: The filepath of the exported file.


