:py:mod:`bw2regional.xtables`
=============================

.. py:module:: bw2regional.xtables


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   bw2regional.xtables.ExtensionTable




.. py:class:: ExtensionTable(name)

   Bases: :py:obj:`bw2regional.loading.Loading`

   .. py:property:: filename

      Remove filesystem-unsafe characters and perform unicode normalization on ``self.name`` using :func:`.filesystem.safe_filename`.

   .. py:attribute:: _metadata
      

      

   .. py:attribute:: validator
      

      

   .. py:attribute:: matrix
      :annotation: = xtable_matrix

      

   .. py:method:: write_to_map(*args, **kwargs)
      :abstractmethod:


   .. py:method:: import_from_map(mask=None)



