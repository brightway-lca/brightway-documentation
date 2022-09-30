# Brightway Documentation (Sphinx/readthedocs.org)

[![Join the chat at https://gitter.im/brightway-lca/documentation](https://badges.gitter.im/brightway-lca/documentation.svg)](https://gitter.im/brightway-lca/documentation?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/brightway-lca/brightway-documentation-readthedocs/discussions)

## ⁉️ FAQ

_"Where can I find more beginner-friendly documentation?"_ \
The interactive training part of the documentation is at [`training.brightway.dev`](https://training.brightway.dev/).

_"How can I contribute to the documentation?"_ \
If you are familiar with [Sphinx](https://www.sphinx-doc.org/en/master/), you can add your changes to a fork of this repo and open a pull request. \
If you would rather get help from a developer, please [start a new discussion here](https://github.com/brightway-lca/brightway-documentation/discussions). Your suggestions/additions will be added for you.

_"Where can I get help beyond the documentation?"_ \
Use the Gitter channel linked above.

## ☑️ Instructions

1. clone the repository
2. install the `sphinx` Python package and other required packages (themes, etc.). A template conda environment yaml file is provided for convenience at

```
setup/sphinx_environment.yml
```

3. edit content or add new files
4. [build the documentation](https://www.sphinx-doc.org/en/master/usage/quickstart.html) by running, from within the repository root

```
make html
```

6. preview the documentation by opening

```
_build/html/index.html
```

## 📚 References

Compare the `sphinx`:

1. [documentation](https://jupyterbook.org/en/stable/intro.html)
2. [feature requests queue](https://executablebooks.org/en/latest/feature-vote.html)
3. [discussions on GitHub](https://github.com/orgs/executablebooks/discussions)

Compare the `readthedocs.org`:

1. [documentation](https://jupyterbook.org/en/stable/intro.html)
2. [feature requests queue](https://executablebooks.org/en/latest/feature-vote.html)
3. [discussions on GitHub](https://github.com/orgs/executablebooks/discussions)