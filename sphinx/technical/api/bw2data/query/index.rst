:py:mod:`bw2data.query`
=======================

.. py:module:: bw2data.query


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.query.Dictionaries
   bw2data.query.Result
   bw2data.query.Query
   bw2data.query.Filter



Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.query.try_op
   bw2data.query.NF
   bw2data.query.PF



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2data.query.operators


.. py:data:: operators
   

   

.. py:function:: try_op(f, x, y)


.. py:class:: Dictionaries(*args)

   Pretends to be a single dictionary when applying a ``Query`` to multiple databases.

   Usage:
       first_database = Database(...).load()
       second_database = Database(...).load()
       my_joined_dataset = Dictionaries(first_database, second_database)
       search_results = Query(filter_1, filter_2)(my_joined_dataset)


   .. py:method:: items()



.. py:class:: Result(result)

   A container that wraps a filtered dataset. Returned by a calling a ``Query`` object. A result object functions like a read-only dictionary; you can call ``Result[some_key]``, or ``some_key in Result``, or ``len(Result)``.

   The dataset can also be sorted, using ``sort(field)``; the underlying data is then a ``collections.OrderedDict``.

   :param \* *result*: The filtered dataset.
   :type \* *result*: dict

   .. py:method:: __str__()

      Return str(self).


   .. py:method:: __repr__()

      Return repr(self).


   .. py:method:: sort(field, reverse=False)

      Sort the filtered dataset. Operates in place; does not return anything.

      :param \* *field*: The key used for sorting.
      :type \* *field*: str
      :param \* *reverse*: Reverse normal sorting order.
      :type \* *reverse*: bool, optional


   .. py:method:: __len__()


   .. py:method:: __iter__()


   .. py:method:: keys()


   .. py:method:: items()


   .. py:method:: items()


   .. py:method:: __getitem__(key)


   .. py:method:: __contains__(key)



.. py:class:: Query(*filters)

   A container for a set of filters applied to a dataset.

   Filters are applied by calling the ``Query`` object, and passing the dataset to filter as the argument. Calling a ``Query`` with some data returns a ``Result`` object with the filtered dataset.

   :param \* *filters*: One or more ``Filter`` objects.
   :type \* *filters*: filters

   .. py:method:: add(filter_)

      Add another filter.

      :param \*filter_*: A Filter object.
      :type \*filter_*: ``Filter``


   .. py:method:: __call__(data)



.. py:class:: Filter(key, function, value)

   A filter on a dataset.

   The following functions are supported:

       * "<", "<=", "==", ">", ">=": Mathematical relations
       * "is", "not": Identity relations. Work on any Python object.
       * "in", "notin": List or string relations.
       * "iin", "iis", "inot": Case-insensitive string relations.
       * "len": Length relation.

   In addition, any function which defines a relationship between an input and an output can also be used.

   .. rubric:: Examples

   * All ``name`` values are *"foo"*: ``Filter("name", "is", "foo")``
   * All ``name`` values include the string *"foo"*: ``Filter("name", "has", "foo")``
   * Category (a list of categories and subcategories) includes *"foo"*: ``Filter("category", "has", "foo")``

   :param \* *key*: The field to filter on.
   :type \* *key*: str
   :param \* *function*: One of the pre-defined filters, or a callable object.
   :type \* *function*: str or object
   :param \* *value*: The value to test against.
   :type \* *value*: object

   :returns: A ``Result`` object which wraps a new data dictionary.

   .. py:method:: __call__(data)



.. py:function:: NF(value)

   Shortcut for a name filter


.. py:function:: PF(value)

   Shortcut for a reference product filter


