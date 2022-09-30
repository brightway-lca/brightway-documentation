# The short X.Y version.
version = '2.0'
# The full version, including alpha/beta/rc tags.
release = '2.0'

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '5.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'IPython.sphinxext.ipython_directive',
    'IPython.sphinxext.ipython_console_highlighting',
    'sphinx.ext.doctest',
    'nbsphinx',
    'sphinx_gallery.load_style'
]

# Load mathjax through https so it works on RTD/Chrome. See:
# http://sphinx-doc.org/ext/math.html
# http://docs.mathjax.org/en/latest/start.html#secure-access-to-the-cdn
# https://github.com/rtfd/readthedocs.org/issues/283
mathjax_path = "https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Brightway'
copyright = 'Brightway Developers'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

html_static_path = ["source/_static"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "pydata_sphinx_theme"

# https://pydata-sphinx-theme.readthedocs.io/en/stable/
html_theme_options = {
    "announcement": "<p>⚠️ Work in Progress! ⚠️</p>",
    "external_links": [
        {
            "url": "https://training.brightway.dev/",
            "name": "Interactive Training",
        },
    ],
    "header_links_before_dropdown": 4,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/brightway-lca",
            "icon": "fab fa-github",
        },
        {
            "name": "Conda",
            "url": "https://anaconda.org/cmutel/brightway2",
            "icon": "fab fa-python",
        },
        {
            "name": "StackOverflow",
            "url": "https://stackoverflow.com/questions/tagged/brightway",
            "icon": "fab fa-stack-overflow",
        },
        {
            "name": "Gitter",
            "url": "https://gitter.im/brightway-lca/community",
            "icon": "fab fa-gitter",
        }
    ],
    "use_edit_page_button": False,
    "collapse_navigation": True,
    "footer_items": ["copyright"],
    "left_sidebar_end": [],
    "logo": {
      "image_light": "BW_clear_transparent_landscape.png",
      "image_dark": "BW_dark_transparent_landscape.png"
    },
    "favicons": [
      {
         "rel": "icon",
         "sizes": "100x100",
         "href": "BW_favicon_100x100.png",
      },
      {
         "rel": "apple-touch-icon",
         "sizes": "500x500",
         "href": "BW_favicon_500x500.png"
      },
   ]
}

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True