### path setup ####################################################################################

from glob import glob
import datetime
import os
 
### project information ###########################################################################

project = 'Brightway'
copyright = datetime.date.today().strftime("%Y") + ' Brightway Developers'

version = '2' # the short X.Y version.

### project configuration #########################################################################

needs_sphinx = '6.2.1'

extensions = [
    # native extensions
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.napoleon',
    'sphinx.ext.inheritance_diagram',
    # iPython extensions
    'IPython.sphinxext.ipython_directive',
    'IPython.sphinxext.ipython_console_highlighting',
    # Markdown support
    'myst_parser', # do not enable separately if using myst_nb, compare https://github.com/executablebooks/MyST-NB/issues/421#issuecomment-1164427544
    # Jupyter Notebook support
    'nbsphinx',
    # API documentation support
    'autoapi',
    # responsive web component support
    'sphinx_design',
    # custom 404 page
    'notfound.extension',
    # custom favicons
    'sphinx_favicon',
    # copy button on code blocks
    "sphinx_copybutton",
]

html_static_path = ['_static']
templates_path = ['_templates']
exclude_patterns = ['_build']
html_theme = "pydata_sphinx_theme"

# The root toctree document.
root_doc = 'index'

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
    #'imported-members',
    'show-inheritance-diagram'
]

autoapi_python_class_content = 'both'
autoapi_member_order = 'groupwise'
autoapi_root = 'source/api'
autoapi_keep_files = False

autoapi_dirs = [
    '../brightway2-io/bw2io',
    '../brightway2-data/bw2data',
    '../brightway2-calc/bw2calc',
    '../brightway2-analyzer/bw2analyzer'
]

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
    '.md': 'markdown'
}

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
]

## nbsphinx configuration ################################################

nbsphinx_execute = 'never'
nbsphinx_allow_errors = True

## sphinx-favicon configuration #########################################

favicons = [
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

## version-switcher configuration #######################################

version: str = 'latest'

## html configuration ###################################################

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

html_css_files = [
    "css/custom.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" # for https://fontawesome.com/ icons
]

html_sidebars = {
    "**": [
        "sidebar_grid_diataxis.html",
        "sidebar-nav-bs.html",
    ],
}

# https://pydata-sphinx-theme.readthedocs.io/en/stable/
html_theme_options = {
    "announcement": "<p>Register Now: <a href='https://2023.brightcon.link/'>Brightcon 2023 Community Conference & Hackathon</a> 📍 Luxembourg 🗓️ 16.-20.September</p>",
    # https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/version-dropdown.html
    "switcher": {
        "json_url": "https://raw.githubusercontent.com/brightway-lca/brightway-documentation/main/source/_static/switcher.json",
        "version_match": version
    },
    "navbar_start": ["navbar-logo", "version-switcher"],
    "header_links_before_dropdown": 7,
    "collapse_navigation": True,
    "footer_start": ["copyright"],
    "footer_end": ["footer"],
    "show_prev_next": False,
    "use_edit_page_button": True,
    "secondary_sidebar_items": ["page-toc", "edit-this-page", "sourcelink", "support"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/brightway-lca",
            "icon": "fab fa-brands fa-github",
        },
        {
            "name": "Conda",
            "url": "https://anaconda.org/cmutel/brightway25",
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
      "image_light": "BW_all_black_transparent_landscape.svg",
      "image_dark": "BW_all_white_transparent_landscape.svg"
    },
}

# required by html_theme_options: "use_edit_page_button"
# and
# To build urls withoug hard-coding them
html_context = {
    # "github_url": "https://github.com", # or your GitHub Enterprise site
    "github_user": "brightway-lca",
    "github_repo": "brightway-documentation",
    "github_version": "main",
    "doc_path": "source",
    "read_the_docs_build": os.getenv('READTHEDOCS', False),
    "read_the_docs_version": os.getenv('READTHEDOCS_VERSION', None),
}
