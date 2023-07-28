:py:mod:`bw2data.backends.json.proxies`
=======================================

.. py:module:: bw2data.backends.json.proxies


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.backends.json.proxies.Activity




.. py:class:: Activity(key, data={})

   Bases: :py:obj:`bw2data.proxies.ActivityProxyBase`

   .. autoapi-inheritance-diagram:: bw2data.backends.json.proxies.Activity
      :parts: 1
      :private-bases:

   A MutableMapping is a generic container for associating
   key/value pairs.

   This class provides concrete generic implementations of all
   methods except for __getitem__, __setitem__, __delitem__,
   __iter__, and __len__.

   .. py:method:: biosphere(raw=False)


   .. py:method:: exchanges(raw=False)


   .. py:method:: save()


   .. py:method:: technosphere(raw=False)


   .. py:method:: upstream(*args, **kwargs)



