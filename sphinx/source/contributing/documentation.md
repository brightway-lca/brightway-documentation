# Brightway Documentation

Details on the concept and technical implementation of the new Brightway documentation are detailed in [Brightway Enhancement Proposal (BEP) 003](https://github.com/brightway-lca/enhancement-proposals/blob/main/proposals/0003_documentation.md).

## Technical Infrastructure

![Read the Docs](https://img.shields.io/readthedocs/brightway-documentation?label=readthedocs.org&logo=Read%20the%20Docs&logoColor=white)

```{note}
The Brightway documentation is built with [Sphinx](https://www.sphinx-doc.org/en/master/), the Python documentation generator. The API documentation is compiled from source by [`sphinx-autoapi`](https://sphinx-autoapi.readthedocs.io/en/latest/). It is hosted on [Read the Docs](https://readthedocs.org/). All relevant code resides in the [`brightway-documentation`](https://github.com/brightway-lca/brightway-documentation) repository.
```

### Syntax

The majority of the Brightway documentation is based on Markdown (`.md`) files. The [MyST](https://myst-parser.readthedocs.io/en/latest/index.html) package is used to enable Markdown support across the project. Wherever necessary, reStructuredText (`.rst`) files or directives are used. The [`eval-rst` function](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html#syntax-directives-parsing) in MyST allows for use of arbitrary `rst` directives in Markdown files. 

### Structure

#### git submodules

The core functionality of Brightway is provided by different packages (e.g. `brightway-calc`, `brightway-data`). For strategic reasons, these packages are maintained as separate repositories. The content of these repositories is included in the `brightway-documentation` repository through [`git submodules`](https://git-scm.com/book/en/v2/Git-Tools-Submodules). This enables `sphinx` to include files from these repositories in the documentation directly (e.g. `README.md`). It further enables `sphinx-autodoc` both locally and in the readthedocs.org service to build the API documentation from source instead of importing all Brightway packages during the build process. 

#### GitHub Actions

To ensure that the `git submodules` are always up-to-date, both locally and in the readthedocs.org service, [GitHub Actions](https://github.com/features/actions) are used.

| package | action |
| ------- | ------ |
| `brightway2-calc` | ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/brightway-lca/brightway2-calc/.github/workflows/github_action_notify_documentation_repo.yml?label=action&logo=GitHub%20Actions&logoColor=white) |
| `brightway2-io` | ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/brightway-lca/brightway2-io/.github/workflows/github_action_notify_documentation_repo.yml?label=action&logo=GitHub%20Actions&logoColor=white) |
| `brightway2-data` | ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/brightway-lca/brightway2-data/.github/workflows/github_action_notify_documentation_repo.yml?label=action&logo=GitHub%20Actions&logoColor=white) |
| `brightway2-analyzer` | ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/brightway-lca/brightway2-analyzer/.github/workflows/github_action_notify_documentation_repo.yml?label=action&logo=GitHub%20Actions&logoColor=white) |


```{eval-rst}
.. tabs::

    .. tab:: :code:`brightway-documentation`

        .. NOTE::

            Compare the `documentation on StackOverflow <https://stackoverflow.com/a/67059629/>`_

        .. code-block::

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

    .. tab:: e.g. :code:`brightway2-calc`

        .. NOTE::

            Compare the `documentation on GitHub <https://github.blog/changelog/2022-09-08-github-actions-use-github_token-with-workflow_dispatch-and-repository_dispatch/>`_

        .. code-block::
           :caption: GHA_WORKFLOW_TRIGGER must be set as a org-wide secret

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

### Building the Documentation

The Brightway documentation is built and published automatically by the readthedocs.org service on every push/merge to the `main` branch of the `brightway-documentation` repository. To build the documentation locally, follow the [instructions in the repository readme](https://github.com/brightway-lca/brightway-documentation).