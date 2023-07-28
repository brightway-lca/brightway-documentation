:py:mod:`bw2data.backends.peewee.proxies`
=========================================

.. py:module:: bw2data.backends.peewee.proxies


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.backends.peewee.proxies.Activity
   bw2data.backends.peewee.proxies.Exchange
   bw2data.backends.peewee.proxies.Exchanges




.. py:class:: Activity(document=None, **kwargs)

   Bases: :py:obj:`bw2data.proxies.ActivityProxyBase`

   .. autoapi-inheritance-diagram:: bw2data.backends.peewee.proxies.Activity
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

   .. py:property:: key


   .. py:method:: _change_code(new_code)


   .. py:method:: _change_database(new_database)


   .. py:method:: biosphere()


   .. py:method:: copy(code=None, **kwargs)

      Copy the activity. Returns a new `Activity`.

      `code` is the new activity code; if not given, a UUID is used.

      `kwargs` are additional new fields and field values, e.g. name='foo'



   .. py:method:: delete()


   .. py:method:: exchanges()


   .. py:method:: new_exchange(**kwargs)

      Create a new exchange linked to this activity


   .. py:method:: production()


   .. py:method:: rp_exchange()

      Return an ``Exchange`` object corresponding to the reference production. Uses the following in order:

      * The ``production`` exchange, if only one is present
      * The ``production`` exchange with the same name as the activity ``reference product``.

      Raises ``ValueError`` if no suitable exchange is found.


   .. py:method:: save()


   .. py:method:: substitution()


   .. py:method:: technosphere(include_substitution=True)


   .. py:method:: upstream(kinds=('technosphere', ))



.. py:class:: Exchange(document=None, **kwargs)

   Bases: :py:obj:`bw2data.proxies.ExchangeProxyBase`

   .. autoapi-inheritance-diagram:: bw2data.backends.peewee.proxies.Exchange
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

   .. autoapi-inheritance-diagram:: bw2data.backends.peewee.proxies.Exchanges
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



