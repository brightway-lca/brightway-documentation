# Contributing to the Documentation

## Building the Documentation

The Brightway documentation is built and published automatically by the readthedocs.org service on every push/merge to the `main` branch of the `brightway-documentation` repository.

To preview your changes, build the documentation locally by following the [instructions in the repository readme](https://github.com/brightway-lca/brightway-documentation).

## Technical Setup Information

### Repository Structure

The content of the Brightway documentation is stored in the `source/content` folder of the `brightway-documentation` repository. The homepage is located in `source/content/index.md`. The `source/conf.py` file contains the configuration for the documentation build.

```
.
├── environment.yml
├── source/
│   ├── conf.py
|   ├── index.md
│   └── content/
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

## Contributing to the Brightway Documentation

```{warning}
The processing of all requests is handled on a best-effort basis by the community of Brightway developers.
```
### Option 1: Request Changes or Report Errors

[Create a new discussion in the `ideas` section of the `brightway-documentation` repository](https://github.com/brightway-lca/brightway-documentation/discussions/categories/ideas), detailing your request and all relevant information.

### Option 2: Contribute Changes

::::{tab-set}

:::{tab-item} Simple

```{note}
This is recommended for Brightway users with limited experience in software development and version control tools.
```

```{admonition} Prerequisites
1. basic knowledge of GitHub (issues, discussions, etc.)
2. basic [knowledge of Markup](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
```

1. Prepare your contribution using the Markdown (`.md`) syntax and save it to a single file.
2. [Start a new discussion in the `ideas` section of the `brightway-documentation` repository](https://github.com/brightway-lca/brightway-documentation/discussions/categories/ideas) and attach the Markdown file to the discussion. The discussion must include the intended location of your page in the Brightway documentation.
3. A member of the Brightway developers community will integrate your contribution into the documentation.

:::

:::{tab-item} Advanced

```{note}
This is recommended for Brightway users with experience in software development and version control tools. The technical infrastructure of the Brightway documentation is detailed on the Contributing Guide pages for the [General Documentation](contributing_general_documentation.md) and the [API Documentation.](contributing_api_documentation.md)
```

```{admonition} Prerequisites
1. knowledge of GitHub (pull-requests, etc.)
2. [knowledge of Markup](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
3. [knowledge of reStructured Text](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
4. basic [knowledge of Sphinx](https://www.sphinx-doc.org/en/master/usage/quickstart.html)
```

1. Fork the [`brightway-documentation`](https://github.com/brightway-lca/brightway-documentation/) repository.
2. Add your contributions and build the documentation locally (compare the [repository readme](https://github.com/brightway-lca/brightway-documentation/))
3. Open a pull request
4. A member of the Brightway developers community will merge your contribution into the main branch of the documentation repository. Your changes will be published to the documentation website automatically following the successful merge.

:::

::::