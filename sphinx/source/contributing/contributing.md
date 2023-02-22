# Contributing: Getting Started

[![contributions welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg?style=flat&logo=GitHub)](https://github.com/brightway-lca/brightway-documentation)

## Contributing to Brightway

If you would like to contribute to the development of Brightway, follow the usual GitHub process: Fork the [relevant Brightway repository on GitHub](https://github.com/brightway-lca), make your changes and open a pull request with your changes. The Brightway project has adopted the [Contributor Covenant](https://www.contributor-covenant.org/).

## Contributing to the Documentation

```{note}
To start contributing, check out the [main discussion page of the new documentation](https://github.com/brightway-lca/brightway-documentation/discussions/41). It includes the proposed table of contents, a list of pages that need to be written, and a list of pages that need to be updated.
```

There are two ways you can contribute to the documentation of Brightway:

### 1. Request new Documentation

[Start a discussion in the `ideas` section of the `brightway-documentation` repository](https://github.com/brightway-lca/brightway-documentation/discussions/categories/ideas), detailing your request and all relevant information.

```{note}
The processing of these requests are handled on a best-effort basis by the community of Brightway developers.
```

### 2. Contribute new Documentation

::::{tab-set}

:::{tab-item} Simple

This is recommended for Brightway users with limited experience in software development and version control tools.

```{admonition} Prerequisites
1. basic knowledge of GitHub (issues, discussions, etc.)
2. basic [knowledge of Markup](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
```
1. In the [main discussion page of the new documentation](https://github.com/brightway-lca/brightway-documentation/discussions/41), find a page that needs to be written or updated. Add yourself as a contributor to the relevant column of that page.
2. Write your contribution using the Markdown (`.md`) syntax and store it in a single file.
3. [Start a discussion in the `ideas` section of the `brightway-documentation` repository](https://github.com/brightway-lca/brightway-documentation/discussions/categories/ideas) and attach the Markdown file to the discussion. The discussion must include the intended location of your page in the Brightway documentation.
4.  A member of the Brightway developers community will integrate your contribution into the documentation.

```{note}
The processing of these requests are handled on a best-effort basis by the community of Brightway developers.
```

:::

:::{tab-item} Advanced

This is recommended for Brightway users with experience in software development and version control tools. The technical infrastructure of the Brightway documentation is [detailed on the Brightway Documentation Technical Infrastructure page.](documentation.md)

```{admonition} Prerequisites
1. knowledge of GitHub (pull-requests, etc.)
2. [knowledge of Markup](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
3. [knowledge of reStructured Text](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
4. basic [knowledge of Sphinx](https://www.sphinx-doc.org/en/master/usage/quickstart.html)
```

1. In the [main discussion page of the new documentation](https://github.com/brightway-lca/brightway-documentation/discussions/41), find a page that needs to be written or updated. Add yourself as a contributor to the relevant column of that page.
2. Fork the [`brightway-documentation`](https://github.com/brightway-lca/brightway-documentation/) repository.
3. Add your contributions and build the documentation locally (compare the [repository readme](https://github.com/brightway-lca/brightway-documentation/))
4. Open a pull request
5. A member of the Brightway developers community will merge your contribution into the main branch of the documentation repository. Your changes will be published on by the readthedorcs.org service following the successful merge.

:::

::::

## Contacting the Developers

[![Mailing List](https://img.shields.io/badge/Community-Mailing%20List-blue.svg?style=flat&logo=Minutemailer&logoColor=white)](https://brightway.groups.io/)
[![Gitter](https://img.shields.io/badge/Community-Chat-ed1965.svg?style=flat&logo=Gitter&logoColor=white)](https://gitter.im/brightway-lca/community)
[![SO](https://img.shields.io/badge/Community-Questions-f48024.svg?style=flat&logo=Stack%20Overflow&logoColor=white)](https://stackoverflow.com/questions/tagged/brightway)


```{toctree}
---
hidden:
maxdepth: 1
---
self
documentation
api_documentation
```