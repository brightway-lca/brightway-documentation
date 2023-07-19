:py:mod:`bw2data.proxies`
=========================

.. py:module:: bw2data.proxies


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.proxies.ActivityProxyBase
   bw2data.proxies.ExchangeProxyBase
   bw2data.proxies.ProxyBase




.. py:class:: ActivityProxyBase(data, *args, **kwargs)

   Bases: :py:obj:`ProxyBase`

   .. autoapi-inheritance-diagram:: bw2data.proxies.ActivityProxyBase
      :parts: 1
      :private-bases:

   A MutableMapping is a generic container for associating
   key/value pairs.

   This class provides concrete generic implementations of all
   methods except for __getitem__, __setitem__, __delitem__,
   __iter__, and __len__.

   .. py:property:: key


   .. py:method:: lca(method=None, amount=1.0)

      Shortcut to construct an LCA object for this activity.


   .. py:method:: valid(why=False)



.. py:class:: ExchangeProxyBase(data, *args, **kwargs)

   Bases: :py:obj:`ProxyBase`

   .. autoapi-inheritance-diagram:: bw2data.proxies.ExchangeProxyBase
      :parts: 1
      :private-bases:

   A MutableMapping is a generic container for associating
   key/value pairs.

   This class provides concrete generic implementations of all
   methods except for __getitem__, __setitem__, __delitem__,
   __iter__, and __len__.

   .. py:property:: amount


   .. py:property:: uncertainty

      Get uncertainty dictionary that can be used in uncertainty analysis.

   .. py:property:: uncertainty_type

      Get uncertainty type as a ``stats_arrays`` class.

   .. py:property:: unit

      Get exchange unit.

      Separate property because the unit is a property of the input, not the exchange itself.

   .. py:attribute:: input

      

   .. py:attribute:: output

      

   .. py:method:: _get_input()

      Get or set the exchange input.

      When getting, returns an `Activity` - this will raise an error if the linked activity doesn't yet exist.

      When setting, either an `Activity` or a tuple can be given. The linked activity does not have to exist yet.


   .. py:method:: _get_output()

      Get or set the exchange output.

      When getting, returns an `Activity` - this will raise an error if the linked activity doesn't yet exist.

      When setting, either an `Activity` or a tuple can be given. The linked activity does not have to exist yet.


   .. py:method:: _set_input(value)


   .. py:method:: _set_output(value)


   .. py:method:: lca(method=None, amount=None)

      Shortcut to construct an LCA object for this exchange **input**.

      Uses the exchange amount if no other amount is provided.


   .. py:method:: random_sample(n=100)

      Draw a random sample from this exchange.


   .. py:method:: valid(why=False)



.. py:class:: ProxyBase(data, *args, **kwargs)

   Bases: :py:obj:`collections.abc.MutableMapping`

   .. autoapi-inheritance-diagram:: bw2data.proxies.ProxyBase
      :parts: 1
      :private-bases:

   A MutableMapping is a generic container for associating
   key/value pairs.

   This class provides concrete generic implementations of all
   methods except for __getitem__, __setitem__, __delitem__,
   __iter__, and __len__.

   .. py:method:: as_dict()



