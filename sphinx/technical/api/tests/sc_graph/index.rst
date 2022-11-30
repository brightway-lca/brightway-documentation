:py:mod:`tests.sc_graph`
========================

.. py:module:: tests.sc_graph


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   tests.sc_graph.UnrollGraphTestCase
   tests.sc_graph.MetadataTestCase
   tests.sc_graph.SimplifyTestCase




.. py:class:: UnrollGraphTestCase(methodName='runTest')

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

   .. py:method:: test_simple_chain()


   .. py:method:: test_multiple_inputs()


   .. py:method:: test_pruning()


   .. py:method:: test_unroll_circular()


   .. py:method:: test_max_links()


   .. py:method:: test_diamond()


   .. py:method:: test_circle_with_branches()



.. py:class:: MetadataTestCase

   Bases: :py:obj:`bw2data.tests.BW2DataTest`

   .. py:class:: LCAMock


   .. py:method:: extra_setup()


   .. py:method:: test_setup_clean()


   .. py:method:: test_without_row()


   .. py:method:: test_with_functional_unit()


   .. py:method:: test_with_row()



.. py:class:: SimplifyTestCase(methodName='runTest')

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

   .. py:method:: test_nodes_dont_change()


   .. py:method:: test_linear()

      Test supply chain graph like this:

      o
      |    o
      x => |
      |    o
      o



   .. py:method:: test_y()

      Test supply chain graph like this:

      o   o     o   o
       \ /       \ /
        x   =>    o
        |
        o



   .. py:method:: test_no_self_edge()

      Test that collapsed edges from a -> a are deleted.


   .. py:method:: test_diamond()

      Test supply chain graph like this:

        o
       / \      o
      x   x =>  |
       \ /      o
        o



   .. py:method:: test_x()

      Test supply chain graph like this:

      o   o
       \ /      o  o
        x   =>  |\/|
       / \      |/\|
      o   o     o  o



