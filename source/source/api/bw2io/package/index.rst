:py:mod:`bw2io.package`
=======================

.. py:module:: bw2io.package


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2io.package.BW2Package



Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.package.download_biosphere
   bw2io.package.download_methods



.. py:class:: BW2Package

   Bases: :py:obj:`object`

   This is a format for saving objects which implement the :ref:`datastore` API.

   Data is stored as a BZip2-compressed file of JSON data.

   This archive format is compatible across Python versions, and is, at least in theory, programming-language agnostic.

   Validation is done with ``bw2data.validate.bw2package_validator``.
   The data format is:

   .. code-block:: python

       {
           'metadata': {},                                     # Dictionary of metadata to be written to metadata-store.
           'name': basestring,                                 # Name of object
           'class': {                                          # Data on the underlying class. A new class is instantiated
                                                               # based on these strings. See _create_class.
               'module': basestring,                           # e.g. "bw2data.database"
               'name': basestring                              # e.g. "Database"
           },
           'unrolled_dict': bool,                              # Flag indicating if dictionary keys needed to
                                                               # be modified for JSON (as JSON keys can't be tuples)
           'data': object                                      # Object data, e.g. LCIA method or LCI database
       }

   .. warning::

      Perfect roundtrips between machines are not guaranteed:
          * All lists are converted to tuples (because JSON does not distinguish between lists and tuples).
          * Absolute filepaths in metadata would be specific to a certain computer and user.

   .. rubric:: Notes

   This class does not need to be instantiated, as all its methods are ``classmethods``, i.e. do ``BW2Package.import_obj("foo")`` instead of ``BW2Package().import_obj("foo")``

   .. py:attribute:: APPROVED

      

   .. py:method:: _create_class(metadata, apply_whitelist=True)
      :classmethod:


   .. py:method:: _create_obj(data)
      :classmethod:


   .. py:method:: _get_class_metadata(obj)
      :classmethod:


   .. py:method:: _is_valid_package(data)
      :classmethod:


   .. py:method:: _is_whitelisted(metadata)
      :classmethod:


   .. py:method:: _load_obj(data, whitelist=True)
      :classmethod:


   .. py:method:: _prepare_obj(obj, backwards_compatible=False)
      :classmethod:


   .. py:method:: _write_file(filepath, data)
      :classmethod:


   .. py:method:: export_obj(obj, filename=None, folder='export', backwards_compatible=False)
      :classmethod:

      Export an object.

      :param obj: Object to export.
      :type obj: object
      :param filename: Name of file to create. Default is ``obj.name``.
      :type filename: str, optional
      :param folder: Folder to create file in. Default is ``export``.
      :type folder: str, optional
      :param backwards_compatible: Create package compatible with bw2data version 1.
      :type backwards_compatible: bool, optional

      :returns: Filepath of created file.
      :rtype: str


   .. py:method:: export_objs(objs, filename, folder='export', backwards_compatible=False)
      :classmethod:

      Export a list of objects. Can have heterogeneous types.

      :param objs: List of objects to export.
      :type objs: list
      :param filename: Name of file to create.
      :type filename: str
      :param folder: Folder to create file in. Default is ``export``.
      :type folder: str, optional
      :param backwards_compatible: Create package compatible with bw2data version 1.
      :type backwards_compatible: bool, optional

      :returns: Filepath of created file.
      :rtype: str


   .. py:method:: import_file(filepath, whitelist=True)
      :classmethod:

      Import bw2package file, and create the loaded objects, including registering, writing, and processing the created objects.

      :param filepath: Path of file to import
      :type filepath: str
      :param whitelist: Apply whitelist to allowed types. Default is ``True``.
      :type whitelist: bool

      :returns: Created object or list of created objects.
      :rtype: object or list of objects


   .. py:method:: load_file(filepath, whitelist=True)
      :classmethod:

      Load a bw2package file with one or more objects. Does not create new objects.

      :param filepath: Path of file to import
      :type filepath: str
      :param whitelist: Apply whitelist of approved classes to allowed types. Default is ``True``.
      :type whitelist: bool

      :returns:

                * ``"class"`` is an actual Python class object (but not instantiated).
      :rtype: The loaded data in the bw2package dict data format, with the following changes



.. py:function:: download_biosphere()


.. py:function:: download_methods()


