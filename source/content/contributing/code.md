# Contributing to the Code

If you would like to contribute to the development of Brightway, follow [the usual GitHub process](https://docs.github.com/en/get-started/quickstart/contributing-to-projects): Fork the [relevant Brightway repository on GitHub](https://github.com/brightway-lca), make your changes and open a pull request with your changes. 

```{note}
The Brightway project has adopted the [Contributor Covenant](https://www.contributor-covenant.org/).
```

```{seealso}
The development of major new features, collecting community input on issues, and documenting Brightway design decisions is managed through [`Brightway Enhancement Proposals`](https://github.com/brightway-lca/enhancement-proposals/tree/main)[^1].
```

## Specific Guidelines

### Code Style

Brightway has currently not adopted a specific code style beyond [Python PEP8](https://peps.python.org/pep-0008/). However, we recommend the use of [Black](https://black.readthedocs.io/en/stable/) to ensure a consistent code style across the code base.

### Docstrings

```{warning}
The use of descriptive docstrings for all Brightway functions, classes and class methods is mandatory. Brightway has adopted the [NumPy Docstring Style](https://numpydoc.readthedocs.io/en/latest/format.html).
```

Writing code that is easy to understand is a key principle of Brightway. This is why it is not enough to write code with descriptive variable names and comments. All functions, classes and class methods must be documented with a [docstring](https://en.wikipedia.org/wiki/Docstring). These docstrings are used to automatically generate the [Brightway API documentation](https://brightway-lca.github.io/brightway-documentation/). As such, they should form the basis of the documentation of the Brightway code base.

Using [the full extend of the NumPy Docstring features](https://numpydoc.readthedocs.io/en/latest/format.html), including the `Examples`, `Raises`, `See Also`, `Notes`, and `References` sections, is recommended:

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

[^1]: The Brightway Enhancement Proposals are inspired by the [Python Enhancement Proposals](https://www.python.org/dev/peps/).