:py:mod:`bw2io.strategies.locations`
====================================

.. py:module:: bw2io.strategies.locations


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.locations.update_ecoinvent_locations



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.locations.GEO_UPDATE


.. py:function:: update_ecoinvent_locations(db)

   Update location names in ecoinvent database to fix inconsistencies and standardize naming.

   Maps the old location names to the updated ones based on a predefined dictionary (GEO_UPDATE).

   :param db: A list of dictionaries representing ecoinvent processes with exchanges.
   :type db: list

   :returns: A list of dictionaries representing the ecoinvent processes with updated location names.
   :rtype: list

   .. rubric:: Examples

   >>> db = [
   ...     {
   ...         "name": "Process 1",
   ...         "location": "IAI Area 2, North America",
   ...         "exchanges": [{"name": "Flow 1", "location": "IAI Area 2, North America"}],
   ...     }
   ... ]
   >>> update_ecoinvent_locations(db)
   [
       {
           "name": "Process 1",
           "location": "IAI Area, North America",
           "exchanges": [{"name": "Flow 1", "location": "IAI Area, North America"}],
       }
   ]

   .. rubric:: Notes

   Includes a hardcoded mapping (GEO_UPDATE) to fix known inconsistencies in location names. This may not
   cover all possible inconsistencies and might need to be updated in the future.


.. py:data:: GEO_UPDATE

   

