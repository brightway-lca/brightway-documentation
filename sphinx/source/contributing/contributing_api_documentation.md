# Contribution Guide: API Documentation

## Style Guidelines

Brightway has adopted the [NumPy Docstring Style](https://numpydoc.readthedocs.io/en/latest/format.html), which is most famously used by the documentation of the [Pandas](https://pandas.pydata.org/docs/reference/index.html) and [NumPy](https://numpy.org/doc/stable/reference/index.html) packages. Its use in all Brightway documentation is mandatory. Using the full extend of the NumPy Docstring Style, including the `Examples`, `Raises`, `See Also`, `Notes`, and `References` sections, is encouraged.

## Tutorial

:::{note}
This tutorial demonstrates how to contribute to the API documentation of the `brightway2-io` package. All steps are equivalent for other Brightway packages (`brightway2-data`, `brightway2-calc`, etc.).
:::

::::{tab-set}

:::{tab-item} Make and Preview your Changes

1. Clone the `brightway-documentation` repo.
2. Fork the `brightway2-io` repo and create a new branch `documentation_improvements`.
3. Make the desired changes to the docstrings on the branch `documentation_improvements` in your fork of the `brightway2-io` repo.

You can now preview your changes:

1. Edit the file `.gitmodules` in the `brightway-documentation` repo to reflect your fork of the `brightway2-io` repo by changing the `<username>` in the `url` field:

```git
[submodule "brightway2-io"]
	path = brightway2-io
	url = https://github.com/<username>/brightway2-io
	branch = documentation_improvements
```

1. Point the `brightway2-io` submodule to your fork of the `brightway2-io` repo. Repeat whenever you have made changes to the docstrings in your fork of the `brightway2-io` repo:

```bash
git submodule update --init --recursive --remote --force
```

3.  Follow [the instructions in the readme](https://github.com/brightway-lca/brightway-documentation) to build the documentation locally. You can now preview your changes.

```{note}
[Git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) offer a convenient way to include the documentation of other Brightway packages in the Brightway documentation. However, they are not updated automatically. You need to manually update the submodule directories whenever you have made changes to the docstrings in your fork of the `brightway2-io` repo.
```

:::

:::{tab-item} Publish your Changes

1. Open a pull request with your edits against the main `brightway2-io` repo.
2. As soon as the changes to `brightway2-io` have been merged into the `main` branch, the `brightway2-io` submodule in the `brightway-documentation` repo will be updated automatically through [a GitHub Actions workflow](https://github.com/brightway-lca/brightway-documentation/tree/main/.github/workflows).
3. The Brightway documentation at readthedocs.org will be built automatically. Your changes are now online!

:::