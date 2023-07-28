:py:mod:`bw2io.strategies.biosphere`
====================================

.. py:module:: bw2io.strategies.biosphere


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.biosphere.drop_unspecified_subcategories
   bw2io.strategies.biosphere.ensure_categories_are_tuples
   bw2io.strategies.biosphere.normalize_biosphere_categories
   bw2io.strategies.biosphere.normalize_biosphere_names
   bw2io.strategies.biosphere.strip_biosphere_exc_locations



.. py:function:: drop_unspecified_subcategories(db)

   Drop subcategories if they are in the following:
   * ``unspecified``
   * ``(unspecified)``
   * ``''`` (empty string)
   * ``None``

   :param db: A list of datasets, each containing exchanges.
   :type db: list

   :returns: A modified list of datasets with unspecified subcategories removed.
   :rtype: list

   .. rubric:: Examples

   >>> db = [{"categories": ["A", "unspecified"]},
               {"exchanges": [{"categories": ["B", ""]}]},
               {"categories": ["C", None]}]
   >>> new_db = drop_unspecified_subcategories(db)
   >>> new_db
   [{"categories": ["A"]}, {"exchanges": [{"categories": ["B"]}]}, {"categories": ["C"]}]


.. py:function:: ensure_categories_are_tuples(db)

   Convert dataset categories to tuples in the given database, if they are not already tuples.

   :param db: A list of datasets, each containing exchanges.
   :type db: list

   :rtype: A modified list of datasets with categories as tuples.

   .. rubric:: Examples

   >>> db = [{"categories": ["A", "B"]}, {"categories": ("C", "D")}]
   >>> new_db = ensure_categories_are_tuples(db)
   >>> new_db
   [{"categories": ("A", "B")}, {"categories": ("C", "D")}]


.. py:function:: normalize_biosphere_categories(db, lcia=False)

   Normalize biosphere categories to ecoinvent 3.1 standard in the given database.

   :param db: A list of datasets, each containing exchanges.
   :type db: list
   :param lcia: If True, only normalize biosphere categories in LCIA datasets. Defaults to False.
   :type lcia: bool, optional

   :returns: A modified list of datasets with normalized biosphere categories.
   :rtype: list

   .. rubric:: Examples

   >>> db = [{"categories": ["old_biosphere_category"]}]
   >>> new_db = normalize_biosphere_categories(db)
   >>> new_db
   [{"categories": ["new_biosphere_category"]}]


.. py:function:: normalize_biosphere_names(db, lcia=False)

   Normalize biosphere flow names to ecoinvent 3.1 standard in the given database.

   Assumes that each dataset and each exchange have a ``name``. Will change names even if exchange is already linked.

   :param db: A list of datasets, each containing exchanges.
   :type db: list
   :param lcia: If True, only normalize biosphere flow names in LCIA datasets. Default is False.
   :type lcia: bool, optional

   :returns: A modified list of datasets with normalized biosphere flow names.
   :rtype: list

   .. rubric:: Examples

   >>> db = [{"name": "old_biosphere_name"}]
   >>> new_db = normalize_biosphere_names(db)
   >>> new_db
   [{"name": "new_biosphere_name"}]


.. py:function:: strip_biosphere_exc_locations(db)

   Remove locations from biosphere exchanges in the given database, as biosphere exchanges are not geographically specific.

   :param db: A list of datasets, each containing exchanges.
   :type db: list

   :returns: A modified list of datasets with locations removed from biosphere exchanges.
   :rtype: list

   .. rubric:: Examples

   >>> db = [{"exchanges": [{"type": "biosphere", "location": "GLO"}]}]
   >>> new_db = strip_biosphere_exc_locations(db)
   >>> new_db
   [{"exchanges": [{"type": "biosphere"}]}]


