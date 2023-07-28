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

   .. py:property:: unlinked

      Iterate through unique unlinked exchanges.

      Uniqueness is determined by ``activity_hash``.

   .. py:method:: _migrate_datasets(migration_name)


   .. py:method:: _migrate_exchanges(migration_name)


   .. py:method:: apply_strategies(strategies=None, verbose=True)

      Apply a list of strategies.

      Uses the default list ``self.strategies`` if ``strategies`` is ``None``.

      :param \*strategies*: List of strategies to apply. Defaults to ``self.strategies``.
      :type \*strategies*: list, optional

      :returns: Nothings, but modifies ``self.data``, and adds each strategy to ``self.applied_strategies``.


   .. py:method:: apply_strategy(strategy, verbose=True)

      Apply ``strategy`` transform to ``self.data``.

      Adds strategy name to ``self.applied_strategies``. If ``StrategyError`` is raised, print error message, but don't raise error.

      .. note:: Strategies should not partially modify data before raising ``StrategyError``.

      :param \*strategy*:
      :type \*strategy*: callable

      :returns: Nothing, but modifies ``self.data``, and strategy to ``self.applied_strategies``.


   .. py:method:: write_unlinked(name)

      Write all data to an ``UnlikedData`` data store (not a ``Database``!)



