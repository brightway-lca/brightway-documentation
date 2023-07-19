:py:mod:`bw2io.remote`
======================

.. py:module:: bw2io.remote


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.remote.get_projects
   bw2io.remote.install_project



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2io.remote.PROJECTS_BW2
   bw2io.remote.PROJECTS_BW25
   bw2io.remote.cache_dir


.. py:function:: get_projects(update_config: Optional[bool] = True) -> dict


.. py:function:: install_project(project_key: str, project_name: Optional[str] = None, projects_config: Optional[dict] = get_projects(), url: Optional[str] = 'https://files.brightway.dev/', overwrite_existing: Optional[bool] = False, __recursive: Union[bool, None] = False)

   Install an existing Brightway project archive.

   By default uses ``https://files.brightway.dev/`` as the file repository, but you can run your own.

   :param project_key: A string uniquely identifying a project, e.g. ``ecoinvent-3.8-biosphere``.
   :type project_key: str
   :param project_name: The name of the new project to create. If not provided will be taken from the archive file.
   :type project_name: str, optional
   :param projects_config: A dictionary that maps ``project_key`` values to filenames at the repository
   :type projects_config: dict, optional
   :param url: The URL, with trailing slash ``/``, where the file can be found.
   :type url: str, optional
   :param overwrite_existing: Allow overwriting an existing project
   :type overwrite_existing: bool, optional
   :param __recursive: Internal flag used to determine if this function has errored out already
   :type __recursive: bool

   :returns: The name of the created project.
   :rtype: str


.. py:data:: PROJECTS_BW2

   

.. py:data:: PROJECTS_BW25

   

.. py:data:: cache_dir

   

