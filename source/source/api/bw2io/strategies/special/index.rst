:py:mod:`bw2io.strategies.special`
==================================

.. py:module:: bw2io.strategies.special


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.special.add_dummy_processes_and_rename_exchanges



.. py:function:: add_dummy_processes_and_rename_exchanges(db)

   Add new processes to link to so-called "dummy" processes in the US LCI database.

   This function adds new processes to link to dummy processes found in the US LCI
   database and renames the exchanges accordingly.

   :param db: A list of datasets containing exchanges with dummy processes.
   :type db: list

   :returns: A modified list of datasets with new processes added and exchanges renamed.
   :rtype: list

   .. rubric:: Examples

   >>> db = [
           {
               "database": "uslci",
               "exchanges": [
                   {
                       "name": "dummy_Production",
                       "input": ("uslci", "dummy_Production"),
                       "type": "production",
                       "amount": 1
                   }
               ]
           }
       ]
   >>> add_dummy_processes_and_rename_exchanges(db)
   [
       {
           "database": "uslci",
           "exchanges": [
               {
                   "name": "dummy_Production",
                   "input": ("uslci", "Production"),
                   "type": "production",
                   "amount": 1
               }
           ]
       },
       {
           "name": "Production",
           "database": "uslci",
           "code": "Production",
           "categories": ("dummy",),
           "location": "GLO",
           "type": "process",
           "exchanges": [
               {
                   "input": ("uslci", "Production"),
                   "type": "production",
                   "amount": 1
               }
           ]
       }
   ]


