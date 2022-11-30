:py:mod:`conf`
==============

.. py:module:: conf


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   conf.Mock



Functions
~~~~~~~~~

.. autoapisummary::

   conf.skip
   conf.setup



Attributes
~~~~~~~~~~

.. autoapisummary::

   conf.MOCK_MODULES
   conf.version
   conf.release
   conf.extensions
   conf.mathjax_path
   conf.templates_path
   conf.source_suffix
   conf.master_doc
   conf.project
   conf.copyright
   conf.exclude_patterns
   conf.pygments_style
   conf.html_theme
   conf.html_static_path
   conf.htmlhelp_basename
   conf.latex_elements
   conf.latex_documents
   conf.man_pages
   conf.texinfo_documents


.. py:class:: Mock(/, *args, **kw)

   Bases: :py:obj:`unittest.mock.MagicMock`

   MagicMock is a subclass of Mock with default implementations
   of most of the magic methods. You can use MagicMock without having to
   configure the magic methods yourself.

   If you use the `spec` or `spec_set` arguments then *only* magic
   methods that exist in the spec will be created.

   Attributes and the return value of a `MagicMock` will also be `MagicMocks`.

   .. py:method:: __getattr__(name)
      :classmethod:



.. py:data:: MOCK_MODULES
   :annotation: = ['pyprind', 'brightway2', 'bw2calc.lca', 'bw2calc.matrices', 'bw2data', 'bw2data.data_store',...

   

.. py:data:: version
   :annotation: = 0.4

   

.. py:data:: release
   :annotation: = 0.4.2

   

.. py:function:: skip(app, what, name, obj, skip, options)


.. py:function:: setup(app)


.. py:data:: extensions
   :annotation: = ['sphinx.ext.autodoc', 'sphinx.ext.mathjax']

   

.. py:data:: mathjax_path
   :annotation: = https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML

   

.. py:data:: templates_path
   :annotation: = ['_templates']

   

.. py:data:: source_suffix
   :annotation: = .rst

   

.. py:data:: master_doc
   :annotation: = index

   

.. py:data:: project
   :annotation: = bw2-regional

   

.. py:data:: copyright
   :annotation: = 2014, Chris Mutel

   

.. py:data:: exclude_patterns
   :annotation: = ['_build']

   

.. py:data:: pygments_style
   :annotation: = sphinx

   

.. py:data:: html_theme
   :annotation: = default

   

.. py:data:: html_static_path
   :annotation: = ['_static']

   

.. py:data:: htmlhelp_basename
   :annotation: = bw2-regionaldoc

   

.. py:data:: latex_elements
   

   

.. py:data:: latex_documents
   :annotation: = [['index', 'bw2-regional.tex', 'bw2-regional Documentation', 'Chris Mutel', 'manual']]

   

.. py:data:: man_pages
   :annotation: = [['index', 'bw2-regional', 'bw2-regional Documentation', ['Chris Mutel'], 1]]

   

.. py:data:: texinfo_documents
   :annotation: = [['index', 'bw2-regional', 'bw2-regional Documentation', 'Chris Mutel', 'bw2-regional', 'One...

   

