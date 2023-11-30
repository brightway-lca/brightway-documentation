# Report Bugs or Errors

```{note}
We are sorry to find you on this page! But we are happy to help you with your problem. Please follow the steps below to report a bug or error.
```

## Errors in the Documentation

The underlying content of the Brightway documentation website is hosted in the [GitHub repository `brightway-documentation`](https://github.com/brightway-lca/brightway-documentation). You can therefore:

### 🥈 Report the Error

```{admonition} Prerequisites
:class: important
1. A [GitHub account](https://github.com/signup)
```

In order to report an error in the documentation, please [open an new issue](https://github.com/brightway-lca/brightway-documentation/issues) in this repository, describing the error and where you found it. A member of the Brightway developer community will then take care of the issue. Please note that all developments are undertaken on a voluntary basis, so it may take some time for your issue to be resolved.

### 🥇 Fix the Error Yourself

```{admonition} Prerequisites
:class: important
1. A [GitHub account](https://github.com/signup)
2. Basic knowledge of [the GitHub contribution workflow (fork, branch, PR)](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests)
3. A [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks) of the [`brightway-examples`](https://github.com/brightway-lca/brightway-examples) repository
4. Basic knowledge of [Markdown](https://www.markdownguide.org/basic-syntax/)
```

In order to fix an error in the documentation, you can make an edit of the underlying content yourself:

1. Use the `✏️ Edit on GitHub` button on the top right of the page to open the corresponding file in the GitHub repository. This shows you which file you need to edit.
2. Edit the file in your fork of the repository. Finally, create a pull request.
3. As soon as a member of the Brightway developer community has merged your pull request, the changes will be visible on the Brightway documentation website.

## Bugs in the Brightway Code

First you must identify which package contains the bug you have found. You can do so by examining the Python Traceback, which is the error message that is displayed when the bug occurs. The traceback will contain the name of the package that contains the bug. This could be:

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
AttributeError: module 'bw2calc' has no attribute 'ComparativeMonteCarlo'
```

All Brightway packages are hosted in the [GitHub organization `brightway-lca`](https://github.com/brightway-lca). You can therefore:

### 🥈 Report the Bug

```{admonition} Prerequisites
:class: important
1. A [GitHub account](https://github.com/signup)
2. Basic knowledge of the [Python Error Traceback](https://web.archive.org/web/20231127162411/https://realpython.com/python-traceback/)
```

In order to report a bug in a Brightway package, please open a new issue in the corresponding repository:

- [`brightway2-data`](https://github.com/brightway-lca/brightway2-data)
- [`brightway2-calc`](https://github.com/brightway-lca/brightway2-calc)
- [`brightway2-io`](https://github.com/brightway-lca/brightway2-io)
- [`brightway2-analyzer`](https://github.com/brightway-lca/brightway2-analyzer)

(all other Brightway packages can be found on the repository overview page of the [`brightway-lca` GitHub organization](https://github.com/brightway-lca?q=&type=all&language=&sort=))

Your issue should include:

1. the complete Python Traceback
2. a description of the bug
3. information your operating system and Python version
4. the steps required to reproduce the bug

A member of the Brightway developer community will then take care of the issue. Please note that all developments are undertaken on a voluntary basis, so it may take some time for your issue to be resolved.

### 🥇 Fix the Bug Yourself

```{admonition} Prerequisites
:class: important
1. A [GitHub account](https://github.com/signup)
2. Basic knowledge of [the GitHub contribution workflow (fork, branch, PR)](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests)
3. A [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks) of the relevant repository
```

Follow the usual GitHub contribution workflow. 