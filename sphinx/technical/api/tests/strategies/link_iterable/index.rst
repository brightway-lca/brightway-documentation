:py:mod:`tests.strategies.link_iterable`
========================================

.. py:module:: tests.strategies.link_iterable


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   tests.strategies.link_iterable.LinkIterableTestCase




.. py:class:: LinkIterableTestCase(methodName='runTest')

   Bases: :py:obj:`unittest.TestCase`

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

   .. py:method:: test_all_datasets_in_target_have_database_field()


   .. py:method:: test_all_datasets_in_target_have_code_field()


   .. py:method:: test_nonunique_target_but_not_linked_no_error()


   .. py:method:: test_nonunique_target_raises_error()


   .. py:method:: test_generic_linking_no_kind_no_relink()


   .. py:method:: test_internal_linking()


   .. py:method:: test_kind_filter()


   .. py:method:: test_kind_filter_and_relink()


   .. py:method:: test_relink()


   .. py:method:: test_linking_with_fields()


   .. py:method:: test_no_relink_skips_linking()



