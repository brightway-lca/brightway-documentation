:py:mod:`bw2data.logs`
======================

.. py:module:: bw2data.logs


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.logs.FakeLog



Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.logs.close_log
   bw2data.logs.get_io_logger
   bw2data.logs.get_logger
   bw2data.logs.get_verbose_logger
   bw2data.logs.upload_logs_to_server



Attributes
~~~~~~~~~~

.. autoapisummary::

   bw2data.logs.anyjson


.. py:class:: FakeLog

   Like a log object, but does nothing

   .. py:method:: fake_function(*args, **kwargs)



.. py:function:: close_log(log)

   Detach log handlers; flush to disk


.. py:function:: get_io_logger(name)

   Build a logger that records only relevent data for display later as HTML.


.. py:function:: get_logger(name, level=logging.INFO)


.. py:function:: get_verbose_logger(name, level=logging.WARNING)


.. py:function:: upload_logs_to_server(metadata={})


.. py:data:: anyjson

   

