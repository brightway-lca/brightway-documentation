# General information about the project.
project = 'Brightway'
copyright = 'Brightway Developers'

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
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.napoleon',
    'IPython.sphinxext.ipython_directive',
    'IPython.sphinxext.ipython_console_highlighting',
    'nbsphinx',
    'sphinx_gallery.load_style',
    'myst_parser',
    'autoapi'
]

templates_path = ['source/_templates']
html_static_path = ["source/_static"]
exclude_patterns = ['_build']

autoapi_dirs = [
    '../brightway2-analyzer',
    '../brightway2-calc',
    '../brightway2-data',
    '../brightway2-io',
    '../brightway2-regional'
]

autoapi_template_dir = '_autoapi_templates'
autoapi_root = 'source/api'

# The suffix of source filenames.
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
# The master toctree document.
master_doc = 'index'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "pydata_sphinx_theme"

# https://pydata-sphinx-theme.readthedocs.io/en/stable/
html_theme_options = {
    "header_links_before_dropdown": 5,
    "announcement": "<p>⚠️ Work in Progress! If you find errors, open an issue on GitHub. ⚠️</p>",
    "collapse_navigation": True,
    "footer_items": ["copyright"],
    "external_links": [
        {
            "url": "https://training.brightway.dev/",
            "name": "Interactive Training",
        },
    ],
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
    "logo": {
      "image_light": "logo/BW_all_black_transparent_landscape.svg",
      "image_dark": "logo/BW_all_white_transparent_landscape.svg"
    },
    "favicons": [
      {
         "rel": "icon",
         "sizes": "100x100",
         "href": "logo/BW_favicon_100x100.png",
      },
      {
         "rel": "apple-touch-icon",
         "sizes": "500x500",
         "href": "logo/BW_favicon_500x500.png"
      },
   ]
}

html_css_files = ['css/custom.css']

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True