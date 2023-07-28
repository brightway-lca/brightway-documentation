:py:mod:`bw2calc.errors`
========================

.. py:module:: bw2calc.errors


Module Contents
---------------

.. py:exception:: AllArraysEmpty

   Bases: :py:obj:`BW2CalcError`

   .. autoapi-inheritance-diagram:: bw2calc.errors.AllArraysEmpty
      :parts: 1
      :private-bases:

   Can't load the numpy arrays if all of them are empty

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: BW2CalcError

   Bases: :py:obj:`Exception`

   .. autoapi-inheritance-diagram:: bw2calc.errors.BW2CalcError
      :parts: 1
      :private-bases:

   Base class for bw2calc errors

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: EfficiencyWarning

   Bases: :py:obj:`RuntimeWarning`

   .. autoapi-inheritance-diagram:: bw2calc.errors.EfficiencyWarning
      :parts: 1
      :private-bases:

   Least squares is much less efficient than direct computation for square, full-rank matrices

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: EmptyBiosphere

   Bases: :py:obj:`BW2CalcError`

   .. autoapi-inheritance-diagram:: bw2calc.errors.EmptyBiosphere
      :parts: 1
      :private-bases:

   Can't do impact assessment with no biosphere flows

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: MalformedFunctionalUnit

   Bases: :py:obj:`BW2CalcError`

   .. autoapi-inheritance-diagram:: bw2calc.errors.MalformedFunctionalUnit
      :parts: 1
      :private-bases:

   The given functional unit cannot be understood

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: NoSolutionFound

   Bases: :py:obj:`UserWarning`

   .. autoapi-inheritance-diagram:: bw2calc.errors.NoSolutionFound
      :parts: 1
      :private-bases:

   No solution to set of linear equations found within given constraints

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: NonsquareTechnosphere

   Bases: :py:obj:`BW2CalcError`

   .. autoapi-inheritance-diagram:: bw2calc.errors.NonsquareTechnosphere
      :parts: 1
      :private-bases:

   The given data do not form a square technosphere matrix

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: OutsideTechnosphere

   Bases: :py:obj:`BW2CalcError`

   .. autoapi-inheritance-diagram:: bw2calc.errors.OutsideTechnosphere
      :parts: 1
      :private-bases:

   The given demand array activity is not in the technosphere matrix

   Initialize self.  See help(type(self)) for accurate signature.


