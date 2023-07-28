:py:mod:`bw2data.backends.iotable`
==================================

.. py:module:: bw2data.backends.iotable


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.backends.iotable.IOTableActivity
   bw2data.backends.iotable.IOTableExchanges
   bw2data.backends.iotable.ReadOnlyExchange




.. py:class:: IOTableActivity

   Bases: :py:obj:`bw2data.backends.proxies.Activity`

   .. autoapi-inheritance-diagram:: bw2data.backends.iotable.IOTableActivity
      :parts: 1
      :private-bases:

   .. py:method:: _get_db()


   .. py:method:: biosphere()


   .. py:method:: delete() -> None
      :abstractmethod:


   .. py:method:: exchanges()


   .. py:method:: production()


   .. py:method:: rp_exchange()


   .. py:method:: substitution()


   .. py:method:: technosphere() -> IOTableExchanges



.. py:class:: IOTableExchanges(datapackage: bw_processing.Datapackage, target: Optional[bw2data.backends.proxies.Activity] = None, biosphere: bool = True, technosphere: bool = True, production: bool = True)

   Bases: :py:obj:`collections.abc.Iterable`

   .. autoapi-inheritance-diagram:: bw2data.backends.iotable.IOTableExchanges
      :parts: 1
      :private-bases:

   
   Iterable of ``ReadOnlyExchange`` objects drawn from Datapackage arrays.

   In the *technosphere matrix*, all positive exchanges are considered *production*, and all negative exchanges are *technosphere*, i.e. consumption, and we use this convention to label the edges. However, to be consistent with SQLite database results, we don't flip signs in the returned dataframe.

   The order of returned edges are production, technosphere, biosphere.

   This function will draw from all resources with the correct matrix types (i.e. ``'biosphere_matrix'``, ``'technosphere_matrix'``). Normally each IO Table database is stored in only one datapackage, and each datapackage only has one such database.

   * ``datapackage``: The datapackage object.
   * ``target``: Limit exchanges to those with the column index ``target``. Target must be an instance of ``IOTableActivity``.
   * ``biosphere``, ``technosphere``, ``production``: Return these types of edges.


   .. py:attribute:: to_dataframe

      

   .. py:method:: _add_arrays_to_resources(resources, datapackage)


   .. py:method:: _group_and_filter_resources(datapackage)


   .. py:method:: _mask_resource_arrays(resource, mask)


   .. py:method:: _raw_biosphere_iterator()


   .. py:method:: _raw_technosphere_iterator(negative=True)


   .. py:method:: _reduce_arrays_to_selected_types(resources, technosphere, production, biosphere)



.. py:class:: ReadOnlyExchange(**kwargs)

   Bases: :py:obj:`collections.abc.Mapping`

   .. autoapi-inheritance-diagram:: bw2data.backends.iotable.ReadOnlyExchange
      :parts: 1
      :private-bases:

   Non-mutable dictionary which mimics ``bw2data.proxies.Exchange``, but is read-only and doesn't link to a SQLite database row.

   .. py:attribute:: as_dict

      

   .. py:attribute:: lca

      

   .. py:attribute:: unit

      

   .. py:method:: valid(dct: dict = None) -> None



