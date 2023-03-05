### path setup ####################################################################################

from glob import glob
import datetime
from git import Repo
 
### project information ###########################################################################

project = 'Brightway'
copyright = datetime.date.today().strftime("%Y") + ' Brightway Developers'

version = '2.0' # the short X.Y version.
release = '2.0' # the full version, including alpha/beta/rc tags.

### project configuration #########################################################################

needs_sphinx = '5.3.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    # native extensions
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.napoleon',
    'sphinx.ext.inheritance_diagram', # for plotting dependency diagrams with sphinx-autoapi
    # iPython extensions
    'IPython.sphinxext.ipython_directive',
    'IPython.sphinxext.ipython_console_highlighting',
    # Markdown support
    # 'myst_parser', do not enable separately if using myst_nb, compare https://github.com/executablebooks/MyST-NB/issues/421#issuecomment-1164427544
    # Jupyter Notebook support
    'myst_nb',
    # API documentation support
    'autoapi',
    # responsive web component support
    'sphinx_design',
    # custom 404 page
    'notfound.extension',
]

staic_path = ['source/_static']
templates_path = ['source/_templates']
exclude_patterns = ['_build']
html_theme = "pydata_sphinx_theme"

# The master toctree document.
master_doc = 'index'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

### suppress warnings ##############################################################################

suppress_warnings = [
    "myst.header" # suppress warnings of the kind "WARNING: Non-consecutive header level increase; H1 to H3"
]

### extension configuration ########################################################################

## notfound configuration ################################################

notfound_context = {
'title': 'Page Not Found',
'body': '''                                                                                                                                           
<h1>Page Not Found (404)</h1>
<p>
Oops! It looks like you've stumbled upon a page that's been recycled into the digital abyss.
But don't worry, we're all about sustainability here.
Why not take a moment to reduce, reuse, and recycle your clicks by heading back to the main page?
And remember, every little bit counts in the grand scheme of things.
</p>
''',
}

## autoapi configuration ################################################
## https://sphinx-autoapi.readthedocs.io/en/latest/reference/config.html#customisation-options

autoapi_options = [
    'members',
    'undoc-members',
    'private-members',
    'show-inheritance',
    'show-module-summary',
    #'special-members',
    'imported-members',
    'show-inheritance-diagram'
]

autoapi_python_class_content = 'both'
autoapi_member_order = 'groupwise'

autoapi_dirs = [
    '../brightway2-io/bw2io',
    '../brightway2-data/bw2data',
    '../brightway2-calc/bw2calc',
    '../brightway2-analyzer/bw2analyzer'
]

autoapi_root = 'source/api'
autoapi_keep_files = False

autoapi_ignore = [
    '*/data/*',
    '*tests/*',
    '*tests.py',
    '*validation.py',
    '*version.py',
    '*.rst',
    '*.yml',
    '*.md',
    '*.json',
    '*.data'
]

## myst_parser configuration ############################################
## https://myst-parser.readthedocs.io/en/latest/configuration.html

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'myst-nb',
    '.ipynb': 'myst-nb',
    '.myst': 'myst-nb',
}

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
]

## myst_nb configuration ################################################

nb_execution_mode = 'off'

## version-switcher configuration #######################################

version: str = 'legacy'

## html configuration ###################################################

html_css_files = ['css/custom.css']

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# enable https://fontawesome.com/ icons
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
]

# https://pydata-sphinx-theme.readthedocs.io/en/stable/
html_theme_options = {
    # https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/version-dropdown.html
    "switcher": {
        "version_match": version,
        "json_url": "https://raw.githubusercontent.com/brightway-lca/brightway-documentation/main/sphinx/source/_static/switcher.json",
    },
    "navbar_start": ["navbar-logo", "version-switcher"],
    "header_links_before_dropdown": 7,
    "announcement": "<p>This is the documentation for the legacy version of Brightway (=Brightway2). This version is compatible with the ActivityBroser user interface.</p>",
    "collapse_navigation": True,
    "footer_start": ["copyright"],
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
            "icon": "fab fa-brands fa-github",
        },
        {
            "name": "Conda",
            "url": "https://anaconda.org/cmutel/brightway2",
            "icon": "fab fa-brands fa-python",
        },
        {
            "name": "StackOverflow",
            "url": "https://stackoverflow.com/questions/tagged/brightway",
            "icon": "fab fa-brands fa-stack-overflow",
        },
        {
            "name": "Matrix",
            "url": "https://app.element.io/#/room/#brightway/community:matrix.org",
            "icon": "fab fa-regular fa-comments",
        }
    ],
    "logo": {
      "image_light": "source/_static/logo/BW_all_black_transparent_landscape.svg",
      "image_dark": "source/_static/logo/BW_all_white_transparent_landscape.svg"
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

