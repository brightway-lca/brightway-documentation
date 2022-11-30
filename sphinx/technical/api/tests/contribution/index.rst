:py:mod:`tests.contribution`
============================

.. py:module:: tests.contribution


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   tests.contribution.ContributionTestCase
   tests.contribution.Contribution2TestCase




.. py:class:: ContributionTestCase(methodName='runTest')

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

   .. py:method:: test_sort_array_number()


   .. py:method:: test_sort_array_percentage()


   .. py:method:: test_sort_array_percentage_negative()


   .. py:method:: test_sort_array_errors()


   .. py:method:: test_top_matrix_array()


   .. py:method:: test_top_matrix_matrix()



.. py:class:: Contribution2TestCase

   Bases: :py:obj:`bw2data.tests.BW2DataTest`

   .. py:method:: install_fixtures()


   .. py:method:: test_hinton_matrix_no_error()


   .. py:method:: test_d3_treemap_no_error()



