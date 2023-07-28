:py:mod:`bw2io.export.gexf`
===========================

.. py:module:: bw2io.export.gexf


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.export.gexf.DatabaseSelectionToGEXF
   bw2io.export.gexf.DatabaseToGEXF



Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.export.gexf.keyword_to_gephi_graph



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.export.gexf.monitor


.. py:class:: DatabaseSelectionToGEXF(database, keys)

   Bases: :py:obj:`DatabaseToGEXF`

   .. autoapi-inheritance-diagram:: bw2io.export.gexf.DatabaseSelectionToGEXF
      :parts: 1
      :private-bases:

   Export a Gephi graph for a selection of activities from a database.

   Also includes all inputs for the filtered activities.

   :param database: Database name.
   :type database: str
   :param keys: The activity keys to export.
   :type keys: str

   .. rubric:: Examples

   >>> dstg = DatabaseSelectionToGEXF(database='example_db', keys=['foo', 'bar'])


.. py:class:: DatabaseToGEXF(database, include_descendants=False)

   Bases: :py:obj:`object`

   Export a Gephi graph for a database.

   :param database: Database name.
   :type database: str
   :param include_descendants: Include databases which are linked from ``database``. (default False)
   :type include_descendants: bool, optional

   .. warning:: ``include_descendants`` is not yet implemented.

   :raises NotImplemented: If ``include_descendants`` is True, as this option is not yet implemented.

   .. method:: export()

      Export the Gephi XML file.

   .. method:: get_data(E)

      Get the nodes and edges for the Gephi XML file.


   .. rubric:: Examples

   >>> dtg = DatabaseToGEXF(database='example_db', include_descendants=False)
   >>> dtg.export()
   '/path/to/example_db.gexf'

   >>> dtg = DatabaseToGEXF(database='example_db', include_descendants=True)
   >>> dtg.get_data()
   (nodes, edges)

   .. py:method:: export()

      Export the Gephi XML file.

      :param None:

      :returns: Filepath of the created file.
      :rtype: str

      .. rubric:: Examples

      >>> dtg = DatabaseToGEXF(database='example_db', include_descendants=False)
      >>> dtg.export()
      '/path/to/example_db.gexf'


   .. py:method:: get_data(E)

      Get Gephi nodes and edges.

      :param E: ElementMaker object for GEXF XML
      :type E: lxml.builder.ElementMaker

      :returns: * **nodes** (*lxml.etree._Element*) -- GEXF nodes
                * **edges** (*lxml.etree._Element*) -- GEXF edges

      .. rubric:: Examples

      >>> dtg = DatabaseToGEXF(database='example_db', include_descendants=False)
      >>> dtg.get_data(E)
      (nodes, edges)



.. py:function:: keyword_to_gephi_graph(database, keyword)

   Export a Gephi graph for a database for all activities whose names include the string ``keyword``.

   :param database: Database name.
   :type database: str
   :param keyword: Keyword to search for.
   :type keyword: str

   :returns: The filepath of the exported file.
   :rtype: str

   .. rubric:: Examples

   >>> keyword_to_gephi_graph(database='example_db', keyword='foo')
   '/path/to/example_db.gexf'


.. py:data:: monitor
   :value: True

   

