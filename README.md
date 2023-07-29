# Brightway Documentation (Sphinx/readthedocs.org)

[![Brightway](https://img.shields.io/static/v1?label=Brightway&message=ecosystem&color=45bfb0&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA2NSIgaGVpZ2h0PSI2OTAiIHZlcnNpb249IjEuMSIgdmlld0JveD0iMCAwIDEwNjUgNjkwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogPGRlZnM+CiAgPGNsaXBQYXRoIGlkPSJjbGlwUGF0aDIxNzMiPgogICA8cGF0aCBkPSJtLTU5NSA0NDBoMWUzdi0xZTNoLTFlM3oiLz4KICA8L2NsaXBQYXRoPgogPC9kZWZzPgogPGcgdHJhbnNmb3JtPSJtYXRyaXgoMS4zIDAgMCAtMS4zIDY1MyA0MDMpIiBjbGlwLXBhdGg9InVybCgjY2xpcFBhdGgyMTczKSIgZmlsbD0iI2ZmZiI+CiAgPHBhdGggZD0ibTAgMGMwLTEuMi0xLjUtMy40LTAuNDctNS4yIDEuMy0yLjQgNS40LTEuNSA1LjgtM3YtMC4wMThsLTQuNy0wLjA1NC0yLTQuMWMtMS45IDAuNzEtMi40IDMuMi0zLjIgNi42LTAuNDQgMi0wLjcxIDMuNCAwLjA4OSA0LjctMTQtMy4zLTMwLTUuNC00NS01LjQtNDkgMC4wMzYtNzEgMTctMTA3IDI0IDEuNS0xLjEgMi43LTMuMyAyLjEtNC45bC02LjEgMi4yLTQtMy4xYy0xLjQgMS40LTAuNTggMi44LTIuMiA0LjgtMi4xIDIuNS01LjMgMi42LTUuMiAzIDAuODctMC4wNzIgMS43LTAuMTQgMi42LTAuMjItMS42IDAuMjQtMi41IDAuNC0yLjYgMC4yMi0zLjkgMC4zMS04IDAuNDktMTIgMC41MS02NiAwLjIyLTEwMi00Mi0xMjItNzkgMy42IDIuOSA4LjcgMS41IDEwIDEuMSA0LjItMS4xIDguOC00LjEgOC40LTYuMWwtNC41LTEuNSAwLjUyLTAuNTRjLTAuMjItMC4wMTktMC40My0wLjAxOS0wLjY1LTAuMDE5LTQuMiAwLjA1NS01LjEgMy45LTkuMiA0LjItMy44IDAuMjktNi40LTIuNy03LjItMS45LTEzLTI3LTE4LTUwLTE4LTUwaC0zNHM2LjcgMzQgMzAgNjhjLTEuNiAxIDEgNS0xLjEgOC4zLTIuNSAzLjgtOC40IDIuNC04LjggNC41LTAuMDE4IDAuMTMtMC4wMzYgMC4yNSAwIDAuMzhsNy4yLTAuNTIgMi41IDUuNWMxLjEtMC40IDItMS43IDMuOS00LjIgMS40LTEuOCAyLjQtMy4yIDMuMS00LjMgMjYgMzQgNjkgNjcgMTM5IDY3IDIuNSAwIDUtMC4wNzMgNy40LTAuMi0wLjU4IDIuMSA1IDMuNSA1LjcgOC4xIDAuNzQgNC44LTQuNyA3LjgtMy40IDEwIDAuMDE4IDAuMDE4IDAuMDM2IDAuMDU0IDAuMDU0IDAuMDcybDUuOC00LjQgNC43IDMuMWMwLjU2LTAuODcgMC42My0xLjctMC40NS04LTEuNC04LjItMS45LTktMi43LTkuNyA0MS01LjIgNjgtMjggMTE4LTI5IDE1LTAuNTQgMzAgMC43OCA0NCAzLjEtMC4yNyAwLjE2LTAuNTIgMC4zNi0wLjc2IDAuNjItMSAxLjEtMS4xIDMuMS0xLjQgNy4xLTAuMjUgNC4zLTAuNCA2LjYgMC40MiA3LjdsMi44LTMuMiAzLjIgMS4yYzAuMDM2LTAuMDcyIDAuMDU0LTAuMTYgMC4wNzItMC4yNCAwLjQ0LTEuOC0xLjEtMi43LTEuMS01LjYgMC0zLjUgMi4zLTQuOSAxLjgtNi41LTAuMDM2LTAuMDktMC4wNzItMC4xOC0wLjExLTAuMjUgNDUgOC43IDc4IDI4IDc5IDI4IDAtMC42My0zNS0yMi03OS0zM20tMzMyLTMwLTU1IDQuMS0zNSA0MC0xNyAyOC0xNSAyNC05LjcgMjctMjYgMTYgMzgtOS40IDM5LTI0IDMxLTI4IDI3LTM5IDE5LTMzem00MTEgNjUgMTEgNzkgNTcgNDYgNjggOS4zIDQ1LTAuMzkgNDcgMTYtMTYtMzYtMTMtMzQtMjQtNTgtMzItNDktMzktMjAtNDMgMy43em04OC0yNDktMTggMzItMjEgMjYtMzUgMzQtMjEgMjYtMjAgMjItMzcgNDgtMTcgMjAgNzAgMC44NyA1Ni00OSAyMi00MCAxNS0zNyAyLjgtMzJ6bTAgMC0xNyAxNy0zOSA2LjItNDQgMTMtNTAgMzMtMzAgNTUtMy4zIDUzIDEzIDI3IDEuOSAzLjcgMTctMjAgMzctNDggMjAtMjIgMjEtMjYgMzUtMzQgMjEtMjZ6bS05MSAzNDgtMTYtNTctMzEtNDYtMzMtMTIgMC4xNSAzLjkgMS42IDQ0IDQuNCAzNiA1LjEgMzQgNC4zIDQwIDIgMzQgMi4zIDM2IDEzIDQyIDQuNS0zNyAxNi0yMiAyMC0zN3ptLTQ3IDE1NC0xMy00Mi0yLjMtMzYtMi0zNC00LjMtNDAtNS4xLTM0LTQuNC0zNi0xLjYtNDQtMC4xNS0zLjktMi44IDMuMi00OCA1NS03LjIgMzcgMC43OCA2NCAyNiA0OCAzMyAyOXptLTE0NS0zOTktMjAgNDMtMTIgNDEtNi4xIDI0LTYuNyAyMCA1OC0yMSAxNS0yNiAxNi00NC00LjItMzctMTItNjEtNS4yIDI0em0yOC02MS0yNyAxOS0yMCAxMS0yOCAyMC0zMSAzMC02LjggNDggMTcgNDIgMjQgMTggMS41LTQuNiA1LjItMTYgNi4xLTI0IDEyLTQxIDIwLTQzIDIyLTM3em0tMTEgMzA1LTE4LTUxLTUyLTM0LTAuMjUgNS44LTAuODMgMTkgMS4yIDM5LTMuMSA0My02LjcgMzgtMTEgNDYtMTUgNjMgMjAtMjUgNDMtNDEgMzAtNDl6bS03MC03OSAwLjI1LTUuOC01NiA0Mi0xNyA2NSAyLjcgNTAgOS40IDQwIDE2IDE3IDguNCA0MCAxNS02MyAxMS00NiA2LjctMzggMy4xLTQzLTEuMi0zOXptLTU0LTE5NC0xMiAyMC0yMiAyNi0xOCAxNS0xNyAxNy0wLjEzLTAuNTYtOS43LTQ1IDIxLTM0IDIzLTEzIDIxLTguMiAzNy0xOS0xNSAxM3ptMjQtNDEtMTUgMTMtOC4zIDI4LTEyIDIwLTIyIDI2LTE4IDE1LTE3IDE3IDQyIDE0IDI0LTQuOCAxNS0xNiA4LjYtMzMgMS41LTI4LTMuNC0yMHptLTExMCAyMDItMjMtNTEtMi44IDQuOS0xOSAzMy0yNyAzOS0zMSAyOC0zOSAyNC0zOCA5LjQgMzIgMS4zIDMxIDEuNiAzMC0wLjI5IDQzLTE2IDMwLTMweiIvPgogPC9nPgo8L3N2Zz4K)](https://github.com/brightway-lca)
![License](https://img.shields.io/github/license/brightway-lca/brightway-documentation?color=green&logo=Open%20Source%20Initiative&logoColor=white)

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat&logo=GitHub)](https://github.com/brightway-lca/brightway-documentation-readthedocs/discussions)
![Read the Docs](https://img.shields.io/readthedocs/brightway-documentation?logo=Read%20the%20Docs)

The primary documentation for the Brightway life-cycle assessment software package. Sphinx and readthedocs.org are used to build/host the documentation.

| static documentation | interactive documentation | development playground |
| ---- | ------------- | ------------- |
| [docs.brightway.dev](https://github.com/brightway-lca/brightway-documentation) | [learn.brightway.dev](https://github.com/brightway-lca/brightway-learn) | [hub.brightway.dev](https://github.com/brightway-lca/brightway-hub) | 

## Repository Structure

Brightway modules are split up into different repositories (`brightway-2-analyzer`, `brightway2-calc`, etc.). These repositories are included as [`git submodules`](https://git-scm.com/book/en/v2/Git-Tools-Submodules) in this repository in order to e.g. enable Sphinx to build a combined changelog page.

## Sphinx/readthedocs.org Structure

All content pages of the documentation are Markdown formatted for reasons of simplicity. The API documentation is build from source automatically by the readthedocs.org Sphinx extension [`AutoAPI`](https://sphinx-autoapi.readthedocs.io/en/latest/).

## Quickstart

### Setup Repository

1. Clone this repository:

```bash
git clone https://github.com/brightway-lca/brightway-documentation.git
```

2. Initialize (=download) the submodules (`brightway-2-analyzer`, `brightway2-calc`, etc.):

```bash
git submodule update --init --recursive --remote --force
```

| option | description |
| ---------------------------- | ----------- |
| init | initializes (=downloads) submodules if not currently present |
| recursive | goes through all submodules specified in the `.gitmodules` file |
| remote | points to the latest commit on the branches specified in the `.gitmodules` file |
| force | ensures that accidental edits in the submodules are always overwritten |

Note that if the `--remote` flag is not set, the submodules will point to the latest commit on the default branches (`main`), **not** to the latest commit on the branches specified in the `.gitmodules` file. On the `main` branch of the `brightway-documentation` repo, all submodule branches specified in the `.gitmodules` should be `main`. This is to ensure the documentation is always up-to-date with the latest changes in the submodules.

To manually update the submodules, use the same command again. There is no need to push changes to the submodules to the remote, since [they are updated by GitHub Actions](https://documentation.brightway.dev/en/latest/source/contributing/documentation.html#github-actions).

### Setup Python Environment

Set up a Python virtual environment that includes all packages required to build the documentation. A [Conda environment file](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) is provided [for convenient setup](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file). The file is located at [``./environment.yml``](environment.yml). Install the environment `sphinx` by running from the repository root directory:

```bash
conda env create -f 'environment.yml'
```

and activate the environment:

```bash
conda activate sphinx
```

You are now ready to build the documentation...

### Building the Documentation

1. You can build the documentation by __triggering every build manually__: To trigger the build, run [`sphinx-build`](https://www.sphinx-doc.org/en/master/man/sphinx-build.html) from the repository root directory:

```bash
sphinx-build source _build/html -b singlehtml -a
```

| option | value | description |
| ---------------------------- | ----- | ----------- |
| sourcedir | `source` | N/A |
| outdir | `_build/html` | N/A |
| -b | `singlehtml` | create only a single html page |
| -a | N/A | always write all output files |
| `-j` | `auto` | [speed up build by using multiple processes](https://www.sphinx-doc.org/en/master/man/sphinx-build.html#cmdoption-sphinx-build-j) |


You can now preview the documentation, built as a single html page at:

```
_build/html/homepage.html
```

2. You can also build the documentation by automatically triggering a build after every change to the source files, providing a "live" preview of changes. To trigger the automated builds, run [`sphinx-autobuild`](https://github.com/executablebooks/sphinx-autobuild) from the repository root directory:

```bash
sphinx-autobuild source _build/html -a -j auto --open-browser
```

| positional argument or option| value | description |
| ---------------------------- | ----- | ----------- |
| sourcedir | `source` | N/A |
| outdir | `_build/html` | N/A |
| `-a` | N/A | always write all output files |
| `-j` | `auto` | [speed up build by using multiple processes](https://www.sphinx-doc.org/en/master/man/sphinx-build.html#cmdoption-sphinx-build-j) |
| `--open-browser` | N/A | automatically open browser |


You can now preview the documentation at (the browser window will open automatically ✨):
http://127.0.0.1:8000/

### Checking for Dead External Links

The documentation contains links to external websites. To check if these links are still valid, run the following command from the repository root directory:

```bash
sphinx-build -b linkcheck -D linkcheck_workers=20 source _build/linkcheck
```

| positional argument or option| value | description |
| ---------------------------- | ----- | ----------- |
| `-b` | `linkcheck` | [`linkcheck` builder](https://www.sphinx-doc.org/en/master/usage/builders/index.html#sphinx.builders.linkcheck.CheckExternalLinksBuilder) |
| `-D` | `linkcheck_workers=20`` | [number of links to check in paralell](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-linkcheck_workers) |
| sourcedir | `source` | N/A |
| outdir | `_build/linkcheck` | `_build/linkcheck/output.txt` contains a list of all broken or redirected links |

Internal links, if formatted according to [the `myst-parser` cross-referencing specifications](https://myst-parser.readthedocs.io/en/latest/syntax/cross-referencing.html#cross-references), are checked automatically during the regular build process.

### Contributing

Please follow the extensive guide we have provided [on the documentation website](https://documentation.brightway.dev/en/latest/source/contributing/contributing.html).

## 📚 References

Compare the `sphinx`:

1. [documentation](https://www.sphinx-doc.org/en/master/)
2. [getting started (from readthedocs)](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html)
3. [issues on GitHub](https://github.com/sphinx-doc/sphinx/issues)

Compare the `readthedocs.org`:

1. [documentation](https://docs.readthedocs.io/en/stable/index.html)
2. [tutorial](https://docs.readthedocs.io/en/stable/tutorial/)
3. [issues on GitHub](https://github.com/readthedocs/readthedocs.org/issues)