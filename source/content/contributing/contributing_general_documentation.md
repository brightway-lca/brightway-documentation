# Instructions: General Documentation

## Building the Documentation

The Brightway documentation is built and published automatically by the readthedocs.org service on every push/merge to the `main` branch of the `brightway-documentation` repository.

To preview your changes, build the documentation locally by following the [instructions in the repository readme](https://github.com/brightway-lca/brightway-documentation).

## Technical Setup Information

### Repository Structure

The content of the Brightway documentation is stored in the `source/content` folder of the `brightway-documentation` repository. The homepage is located in `source/content/index.md`. The `source/conf.py` file contains the configuration for the documentation build.

```
.
├── setup/
│   └── environment.yml
├── source/
│   ├── conf.py
│   └── content/
│       ├── index.md
│       ├── setup/
│       ├── introduction/
│       └── (...other documentation sections)
├── README.md
├── brightway2-io/
├── brightway2-data/
└── (...other Brightway modules)
```
### Document Syntax

### Markdown (and reStructuredText)

The the different pages of the Brightway documentation are based on Markdown (`md`) files. The [MyST](https://myst-parser.readthedocs.io/en/latest/index.html) package is used to enable Markdown support across the project. The [`eval-rst` function](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html#syntax-directives-parsing) in MyST allows for use of arbitrary ReStructured Text (`rst`) directives in Markdown files. The [`sphinx-design`](https://sphinx-design.readthedocs.io/en/furo-theme/) package is used for advanced layout and interactive element support.

#### Jupyter Notebooks

The `myst-nb` package is being used to render Jupyter Notebooks in the documentation. This allows for the use of Jupyter Notebooks as a documentation format. The notebooks are stored in the `notebooks` folder in the `brightway-documentation` repository. Curtrently, the notebooks are not executed during the build process. Any markdown cell in a notebook supports the features of the `myst-parser`, including admonitions, `eval-rst` directives, and `myst` directives.