:py:mod:`bw2data.bin.bw2_uptodate`
==================================

.. py:module:: bw2data.bin.bw2_uptodate

.. autoapi-nested-parse::

   Brightway2 updating made simple.

   Usage:
     bw2-uptodate
     bw2-uptodate -l | --list
     bw2-uptodate -h | --help
     bw2-uptodate --version

   Options:
     --list        List the updates needed, but don't do anything
     -h --help     Show this screen.
     --version     Show version.



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2data.bin.bw2_uptodate.UpdaterInterface



Functions
~~~~~~~~~

.. autoapisummary::

   bw2data.bin.bw2_uptodate.main



.. py:class:: UpdaterInterface

   .. py:method:: needed()


   .. py:method:: list()


   .. py:method:: update(confirm=True)



.. py:function:: main()


