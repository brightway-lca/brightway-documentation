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
   bw2io.utils.format_for_logging
   bw2io.utils.load_json_data_file
   bw2io.utils.rescale_exchange
   bw2io.utils.standardize_method_to_len_3



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.utils.DEFAULT_FIELDS


.. py:function:: activity_hash(data, fields=None, case_insensitive=True)

   Hash an activity dataset.

   Used to import data formats like ecospold 1 (ecoinvent v1-2) and SimaPro, where no unique attributes for datasets are given.

   This is clearly an imperfect and brittle solution, but there is no other obvious approach at this time.

   By default, uses the following, in order:
   * name
   * categories
   * unit
   * reference product
   * location

   :param data: The :ref:`activity dataset data <database-documents>`.
   :type data: dict

   fields : list, optional
       Optional list of fields to hash together. Default is ``('name', 'categories', 'unit', 'reference product', 'location')``.

       An empty string is used if a field isn't present. All fields are cast to lower case.


   case_insensitive : bool, optional
       Cast everything to lowercase before computing hash. Default is ``True``.

   :returns: A MD5 hash string, hex-encoded.
   :rtype: str


.. py:function:: es2_activity_hash(activity, flow)

   Generate unique ID for ecoinvent3 dataset.

   Despite using a million UUIDs, there is actually no unique ID in an ecospold2 dataset.

   Datasets are uniquely identified by the combination of activity and flow UUIDs.

   :param activity: The activity UUID.
   :type activity: str
   :param flow: The flow UUID.
   :type flow: str

   :returns: The unique ID.
   :rtype: str


.. py:function:: format_for_logging(obj)


.. py:function:: load_json_data_file(filename)


.. py:function:: rescale_exchange(exc, factor)

   Rescale exchanges, including formulas and uncertainty values, by a constant factor.

   :param exc: The exchange to rescale.
   :type exc: dict
   :param factor: The factor to rescale by.
   :type factor: float

   :returns: The rescaled exchange.
   :rtype: dict

   :raises AssertionError: If factor is not a number.
   :raises AssertionError: If factor is not greater than 0.
   :raises AssertionError: If uncertainty type is not in {UndefinedUncertainty.id, NoUncertainty.id, NormalUncertainty.id}.

   .. warning:: No generally recommended, but needed for use in unit conversions. Not well tested.


.. py:function:: standardize_method_to_len_3(name, padding='--', joiner=',')

   Standardize an LCIA method name to a length 3 tuple.

   :param name: The current name.
   :type name: tuple
   :param padding: The string to use for missing fields. The default is "--".
   :type padding: str, optional
   :param joiner: The string to use to join the fields. The default is ",".
   :type joiner: str, optional

   :returns: The standardized name.
   :rtype: tuple


.. py:data:: DEFAULT_FIELDS
   :value: ('name', 'categories', 'unit', 'reference product', 'location')

   

