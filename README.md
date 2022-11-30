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

1. Clone this repository recursively, thus populating all submodule directories

```
git clone https://github.com/brightway-lca/brightway-documentation.git --recursive
```

or, if the submodule directories are still empty, populate them with

```
git submodule update --init
```

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

`dependabot` is [set up to track changes in the submodule parent repositories](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file#registries):

```
.github/dependabot.yml
```

`dependabot` pull requests are [approved](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/automating-dependabot-with-github-actions#approve-a-pull-request) and [merged](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/automatically-merging-a-pull-request) automatically through GitHub actions.

[Automatically merging a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/automatically-merging-a-pull-request):

```
.github/workflows/dependabot_auto_approve.yml
.github/workflows/dependabot_auto_merge.yml
```

📚 [Getting started with GitHub actions](https://docs.github.com/en/actions/quickstart)


## 📚 References

Compare the `sphinx`:

1. [documentation](https://www.sphinx-doc.org/en/master/)
2. [getting started (from readthedocs)](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html)
3. [issues on GitHub](https://github.com/sphinx-doc/sphinx/issues)

Compare the `readthedocs.org`:

1. [documentation](https://docs.readthedocs.io/en/stable/index.html)
2. [tutorial](https://docs.readthedocs.io/en/stable/tutorial/)
3. [issues on GitHub](https://github.com/readthedocs/readthedocs.org/issues)