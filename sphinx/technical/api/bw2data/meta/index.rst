:py:mod:`bw2data.meta`
======================

.. py:module:: bw2data.meta


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.meta.GeoMapping
   bw2data.meta.Databases
   bw2data.meta.CalculationSetups
   bw2data.meta.DynamicCalculationSetups
   bw2data.meta.Methods
   bw2data.meta.WeightingMeta
   bw2data.meta.NormalizationMeta
   bw2data.meta.Preferences




Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2data.meta.geomapping
   bw2data.meta.methods
   bw2data.meta.normalizations
   bw2data.meta.preferences
   bw2data.meta.weightings
   bw2data.meta.calculation_setups
   bw2data.meta.dynamic_calculation_setups


.. py:class:: GeoMapping(*args, **kwargs)

   Bases: :py:obj:`bw2data.serialization.PickledDict`

   A dictionary that maps location codes to integers. Needed because parameter arrays have integer ``geo`` fields.

   File data is stored in ``geomapping.pickle``.

   This dictionary does not support setting items directly; instead, use the ``add`` method to add multiple keys.

   .. py:attribute:: filename
      :annotation: = geomapping.pickle

      

   .. py:method:: add(keys)

      Add a set of keys. These keys can already be in the mapping; only new keys will be added.

      :param \* *keys*: The keys to add.
      :type \* *keys*: list


   .. py:method:: delete(keys)

      Delete a set of keys.

      :param \*keys*: The keys to delete.
      :type \*keys*: list


   .. py:method:: __setitem__(key, value)
      :abstractmethod:


   .. py:method:: __str__()

      Return str(self).


   .. py:method:: __len__()



.. py:class:: Databases(dirpath=None)

   Bases: :py:obj:`bw2data.serialization.SerializedDict`

   A dictionary for database metadata. This class includes methods to manage database versions. File data is saved in ``databases.json``.

   .. py:attribute:: filename
      :annotation: = databases.json

      

   .. py:method:: increment_version(database, number=None)

      Increment the ``database`` version. Returns the new version.


   .. py:method:: version(database)

      Return the ``database`` version


   .. py:method:: set_modified(database)


   .. py:method:: set_dirty(database)


   .. py:method:: clean()


   .. py:method:: __delitem__(name)



.. py:class:: CalculationSetups(dirpath=None)

   Bases: :py:obj:`bw2data.serialization.PickledDict`

   A dictionary for calculation setups.

   Keys:
   * `inv`: List of functional units, e.g. ``[{(key): amount}, {(key): amount}]``
   * `ia`: List of LCIA methods, e.g. ``[(method), (method)]``.


   .. py:attribute:: filename
      :annotation: = setups.pickle

      


.. py:class:: DynamicCalculationSetups(dirpath=None)

   Bases: :py:obj:`bw2data.serialization.PickledDict`

   A dictionary for Dynamic calculation setups.

   Keys:
   * `inv`: List of functional units, e.g. ``[{(key): amount}, {(key): amount}]``
   * `ia`: Dictionary of orst case LCIA method and the relative dynamic LCIA method, e.g. `` [{dLCIA_method_1_worstcase:dLCIA_method_1 , dLCIA_method_2_worstcase:dLCIA_method_2}]``.


   .. py:attribute:: filename
      :annotation: = dynamicsetups.pickle

      


.. py:class:: Methods(dirpath=None)

   Bases: :py:obj:`bw2data.serialization.CompoundJSONDict`

   A dictionary for method metadata. File data is saved in ``methods.json``.

   .. py:attribute:: filename
      :annotation: = methods.json

      


.. py:class:: WeightingMeta(dirpath=None)

   Bases: :py:obj:`Methods`

   A dictionary for weighting metadata. File data is saved in ``methods.json``.

   .. py:attribute:: filename
      :annotation: = weightings.json

      


.. py:class:: NormalizationMeta(dirpath=None)

   Bases: :py:obj:`Methods`

   A dictionary for normalization metadata. File data is saved in ``methods.json``.

   .. py:attribute:: filename
      :annotation: = normalizations.json

      


.. py:class:: Preferences(*args, **kwargs)

   Bases: :py:obj:`bw2data.serialization.PickledDict`

   A dictionary of project-specific preferences.

   .. py:attribute:: filename
      :annotation: = preferences.pickle

      


.. py:data:: geomapping
   

   

.. py:data:: methods
   

   

.. py:data:: normalizations
   

   

.. py:data:: preferences
   

   

.. py:data:: weightings
   

   

.. py:data:: calculation_setups
   

   

.. py:data:: dynamic_calculation_setups
   

   

