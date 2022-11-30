:py:mod:`bw2regional.pandarus_remote`
=====================================

.. py:module:: bw2regional.pandarus_remote


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2regional.pandarus_remote.PendingJob
   bw2regional.pandarus_remote.PandarusRemote



Functions
~~~~~~~~~

.. autoapisummary::

   bw2regional.pandarus_remote.run_job
   bw2regional.pandarus_remote.check_alive



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2regional.pandarus_remote.remote


.. py:exception:: RemoteError

   Bases: :py:obj:`Exception`

   Can't reach pandarus-remote web service


.. py:exception:: NotYetCalculated

   Bases: :py:obj:`Exception`

   Resource hasn't been calculated yet


.. py:exception:: AlreadyExists

   Bases: :py:obj:`Exception`

   Resource has already been calculated


.. py:class:: PendingJob(url)

   Bases: :py:obj:`object`

   A calculation job enqueued on a remote server

   .. py:property:: status


   .. py:method:: poll(interval=10)



.. py:function:: run_job(job)

   Handler that blocks until job is finished.


.. py:function:: check_alive(wrapped, instance, args, kwargs)


.. py:class:: PandarusRemote(url=None)

   Bases: :py:obj:`object`

   Interaction with `pandarus_remote <https://github.com/cmutel/pandarus_remote>`__ web service.

   Default URL is `https://pandarus.brightway.dev`.

   .. py:property:: alive


   .. py:method:: _download_file(resp)


   .. py:method:: catalog()


   .. py:method:: status(url)


   .. py:method:: upload(collection)


   .. py:method:: intersection(collection_one, collection_two)


   .. py:method:: intersection_as_new_geocollection(collection_one, collection_two, new_name)


   .. py:method:: rasterstats_as_xt(vector, raster, name)


   .. py:method:: calculate_rasterstats(vector, raster)


   .. py:method:: calculate_intersection(collection_one, collection_two)


   .. py:method:: hash_and_upload(collection, catalog=None)


   .. py:method:: handle_errors(response)



.. py:data:: remote
   

   

