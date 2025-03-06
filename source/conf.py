### path setup ####################################################################################

import datetime
 
###################################################################################################
### Project Information ###########################################################################
###################################################################################################

project = 'Brightway'
copyright = datetime.date.today().strftime("%Y") + ' Brightway Developers'
version: str = 'latest' # required by the version switcher

###################################################################################################
### Project Configuration #########################################################################
###################################################################################################

needs_sphinx = '7.3.0'

extensions = [
    # core extensions
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.napoleon',
    # iPython extensions
    'IPython.sphinxext.ipython_directive',
    'IPython.sphinxext.ipython_console_highlighting',
    # Markdown support
    # 'myst_parser', # do not enable separately if using myst_nb, compare: https://github.com/executablebooks/MyST-NB/issues/421#issuecomment-1164427544
    # Mermaid diagram support
    "sphinxcontrib.mermaid",
    # Jupyter Notebook support
    'myst_nb',
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
    # hover-over tooltips for cross-references
    # 'hoverxref.extension', # currently no support for markdown as per https://github.com/readthedocs/sphinx-hoverxref/issues/250
    # powerful search engine
    "sphinx_docsearch",
]

root_doc = 'index'
html_static_path = ['_static']
templates_path = ['_templates']
exclude_patterns = [
    '_build',
    'source/content/api/*'
]
html_theme = "pydata_sphinx_theme"

suppress_warnings = [
    "myst.header", # suppress warnings of the kind "WARNING: Non-consecutive header level increase; H1 to H3"
]

napoleon_numpy_docstring = True

# https://myst-nb.readthedocs.io/en/v0.8.4/use/myst.html#parse-extensions-other-than-md-and-ipynb
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'myst-nb',
    '.ipynb': 'myst-nb',
    '.myst': 'myst-nb',
}

####################################################################################################
### Theme html Configuration #######################################################################
####################################################################################################

html_show_sphinx = False
html_show_copyright = True

html_css_files = [
    "css/custom.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" # for https://fontawesome.com/ icons
]

html_sidebars = {
    "**": [
        "sidebar-nav-bs.html",
    ],
    "content/contact/contact": [],
    "content/other/support": [],
    "content/other/credits": [],
}

html_theme_options = {
    "announcement": "<p>🌏 <a href='https://www.d-d-s.ch/schools/nov-25/'>REGISTER NOW</a>: 🇨🇭 Autumn School November 9 - 14 in Switzerland</p>",
    # https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/version-dropdown.html
    "switcher": {
        "json_url": "https://raw.githubusercontent.com/brightway-lca/brightway-documentation/main/source/_static/switcher.json",
        "version_match": version
    },
    # page elements
    "navbar_start": ["navbar-logo", "version-switcher"],
    "navbar_end": ["theme-switcher", "navbar-icon-links.html"],
    "footer_start": ["copyright"],
    "footer_end": ["footer"],
    "secondary_sidebar_items": ["page-toc", "edit-this-page", "sourcelink", "support"],
    "header_links_before_dropdown": 7,
    # page elements content
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/brightway-lca",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        },
        {
            "name": "PyPi",
            "url": "https://pypi.org/project/brightway25/#description",
            "icon": "fa-brands fa-python",
            "type": "fontawesome",
        },
        {
            "name": "Matrix Group Chat",
            "url": "https://app.element.io/#/room/#brightway/community:matrix.org",
            "icon": "fa-regular fa-comments",
            "type": "fontawesome",
        }
    ],
    # various settings
    "collapse_navigation": True,
    "show_prev_next": False,
    "use_edit_page_button": True,
    "navigation_with_keys": True,
    # https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/branding.html#different-logos-for-light-and-dark-mode
    "logo": {
        "text": "Brightway",
        "image_light": "_static/logo/BW_all_black_transparent_landscape.svg",
        "image_dark": "_static/logo/BW_all_white_transparent_landscape.svg"
    },
}

# required by html_theme_options: "use_edit_page_button"
html_context = {
    "github_user": "brightway-lca",
    "github_repo": "brightway-documentation",
    "github_version": "main",
    "doc_path": "source",
}

####################################################################################################
### Extension Configuration ########################################################################
####################################################################################################

# sphinx DocSearch configuration #########################################

# "exposed anyway", so we can just set the values here
# https://sphinx-docsearch.readthedocs.io/credentials.html

docsearch_app_id = "AB3D1FH6W0"
docsearch_api_key = "5f985eef1633581416cd50fb544ab61c"
docsearch_index_name = "brightway"

# copybutton Configuration ###############################################

copybutton_prompt_text = ">>>"

# linkcheck Configuration ###############################################
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder

linkcheck_retries = 1
linkcheck_workers = 20
linkcheck_exclude_documents = []

# notfound Configuration ################################################
# https://sphinx-notfound-page.readthedocs.io

notfound_context = {
    'title': 'Page Not Found',
    'body': '''                                                                                                                                           
        <h1>🍂 Page Not Found (404)</h1>
        <p>
        Oops! It looks like you've stumbled upon a page that's been recycled into the digital abyss.
        But don't worry, we're all about sustainability here.
        Why not take a moment to reduce, reuse, and recycle your clicks by heading back to the main page?
        And remember, every little bit counts in the grand scheme of things.
        </p>
    ''',
}

# autoapi Configuration ################################################
# https://sphinx-autoapi.readthedocs.io/en/latest/reference/config.html#customisation-options

autoapi_dirs = [
    '../brightway2-io/bw2io',
    '../brightway2-data/bw2data',
    '../brightway2-calc/bw2calc',
    '../brightway2-analyzer/bw2analyzer',
    '../brightway2-parameters/bw2parameters',
]

autoapi_ignore = [
    '*tests/*',
    '*tests.py',
    '*validation.py',
    '*version.py',
    '*.rst',
    '*.yml',
    '*.md',
    '*.json',
]

autoapi_options = [
    'members',
    'undoc-members',
    'private-members',
    'show-inheritance',
    'show-module-summary',
    #'special-members',
    #'imported-members',
    #'show-inheritance-diagram' # disabled due to https://github.com/brightway-lca/brightway-documentation/issues/162
]

graphviz_output_format = 'svg' # https://pydata-sphinx-theme.readthedocs.io/en/stable/examples/graphviz.html#inheritance-diagram

autoapi_python_class_content = 'both'
autoapi_member_order = 'groupwise'
autoapi_root = 'content/api'
autoapi_keep_files = True

autoapi_template_dir = '_templates/autoapi' # https://sphinx-autoapi.readthedocs.io/en/latest/how_to.html#how-to-customise-the-index-page

# myst_parser Configuration ############################################
# https://myst-parser.readthedocs.io/en/latest/configuration.html

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
    "attrs_block",
]

# myst-nb configuration ################################################
# https://myst-nb.readthedocs.io/en/latest/configuration.html

nb_execution_mode = 'off'

# sphinx-favicon configuration #########################################
# https://github.com/tcmetzger/sphinx-favicon

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

# hoverxref configuration ###############################################
# https://github.com/readthedocs/sphinx-hoverxref

"""

hoverxref_auto_ref = True
hoverxref_domains = ["py"]
hoverxref_role_types = dict.fromkeys(
    ["obj", "mod", "ref", "class", "func", "meth", "attr", "exc", "data"],
    "tooltip",
)
hoverxref_default_type = 'tooltip'
hoverxref_tooltip_lazy = False
"""
