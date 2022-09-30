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
2. install the `sphinx` Python package and other required packages (themes, etc.). A template conda yaml file is provided [for convenient environment setup](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) at

```
setup/sphinx_environment.yml
```

3. edit content or add new files
4. [build the documentation](https://www.sphinx-doc.org/en/master/usage/quickstart.html) by running from within the `sphinx` directory:

```
make clean html
```

5. preview the documentation by opening

```
_build/html/index.html
```

6. the `documentation.brightway.dev` site is based on `readthedocs.org`, which triggers it own builds of the documentation. a new build is triggered with every merge into the `master` branch of this repository.

## 📚 References

Compare the `sphinx`:

1. [documentation](https://www.sphinx-doc.org/en/master/)
2. [getting started (from readthedocs)](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html)
3. [issues on GitHub](https://github.com/sphinx-doc/sphinx/issues)

Compare the `readthedocs.org`:

1. [documentation](https://docs.readthedocs.io/en/stable/index.html)
2. [tutorial](https://docs.readthedocs.io/en/stable/tutorial/)
3. [issues on GitHub](https://github.com/readthedocs/readthedocs.org/issues)