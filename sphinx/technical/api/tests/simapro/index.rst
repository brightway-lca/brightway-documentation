:py:mod:`tests.simapro`
=======================

.. py:module:: tests.simapro


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   tests.simapro.SimaProCSVImporterTest



Functions
~~~~~~~~~

.. autoapisummary::

   tests.simapro.test_sp_import_allocation
   tests.simapro.test_sp_wrong_field_ordering
   tests.simapro.test_sp_python_builtin_as_unit_name
   tests.simapro.test_damage_category_import
   tests.simapro.test_set_lognormal_loc_value_on_import



Attributes
~~~~~~~~~~

.. autoapisummary::

   tests.simapro.SP_FIXTURES_DIR


.. py:data:: SP_FIXTURES_DIR
   

   

.. py:function:: test_sp_import_allocation()


.. py:function:: test_sp_wrong_field_ordering()


.. py:function:: test_sp_python_builtin_as_unit_name()


.. py:function:: test_damage_category_import()


.. py:function:: test_set_lognormal_loc_value_on_import()


.. py:class:: SimaProCSVImporterTest(methodName='runTest')

   Bases: :py:obj:`bw2data.tests.BW2DataTest`

   A class whose instances are single test cases.

   By default, the test code itself should be placed in a method named
   'runTest'.

   If the fixture may be used for many test cases, create as
   many test methods as are needed. When instantiating such a TestCase
   subclass, specify in the constructor arguments the name of the test method
   that the instance is to execute.

   Test authors should subclass TestCase for their own tests. Construction
   and deconstruction of the test's environment ('fixture') can be
   implemented by overriding the 'setUp' and 'tearDown' methods respectively.

   If it is necessary to override the __init__ method, the base class
   __init__ method must always be called. It is important that subclasses
   should not change the signature of their __init__ method, since instances
   of the classes are instantiated automatically by parts of the framework
   in order to be run.

   When subclassing TestCase, you can set these attributes:
   * failureException: determines which exception will be raised when
       the instance's assertion methods fail; test methods raising this
       exception will be deemed to have 'failed' rather than 'errored'.
   * longMessage: determines whether long messages (including repr of
       objects used in assert methods) will be printed on failure in *addition*
       to any explicit message passed.
   * maxDiff: sets the maximum length of a diff in failure messages
       by assert methods using difflib. It is looked up as an instance
       attribute so can be configured by individual tests if required.


