:py:mod:`bw2io.importers.base`
==============================

.. py:module:: bw2io.importers.base


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.importers.base.ImportBase




.. py:class:: ImportBase(*args, **kwargs)

   Bases: :py:obj:`object`

   Base class for format-specific importers.
   Defines workflow for applying strategies.


   Initialize the ImportBase object.

   :param \*args: Variable length argument list.
   :param \*\*kwargs: Arbitrary keyword arguments.

   :raises NotImplemented :: This class should be subclassed.

   .. py:property:: unlinked

      Iterate through unique unlinked exchanges.

      Uniqueness is determined by `activity_hash`.

      :Yields: *exc* -- The unlinked exchange that is currently being iterated over.

   .. py:method:: _migrate_datasets(migration_name)

      Apply a migration function to the importer's datasets.

      This method applies a given migration function to the importer's datasets, using `migrate_datasets`. The
      migration function must be specified by name in the `migrations` dictionary.

      :param migration_name: The name of the migration function to apply to the importer's datasets.
      :type migration_name: str

      :returns: Modifies the importer's data in place.
      :rtype: None

      :raises AssertionError: If the specified migration function is not in the `migrations` dictionary.


   .. py:method:: _migrate_exchanges(migration_name)

      Apply a migration function to the importer's exchanges.

      This method applies a given migration function to the importer's exchanges, using `migrate_exchanges`. The
      migration function must be specified by name in the `migrations` dictionary.

      :param migration_name: The name of the migration function to apply to the importer's exchanges.
      :type migration_name: str

      :returns: Modifies the importer's data in place.
      :rtype: None

      :raises AssertionError: If the specified migration function is not in the `migrations` dictionary.


   .. py:method:: apply_strategies(strategies=None, verbose=True)

      Apply a list of strategies to the importer's data.

      This method applies a list of given strategies to the importer's data and logs the applied strategies' names to
      `self.applied_strategies`. If no list of strategies is provided, it uses `self.strategies`.

      :param strategies: List of strategies to apply. Defaults to `self.strategies`.
      :type strategies: list, optional
      :param verbose: If True, print a message indicating which strategy is being applied. Defaults to True.
      :type verbose: bool, optional

      :returns: Modifies the importer's data in place.
      :rtype: None

      .. rubric:: Notes

      The method `apply_strategy` is called to apply each individual strategy to the importer's data. Strategies
      that partially modify data before raising a `StrategyError` should be avoided.


   .. py:method:: apply_strategy(strategy, verbose=True)

      Apply the specified strategy transform to the importer's data.

      This method applies a given strategy to the importer's data and logs the applied strategy's name to
      `self.applied_strategies`. If the strategy raises a `StrategyError`, the error message is printed but
      not raised.

      :param strategy: The strategy function to apply to the importer's data.
      :type strategy: callable
      :param verbose: If True, print a message indicating which strategy is being applied. Defaults to True.
      :type verbose: bool, optional

      :returns: Modifies the importer's data in place.
      :rtype: None

      :raises None: If the strategy raises a `StrategyError`, the error message is printed but not raised.

      .. rubric:: Notes

      Strategies should not partially modify data before raising a `StrategyError`.


   .. py:method:: write_unlinked(name)

      Write all data to an `UnlinkedData` data store.

      This method writes all of the importer's data to an `UnlinkedData` data store with the specified `name`. The
      `UnlinkedData` object is created with the importer's class name appended to the `name`. The applied strategies
      are logged to the `unlinked_data` dictionary.

      :param name: The name of the `UnlinkedData` data store to be written.
      :type name: str



