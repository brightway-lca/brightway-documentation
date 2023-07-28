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
   bw2io.export.csv.MAPPING
   bw2io.export.csv.PARAMETER_COLUMNS


.. py:class:: CSVFormatter(database_name, objs=None)

   Bases: :py:obj:`object`

   .. py:method:: exchange_as_dict(exc)


   .. py:method:: get_activity(act)


   .. py:method:: get_activity_metadata(act)


   .. py:method:: get_activity_parameters(act)


   .. py:method:: get_database_metadata()


   .. py:method:: get_database_parameters()


   .. py:method:: get_exchanges(act)


   .. py:method:: get_formatted_data(sections=None)


   .. py:method:: get_project_parameters()


   .. py:method:: get_unformatted_data()

      Return all database data as a nested dictionary:

      :returns: A nested python dictionary with the following structure:

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
      :rtype: dict


   .. py:method:: order_dicts(data, kind='exchange')



.. py:function:: reformat(value)


.. py:function:: write_lci_csv(database_name, objs=None, sections=None, dirpath=None)

   Export database `database_name` to a CSV file.

   .. rubric:: Notes

   Not all data can be exported. The following constraints apply:

   * Nested data, e.g. `{'foo': {'bar': 'baz'}}` are excluded.
   * CSV is not a great format for nested data. However, *tuples* are exported, and the characters `::` are used to join elements of the tuple.
   * The only well-supported data types are strings, numbers, and booleans.

   Default directory is ``projects.output_dir``, set ``dirpath`` to have save the file somewhere else.

   :param database_name: The name of the database to export.
   :type database_name: str
   :param objs: A list of objects to export. If not provided, all objects in the database will be exported.
   :type objs: list, optional
   :param sections: A list of sections to export. If not provided, all sections will be exported.
   :type sections: list, optional
   :param dirpath: The directory to save the file to. If not provided, the default directory is ``projects.output_dir``.
   :type dirpath: str, optional

   :returns: The filepath of the exported file.
   :rtype: str


.. py:data:: EXCHANGE_COLUMNS
   :value: ['name', 'amount', 'database', 'location', 'unit', 'categories', 'type', 'formula', 'uncertainty...

   

.. py:data:: MAPPING

   

.. py:data:: PARAMETER_COLUMNS
   :value: ['name', 'amount', 'formula', 'uncertainty type', 'loc', 'scale', 'shape', 'minimum', 'maximum']

   

