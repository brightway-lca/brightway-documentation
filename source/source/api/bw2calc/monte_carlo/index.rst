:py:mod:`bw2calc.monte_carlo`
=============================

.. py:module:: bw2calc.monte_carlo


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2calc.monte_carlo.ComparativeMonteCarlo
   bw2calc.monte_carlo.DirectSolvingMixin
   bw2calc.monte_carlo.DirectSolvingMonteCarloLCA
   bw2calc.monte_carlo.IterativeMonteCarlo
   bw2calc.monte_carlo.MonteCarloLCA
   bw2calc.monte_carlo.MultiMonteCarlo
   bw2calc.monte_carlo.ParallelMonteCarlo



Functions
~~~~~~~~~

.. autoapisummary::

   bw2calc.monte_carlo.direct_solving_worker
   bw2calc.monte_carlo.multi_worker
   bw2calc.monte_carlo.pool_adapter
   bw2calc.monte_carlo.single_worker



.. py:class:: ComparativeMonteCarlo(demands, *args, **kwargs)

   Bases: :py:obj:`IterativeMonteCarlo`

   .. autoapi-inheritance-diagram:: bw2calc.monte_carlo.ComparativeMonteCarlo
      :parts: 1
      :private-bases:

   First draft approach at comparative LCA

   Create a new LCA calculation.

   :param \* *demand*: The demand or functional unit. Needs to be a dictionary to indicate amounts, e.g. ``{("my database", "my process"): 2.5}``.
   :type \* *demand*: dict
   :param \* *method*: LCIA Method tuple, e.g. ``("My", "great", "LCIA", "method")``. Can be omitted if only interested in calculating the life cycle inventory.
   :type \* *method*: tuple, optional

   :returns: A new LCA object

   .. py:method:: load_data()



.. py:class:: DirectSolvingMixin(demand, method=None, iter_solver=cgs, seed=None, *args, **kwargs)

   Bases: :py:obj:`IterativeMonteCarlo`

   .. autoapi-inheritance-diagram:: bw2calc.monte_carlo.DirectSolvingMixin
      :parts: 1
      :private-bases:

   Base class to use iterative techniques instead of `LU factorization <http://en.wikipedia.org/wiki/LU_decomposition>`_ in Monte Carlo.

   Create a new LCA calculation.

   :param \* *demand*: The demand or functional unit. Needs to be a dictionary to indicate amounts, e.g. ``{("my database", "my process"): 2.5}``.
   :type \* *demand*: dict
   :param \* *method*: LCIA Method tuple, e.g. ``("My", "great", "LCIA", "method")``. Can be omitted if only interested in calculating the life cycle inventory.
   :type \* *method*: tuple, optional

   :returns: A new LCA object

   .. py:method:: solve_linear_system()

      Master solution function for linear system :math:`Ax=B`.

          To most numerical analysts, matrix inversion is a sin.

          -- Nicolas Higham, Accuracy and Stability of Numerical Algorithms, Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 2002, p. 260.

      We use `UMFpack <http://www.cise.ufl.edu/research/sparse/umfpack/>`_, which is a very fast solver for sparse matrices.

      If the technosphere matrix has already been factorized, then the decomposed technosphere (``self.solver``) is reused. Otherwise the calculation is redone completely.





.. py:class:: DirectSolvingMonteCarloLCA(demand, method=None, iter_solver=cgs, seed=None, *args, **kwargs)

   Bases: :py:obj:`MonteCarloLCA`, :py:obj:`DirectSolvingMixin`

   .. autoapi-inheritance-diagram:: bw2calc.monte_carlo.DirectSolvingMonteCarloLCA
      :parts: 1
      :private-bases:

   Monte Carlo uncertainty analysis with separate `random number generators <http://en.wikipedia.org/wiki/Random_number_generation>`_ (RNGs) for each set of parameters.

   Create a new LCA calculation.

   :param \* *demand*: The demand or functional unit. Needs to be a dictionary to indicate amounts, e.g. ``{("my database", "my process"): 2.5}``.
   :type \* *demand*: dict
   :param \* *method*: LCIA Method tuple, e.g. ``("My", "great", "LCIA", "method")``. Can be omitted if only interested in calculating the life cycle inventory.
   :type \* *method*: tuple, optional

   :returns: A new LCA object


.. py:class:: IterativeMonteCarlo(demand, method=None, iter_solver=cgs, seed=None, *args, **kwargs)

   Bases: :py:obj:`bw2calc.lca.LCA`

   .. autoapi-inheritance-diagram:: bw2calc.monte_carlo.IterativeMonteCarlo
      :parts: 1
      :private-bases:

   Base class to use iterative techniques instead of `LU factorization <http://en.wikipedia.org/wiki/LU_decomposition>`_ in Monte Carlo.

   Create a new LCA calculation.

   :param \* *demand*: The demand or functional unit. Needs to be a dictionary to indicate amounts, e.g. ``{("my database", "my process"): 2.5}``.
   :type \* *demand*: dict
   :param \* *method*: LCIA Method tuple, e.g. ``("My", "great", "LCIA", "method")``. Can be omitted if only interested in calculating the life cycle inventory.
   :type \* *method*: tuple, optional

   :returns: A new LCA object

   .. py:method:: solve_linear_system()

      Master solution function for linear system :math:`Ax=B`.

          To most numerical analysts, matrix inversion is a sin.

          -- Nicolas Higham, Accuracy and Stability of Numerical Algorithms, Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 2002, p. 260.

      We use `UMFpack <http://www.cise.ufl.edu/research/sparse/umfpack/>`_, which is a very fast solver for sparse matrices.

      If the technosphere matrix has already been factorized, then the decomposed technosphere (``self.solver``) is reused. Otherwise the calculation is redone completely.





.. py:class:: MonteCarloLCA(demand, method=None, iter_solver=cgs, seed=None, *args, **kwargs)

   Bases: :py:obj:`IterativeMonteCarlo`

   .. autoapi-inheritance-diagram:: bw2calc.monte_carlo.MonteCarloLCA
      :parts: 1
      :private-bases:

   Monte Carlo uncertainty analysis with separate `random number generators <http://en.wikipedia.org/wiki/Random_number_generation>`_ (RNGs) for each set of parameters.

   Create a new LCA calculation.

   :param \* *demand*: The demand or functional unit. Needs to be a dictionary to indicate amounts, e.g. ``{("my database", "my process"): 2.5}``.
   :type \* *demand*: dict
   :param \* *method*: LCIA Method tuple, e.g. ``("My", "great", "LCIA", "method")``. Can be omitted if only interested in calculating the life cycle inventory.
   :type \* *method*: tuple, optional

   :returns: A new LCA object

   .. py:method:: load_data()



.. py:class:: MultiMonteCarlo(demands, method, iterations, cpus=None)

   Bases: :py:obj:`object`

   This is a class for the efficient calculation of *many* demand vectors from
   each Monte Carlo iteration.

   :param \* ``args`` is a list of demand dictionaries:
   :param \* ``method`` is a LCIA method:
   :param \* ``iterations`` is the number of Monte Carlo iterations desired:
   :param \* ``cpus`` is the:
   :type \* ``cpus`` is the: optional

   The input list can have complex demands, so ``[{('foo', 'bar'): 1, ('foo', 'baz'): 1}, {('foo', 'another'): 1}]`` is OK.

   Call ``.calculate()`` to generate results.



   .. py:method:: calculate(worker=multi_worker)

      Calculate Monte Carlo results for many demand vectors.

      Returns a list of results with the format::

          [(demand dictionary, [lca scores])]

      There is no guarantee that the results are returned in the same order as the ``demand`` input variable.



   .. py:method:: merge_results(objs)

      Merge the results from each ``multi_worker`` worker.

      ``[('a', [0,1]), ('a', [2,3])]`` becomes ``[('a', [0,1,2,3)]``.




.. py:class:: ParallelMonteCarlo(demand, method, iterations=1000, chunk_size=None, cpus=None, log_config=None)

   Bases: :py:obj:`object`

   Split a Monte Carlo calculation into parallel jobs

   .. py:method:: calculate(worker=single_worker)



.. py:function:: direct_solving_worker(args)


.. py:function:: multi_worker(args)

   Calculate a single Monte Carlo iteration for many demands.

   ``args`` are in order:
       * ``project``: Name of project
       * ``demands``: List of demand dictionaries
       * ``method``: LCIA method

   Returns a list of results: ``[(demand dictionary, result)]``



.. py:function:: pool_adapter(pool)


.. py:function:: single_worker(args)


