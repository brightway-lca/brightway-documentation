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

1. Clone this repository (use `git clone --recursive`, because the repository has submodules. See below).
2. Set up a Python virtual environment that includes all packages required to build the documentation. A [Conda `yaml` file](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) is provided [for convenient setup](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) at [``setup/conda_environment.yml``](setup/conda_environment.yml). Install the environment by running from the repository root directory:

```
conda env create -f 'setup/conda_environment.yml'
```

and activate the environment:

```
conda activate sphinx
```
3. [Build the documentation](https://www.sphinx-doc.org/en/master/usage/quickstart.html) (manually). To trigger the build manually, run [`sphinx-build`](https://www.sphinx-doc.org/en/master/man/sphinx-build.html) from the repository root directory:

```
sphinx-build sphinx _build/html -b singlehtml -a
```

| positional argument or option| value | description |
| ---------------------------- | ----- | ----------- |
| sourcedir | `./sphinx` | N/A |
| outdir | `./_build/html` | N/A |
| -b | `singlehtml` | create only a single html page |
| -a | N/A | always write all output files |

and preview the documentation by opening:

```
_build/html/index.html
```

4. [Build the documentation](https://www.sphinx-doc.org/en/master/usage/quickstart.html) (automatically): For automatic builds, providing a live preview of changes, run [`sphinx-autobuild`](https://github.com/executablebooks/sphinx-autobuild) from the repository root directory:

```
sphinx-autobuild sphinx _build/html -a
```

| positional argument or option| value | description |
| ---------------------------- | ----- | ----------- |
| sourcedir | `./sphinx` | N/A |
| outdir | `./_build/html` | N/A |
| -a | N/A | always write all output files |


This will start watching all changes in the `./sphinx` directory and provide a live html preview of the Sphinx documentation at http://127.0.0.1:8000/.

5. Push changes to the documentation website `documentation.brightway.dev`. The site is based on `readthedocs.org`, which triggers it own builds of the documentation. A new build is triggered with every merge into the `master` branch of this repository.

## 📁 `git` submodules

### clonning

If you are **clonning for the first time the repository**, clone it with:

```
# for ssh based clonning
git clone --recursive git@github.com:brightway-lca/brightway-documentation.git
```
or
```
# for https based clonning
git clone --recursive https://github.com/brightway-lca/brightway-documentation.git
```
If you already have a working copy of the repository, update your copy with:

```
git submodule update --init
```
### updating

If you have set up the submodules, you can update the repository with pull like you would normally do.
**To pull everything including the submodules**, add `--recurse-submodules` to `git pull`

```
# pull the changes in the brightway documentation repo and changes in the submodules
git pull --recurse-submodules
```

**To pull the changes in the submodules only**, use:
```
# pull the changes in the submodules
git submodule update --remote
```

## 📚 References

Compare the `sphinx`:

1. [documentation](https://www.sphinx-doc.org/en/master/)
2. [getting started (from readthedocs)](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html)
3. [issues on GitHub](https://github.com/sphinx-doc/sphinx/issues)

Compare the `readthedocs.org`:

1. [documentation](https://docs.readthedocs.io/en/stable/index.html)
2. [tutorial](https://docs.readthedocs.io/en/stable/tutorial/)
3. [issues on GitHub](https://github.com/readthedocs/readthedocs.org/issues)
