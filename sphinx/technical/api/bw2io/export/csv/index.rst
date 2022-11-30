:py:mod:`bw2io.export.csv`
==========================

.. py:module:: bw2io.export.csv


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.export.csv.CSVFormatter



Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.export.csv.reformat
   bw2io.export.csv.write_lci_csv



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.export.csv.EXCHANGE_COLUMNS
   bw2io.export.csv.PARAMETER_COLUMNS
   bw2io.export.csv.MAPPING


.. py:function:: reformat(value)


.. py:data:: EXCHANGE_COLUMNS
   :annotation: = ['name', 'amount', 'database', 'location', 'unit', 'categories', 'type', 'formula', 'uncertainty...

   

.. py:data:: PARAMETER_COLUMNS
   :annotation: = ['name', 'amount', 'formula', 'uncertainty type', 'loc', 'scale', 'shape', 'minimum', 'maximum']

   

.. py:data:: MAPPING
   

   

.. py:class:: CSVFormatter(database_name, objs=None)

   Bases: :py:obj:`object`

   .. py:method:: get_project_parameters()


   .. py:method:: get_database_parameters()


   .. py:method:: get_activity_parameters(act)


   .. py:method:: get_database_metadata()


   .. py:method:: get_activity_metadata(act)


   .. py:method:: exchange_as_dict(exc)


   .. py:method:: order_dicts(data, kind='exchange')


   .. py:method:: get_exchanges(act)


   .. py:method:: get_activity(act)


   .. py:method:: get_unformatted_data()

      Return all database data as a nested dictionary:

      .. code-block:: python

          {
              'database': {
                  'name': name,
                  'metadata': [(key, value)],
                  'parameters': {
                      'columns': [column names],
                      'data': [[column values for each row]]
                  },
                  'project parameters': {
                      'columns': [column names],
                      'data': [[column values for each row]]
                  }
              },
              'activities': [{
                  'name': name,
                  'metadata': [(key, value)],
                  'parameters': {
                      'columns': [column names],
                      'group': 'group name',
                      'data': [[column values for each row]]
                  },
                  'exchanges': {
                      'columns': [column names],
                      'data': [[column values for each row]]
                  }
              }]
          }



   .. py:method:: get_formatted_data(sections=None)



.. py:function:: write_lci_csv(database_name, objs=None, sections=None, dirpath=None)

   Export database `database_name` to a CSV file.

   Not all data can be exported. The following constraints apply:

   * Nested data, e.g. `{'foo': {'bar': 'baz'}}` are excluded. CSV is not a great format for nested data. However, *tuples* are exported, and the characters `::` are used to join elements of the tuple.
   * The only well-supported data types are strings, numbers, and booleans.

   Default directory is ``projects.output_dir``, set ``dirpath`` to have save the file somewhere else.

   Returns the filepath of the exported file.



