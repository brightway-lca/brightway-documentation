# Contributing Guide

You can contribute examples to the Brightway Documentation webpage by following these steps:

## Write your Notebook

```{admonition} Prerequisites
:class: important
1. Basic knowledge of [Jupyter Notebooks](https://jupyter.org)
3. A working installation of [Conda](https://docs.conda.io/en/latest/)
3. Basic knowledge of [Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
```

Write your Jupyter Notebook, using the template provided below.
Make sure to include [a Conda environment file in YAML format](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment) to ensure other users will be able to re-create your example from scratch.

```{admonition} Download Notebook Template
{download}`template.ipynb <./brightway-examples/guide/template.ipynb>` \
{download}`template.yaml <./brightway-examples/guide/template.yaml>`
```

## Format your Notebook

```{admonition} Prerequisites
:class: important
1. Basic knowledge of the [MyST Markdown syntax](https://myst-parser.readthedocs.io/en/latest/syntax/typography.html)
```

You can use additional formatting in your example notebook to make it more readable.

The Brightway Documentation webpage uses the [MyST markdown format](https://myst-parser.readthedocs.io/en/latest/index.html). _Markdown_ is a is a lightweight markup language (=text-encoding system) for creating formatted text using a plain-text editor. MyST is a dialect of Markdown that supports many visual elements useful in scientific publishing. 

For instance, you can use plain text:

```markdown
$y = mx^2 + b$
```

to include a LaTeX equation in your text:

$y = mx^2 + b$

Other functions include [cross-references, footnotes, embedded images, tables, colored information boxes and more](https://myst-parser.readthedocs.io/en/latest/index.html). To provide this functionality in Jupyter Notebooks, the Brightway Documentation webpage uses the [MyST-NB](https://myst-nb.readthedocs.io/en/latest/index.html) extension.

## Add your Notebook

```{admonition} Prerequisites
:class: important
1. Basic knowledge of [the GitHub contribution workflow (fork, branch, pull request)](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests)
2. A fork of the [`brightway-examples`](https://github.com/brightway-lca/brightway-examples) repository
3. Your finished example notebook
```

Once you are happy with your example, you can start the process to add it to the Brightway Documentation webpage.

All examples are collected in the [`brightway-examples` repository](https://github.com/brightway-lca/brightway-examples). To add your example, determine the appropriate location for it in the repository structure.

For instance, an example about importing data from the Ecoinvent 3.9.1 database should be added to the `data_import` directory:

```
.
└── brightway-examples/
    └── data_import/
        └── ecoinvent_3-9-1_import/
            ├── ecoinvent_3-9-1_import.ipynb
            └── ecoinvent_3-9-1_import.yaml
```

Add your example to the approriate location in your fork of the `brightway-examples` repository. Make sure to include the `.ipynb` and `.yaml` files. Finally, open a pull request. Once the pull request has been merged by a member of the Brightway Development team, your example will be added to the Brightway Documentation webpage.