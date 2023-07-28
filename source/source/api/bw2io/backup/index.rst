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

   Backup data directory to a ``.tar.gz`` (compressed tar archive).

   Backup archive is saved to the user's home directory.

   Restoration is done manually. Returns the filepath of the backup archive.


.. py:function:: backup_project_directory(project)

   Backup project data directory to a ``.tar.gz`` (compressed tar archive).

   ``project`` is the name of a project.

   Backup archive is saved to the user's home directory.

   Restoration is done using ``restore_project_directory``.

   Returns the filepath of the backup archive.


.. py:function:: restore_project_directory(fp)

   Restore backup created using ``backup_project_directory``.

   Raises an error is the project already exists.

   ``fp`` is the filepath of the backup archive.

   Returns the name of the newly created project.


