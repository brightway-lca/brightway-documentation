:py:mod:`bw2calc.errors`
========================

.. py:module:: bw2calc.errors


Module Contents
---------------

.. py:exception:: BW2CalcError

   Bases: :py:obj:`Exception`

   Base class for bw2calc errors


.. py:exception:: OutsideTechnosphere

   Bases: :py:obj:`BW2CalcError`

   The given demand array activity is not in the technosphere matrix


.. py:exception:: EfficiencyWarning

   Bases: :py:obj:`RuntimeWarning`

   Least squares is much less efficient than direct computation for square, full-rank matrices


.. py:exception:: NoSolutionFound

   Bases: :py:obj:`UserWarning`

   No solution to set of linear equations found within given constraints


.. py:exception:: NonsquareTechnosphere

   Bases: :py:obj:`BW2CalcError`

   The given data do not form a square technosphere matrix


.. py:exception:: MalformedFunctionalUnit

   Bases: :py:obj:`BW2CalcError`

   The given functional unit cannot be understood


.. py:exception:: EmptyBiosphere

   Bases: :py:obj:`BW2CalcError`

   Can't do impact assessment with no biosphere flows


.. py:exception:: AllArraysEmpty

   Bases: :py:obj:`BW2CalcError`

   Can't load the numpy arrays if all of them are empty


.. py:exception:: NoArrays

   Bases: :py:obj:`BW2CalcError`

   No arrays for given matrix


.. py:exception:: InconsistentGlobalIndex

   Bases: :py:obj:`BW2CalcError`

   LCIA matrices are diagonal, and use the ``col`` field for regionalization. If multiple LCIA datapackages are present, they must use the same value for ``GLO``, the global location, in order for filtering for site-generic LCIA to work correctly.


.. py:exception:: MultipleValues

   Bases: :py:obj:`BW2CalcError`

   Multiple values are present, but only one value is expected


