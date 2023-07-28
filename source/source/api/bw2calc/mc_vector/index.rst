:py:mod:`bw2calc.mc_vector`
===========================

.. py:module:: bw2calc.mc_vector


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2calc.mc_vector.ParameterVectorLCA




.. py:class:: ParameterVectorLCA(demand, method=None, iter_solver=cgs, seed=None, *args, **kwargs)

   Bases: :py:obj:`bw2calc.monte_carlo.IterativeMonteCarlo`

   .. autoapi-inheritance-diagram:: bw2calc.mc_vector.ParameterVectorLCA
      :parts: 1
      :private-bases:

   A Monte Carlo class where all uncertain parameters are stored in a single large array.

   Useful for sensitivity analysis and easy manipulation.

   Create a new LCA calculation.

   :param \* *demand*: The demand or functional unit. Needs to be a dictionary to indicate amounts, e.g. ``{("my database", "my process"): 2.5}``.
   :type \* *demand*: dict
   :param \* *method*: LCIA Method tuple, e.g. ``("My", "great", "LCIA", "method")``. Can be omitted if only interested in calculating the life cycle inventory.
   :type \* *method*: tuple, optional

   :returns: A new LCA object

   .. py:property:: bio_sample


   .. py:property:: cf_sample


   .. py:property:: tech_sample


   .. py:property:: weighting_sample


   .. py:method:: load_data()


   .. py:method:: rebuild_all(vector=None)

      Rebuild the LCI/LCIA matrices from a new Monte Carlo sample or provided vector.



