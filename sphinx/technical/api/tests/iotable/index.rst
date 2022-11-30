:py:mod:`tests.iotable`
=======================

.. py:module:: tests.iotable


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   tests.iotable.iotable_fixture
   tests.iotable.test_iotable_setup_clean
   tests.iotable.test_iotable_matrix_construction
   tests.iotable.test_iotable_process_method
   tests.iotable.test_iotable_edges_to_dataframe
   tests.iotable.test_iotable_nodes_to_dataframe
   tests.iotable.test_iotable_get_methods_correct_class
   tests.iotable.test_iotable_activity
   tests.iotable.test_iotable_activity_edges_to_dataframe
   tests.iotable.test_correct_backend_fixture
   tests.iotable.test_iotable_edges_production
   tests.iotable.test_iotable_edges_technosphere
   tests.iotable.test_iotable_edges_biosphere
   tests.iotable.test_substitution
   tests.iotable.test_iotabe_readonlyexchange
   tests.iotable.test_iotabe_readonlyexchange_missing_methods
   tests.iotable.test_iotabe_readonlyexchange_not_setitem
   tests.iotable.test_iotable_filtered_datapackage



.. py:function:: iotable_fixture()

   Technosphere matrix:

       a   b   c
   a   2   0   -3
   b   -1  1   0
   c   4   0.2 -1

   Biosphere matrix:

       a   b   c
   d   0   1   2

   Characterization matrix:

       d
   d   42



.. py:function:: test_iotable_setup_clean(iotable_fixture)


.. py:function:: test_iotable_matrix_construction(iotable_fixture)


.. py:function:: test_iotable_process_method(iotable_fixture)


.. py:function:: test_iotable_edges_to_dataframe(iotable_fixture)


.. py:function:: test_iotable_nodes_to_dataframe(iotable_fixture)


.. py:function:: test_iotable_get_methods_correct_class(iotable_fixture)


.. py:function:: test_iotable_activity(iotable_fixture)


.. py:function:: test_iotable_activity_edges_to_dataframe(iotable_fixture)


.. py:function:: test_correct_backend_fixture(iotable_fixture)


.. py:function:: test_iotable_edges_production(iotable_fixture)


.. py:function:: test_iotable_edges_technosphere(iotable_fixture)


.. py:function:: test_iotable_edges_biosphere(iotable_fixture)


.. py:function:: test_substitution(iotable_fixture)


.. py:function:: test_iotabe_readonlyexchange(iotable_fixture)


.. py:function:: test_iotabe_readonlyexchange_missing_methods(iotable_fixture)


.. py:function:: test_iotabe_readonlyexchange_not_setitem(iotable_fixture)


.. py:function:: test_iotable_filtered_datapackage(iotable_fixture)


