:py:mod:`bw2io.unlinked_data`
=============================

.. py:module:: bw2io.unlinked_data


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.unlinked_data.UnlinkedData
   bw2io.unlinked_data._UnlinkedData




Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.unlinked_data.unlinked_data


.. py:class:: UnlinkedData

   Bases: :py:obj:`bw2data.data_store.DataStore`

   .. autoapi-inheritance-diagram:: bw2io.unlinked_data.UnlinkedData
      :parts: 1
      :private-bases:

   .. py:attribute:: _intermediate_dir
      :value: 'unlinked'

      

   .. py:attribute:: _metadata

      

   .. py:method:: validate(*args, **kwargs)



.. py:class:: _UnlinkedData

   Bases: :py:obj:`bw2data.serialization.SerializedDict`

   .. autoapi-inheritance-diagram:: bw2io.unlinked_data._UnlinkedData
      :parts: 1
      :private-bases:

   .. py:attribute:: filename
      :value: 'unlinked_data.json'

      


.. py:data:: unlinked_data

   

