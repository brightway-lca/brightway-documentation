:py:mod:`lca_old`
=================

.. py:module:: lca_old


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   lca_old.LCACalculationTestCase



Functions
~~~~~~~~~

.. autoapisummary::

   lca_old.test_empty_biosphere_lcia
   lca_old.test_warning_empty_biosphere



.. py:function:: test_empty_biosphere_lcia()


.. py:function:: test_warning_empty_biosphere()


.. py:class:: LCACalculationTestCase

   Bases: :py:obj:`bw2data.tests.BW2DataTest`

   .. py:method:: add_basic_biosphere()


   .. py:method:: test_basic()


   .. py:method:: test_redo_lci_fails_if_activity_outside_technosphere()


   .. py:method:: test_redo_lci_with_no_new_demand_no_error()


   .. py:method:: test_passing_falsey_key()


   .. py:method:: test_pass_object_as_demand()


   .. py:method:: test_production_values()


   .. py:method:: test_substitution()


   .. py:method:: test_substitution_no_type()


   .. py:method:: test_circular_chains()


   .. py:method:: test_only_products()


   .. py:method:: test_activity_product_dict()


   .. py:method:: test_process_product_split()


   .. py:method:: test_activity_as_fu_raises_error()


   .. py:method:: test_nonsquare_technosphere_error()


   .. py:method:: test_multiple_lci_calculations()


   .. py:method:: test_dependent_databases()


   .. py:method:: test_filepaths_full()


   .. py:method:: test_filepaths_empty()


   .. py:method:: test_demand_type()


   .. py:method:: test_decomposed_uses_solver()


   .. py:method:: test_fix_dictionaries()


   .. py:method:: test_redo_lci_switches_demand()


   .. py:method:: test_basic_lcia()


   .. py:method:: test_redo_lcia_switches_demand()


   .. py:method:: test_lcia_regionalized_ignored()



