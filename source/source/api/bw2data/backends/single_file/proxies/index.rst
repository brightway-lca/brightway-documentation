:py:mod:`bw2data.backends.single_file.proxies`
==============================================

.. py:module:: bw2data.backends.single_file.proxies


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.backends.single_file.proxies.Activity
   bw2data.backends.single_file.proxies.Exchange




.. py:class:: Activity(key, data={})

   Bases: :py:obj:`bw2data.proxies.ActivityProxyBase`

   .. autoapi-inheritance-diagram:: bw2data.backends.single_file.proxies.Activity
      :parts: 1
      :private-bases:

   A MutableMapping is a generic container for associating
   key/value pairs.

   This class provides concrete generic implementations of all
   methods except for __getitem__, __setitem__, __delitem__,
   __iter__, and __len__.

   .. py:method:: biosphere()


   .. py:method:: exchanges()


   .. py:method:: save()


   .. py:method:: technosphere()


   .. py:method:: upstream(*args, **kwargs)



.. py:class:: Exchange(data, *args, **kwargs)

   Bases: :py:obj:`bw2data.proxies.ExchangeProxyBase`

   .. autoapi-inheritance-diagram:: bw2data.backends.single_file.proxies.Exchange
      :parts: 1
      :private-bases:

   Simple proxy for an exchange between activity datasets. Makes manipulation and use in command line more convenient.

   .. warning:: This proxy is read only! To save changes to a dataset, you will need to work with the raw database data.

   Usually these proxies are created by the :ref:`activity`, but you can instantiate one with the dictionary of exchange data and an Activity proxy of the consuming activity:

   .. code-block:: python

       exchange = Exchange({"my exchange data": "goes here"})

   Properties:

   * ``input``: Returns :ref:`activity`
   * ``output``: Returns :ref:`activity`
   * ``amount``
   * ``uncertainty``: Returns dictionary of uncertainty data
   * ``uncertainty_type``: Returns ``stats_arrays`` uncertainty type
   * ``unit``



   .. py:method:: save()



