:py:mod:`bw2data.project`
=========================

.. py:module:: bw2data.project


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.project.ProjectDataset
   bw2data.project.ProjectManager



Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.project.lockable
   bw2data.project.writable_project



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2data.project.READ_ONLY_PROJECT
   bw2data.project.projects


.. py:class:: ProjectDataset

   Bases: :py:obj:`peewee.Model`

   .. autoapi-inheritance-diagram:: bw2data.project.ProjectDataset
      :parts: 1
      :private-bases:

   .. py:attribute:: data

      

   .. py:attribute:: name

      


.. py:class:: ProjectManager

   Bases: :py:obj:`collections.abc.Iterable`

   .. autoapi-inheritance-diagram:: bw2data.project.ProjectManager
      :parts: 1
      :private-bases:

   .. py:property:: current


   .. py:property:: dir


   .. py:property:: logs_dir


   .. py:property:: output_dir

      Get directory for output files.

      Uses environment variable ``BRIGHTWAY2_OUTPUT_DIR``; ``preferences['output_dir']``; or directory ``output`` in current project.

      Returns output directory path.

   .. py:attribute:: _basic_directories
      :value: ('backups', 'intermediate', 'lci', 'processed')

      

   .. py:attribute:: _is_temp_dir
      :value: False

      

   .. py:attribute:: read_only
      :value: False

      

   .. py:method:: _create_base_directories()


   .. py:method:: _do_automatic_updates()

      Run any available automatic updates


   .. py:method:: _get_base_directories()


   .. py:method:: _reset_meta()


   .. py:method:: _reset_sqlite3_databases()


   .. py:method:: _restore_orig_directory()

      Point the ProjectManager back to original directories.

      Used exclusively in tests.


   .. py:method:: _use_temp_directory()

      Point the ProjectManager towards a temporary directory instead of `user_data_dir`.

      Used exclusively for tests.


   .. py:method:: copy_project(new_name, switch=True)

      Copy current project to a new project named ``new_name``. If ``switch``, switch to new project.


   .. py:method:: create_project(name=None, **kwargs)


   .. py:method:: delete_project(name=None, delete_dir=False)

      Delete project ``name``, or the current project.

      ``name`` is the project to delete. If ``name`` is not provided, delete the current project.

      By default, the underlying project directory is not deleted; only the project name is removed from the list of active projects. If ``delete_dir`` is ``True``, then also delete the project directory.

      If deleting the current project, this function sets the current directory to ``default`` if it exists, or to a random project.

      Returns the current project.


   .. py:method:: purge_deleted_directories()

      Delete project directories for projects which are no longer registered.

      Returns number of directories deleted.


   .. py:method:: report()

      Give a report on current projects, including installed databases and file sizes.

      Returns tuples of ``(project name, number of databases, size of all databases (GB))``.


   .. py:method:: request_directory(name)

      Return the absolute path to the subdirectory ``dirname``, creating it if necessary.

      Returns ``False`` if directory can't be created.


   .. py:method:: set_current(name, writable=True, update=True)



.. py:function:: lockable()


.. py:function:: writable_project(wrapped, instance, args, kwargs)


.. py:data:: READ_ONLY_PROJECT
   :value: Multiline-String

    .. raw:: html

        <details><summary>Show Value</summary>

    .. code-block:: python

        """
        ***Read only project***
        
        This project is being used by another process and no writes can be made until:
            1. You close the other program, or switch to a different project, *and*
            2. You call `projects.enable_writes` *and* get the response `True`.
        
            If you are **sure** that this warning is incorrect, call
            `projects.enable_writes(force=True)` to enable writes.
        """

    .. raw:: html

        </details>

   

.. py:data:: projects

   

