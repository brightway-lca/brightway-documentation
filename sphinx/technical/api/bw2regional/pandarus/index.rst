:py:mod:`bw2regional.pandarus`
==============================

.. py:module:: bw2regional.pandarus


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   bw2regional.pandarus.relabel
   bw2regional.pandarus.load_file
   bw2regional.pandarus.get_possible_collections
   bw2regional.pandarus.import_from_pandarus
   bw2regional.pandarus.handle_topographical_intersection
   bw2regional.pandarus.import_xt_from_rasterstats



.. py:function:: relabel(data, first, second)

   Add geocollection names to geo identifiers


.. py:function:: load_file(filepath)

   Load Pandarus JSON output file.

   Returns metadata and calculation results.


.. py:function:: get_possible_collections(kwargs)

   Return all geo- and topocollections for a file hash.

   Returns list of (collection name, collection type) tuples.


.. py:function:: import_from_pandarus(fp)

   Load output file from Pandarus job.

   This function will:

   * Load pandarus output file
   * Locate the appropriate geo- or topocollection
   * Check to make sure that SHA256 hashes and other metadata match
   * If ``first`` is a topocollection, make sure the appropriate ``Topology`` exists, and squash the pandarus results to the linked geocollection(s).



.. py:function:: handle_topographical_intersection(metadata, data, first_collections, second_collections, filepath)

   Handle an intersection between one or more topographies and a single geocollection.

   Each topography is associated with exactly one geocollection.

   Each topography is not empty, i.e. we can use the topographical definitions to filter.

   The procedure is:
   #. Check metadata validity, and make sure the topography ids are in the first column
   #. To split data into each topography
   #. Squash the topography to geocollections
   #. Create a new intersection for each geocollection/topography pair

   We use Pandas DataFrames to do aggregation in a resource efficient way. We also write the processed Intersection arrays directly.



.. py:function:: import_xt_from_rasterstats(fp, name, gc, **kwargs)


