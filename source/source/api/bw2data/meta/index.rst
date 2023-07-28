:py:mod:`bw2data.meta`
======================

.. py:module:: bw2data.meta


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.meta.CalculationSetups
   bw2data.meta.Databases
   bw2data.meta.DynamicCalculationSetups
   bw2data.meta.GeoMapping
   bw2data.meta.Methods
   bw2data.meta.NormalizationMeta
   bw2data.meta.Preferences
   bw2data.meta.WeightingMeta




Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2data.meta.calculation_setups
   bw2data.meta.dynamic_calculation_setups
   bw2data.meta.geomapping
   bw2data.meta.methods
   bw2data.meta.normalizations
   bw2data.meta.preferences
   bw2data.meta.weightings


.. py:class:: CalculationSetups(dirpath=None)

   Bases: :py:obj:`bw2data.serialization.PickledDict`

   .. autoapi-inheritance-diagram:: bw2data.meta.CalculationSetups
      :parts: 1
      :private-bases:

   A dictionary for calculation setups.

   Keys:
   * `inv`: List of functional units, e.g. ``[{(key): amount}, {(key): amount}]``
   * `ia`: List of LCIA methods, e.g. ``[(method), (method)]``.


   .. py:attribute:: filename
      :value: 'setups.pickle'

      


.. py:class:: Databases(dirpath=None)

   Bases: :py:obj:`bw2data.serialization.SerializedDict`

   .. autoapi-inheritance-diagram:: bw2data.meta.Databases
      :parts: 1
      :private-bases:

   A dictionary for database metadata. This class includes methods to manage database versions. File data is saved in ``databases.json``.

   .. py:attribute:: filename
      :value: 'databases.json'

      

   .. py:method:: clean()


   .. py:method:: increment_version(database, number=None)

      Increment the ``database`` version. Returns the new version.


   .. py:method:: set_dirty(database)


   .. py:method:: set_modified(database)


   .. py:method:: version(database)

      Return the ``database`` version



.. py:class:: DynamicCalculationSetups(dirpath=None)

   Bases: :py:obj:`bw2data.serialization.PickledDict`

   .. autoapi-inheritance-diagram:: bw2data.meta.DynamicCalculationSetups
      :parts: 1
      :private-bases:

   A dictionary for Dynamic calculation setups.

   Keys:
   * `inv`: List of functional units, e.g. ``[{(key): amount}, {(key): amount}]``
   * `ia`: Dictionary of orst case LCIA method and the relative dynamic LCIA method, e.g. `` [{dLCIA_method_1_worstcase:dLCIA_method_1 , dLCIA_method_2_worstcase:dLCIA_method_2}]``.


   .. py:attribute:: filename
      :value: 'dynamicsetups.pickle'

      


.. py:class:: GeoMapping(*args, **kwargs)

   Bases: :py:obj:`bw2data.serialization.PickledDict`

   .. autoapi-inheritance-diagram:: bw2data.meta.GeoMapping
      :parts: 1
      :private-bases:

   A dictionary that maps location codes to integers. Needed because parameter arrays have integer ``geo`` fields.

   File data is stored in ``geomapping.pickle``.

   This dictionary does not support setting items directly; instead, use the ``add`` method to add multiple keys.

   .. py:attribute:: filename
      :value: 'geomapping.pickle'

      

   .. py:method:: add(keys)

      Add a set of keys. These keys can already be in the mapping; only new keys will be added.

      :param \* *keys*: The keys to add.
      :type \* *keys*: list


   .. py:method:: delete(keys)

      Delete a set of keys.

      :param \*keys*: The keys to delete.
      :type \*keys*: list



.. py:class:: Methods(dirpath=None)

   Bases: :py:obj:`bw2data.serialization.CompoundJSONDict`

   .. autoapi-inheritance-diagram:: bw2data.meta.Methods
      :parts: 1
      :private-bases:

   A dictionary for method metadata. File data is saved in ``methods.json``.

   .. py:attribute:: filename
      :value: 'methods.json'

      


.. py:class:: NormalizationMeta(dirpath=None)

   Bases: :py:obj:`Methods`

   .. autoapi-inheritance-diagram:: bw2data.meta.NormalizationMeta
      :parts: 1
      :private-bases:

   A dictionary for normalization metadata. File data is saved in ``methods.json``.

   .. py:attribute:: filename
      :value: 'normalizations.json'

      


.. py:class:: Preferences(*args, **kwargs)

   Bases: :py:obj:`bw2data.serialization.PickledDict`

   .. autoapi-inheritance-diagram:: bw2data.meta.Preferences
      :parts: 1
      :private-bases:

   A dictionary of project-specific preferences.

   .. py:attribute:: filename
      :value: 'preferences.pickle'

      


.. py:class:: WeightingMeta(dirpath=None)

   Bases: :py:obj:`Methods`

   .. autoapi-inheritance-diagram:: bw2data.meta.WeightingMeta
      :parts: 1
      :private-bases:

   A dictionary for weighting metadata. File data is saved in ``methods.json``.

   .. py:attribute:: filename
      :value: 'weightings.json'

      


.. py:data:: calculation_setups

   

.. py:data:: dynamic_calculation_setups

   

.. py:data:: geomapping

   

.. py:data:: methods

   

.. py:data:: normalizations

   

.. py:data:: preferences

   

.. py:data:: weightings

   

