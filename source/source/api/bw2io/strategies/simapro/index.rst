:py:mod:`bw2io.strategies.simapro`
==================================

.. py:module:: bw2io.strategies.simapro


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.simapro.change_electricity_unit_mj_to_kwh
   bw2io.strategies.simapro.fix_iff_formula
   bw2io.strategies.simapro.fix_localized_water_flows
   bw2io.strategies.simapro.fix_zero_allocation_products
   bw2io.strategies.simapro.flip_sign_on_waste
   bw2io.strategies.simapro.link_technosphere_based_on_name_unit_location
   bw2io.strategies.simapro.normalize_simapro_biosphere_categories
   bw2io.strategies.simapro.normalize_simapro_biosphere_names
   bw2io.strategies.simapro.normalize_simapro_formulae
   bw2io.strategies.simapro.set_lognormal_loc_value_uncertainty_safe
   bw2io.strategies.simapro.sp_allocate_products
   bw2io.strategies.simapro.split_simapro_name_geo



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.strategies.simapro.detoxify_pattern
   bw2io.strategies.simapro.detoxify_re
   bw2io.strategies.simapro.iff_exp


.. py:function:: change_electricity_unit_mj_to_kwh(db)

   Change datasets with the string "electricity" in their name from units of MJ to kilowatt hour.

   Iterates through a given database (list of datasets) and modifies the unit of exchanges
   containing the string "electricity" or "market for electricity" in their name from "megajoule" (MJ) to
   "kilowatt hour" (kWh). It also rescales the exchange accordingly.

   :param db: A list of datasets containing exchanges with the unit "megajoule" (MJ).
   :type db: list

   :returns: A modified list of datasets with exchanges containing the string "electricity" or
             "market for electricity" in their name updated to have the unit "kilowatt hour" (kWh).
   :rtype: list

   .. rubric:: Examples

   >>> db = [
           {
               "exchanges": [
                   {"name": "Electricity", "unit": "megajoule", "amount": 3.6}
               ]
           }
       ]
   >>> change_electricity_unit_mj_to_kwh(db)
   [{'exchanges': [{'name': 'Electricity', 'unit': 'kilowatt hour', 'amount': 1.0}]}]


.. py:function:: fix_iff_formula(string)

   Replace SimaPro 'iff' formula with a Python equivalent 'if-else' expression.

   Processes a given string containing SimaPro 'iff' formulae and
   replaces them with Python equivalent 'if-else' expressions. The conversion
   is done using regular expressions.

   :param string: A string containing SimaPro 'iff' formulae.
   :type string: str

   :returns: **string** -- A string with SimaPro 'iff' formulae replaced by Python 'if-else' expressions.
   :rtype: str

   .. rubric:: Examples

   >>> string = "iff(A > 0, A, 0)"
   >>> fix_iff_formula(string)
   "((A) if (A > 0) else (0))"


.. py:function:: fix_localized_water_flows(db)

   Change water flows with location information to generic water flows.

   Biosphere flows cannot have locations; locations are defined by the activity dataset.
   Iterates through a given database (list of datasets) and modifies the name of
   exchanges containing water flows with location information by removing the location details.

   :param db: A list of datasets containing exchanges with water flows including location information.
   :type db: list

   :returns: A modified list of datasets with exchanges containing water flows updated to have generic names,
             without location information.
   :rtype: list

   .. rubric:: Examples

   >>> db = [
           {
               "exchanges": [
                   {"name": "Water, river, BR", "type": "biosphere"}
               ]
           }
       ]
   >>> fix_localized_water_flows(db)
   [{'exchanges': [{'name': 'Water, river', 'type': 'biosphere', 'simapro location': 'BR'}]}]


.. py:function:: fix_zero_allocation_products(db)

   Fix datasets with a single production exchange and zero allocation factors.

   For datasets with a single production exchange and zero allocation factors,
   sets the production amount to one and removes all inputs. This prevents the creation of a singular technosphere matrix.

   :param db: A list of dictionaries representing datasets with production exchanges.
   :type db: list

   :returns: **db** -- A list of dictionaries representing modified datasets with fixed zero allocation factors.
   :rtype: list

   .. rubric:: Examples

   >>> db = [
   ...     {
   ...         "name": "Dataset 1",
   ...         "exchanges": [
   ...             {"type": "production", "name": "Product A", "unit": "kg", "amount": 0},
   ...             {"type": "input", "name": "Resource 1", "unit": "kg", "amount": 5},
   ...         ],
   ...     }
   ... ]
   >>> fix_zero_allocation_products(db)
   [
       {
           "name": "Dataset 1",
           "exchanges": [
               {"type": "production", "name": "Product A", "unit": "kg", "amount": 1, "uncertainty type": 0},
           ],
       },
   ]


.. py:function:: flip_sign_on_waste(db, other)

   Flip the sign on waste exchanges in the imported database based on the waste convention.

   Adjusts the sign of waste exchanges in the imported database
   to match the waste exchange convention in SimaPro.

   :param db: A list of datasets containing waste exchanges to be adjusted.
   :type db: list
   :param other: The name of the external database (e.g., ecoinvent) that is linked to
                 the imported database.
   :type other: str

   :returns: A modified list of datasets with the sign of waste exchanges updated.
   :rtype: list

   .. rubric:: Notes

   This strategy needs to be run *after* matching with ecoinvent.
   The strategy should be run as follows:
   sp_imported.apply_strategy(functools.partial(flip_sign_on_waste, other="name_of_other"))

   .. rubric:: Examples

   >>> db = [
           {
               "exchanges": [
                   {
                       "amount": -10,
                       "input": ("key",),
                       "uncertainty type": 0,
                       "loc": -10
                   }
               ]
           }
       ]
   >>> other_db_name = "name_of_other"
   >>> flip_sign_on_waste(db, other_db_name)
   [{'exchanges': [{'amount': 10, 'input': ('key',), 'uncertainty type': 0, 'loc': 10}]}]


.. py:function:: link_technosphere_based_on_name_unit_location(db, external_db_name=None)

   Link technosphere exchanges based on name, unit, and location.

   Links technosphere exchanges internally or against an external database
   based on their name, unit, and location. It doesn't use categories because categories
   cannot be reliably extracted from SimaPro exports.

   :param db: A list of dictionaries representing datasets with technosphere exchanges.
   :type db: list
   :param external_db_name: The name of the external database to link against, by default None.
                            If None, link technosphere exchanges internally within the given database.
   :type external_db_name: str, optional

   :returns: **db** -- A list of dictionaries representing modified datasets with linked technosphere exchanges.
   :rtype: list

   .. rubric:: Examples

   >>> db = [
   ...     {
   ...         "name": "Dataset 1",
   ...         "exchanges": [
   ...             {"type": "technosphere", "name": "Product A", "unit": "kg", "location": "GLO"},
   ...         ],
   ...     }
   ... ]
   >>> link_technosphere_based_on_name_unit_location(db)
   [
       {
           "name": "Dataset 1",
           "exchanges": [
               {"type": "technosphere", "name": "Product A", "unit": "kg", "location": "GLO"},
           ],
       },
   ]


.. py:function:: normalize_simapro_biosphere_categories(db)

   Normalize biosphere categories in a dataset to the ecoinvent standard.

   Processes datasets and their exchanges by normalizing biosphere
   categories and subcategories to match the ecoinvent standard. It uses predefined
   mappings for SimaPro and ecoinvent categories.

   :param db: A list of dictionaries representing datasets with biosphere exchanges.
   :type db: list

   :returns: **db** -- A list of dictionaries representing modified datasets with normalized biosphere categories.
   :rtype: list

   .. rubric:: Examples

   >>> db = [
   ...     {
   ...         "exchanges": [
   ...             {
   ...                 "type": "biosphere",
   ...                 "categories": ["emission", "air"],
   ...             },
   ...         ],
   ...     }
   ... ]
   >>> normalize_simapro_biosphere_categories(db)
   [
       {
           "exchanges": [
               {
                   "type": "biosphere",
                   "categories": ("Emissions", "Air"),
               },
           ],
       },
   ]


.. py:function:: normalize_simapro_biosphere_names(db)

   Normalize biosphere flow names in a dataset to the ecoinvent standard.

   Processes datasets and their exchanges by normalizing biosphere
   flow names to match the ecoinvent standard. It uses a predefined mapping for
   SimaPro and ecoinvent flow names.

   :param db: A list of dictionaries representing datasets with biosphere exchanges.
   :type db: list

   :returns: **db** -- A list of dictionaries representing modified datasets with normalized biosphere flow names.
   :rtype: list

   .. rubric:: Examples

   >>> db = [
   ...     {
   ...         "exchanges": [
   ...             {
   ...                 "type": "biosphere",
   ...                 "categories": ["Emissions", "Air"],
   ...                 "name": "Example emission",
   ...             },
   ...         ],
   ...     }
   ... ]
   >>> normalize_simapro_biosphere_names(db)
   [
       {
           "exchanges": [
               {
                   "type": "biosphere",
                   "categories": ["Emissions", "Air"],
                   "name": "Normalized emission",
               },
           ],
       },
   ]


.. py:function:: normalize_simapro_formulae(formula, settings)

   Convert SimaPro formulae to Python expressions.

   Processes a given formula string containing SimaPro formulae
   and converts them to Python expressions. The conversion is done using
   string manipulation and by calling the `fix_iff_formula` function.

   :param formula: A string containing SimaPro formulae.
   :type formula: str
   :param settings: A dictionary containing settings that affect the formula conversion,
                    e.g., decimal separator.
   :type settings: dict

   :returns: A string with SimaPro formulae replaced by equivalent Python expressions.
   :rtype: str

   .. rubric:: Examples

   >>> formula = "A^2"
   >>> settings = {"Decimal separator": ","}
   >>> normalize_simapro_formulae(formula, settings)
   "A**2"


.. py:function:: set_lognormal_loc_value_uncertainty_safe(db)

   Ensure the 'loc' value is correct for lognormal uncertainty distributions in the given database.

   Iterates through a given database (list of datasets) and updates the 'loc' value
   of exchanges with lognormal uncertainty distributions, setting it to the natural logarithm of
   the absolute value of the exchange amount.

   :param db: A list of datasets containing exchanges with lognormal uncertainty distributions.
   :type db: list

   :returns: A modified list of datasets with the 'loc' value updated for exchanges with lognormal
             uncertainty distributions.
   :rtype: list

   .. rubric:: Examples

   >>> db = [
           {
               "exchanges": [
                   {
                       "amount": 10,
                       "uncertainty type": LognormalUncertainty.id,
                       "loc": 0
                   }
               ]
           }
       ]
   >>> set_lognormal_loc_value_uncertainty_safe(db)
   [{'exchanges': [{'amount': 10, 'uncertainty type': 2, 'loc': 2.302585092994046}]}]


.. py:function:: sp_allocate_products(db)

   Allocate products in a SimaPro dataset by creating a separate dataset for each product.

   For raw SimaPro datasets, creates a separate dataset for each product,
   taking into account the allocation factor if provided. Also handles
   waste treatment datasets with a single product.

   :param db: A list of dictionaries representing raw SimaPro datasets.
   :type db: list

   :returns: **new_db** -- A list of dictionaries representing the allocated datasets with separate
             entries for each product.
   :rtype: list

   .. rubric:: Examples

   >>> db = [
   ...     {
   ...         "name": "Dataset 1",
   ...         "exchanges": [
   ...             {"type": "production", "name": "Product A", "unit": "kg", "amount": 10, "allocation": 80},
   ...             {"type": "production", "name": "Product B", "unit": "kg", "amount": 20, "allocation": 20},
   ...         ],
   ...     }
   ... ]
   >>> sp_allocate_products(db)
   [
       {
           "name": "Product A",
           "reference product": "Product A",
           "unit": "kg",
           "production amount": 10,
           "exchanges": [
               {"type": "production", "name": "Product A", "unit": "kg", "amount": 10, "allocation": 80},
               {"type": "production", "name": "Product B", "unit": "kg", "amount": 5, "allocation": 20},
           ],
       },
       {
           "name": "Product B",
           "reference product": "Product B",
           "unit": "kg",
           "production amount": 5,
           "exchanges": [
               {"type": "production", "name": "Product A", "unit": "kg", "amount": 2.5, "allocation": 80},
               {"type": "production", "name": "Product B", "unit": "kg", "amount": 5, "allocation": 20},
           ],
       },
   ]


.. py:function:: split_simapro_name_geo(db)

   Split a name like 'foo/CH U' into name and geo components in a dataset.

   Processes datasets and their exchanges by splitting their names
   into name and geo components (e.g., 'foo/CH U' into 'foo' and 'CH U'). The original
   name is stored in a new field called 'simapro name'.

   :param db: A list of dictionaries representing datasets with names to be split.
   :type db: list

   :returns: **db** -- A list of dictionaries representing modified datasets with split names and geo components.
   :rtype: list

   .. rubric:: Examples

   >>> db = [
   ...     {
   ...         "name": "foo/CH U",
   ...         "exchanges": [
   ...             {"name": "bar/US U", "type": "technosphere"},
   ...         ],
   ...     }
   ... ]
   >>> split_simapro_name_geo(db)
   [
       {
           "name": "foo",
           "simapro name": "foo/CH U",
           "location": "CH U",
           "exchanges": [
               {"name": "bar", "simapro name": "bar/US U", "location": "US U", "type": "technosphere"},
           ],
       },
   ]


.. py:data:: detoxify_pattern
   :value: '^(?P<name>.+?)/(?P<geo>[A-Za-z]{2,10})(/I)? [SU]$'

   

.. py:data:: detoxify_re

   

.. py:data:: iff_exp

   

