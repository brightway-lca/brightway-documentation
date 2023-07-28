:py:mod:`bw2data`
=================

.. py:module:: bw2data


Subpackages
-----------
.. toctree::
   :titlesonly:
   :maxdepth: 3

   backends/index.rst
   bin/index.rst
   search/index.rst


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   configuration/index.rst
   data_store/index.rst
   database/index.rst
   errors/index.rst
   fatomic/index.rst
   filesystem/index.rst
   ia_data_store/index.rst
   logs/index.rst
   meta/index.rst
   method/index.rst
   parameters/index.rst
   project/index.rst
   proxies/index.rst
   query/index.rst
   serialization/index.rst
   sqlite/index.rst
   updates/index.rst
   utils/index.rst
   validate/index.rst
   weighting_normalization/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.IndexManager
   bw2data.JsonWrapper
   bw2data.Method
   bw2data.Normalization
   bw2data.Searcher
   bw2data.Weighting



Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.Database
   bw2data.convert_backend
   bw2data.get_activity
   bw2data.set_data_dir



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2data.calculation_setups
   bw2data.config
   bw2data.databases
   bw2data.dynamic_calculation_setups
   bw2data.geomapping
   bw2data.mapping
   bw2data.methods
   bw2data.normalizations
   bw2data.parameters
   bw2data.preferences
   bw2data.projects
   bw2data.weightings


.. py:class:: IndexManager(database_path, dir_name='whoosh')

   Bases: :py:obj:`object`

   .. py:method:: _format_dataset(ds)


   .. py:method:: add_dataset(ds)


   .. py:method:: add_datasets(datasets)


   .. py:method:: create()


   .. py:method:: delete_database()


   .. py:method:: delete_dataset(ds)


   .. py:method:: get()


   .. py:method:: update_dataset(ds)



.. py:class:: JsonWrapper

   Bases: :py:obj:`object`

   .. py:method:: dump(data, filepath)
      :classmethod:


   .. py:method:: dump_bz2(data, filepath)
      :classmethod:


   .. py:method:: dumps(data)
      :classmethod:


   .. py:method:: load(file)
      :classmethod:


   .. py:method:: load_bz2(filepath)
      :classmethod:


   .. py:method:: loads(data)
      :classmethod:



.. py:class:: Method(name)

   Bases: :py:obj:`bw2data.ia_data_store.ImpactAssessmentDataStore`

   .. autoapi-inheritance-diagram:: bw2data.Method
      :parts: 1
      :private-bases:

   A manager for an impact assessment method. This class can register or deregister methods, write intermediate data, process data to parameter arrays, validate, and copy methods.

   The Method class never holds intermediate data, but it can load or write intermediate data. The only attribute is *name*, which is the name of the method being managed.

   Instantiation does not load any data. If this method is not yet registered in the metadata store, a warning is written to ``stdout``.

   Methods are hierarchally structured, and this structure is preserved in the method name. It is a tuple of strings, like ``('ecological scarcity 2006', 'total', 'natural resources')``.

   The data schema for IA methods is:

   .. code-block:: python

           Schema([Any(
               [valid_tuple, maybe_uncertainty],         # site-generic
               [valid_tuple, maybe_uncertainty, object]  # regionalized
           )])

   where:
       * *valid_tuple* (tuple): A dataset identifier, like ``("biosphere", "CO2")``.
       * *maybe_uncertainty* (uncertainty dict or number): Either a number or an uncertainty dictionary.
       * *object* (object, optional) is a location identifier, used only for regionalized LCIA.

   :param \* *name*: Name of impact assessment method to manage.
   :type \* *name*: tuple

   .. py:attribute:: _metadata

      

   .. py:attribute:: dtype_fields
      :value: [(), (), (), ()]

      

   .. py:attribute:: validator

      

   .. py:method:: add_mappings(data)

      Add objects to ``mapping`` or ``geomapping``, if necessary.

      :param \* *data*: The data
      :type \* *data*: object


   .. py:method:: process_data(row)

      Translate data into correct order


   .. py:method:: write(data, process=True)

      Serialize intermediate data to disk.

      Sets the metadata key ``num_cfs`` automatically.



.. py:class:: Normalization

   Bases: :py:obj:`bw2data.ia_data_store.ImpactAssessmentDataStore`

   .. autoapi-inheritance-diagram:: bw2data.Normalization
      :parts: 1
      :private-bases:

   LCIA normalization data - used to transform meaningful units, like mass or damage, into "person-equivalents" or some such thing.

   The data schema for IA normalization is:

   .. code-block:: python

           Schema([
               [valid_tuple, maybe_uncertainty]
           ])

   where:
       * ``valid_tuple`` is a dataset identifier, like ``("biosphere", "CO2")``
       * ``maybe_uncertainty`` is either a number or an uncertainty dictionary


   .. py:attribute:: _metadata

      

   .. py:attribute:: dtype_fields
      :value: [(), ()]

      

   .. py:attribute:: validator

      

   .. py:method:: add_mappings(data)

      Add each normalization flow (should be biosphere flows) to global mapping


   .. py:method:: process_data(row)

      Return values that match ``dtype_fields``, as well as number or uncertainty dictionary



.. py:class:: Searcher(database)

   Bases: :py:obj:`object`

   .. py:method:: search(string, limit=25, facet=None, proxy=True, boosts=None, filter=None, mask=None)



.. py:class:: Weighting

   Bases: :py:obj:`bw2data.ia_data_store.ImpactAssessmentDataStore`

   .. autoapi-inheritance-diagram:: bw2data.Weighting
      :parts: 1
      :private-bases:

   LCIA weighting data - used to combine or compare different impact categories.

   The data schema for weighting is a one-element list:

   .. code-block:: python

           Schema(All(
               [uncertainty_dict],
               Length(min=1, max=1)
           ))


   .. py:attribute:: _metadata

      

   .. py:attribute:: dtype_fields
      :value: []

      

   .. py:attribute:: validator

      

   .. py:method:: process_data(row)

      Return an empty tuple (as ``dtype_fields`` is empty), and the weighting uncertainty dictionary.


   .. py:method:: write(data)

      Because of DataStore assumptions, need a one-element list



.. py:function:: Database(name, backend=None)

   A method that returns a database class instance. The default database type is `SingleFileDatabase`. `JSONDatabase` stores each process dataset in indented JSON in a separate file. Database types are specified in `databases[database_name]['backend']`.

   New database types can be registered with the config object:

   .. code-block:: python

       config.backends['backend type string'] = MyNewBackendClass

   .. warning:: Registering new backends must be done each time you start the Python interpreter.

   To test whether an object is a database subclass, do:

   .. code-block:: python

       from bw2data.backends import LCIBackend
       isinstance(my_database, LCIBackend)



.. py:function:: convert_backend(database_name, backend)

   Convert a Database to another backend.

   bw2data currently supports the `default` and `json` backends.

   :param \* `database_name`: Name of database.
   :type \* `database_name`: unicode
   :param \* `backend`: Type of database. `backend` should be recoginized by `DatabaseChooser`.
   :type \* `backend`: unicode

   Returns `False` if the old and new backend are the same. Otherwise returns an instance of the new Database object.


.. py:function:: get_activity(key)


.. py:function:: set_data_dir(dirpath, permanent=True)

   Set the Brightway2 data directory to ``dirpath``.

   If ``permanent`` is ``True``, then set ``dirpath`` as the default data directory.

   Creates ``dirpath`` if needed. Also creates basic directories, and resets metadata.



.. py:data:: calculation_setups

   

.. py:data:: config

   

.. py:data:: databases

   

.. py:data:: dynamic_calculation_setups

   

.. py:data:: geomapping

   

.. py:data:: mapping

   

.. py:data:: methods

   

.. py:data:: normalizations

   

.. py:data:: parameters

   

.. py:data:: preferences

   

.. py:data:: projects

   

.. py:data:: weightings

   

