:py:mod:`bw2io.backup`
======================

.. py:module:: bw2io.backup


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.backup.backup_data_directory
   bw2io.backup.backup_project_directory
   bw2io.backup.restore_project_directory



.. py:function:: backup_data_directory()

   Backup data directory to a ``.tar.gz`` (compressed tar archive) in the user's home directory.
   Restoration is done manually.

   .. rubric:: Examples

   >>> bw2io.bw2setup()
   >>> bw2io.backup.backup_data_directory()
   Creating backup archive - this could take a few minutes...


.. py:function:: backup_project_directory(project: str)

   Backup project data directory to a ``.tar.gz`` (compressed tar archive) in the user's home directory.

   :param project: Name of the project to backup.
   :type project: str

   :returns: **project_name** -- Name of the project that was backed up.
   :rtype: str

   :raises ValueError: If the project does not exist.

   .. seealso::

      :obj:`bw2io.backup.restore_project_directory`
          To restore a project directory from a backup.


.. py:function:: restore_project_directory(fp: str, project_name: Optional[str] = None, overwrite_existing: Optional[bool] = False)

   Restore a backed up project data directory from a ``.tar.gz`` (compressed tar archive) in the user's home directory.

   :param fp: File path of the project to restore.
   :type fp: str
   :param project_name: Name of new project to create
   :type project_name: str, optional
   :param overwrite_existing:
   :type overwrite_existing: bool, optional

   :returns: **project_name** -- Name of the project that was restored.
   :rtype: str

   :raises ValueError: If the project does not exist.

   .. seealso::

      :obj:`bw2io.backup.backup_project_directory`
          To restore a project directory from a backup.


