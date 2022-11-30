:py:mod:`bw2data.backends.iotable`
==================================

.. py:module:: bw2data.backends.iotable


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.backends.iotable.ReadOnlyExchange
   bw2data.backends.iotable.IOTableExchanges
   bw2data.backends.iotable.IOTableActivity




.. py:class:: ReadOnlyExchange(**kwargs)

   Bases: :py:obj:`collections.abc.Mapping`

   Non-mutable dictionary which mimics ``bw2data.proxies.Exchange``, but is read-only and doesn't link to a SQLite database row.

   .. py:attribute:: __contains__
      

      

   .. py:attribute:: __iter__
      

      

   .. py:attribute:: __len__
      

      

   .. py:attribute:: __getitem__
      

      

   .. py:attribute:: __eq__
      

      

   .. py:attribute:: __hash__
      

      

   .. py:attribute:: unit
      

      

   .. py:attribute:: lca
      

      

   .. py:attribute:: as_dict
      

      

   .. py:method:: __lt__(other)

      Return self<value.


   .. py:method:: __str__()

      Return str(self).


   .. py:method:: valid(dct: dict = None) -> None



.. py:class:: IOTableExchanges(datapackage: bw_processing.Datapackage, target: Optional[bw2data.backends.proxies.Activity] = None, biosphere: bool = True, technosphere: bool = True, production: bool = True)

   Bases: :py:obj:`collections.abc.Iterable`

   .. py:attribute:: to_dataframe
      

      

   .. py:method:: _group_and_filter_resources(datapackage)


   .. py:method:: _add_arrays_to_resources(resources, datapackage)


   .. py:method:: _reduce_arrays_to_selected_types(resources, technosphere, production, biosphere)


   .. py:method:: _mask_resource_arrays(resource, mask)


   .. py:method:: __iter__()


   .. py:method:: _raw_technosphere_iterator(negative=True)


   .. py:method:: _raw_biosphere_iterator()


   .. py:method:: __next__()
      :abstractmethod:


   .. py:method:: __len__()



.. py:class:: IOTableActivity

   Bases: :py:obj:`bw2data.backends.proxies.Activity`

   .. py:method:: delete() -> None
      :abstractmethod:


   .. py:method:: rp_exchange()


   .. py:method:: _get_db()


   .. py:method:: technosphere() -> IOTableExchanges


   .. py:method:: biosphere()


   .. py:method:: production()


   .. py:method:: exchanges()


   .. py:method:: substitution()



