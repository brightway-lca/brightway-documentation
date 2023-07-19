:py:mod:`bw2io.strategies.parameterization`
===========================================

.. py:module:: bw2io.strategies.parameterization


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.strategies.parameterization.ReservedVariableNameSubstitutor




Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.parameterization.RESERVED
   bw2io.strategies.parameterization.variable_subtitutor


.. py:class:: ReservedVariableNameSubstitutor

   A class to substitute reserved variable names in formulas with their uppercase versions.

   This class replaces reserved Python keywords, as well as built-in function names,
   with their uppercase versions in a given formula string.

   .. attribute:: symbols

      A set of reserved Python keywords and built-in function names.

      :type: set

   .. attribute:: matches

      A list of tuples, where each tuple contains a compiled regular expression pattern
      and a substitution string for each reserved symbol.

      :type: list

   .. rubric:: Examples

   >>> variable_substitutor = ReservedVariableNameSubstitutor()
   >>> formula = "sum = a + b + max(1, 2)"
   >>> variable_substitutor.fix_formula(formula)
   'SUM = a + b + MAX(1, 2)'

   >>> variable_name = "sum"
   >>> variable_substitutor.fix_variable_name(variable_name)
   'SUM'

   .. py:method:: fix_formula(string)

      Substitute reserved variable names in a formula with their uppercase versions.

      :param string: The formula containing reserved variable names to be replaced.
      :type string: str

      :returns: The updated formula with reserved variable names replaced with their uppercase versions.
      :rtype: str


   .. py:method:: fix_variable_name(string)

      Substitute a reserved variable name with its uppercase version if necessary.

      :param string: The variable name to be checked and possibly replaced.
      :type string: str

      :returns: The updated variable name, replaced with its uppercase version if it was a reserved variable name.
      :rtype: str



.. py:data:: RESERVED

   

.. py:data:: variable_subtitutor

   

