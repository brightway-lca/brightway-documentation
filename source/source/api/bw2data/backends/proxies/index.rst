:py:mod:`bw2data.backends.proxies`
==================================

.. py:module:: bw2data.backends.proxies


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.backends.proxies.Activity
   bw2data.backends.proxies.Exchange
   bw2data.backends.proxies.Exchanges




.. py:class:: Activity(document=None, **kwargs)

   Bases: :py:obj:`bw2data.proxies.ActivityProxyBase`

   .. autoapi-inheritance-diagram:: bw2data.backends.proxies.Activity
      :parts: 1
      :private-bases:

   A MutableMapping is a generic container for associating
   key/value pairs.

   This class provides concrete generic implementations of all
   methods except for __getitem__, __setitem__, __delitem__,
   __iter__, and __len__.

   Create an `Activity` proxy object.

   If this is a new activity, can pass `kwargs`.

   If the activity exists in the database, `document` should be an `ActivityDataset`.

   .. py:property:: id


   .. py:property:: key


   .. py:method:: _change_code(new_code)


   .. py:method:: _change_database(new_database)


   .. py:method:: biosphere()


   .. py:method:: consumers(kinds=('technosphere', 'generic consumption'))


   .. py:method:: copy(code=None, **kwargs)

      Copy the activity. Returns a new `Activity`.

      `code` is the new activity code; if not given, a UUID is used.

      `kwargs` are additional new fields and field values, e.g. name='foo'



   .. py:method:: delete()


   .. py:method:: edges()


   .. py:method:: exchanges()


   .. py:method:: new_edge(**kwargs)

      Create a new exchange linked to this activity


   .. py:method:: new_exchange(**kwargs)


   .. py:method:: producers()


   .. py:method:: production(include_substitution=False)


   .. py:method:: rp_exchange()

      Return an ``Exchange`` object corresponding to the reference production. Uses the following in order:

      * The ``production`` exchange, if only one is present
      * The ``production`` exchange with the same name as the activity ``reference product``.

      Raises ``ValueError`` if no suitable exchange is found.


   .. py:method:: save()


   .. py:method:: substitution()


   .. py:method:: technosphere(include_substitution=False)


   .. py:method:: upstream(kinds=('technosphere', 'generic consumption'))



.. py:class:: Exchange(document=None, **kwargs)

   Bases: :py:obj:`bw2data.proxies.ExchangeProxyBase`

   .. autoapi-inheritance-diagram:: bw2data.backends.proxies.Exchange
      :parts: 1
      :private-bases:

   A MutableMapping is a generic container for associating
   key/value pairs.

   This class provides concrete generic implementations of all
   methods except for __getitem__, __setitem__, __delitem__,
   __iter__, and __len__.

   Create an `Exchange` proxy object.

   If this is a new exchange, can pass `kwargs`.

   If the exchange exists in the database, `document` should be an `ExchangeDataset`.

   .. py:method:: delete()


   .. py:method:: save()



.. py:class:: Exchanges(key, kinds=None, reverse=False)

   Bases: :py:obj:`collections.abc.Iterable`

   .. autoapi-inheritance-diagram:: bw2data.backends.proxies.Exchanges
      :parts: 1
      :private-bases:

   Iterator for exchanges with some additional methods.

   This is not a generator; ``next()`` is not supported. Everything time you start to iterate over the object you get a new list starting from the beginning. However, to get a single item you can do ``next(iter(foo))``.

   Ordering is by database row id.

   Supports the following:

   .. code-block:: python

       exchanges = activity.exchanges()

       # Iterate
       for exc in exchanges:
           pass

       # Length
       len(exchanges)

       # Delete all
       exchanges.delete()


   .. py:method:: _get_queryset()


   .. py:method:: delete()


   .. py:method:: filter(expr)


   .. py:method:: to_dataframe(categorical: bool = True, formatters: Optional[List[Callable]] = None) -> pandas.DataFrame

      Return a pandas DataFrame with all node exchanges. Standard DataFrame columns are:

          target_id: int,
          target_database: str,
          target_code: str,
          target_name: Optional[str],
          target_reference_product: Optional[str],
          target_location: Optional[str],
          target_unit: Optional[str],
          target_type: Optional[str]
          source_id: int,
          source_database: str,
          source_code: str,
          source_name: Optional[str],
          source_product: Optional[str],  # Note different label
          source_location: Optional[str],
          source_unit: Optional[str],
          source_categories: Optional[str]  # Tuple concatenated with "::" as in `bw2io`
          edge_amount: float,
          edge_type: str,

      Target is the node consuming the edge, source is the node or flow being consumed. The terms target and source were chosen because they also work well for biosphere edges.

      Args:

      ``categorical`` will turn each string column in a `pandas Categorical Series <https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html>`__. This takes 1-2 extra seconds, but saves around 50% of the memory consumption.

      ``formatters`` is a list of callables that modify each row. These functions must take the following keyword arguments, and use the `Wurst internal data format <https://wurst.readthedocs.io/#internal-data-format>`__:

          * ``node``: The target node, as a dict
          * ``edge``: The edge, including attributes of the source node
          * ``row``: The current row dict being modified.

      The functions in ``formatters`` don't need to return anything, they modify ``row`` in place.

      Returns a pandas ``DataFrame``.




