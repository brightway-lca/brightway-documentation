:py:mod:`bw2io.utils`
=====================

.. py:module:: bw2io.utils


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.utils.activity_hash
   bw2io.utils.es2_activity_hash
   bw2io.utils.load_json_data_file
   bw2io.utils.format_for_logging
   bw2io.utils.rescale_exchange
   bw2io.utils.standardize_method_to_len_3



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.utils.DEFAULT_FIELDS


.. py:data:: DEFAULT_FIELDS
   :annotation: = ['name', 'categories', 'unit', 'reference product', 'location']

   

.. py:function:: activity_hash(data, fields=None, case_insensitive=True)

   Hash an activity dataset.

   Used to import data formats like ecospold 1 (ecoinvent v1-2) and SimaPro, where no unique attributes for datasets are given. This is clearly an imperfect and brittle solution, but there is no other obvious approach at this time.

   The fields used can be optionally specified in ``fields``.

   No fields are required; an empty string is used if a field isn't present. All fields are cast to lower case.

   By default, uses the following, in order:
       * name
       * categories
       * unit
       * reference product
       * location

   :param \* *data*: The :ref:`activity dataset data <database-documents>`.
   :type \* *data*: dict
   :param \* *fields*: Optional list of fields to hash together. Default is ``('name', 'categories', 'unit', 'reference product', 'location')``.
   :type \* *fields*: list
   :param \* *case_insensitive*: Cast everything to lowercase before computing hash. Default is ``True``.
   :type \* *case_insensitive*: bool

   :returns: A MD5 hash string, hex-encoded.


.. py:function:: es2_activity_hash(activity, flow)

   Generate unique ID for ecoinvent3 dataset.

   Despite using a million UUIDs, there is actually no unique ID in an ecospold2 dataset. Datasets are uniquely identified by the combination of activity and flow UUIDs.


.. py:function:: load_json_data_file(filename)


.. py:function:: format_for_logging(obj)


.. py:function:: rescale_exchange(exc, factor)

   Rescale exchanges, including formulas and uncertainty values, by a constant factor.

   No generally recommended, but needed for use in unit conversions. Not well tested.



.. py:function:: standardize_method_to_len_3(name, padding='--', joiner=',')

   Standardize an LCIA method name to a length 3 tuple.

   ``name`` is the current name.
   ``padding`` is the string to use for missing fields.



