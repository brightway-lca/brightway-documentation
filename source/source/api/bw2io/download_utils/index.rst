:py:mod:`bw2io.download_utils`
==============================

.. py:module:: bw2io.download_utils


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2io.download_utils.download_with_progressbar
   bw2io.download_utils.get_filename



.. py:function:: download_with_progressbar(url, filename=None, dirpath=None, chunk_size=4096 * 8)

   Download file from URL and show progress bar.

   :param url: URL to download from.
   :type url: str
   :param filename: Filename to save to. If not given, will be determined from URL.
   :type filename: str, optional
   :param dirpath: Directory to save to. If not given, will be current working directory.
   :type dirpath: str, optional
   :param chunk_size: Chunk size to use when downloading.
   :type chunk_size: int, optional

   :returns: Path to downloaded file.
   :rtype: pathlib.Path


.. py:function:: get_filename(response)

   Get filename from response headers or URL.

   :param response:
   :type response: requests.Response

   :returns: Filename
   :rtype: str


