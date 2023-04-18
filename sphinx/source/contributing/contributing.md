# Contributing

## Contributing to the Brightway Code

If you would like to contribute to the development of Brightway, follow the usual GitHub process: Fork the [relevant Brightway repository on GitHub](https://github.com/brightway-lca), make your changes and open a pull request with your changes. The Brightway project has adopted the [Contributor Covenant](https://www.contributor-covenant.org/).

## Contributing to the Brightway Documentation

```{warning}
The processing of all requests is handled on a best-effort basis by the community of Brightway developers.
```
### Option 1: Request Changes

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
4. A member of the Brightway developers community will merge your contribution into the main branch of the documentation repository. Your changes will be published on by the readthedorcs.org service following the successful merge.

:::

::::


```{toctree}
---
hidden:
maxdepth: 1
---
self
contributing_general_documentation
contributing_api_documentation
```