:py:mod:`bw2data.proxies`
=========================

.. py:module:: bw2data.proxies


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.proxies.ProxyBase
   bw2data.proxies.ActivityProxyBase
   bw2data.proxies.ExchangeProxyBase




.. py:class:: ProxyBase(data, *args, **kwargs)

   Bases: :py:obj:`collections.abc.MutableMapping`

   A MutableMapping is a generic container for associating
   key/value pairs.

   This class provides concrete generic implementations of all
   methods except for __getitem__, __setitem__, __delitem__,
   __iter__, and __len__.

   .. py:attribute:: __repr__
      

      

   .. py:method:: as_dict()


   .. py:method:: __str__()

      Return str(self).


   .. py:method:: __contains__(key)


   .. py:method:: __iter__()


   .. py:method:: __len__()


   .. py:method:: __getitem__(key)


   .. py:method:: __setitem__(key, value)


   .. py:method:: __delitem__(key)


   .. py:method:: __eq__(other)

      Return self==value.


   .. py:method:: __hash__()

      Return hash(self).



.. py:class:: ActivityProxyBase(data, *args, **kwargs)

   Bases: :py:obj:`ProxyBase`

   A MutableMapping is a generic container for associating
   key/value pairs.

   This class provides concrete generic implementations of all
   methods except for __getitem__, __setitem__, __delitem__,
   __iter__, and __len__.

   .. py:property:: key


   .. py:method:: __str__()

      Return str(self).


   .. py:method:: __eq__(other)

      Return self==value.


   .. py:method:: __lt__(other)

      Return self<value.


   .. py:method:: __hash__()

      Return hash(self).


   .. py:method:: __getitem__(key)


   .. py:method:: __delitem__(key)


   .. py:method:: valid(why=False)


   .. py:method:: lca(method=None, amount=1.0)

      Shortcut to construct an LCA object for this activity.



.. py:class:: ExchangeProxyBase(data, *args, **kwargs)

   Bases: :py:obj:`ProxyBase`

   A MutableMapping is a generic container for associating
   key/value pairs.

   This class provides concrete generic implementations of all
   methods except for __getitem__, __setitem__, __delitem__,
   __iter__, and __len__.

   .. py:property:: unit

      Get exchange unit.

      Separate property because the unit is a property of the input, not the exchange itself.

   .. py:property:: amount


   .. py:property:: uncertainty

      Get uncertainty dictionary that can be used in uncertainty analysis.

   .. py:property:: uncertainty_type

      Get uncertainty type as a ``stats_arrays`` class.

   .. py:attribute:: input
      

      

   .. py:attribute:: output
      

      

   .. py:method:: __str__()

      Return str(self).


   .. py:method:: __lt__(other)

      Return self<value.


   .. py:method:: __eq__(other)

      Return self==value.


   .. py:method:: __hash__()

      Return hash(self).


   .. py:method:: _get_input()

      Get or set the exchange input.

      When getting, returns an `Activity` - this will raise an error if the linked activity doesn't yet exist.

      When setting, either an `Activity` or a tuple can be given. The linked activity does not have to exist yet.


   .. py:method:: _set_input(value)


   .. py:method:: _get_output()

      Get or set the exchange output.

      When getting, returns an `Activity` - this will raise an error if the linked activity doesn't yet exist.

      When setting, either an `Activity` or a tuple can be given. The linked activity does not have to exist yet.


   .. py:method:: _set_output(value)


   .. py:method:: __setitem__(key, value)


   .. py:method:: valid(why=False)


   .. py:method:: random_sample(n=100)

      Draw a random sample from this exchange.


   .. py:method:: lca(method=None, amount=None)

      Shortcut to construct an LCA object for this exchange **input**.

      Uses the exchange amount if no other amount is provided.



