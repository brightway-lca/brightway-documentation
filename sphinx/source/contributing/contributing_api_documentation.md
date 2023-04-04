# API Documentation

![Read the Docs](https://img.shields.io/readthedocs/brightway-documentation?label=readthedocs.org&logo=Read%20the%20Docs&logoColor=white)

Details on the concept and technical implementation of the new Brightway documentation are detailed in [Brightway Enhancement Proposal (BEP) 003](https://github.com/brightway-lca/enhancement-proposals/blob/main/proposals/0003_documentation.md).

```{note}
The API documentation is compiled from source by [`sphinx-autoapi`](https://sphinx-autoapi.readthedocs.io/en/latest/). It is hosted on [Read the Docs](https://readthedocs.org/). All relevant code resides in the [`brightway-documentation`](https://github.com/brightway-lca/brightway-documentation) repository.
```

## Docstring Guidelines

```{note}
The use of descriptive docstrings for all Brightway functions, classes and class methods is mandatory. Brightway has adopted the [NumPy Docstring Style](https://numpydoc.readthedocs.io/en/latest/format.html).
```

Using the full extend of the NumPy Docstring features, including the `Examples`, `Raises`, `See Also`, `Notes`, and `References` sections, is recommended:

:::{dropdown} Docstring Features
| Feature | Required | Comment |
| ------- | --------- | ---------- |
| short summary | yes | N/A |
| extended summary | yes | N/A |
| `attributes` | yes | N/A |
| `parameters` | yes | must include types |
| `returns` | yes | must be `Nothing` the function does not return anything |
| `raises` | yes | N/A |
| `see also` | optional | should like to other relevant functions |
| `notes` | optional | scientific/mathematical explanation of the life-cycle assessment functionality |
| `references` | optional | references for the information used in `notes` |
| `examples` | yes | mandatory for all public functions, classes and class methods |

The `__init__` method should be documented as a docstring on the __init__ method itself. This means that The `attributes` and `parameters` sections [will be split between the class docstring the the `__init__` docstring.](https://github.com/sphinx-contrib/napoleon/blob/dce30797b7a229ccebda4030f65482d501427794/docs/source/example_numpy.py#L226)
:::

## Contributing Tutorial

```{note}
This tutorial demonstrates how to contribute to the API documentation of the `brightway2-io` package. All steps are equivalent for other Brightway packages (`brightway2-data`, `brightway2-calc`, etc.).
```

::::{tab-set}

:::{tab-item} Make and Preview your Changes

1. Clone the `brightway-documentation` repo.
2. Fork the `brightway2-io` repo and create a new branch (e.g. `documentation_improvements`).
3. Make the desired changes to the docstrings on your branch (e.g. `documentation_improvements`) in your fork of the `brightway2-io` repo.

You can now preview your changes:

4. Edit the file `.gitmodules` in the `brightway-documentation` repo to reflect your fork of the `brightway2-io` repo by changing the `<username>` in the `url` field:

```
[submodule "brightway2-io"]
	path = brightway2-io
	url = https://github.com/<username>/brightway2-io
	branch = documentation_improvements
```

5. Point the `brightway2-io` submodule to your fork of the `brightway2-io` repo. Repeat whenever you have made changes to the docstrings in your fork of the `brightway2-io` repo:

```bash
git submodule update --init --recursive --remote --force
```

6.  Follow [the instructions in the readme](https://github.com/brightway-lca/brightway-documentation) to build the documentation locally. You can now preview your changes.

```{note}
[Git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) offer a convenient way to include the documentation of other Brightway packages in the Brightway documentation. However, they are not updated automatically. You need to manually update the submodule directories whenever you have made changes to the docstrings in your fork of the `brightway2-io` repo.
```

:::

:::{tab-item} Publish your Changes

1. Open a pull request with your edits against the main `brightway2-io` repo.
   
```{note}
One pull request per file (e.g. `bw2io/chemidplus.py`) is recommended. Please follow the naming convention:
```bash
Update docstrings to NumPy standards (`bw2io/chemidplus` etc.)
```

2. As soon as the changes to `brightway2-io` have been merged into the `main` branch, the `brightway2-io` submodule in the `brightway-documentation` repo will be updated automatically through [a GitHub Actions workflow](https://github.com/brightway-lca/brightway-documentation/tree/main/.github/workflows).
3. The Brightway documentation at readthedocs.org will be built automatically. Your changes are now online!

:::

::::

## Technical Setup Information

### git submodules

The core functionality of Brightway is provided by different packages (e.g. `brightway-calc`, `brightway-data`). For strategic reasons, these packages are maintained as separate repositories. The content of these repositories is included in the `brightway-documentation` repository through [`git submodules`](https://git-scm.com/book/en/v2/Git-Tools-Submodules). This enables `sphinx` to include files from these repositories in the documentation directly (e.g. `README.md`). It further enables `sphinx-autodoc` both locally and in the readthedocs.org service to build the API documentation from source instead of importing all Brightway packages during the build process. 

### GitHub Actions

To ensure that the `git submodules` are always up-to-date, both locally and in the readthedocs.org service, [GitHub Actions](https://github.com/features/actions) are used. Whenever changes are made to the `main` branch of a Brightway package (e.g. `brightway-calc`, `brightway-data`), a GitHub action workflow triggers another GitHub actions workflow in the `brightway-documentation` repository. This workflow updates the `git submodules` and commits the changes to the `main` branch of the `brightway-documentation` repository.

| package | action |
| ------- | ------ |
| `brightway-documentation` | ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/brightway-lca/brightway-documentation/.github/workflows/github_action_update_submodules.yml?label=action&logo=GitHub%20Actions&logoColor=white) |
| `brightway2-calc` | ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/brightway-lca/brightway2-calc/.github/workflows/github_action_trigger_submodule_pull.yml?label=action&logo=GitHub%20Actions&logoColor=white) |
| `brightway2-io` | ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/brightway-lca/brightway2-io/.github/workflows/github_action_trigger_submodule_pull.yml?label=action&logo=GitHub%20Actions&logoColor=white) |
| `brightway2-data` | ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/brightway-lca/brightway2-data/.github/workflows/github_action_trigger_submodule_pull.yml?label=action&logo=GitHub%20Actions&logoColor=white) |
| `brightway2-analyzer` | ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/brightway-lca/brightway2-analyzer/.github/workflows/github_action_trigger_submodule_pull.yml?label=action&logo=GitHub%20Actions&logoColor=white) |


::::{tab-set}

:::{tab-item} brightway-documentation

```{note}
Compare the [documentation on StackOverflow.](https://stackoverflow.com/a/67059629/)
```

```
name: 'Update Submodules'

on:
workflow_dispatch:

jobs:
sync:
    name: 'Update Submodules'
    runs-on: ubuntu-latest

    defaults:
    run:
        shell: bash

    steps:
    - name: Checkout
    uses: actions/checkout@v2
    with:
        token: ${{ secrets.GITHUB_TOKEN }}
        submodules: true

    - name: Update Submodules
    run: |
        git pull --recurse-submodules
        git submodule update --remote --recursive

    - name: Commit Update
    run: |
        git config --global user.name 'GitHub Actions Submodule Updater'
        git config --global user.email 'bot@noreply.github.com'
        git remote set-url origin https://x-access-token:${{ secrets.GITHUB_TOKEN }}@github.com/${{ github.repository }}
        git commit -am "auto updated submodule" && git push || echo "no changes in submodule to commit"
```
:::

:::{tab-item} other repos (eg. brightway2-calc)

```{note}
Compare the [documentation on GitHub.](https://github.blog/changelog/2022-09-08-github-actions-use-github_token-with-workflow_dispatch-and-repository_dispatch/)
```

```{warning}
`GHA_WORKFLOW_TRIGGER` must be set as an org-wide secret
```

```
name: Create Workflow Dispatch

on:
push:
    branches:
    - main  
workflow_dispatch:

jobs:
build:
    runs-on: ubuntu-latest
    steps:
    - name: Trigger Workflow
        uses: actions/github-script@v6
        with:
        github-token: ${{ secrets.GHA_WORKFLOW_TRIGGER }}
        script: |
            github.rest.actions.createWorkflowDispatch({
                owner: 'brightway-lca',
                repo: 'brightway-documentation',
                workflow_id: 'github_action_update_submodules.yml',
                ref: 'main',
            })
```
:::

::::