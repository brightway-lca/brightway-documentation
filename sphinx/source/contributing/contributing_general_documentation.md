# Instructions: General Documentation

## Document Syntax

### Markdown (and reStructuredText)

The majority of the Brightway documentation is based on Markdown (`.md`) files. The [MyST](https://myst-parser.readthedocs.io/en/latest/index.html) package is used to enable Markdown support across the project. The [`eval-rst` function](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html#syntax-directives-parsing) in MyST allows for use of arbitrary `rst` directives in Markdown files.  The [`sphinx-design`](https://sphinx-design.readthedocs.io/en/furo-theme/) package is used for advanced layout and interactive element support. Wherever necessary, reStructuredText (`.rst`) files or directives can also be used. 

### Jupyter Notebooks

The `myst-nb` package is being used to render Jupyter Notebooks in the documentation. This allows for the use of Jupyter Notebooks as a documentation format. The notebooks are stored in the `notebooks` folder in the `brightway-documentation` repository. Curtrently, the notebooks are not executed during the build process. Any markdown cell in a notebook supports the features of the `myst-parser`, including admonitions, `eval-rst` directives, and `myst` directives.

## Building the Documentation

The Brightway documentation is built and published automatically by the readthedocs.org service on every push/merge to the `main` branch of the `brightway-documentation` repository. To preview your changes, build the documentation locally by following the [instructions in the repository readme](https://github.com/brightway-lca/brightway-documentation).

## Technical Setup Information

The content of the Brightway documentation is stored in the `sphinx/source` folder of the `brightway-documentation` repository. The homepage is located in `sphinx/source/index.md`. The `sphinx/source/conf.py` file contains the configuration for the documentation build.

```
.
├── setup/
│   └── environment.yml
├── sphinx/
│   └── source/
│       ├── conf.py
│       ├── index.md
│       ├── setup/
│       ├── introduction/
│       └── (...other documentation sections)
├── README.md
├── brightway2-io/
├── brightway2-data/
└── (...other brightway2 modules)
```