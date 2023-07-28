:py:mod:`bw2io.strategies.generic`
==================================

.. py:module:: bw2io.strategies.generic


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.generic.add_database_name
   bw2io.strategies.generic.assign_only_product_as_production
   bw2io.strategies.generic.convert_activity_parameters_to_list
   bw2io.strategies.generic.convert_uncertainty_types_to_integers
   bw2io.strategies.generic.drop_falsey_uncertainty_fields_but_keep_zeros
   bw2io.strategies.generic.drop_unlinked
   bw2io.strategies.generic.format_nonunique_key_error
   bw2io.strategies.generic.link_technosphere_by_activity_hash
   bw2io.strategies.generic.normalize_units
   bw2io.strategies.generic.set_code_by_activity_hash
   bw2io.strategies.generic.split_exchanges
   bw2io.strategies.generic.tupleize_categories



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.generic.link_iterable_by_fields


.. py:function:: add_database_name(db, name)

   Add database name to datasets


.. py:function:: assign_only_product_as_production(db)

   Assign only product as reference product.

   Skips datasets that already have a reference product or no production exchanges. Production exchanges must have a ``name`` and an amount.

   Will replace the following activity fields, if not already specified:

   * 'name' - name of reference product
   * 'unit' - unit of reference product
   * 'production amount' - amount of reference product



.. py:function:: convert_activity_parameters_to_list(data)

   Convert activity parameters from dictionary to list of dictionaries


.. py:function:: convert_uncertainty_types_to_integers(db)

   Generic number conversion function convert to floats. Return to integers.


.. py:function:: drop_falsey_uncertainty_fields_but_keep_zeros(db)

   Drop fields like '' but keep zero and NaN.

   Note that this doesn't strip `False`, which behaves *exactly* like 0.



.. py:function:: drop_unlinked(db)

   This is the nuclear option - use at your own risk!


.. py:function:: format_nonunique_key_error(obj, fields, others)


.. py:function:: link_technosphere_by_activity_hash(db, external_db_name=None, fields=None)

   Link technosphere exchanges using ``activity_hash`` function.

   If ``external_db_name``, link against a different database; otherwise link internally.

   If ``fields``, link using only certain fields.


.. py:function:: normalize_units(db)

   Normalize units in datasets and their exchanges


.. py:function:: set_code_by_activity_hash(db, overwrite=False)

   Use ``activity_hash`` to set dataset code.

   By default, won't overwrite existing codes, but will if ``overwrite`` is ``True``.


.. py:function:: split_exchanges(data, filter_params, changed_attributes, allocation_factors=None)

   Split unlinked exchanges in ``data`` which satisfy ``filter_params`` into new exchanges with changed attributes.

   ``changed_attributes`` is a list of dictionaries with the attributes that should be changed.

   ``allocation_factors`` is an optional list of floats to allocate the original exchange amount to the respective copies defined in ``changed_attributes``. They don't have to sum to one. If ``allocation_factors`` are not defined, then exchanges are split equally.

   Resets uncertainty to ``UndefinedUncertainty`` (0).

   To use this function as a strategy, you will need to curry it first using ``functools.partial``.

   Example usage::

       split_exchanges(
           [
               {'exchanges': [{
                   'name': 'foo',
                   'location': 'bar',
                   'amount': 20
               }, {
                   'name': 'food',
                   'location': 'bar',
                   'amount': 12
               }]}
           ],
           {'name': 'foo'},
           [{'location': 'A'}, {'location': 'B', 'cat': 'dog'}
       ]
       >>> [
           {'exchanges': [{
               'name': 'food',
               'location': 'bar',
               'amount': 12
           }, {
               'name': 'foo',
               'location': 'A',
               'amount': 12.,
               'uncertainty_type': 0
           }, {
               'name': 'foo',
               'location': 'B',
               'amount': 8.,
               'uncertainty_type': 0,
               'cat': 'dog',
           }]}
       ]



.. py:function:: tupleize_categories(db)


.. py:data:: link_iterable_by_fields

   

