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
   bw2io.strategies.generic.link_iterable_by_fields
   bw2io.strategies.generic.link_technosphere_by_activity_hash
   bw2io.strategies.generic.normalize_units
   bw2io.strategies.generic.set_code_by_activity_hash
   bw2io.strategies.generic.split_exchanges
   bw2io.strategies.generic.tupleize_categories



.. py:function:: add_database_name(db, name)

   Adds a database name to each dataset in a list of datasets.

   :param db: The list of datasets to add the database name to.
   :type db: list[dict]
   :param name: The name of the database to be added to each dataset.
   :type name: str

   :returns: The updated list of datasets with the database name added to each dataset.
   :rtype: list[dict]

   .. rubric:: Examples

   >>> db = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
   >>> add_database_name(db, "X")
   [{'id': 1, 'name': 'A', 'database': 'X'}, {'id': 2, 'name': 'B', 'database': 'X'}]

   An empty list input returns an empty list.
   >>> add_database_name([], "Y")
   []


.. py:function:: assign_only_product_as_production(db)

   Assign only product as reference product.

   For each dataset in ``db``, this function checks if there is only one production exchange and no reference product already assigned.
   If this is the case, the reference product is set to the name of the production exchange, and the following fields are replaced if not already specified:

   * 'name' - name of reference product
   * 'unit' - unit of reference product
   * 'production amount' - amount of reference product

   :param db: An iterable of dictionaries containing the datasets to process.
   :type db: iterable

   :returns: An iterable of dictionaries containing the processed datasets.
   :rtype: iterable

   :raises AssertionError: If a production exchange does not have a `name` attribute.

   .. rubric:: Examples

   >>> data = [{'name': 'Input 1', 'exchanges': [{'type': 'production', 'name': 'Product 1', 'amount': 1}, {'type': 'technosphere', 'name': 'Input 2', 'amount': 2}]}, {'name': 'Input 2', 'exchanges': [{'type': 'production', 'name': 'Product 2', 'amount': 3}, {'type': 'technosphere', 'name': 'Input 3', 'amount': 4}]}]
   >>> processed_data = assign_only_product_as_production(data)
   >>> processed_data[0]['reference product']
   'Product 1'
   >>> processed_data[0]['name']
   'Input 1'
   >>> processed_data[1]['reference product']
   'Product 2'
   >>> processed_data[1]['unit']
   'Unknown'


.. py:function:: convert_activity_parameters_to_list(data)

   "
   Convert activity parameters from a dictionary to a list of dictionaries.

   :param data: The list of activities to convert parameters from.
   :type data: list[dict]

   :returns: The updated list of activities with parameters converted to a list of dictionaries.
   :rtype: list[dict]

   .. rubric:: Examples

   >>> data = [{"name": "A", "parameters": {"param1": 1, "param2": 2}}, {"name": "B", "parameters": {"param3": 3, "param4": 4}}]
   >>> convert_activity_parameters_to_list(data)
   [{'name': 'A', 'parameters': [{'name': 'param1', 1}, {'name': 'param2', 2}]}, {'name': 'B', 'parameters': [{'name': 'param3', 3}, {'name': 'param4', 4}]}]

   Activities without parameters remain unchanged.
   >>> data = [{"name": "C"}]
   >>> convert_activity_parameters_to_list(data)
   [{'name': 'C'}]


.. py:function:: convert_uncertainty_types_to_integers(db)

   Convert uncertainty types in a list of datasets to integers.

   :param db: The list of datasets containing uncertainty types to convert.
   :type db: list[dict]

   :returns: The updated list of datasets with uncertainty types converted to integers where possible.
   :rtype: list[dict]

   .. rubric:: Examples

   >>> db = [{"name": "A", "exchanges": [{"uncertainty type": "triangular"}]}, {"name": "B", "exchanges": [{"uncertainty type": "lognormal"}]}]
   >>> convert_uncertainty_types_to_integers(db)
   [{'name': 'A', 'exchanges': [{'uncertainty type': 'triangular'}]}, {'name': 'B', 'exchanges': [{'uncertainty type': 'lognormal'}]}]

   Float values are rounded down to integers.
   >>> db = [{"name": "C", "exchanges": [{"uncertainty type": "1"}, {"uncertainty type": "2.0"}]}]
   >>> convert_uncertainty_types_to_integers(db)
   [{'name': 'C', 'exchanges': [{'uncertainty type': 1}, {'uncertainty type': 2}]}]


.. py:function:: drop_falsey_uncertainty_fields_but_keep_zeros(db)

   Drop uncertainty fields that are falsey (e.g. '', None, False) but keep zero and NaN.

   Note that this function doesn't strip `False`, which behaves exactly like 0.

   :param db: The list of datasets to drop uncertainty fields from.
   :type db: list[dict]

   :returns: The updated list of datasets with falsey uncertainty fields dropped.
   :rtype: list[dict]

   .. rubric:: Examples

   >>> db = [{"name": "A", "exchanges": [{"amount": 1, "minimum": 0, "maximum": None, "shape": ""}]}]
   >>> drop_falsey_uncertainty_fields_but_keep_zeros(db)
   [{'name': 'A', 'exchanges': [{'amount': 1, 'minimum': 0}]}]

   Float values of NaN are kept in the dictionary.
   >>> db = [{"name": "B", "exchanges": [{"loc": 0.0, "scale": 0.5, "minimum": float('nan')},... {"loc": 0.0, "scale": 0.5}]}]
   >>> drop_falsey_uncertainty_fields_but_keep_zeros(db)
   [{'name': 'B', 'exchanges': [{'loc': 0.0, 'scale': 0.5, 'minimum': nan},{'loc': 0.0, 'scale': 0.5}]}]


.. py:function:: drop_unlinked(db)

   Remove all exchanges in a given database that don't have inputs.

   Exchanges that don't have any inputs are often referred to as "unlinked exchanges".
   These exchanges can be a sign of an incomplete or poorly structured database.

   :param db: The database to remove unlinked exchanges from.
   :type db: obj

   :returns: The modified database object with removed unlinked exchanges.
   :rtype: obj

   .. rubric:: Notes

   This is the nuclear option - use at your own risk! ⚠️

   .. rubric:: Examples

   >>> db = [
   ...    {"name": "Product A", "unit": "kg", "exchanges": [{"input": True, "amount": 1, "name": "Input 1", "unit": "kg"}]},
   ...    {"name": "Product B", "unit": "kg", "exchanges": [{"input": True, "amount": 1, "name": "Input 2", "unit": "kg"}, {"input": False, "amount": 0.5, "name": "Product A", "unit": "kg"}]},
   ...    {"name": "Product C", "unit": "kg", "exchanges": [{"input": False, "amount": 0.75, "name": "Product A", "unit": "kg"}]}
   ... ]
   >>> drop_unlinked(db)
   [
       {'name': 'Product A', 'unit': 'kg', 'exchanges': [{'input': True, 'amount': 1, 'name': 'Input 1', 'unit': 'kg'}]},
   ... {'name': 'Product B', 'unit': 'kg', 'exchanges': [{'input': True, 'amount': 1, 'name': 'Input 2', 'unit': 'kg'},
   ... {'input': False, 'amount': 0.5, 'name': 'Product A', 'unit': 'kg'}]},
   ... {'name': 'Product C', 'unit': 'kg', 'exchanges': []}
   ]


.. py:function:: format_nonunique_key_error(obj, fields, others)

       Generate a formatted error message for a dataset that can't be uniquely linked to the target database.

       Parameters
       ----------
       obj : dict
           The problematic dataset that can't be uniquely linked to the target database.
       fields : list
           The list of fields to include in the error message.
       others : list
           A list of other similar datasets.

       Returns
       -------
       str
           A formatted error message.

       See Also
       --------
       pprint.pformat : Format a Python object into a pretty-printed string.

       Notes
       -----
       This function is used to generate a formatted error message for a dataset that can't be uniquely linked to the target
       database. It takes the problematic dataset and a list of other similar datasets and returns an error message that
       includes the problematic dataset and a list of possible target datasets that may match the problematic dataset.

       Raises
       ------
       None

       Examples
       --------
       >>> obj = {'name': 'Electricity', 'location': 'CH'}
       >>> fields = ['name', 'location']
       >>> others = [{'name': 'Electricity', 'location': 'CH', 'filename': 'file1'},                {'name': 'Electricity', 'location': 'CH', 'filename': 'file2'}]
       >>> format_nonunique_key_error(obj, fields, others)
       "Object in source database can't be uniquely linked to target database.
   Problematic dataset is:
   {'name': 'Electricity', 'location': 'CH'}
   Possible targets include (at least one not shown):
   [{'name': 'Electricity', 'location': 'CH', 'filename': 'file1'}, {'name': 'Electricity', 'location': 'CH', 'filename': 'file2'}]"



.. py:function:: link_iterable_by_fields(unlinked, other=None, fields=None, kind=None, internal=False, relink=False)

   Link objects in ``unlinked`` to objects in ``other`` using fields ``fields``.

   :param unlinked: An iterable of dictionaries containing objects to be linked.
   :type unlinked: iterable
   :param other: An iterable of dictionaries containing objects to link to. If not specified, `other` is set to `unlinked`.
   :type other: iterable, optional
   :param fields: An iterable of strings indicating which fields should be used to match objects. If not specified, all fields will be used.
   :type fields: iterable, optional
   :param kind: If specified, limit the exchange to objects of the given kind. `kind` can be a string or an iterable of strings.
   :type kind: str or iterable, optional
   :param internal: If `True`, link objects in `unlinked` to other objects in `unlinked`. Each object must have the attributes `database` and `code`.
   :type internal: bool, optional
   :param relink: If `True`, link to objects that already have an `input`. Otherwise, skip objects that have already been linked.
   :type relink: bool, optional

   :returns: An iterable of dictionaries containing linked objects.
   :rtype: iterable

   :raises StrategyError: If not all datasets in the database to be linked have ``database`` or ``code`` attributes.
       If there are duplicate keys for the given fields.

   .. seealso::

      :obj:`activity_hash`
          Generate a unique hash key for a dataset.

      :obj:`format_nonunique_key_error`
          Generate an error message for datasets that can't be uniquely linked to the target database.

   .. rubric:: Notes

   This function takes two iterables of dictionaries: ``unlinked`` and ``other``, where each dictionary represents an object to be linked.
   The objects are linked by matching their fields ``fields``. The function returns an iterable of dictionaries containing linked objects.

   If the parameter ``kind`` is specified, only objects of the given kind are linked. If ``internal`` is True, objects in ``unlinked``
   are linked to other objects in ``unlinked``. If ``relink`` is True, objects that already have an input are linked again.

   If a link is not unique, a ``StrategyError`` is raised, which includes a formatted error message generated by the
   ``format_nonunique_key_error`` function.

   .. rubric:: Examples

   >>> data = [    ...     {"exchanges": [    ...         {"type": "A", "value": 1},    ...         {"type": "B", "value": 2}    ...     ]},
   ...     {"exchanges": [    ...         {"type": "C", "value": 3},    ...         {"type": "D", "value": 4}    ...     ]}
   ... ]
   >>> other = [    ...     {"database": "db1", "code": "A"},    ...     {"database": "db2", "code": "C"}    ... ]
   >>> linked = link_iterable_by_fields(data, other=other, fields=["code"])
   >>> linked[0]["exchanges"][0]["input"]
   ('db1', 'A')
   >>> linked[1]["exchanges"][0]["input"]
   ('db2', 'C')


.. py:function:: link_technosphere_by_activity_hash(db, external_db_name=None, fields=None)

   Link technosphere exchanges using the `activity_hash` function.
   If ``external_db_name`` is provided, link technosphere exchanges against an external database, otherwise link internally.

   :param db: The database to link exchanges in.
   :type db: obj
   :param external_db_name: The name of an external database to link against. Default is None.
   :type external_db_name: str, optional
   :param fields: The fields to use for linking exchanges. If None, all fields will be used.
   :type fields: list of str, optional

   :returns: **linked** -- A list of tuples representing the linked exchanges.
   :rtype: list of tuples

   :raises StrategyError: If the external database name provided is not found in the list of available databases.

   .. rubric:: Examples

   Link technosphere exchanges internally:

   >>> db = Database('example_db')
   >>> linked = link_technosphere_by_activity_hash(db)

   Link technosphere exchanges against an external database using specific fields:

   >>> linked = link_technosphere_by_activity_hash(db, external_db_name='other_db', fields=['name', 'unit'])


.. py:function:: normalize_units(db)

   Normalize units in datasets and their exchanges.

   :param db: The database that needs to be normalized.
   :type db: dict

   :returns: The normalized database.
   :rtype: dict

   .. rubric:: Examples

   Example 1: Normalize the units of a given database.

   >>> db = {'name': 'test_db', 'unit': 'kg'}
   >>> normalize_units(db)
   {'name': 'test_db', 'unit': 'kilogram'}

   Example 2: Normalize the units of a dataset and its exchanges.

   >>> db = {
   ...     'name': 'test_db',
   ...     'unit': 'kg',
   ...     'exchanges': [
   ...         {'name': 'input', 'unit': 't'},
   ...         {'name': 'output', 'unit': 'lb'},
   ...     ]
   ... }
   >>> normalize_units(db)
   {'name': 'test_db',
    'unit': 'kilogram',
    'exchanges': [
        {'name': 'input', 'unit': 'tonne'},
        {'name': 'output', 'unit': 'pound'}
    ]}


.. py:function:: set_code_by_activity_hash(db, overwrite=False)

   Set the dataset code for each dataset in the given database using `activity_hash`.

   :param db: The database to set the dataset codes in.
   :type db: obj
   :param overwrite: Whether to overwrite existing codes. Default is False.
   :type overwrite: bool, optional

   :returns: The modified database object with updated dataset codes.
   :rtype: obj

   .. rubric:: Notes

   The dataset code is a unique identifier for each dataset in the database. It is generated by hashing the dataset dictionary with `activity_hash`.

   .. rubric:: Examples

   >>> db = Database('example_db')
   >>> set_code_by_activity_hash(db)


.. py:function:: split_exchanges(data, filter_params, changed_attributes, allocation_factors=None)

   Split unlinked exchanges in ``data`` which satisfy ``filter_params`` into new exchanges with changed attributes.

   ``changed_attributes`` is a list of dictionaries with the attributes that should be changed.

   ``allocation_factors`` is an optional list of floats to allocate the original exchange amount to the respective copies defined in ``changed_attributes``. They don't have to sum to one. If ``allocation_factors`` are not defined, then exchanges are split equally.

   Resets uncertainty to ``UndefinedUncertainty`` (0).

   To use this function as a strategy, you will need to curry it first using ``functools.partial``.

   :param data: The list of activities to split exchanges in.
   :type data: list[dict]
   :param filter_params: A dictionary of filter parameters to apply to the exchanges that will be split.
   :type filter_params: dict
   :param changed_attributes: A list of dictionaries with the attributes that should be changed in the new exchanges.
   :type changed_attributes: list[dict]
   :param allocation_factors: An optional list of floats to allocate the original exchange amount to the respective copies defined in ``changed_attributes``, by default None. If ``allocation_factors`` are not defined, then exchanges are split equally.
   :type allocation_factors: Optional[List[float]], optional

   :returns: The updated list of activities with exchanges split.
   :rtype: list[dict]

   .. rubric:: Examples

   >>> data = [{"name": "A", "exchanges": [{"name": "foo", "location": "bar", "amount": 20}, {"name": "food", "location": "bar", "amount": 12}]}]
   >>> split_exchanges(data, {"name": "foo"}, [{"location": "A"}, {"location": "B", "cat": "dog"}])
   [{'name': 'A', 'exchanges': [{'name': 'food', 'location': 'bar', 'amount': 12}, {'name': 'foo', 'location': 'A', 'amount': 12.0, 'uncertainty_type': 0}, {'name': 'foo', 'location': 'B', 'amount': 8.0, 'uncertainty_type': 0, 'cat': 'dog'}]}]
   >>> data = [{"name": "B", "exchanges": [{"name": "bar", "location": "foo", "amount": 25}, {"name": "bard", "location": "foo", "amount": 13}]}]
   >>> split_exchanges(data, {"name": "bard", "location": "foo"}, [{"name": "new", "location": "bar"}], [0.3])
   [{'name': 'B', 'exchanges': [{'name': 'bar', 'location': 'foo', 'amount': 25}, {'name': 'new', 'location': 'bar', 'amount': 3.9000000000000004, 'uncertainty_type': 0}]}]


.. py:function:: tupleize_categories(db)

   Convert the "categories" fields in a given database and its exchanges to tuples.

   :param db: The database to convert categories in.
   :type db: obj

   :returns: The modified database object with converted category fields.
   :rtype: obj

   .. rubric:: Examples

   >>> from bw2data import Database
   >>> db = Database('example_db')
   >>> tupleize_categories(db)


