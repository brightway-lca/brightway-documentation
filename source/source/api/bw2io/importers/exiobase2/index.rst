:py:mod:`bw2io.importers.exiobase2`
===================================

.. py:module:: bw2io.importers.exiobase2


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.importers.exiobase2.Exiobase22Importer



Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.importers.exiobase2.extract_exiobase_technosphere
   bw2io.importers.exiobase2.get_biosphere_lookup_dict
   bw2io.importers.exiobase2.relabel_emissions
   bw2io.importers.exiobase2.relabel_exchanges



.. py:class:: Exiobase22Importer(filepath, db_name='EXIOBASE 2.2')

   Bases: :py:obj:`object`

   .. py:attribute:: format
      :value: 'Exiobase 2.2'

      

   .. py:method:: apply_strategies(biosphere=None)


   .. py:method:: write_database()



.. py:function:: extract_exiobase_technosphere(industries, countries, db_name)

   Create activity datasets for each combination of `industries` and `countries`.


.. py:function:: get_biosphere_lookup_dict(substances, extractions, biosphere=None)


.. py:function:: relabel_emissions(emissions_table, db_name, lookup)

   Turn rows into a generator of (flow, process, type, amount) tuples.

   Original data format:

       (
           'AT',
           'Cultivation of wheat',
           'CO2 - combustion',
           'air',
           'kg/M.EUR',
           289687.6972210754
       )

   * `emissions_table` is the list of raw data lines.
   * `db_name` is the string name of the database, 'Exiobase 2.2' by default.
   * `lookup` is a dictionary from string flow names to biosphere keys.

   :returns:

             (
                 ("biosphere3", "some-code"),  # Looks up 'CO2 - combustion' in `lookup`
                 ("Exiobase 2.2", "Cultivation of wheat:AT"),
                 289687.6972210754
             )


.. py:function:: relabel_exchanges(table, db_name)


