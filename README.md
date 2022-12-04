# Brightway Documentation (Sphinx/readthedocs.org)

[![Read the Docs](https://readthedocs.org/projects/brightway-documentation/badge/?version=latest)](https://brightway-documentation.readthedocs.io/en/latest/)
[![Dependabot auto-approve](https://github.com/brightway-lca/brightway-documentation/actions/workflows/dependabot_auto_approve.yml/badge.svg)](https://github.com/brightway-lca/brightway-documentation/actions/workflows/dependabot_auto_approve.yml)
[![Dependabot auto-merge](https://github.com/brightway-lca/brightway-documentation/actions/workflows/dependabot_auto_merge.yml/badge.svg)](https://github.com/brightway-lca/brightway-documentation/actions/workflows/dependabot_auto_merge.yml)



[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/brightway-lca/brightway-documentation-readthedocs/discussions)
[![Join the chat at https://gitter.im/brightway-lca/documentation](https://badges.gitter.im/brightway-lca/documentation.svg)](https://gitter.im/brightway-lca/documentation?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![icense](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)



## Quickstart

### Setup

1. Clone this repository [recursively, thus populating all submodule directories](https://git-scm.com/book/en/v2/Git-Tools-Submodules):

```
git clone https://github.com/brightway-lca/brightway-documentation.git --recursive
```

If you cloned the repository and the submodule directories (`brightway-2-analyzer`, `brightway2-calc`, etc.) are still empty, populate them with:

```
git submodule update --init
```

2. Ensure the submodule directories are up-to-date:

```
git pull --recurse-submodules
```

> They are updated automatically on the remote by [Dependabot](https://github.com/dependabot) + [GitHub Actions](https://github.com/features/actions), so there is no need to push changes to the submodules to the remote.

3. Set up a Python virtual environment that includes all packages required to build the documentation. A [Conda `yaml` file](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) is provided [for convenient setup](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) at [``setup/conda_environment.yml``](setup/conda_environment.yml). Install the environment by running from the repository root directory:

```
conda env create -f 'setup/conda_environment.yml'
```

and activate the environment:

```
conda activate sphinx
```

### Documentation Build

1. You can build the documentation by __triggering every build manually__: To trigger the build, run [`sphinx-build`](https://www.sphinx-doc.org/en/master/man/sphinx-build.html) from the repository root directory:

```
sphinx-build sphinx _build/html -b singlehtml -a
```

| positional argument or option| value | description |
| ---------------------------- | ----- | ----------- |
| sourcedir | `./sphinx` | N/A |
| outdir | `./_build/html` | N/A |
| -b | `singlehtml` | create only a single html page |
| -a | N/A | always write all output files |

You can now preview the documentation, built as a single html page at:

```
_build/html/index.html
```

1. You can build the documentation by triggering a build after every change to the source files, providing a "live" preview of changes. To trigger the automated builds, run [`sphinx-autobuild`](https://github.com/executablebooks/sphinx-autobuild) from the repository root directory:

```
sphinx-autobuild sphinx _build/html -a
```

| positional argument or option| value | description |
| ---------------------------- | ----- | ----------- |
| sourcedir | `./sphinx` | N/A |
| outdir | `./_build/html` | N/A |
| -a | N/A | always write all output files |


You can now preview the documentation at:
http://127.0.0.1:8000/

### Contributing

1. Fork this repository, create an aptly named branch and add your contributions.
2. Open a pull request and tag Brightway contributors.
3. Your changes will go live at https://documentation.brightway.dev after your branch is merged into main.

## 📚 References

Compare the `sphinx`:

1. [documentation](https://www.sphinx-doc.org/en/master/)
2. [getting started (from readthedocs)](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html)
3. [issues on GitHub](https://github.com/sphinx-doc/sphinx/issues)

Compare the `readthedocs.org`:

1. [documentation](https://docs.readthedocs.io/en/stable/index.html)
2. [tutorial](https://docs.readthedocs.io/en/stable/tutorial/)
3. [issues on GitHub](https://github.com/readthedocs/readthedocs.org/issues)
