# Formatting Guide

The Brightway Documentation webpage, including the Example Gallery, uses the [MyST markdown format](https://myst-parser.readthedocs.io/en/latest/index.html). _Markdown_ is a is a lightweight markup language (=text-encoding system) for creating formatted text using a plain-text editor. MyST is a dialect of Markdown that supports many visual elements useful in scientific publishing.

## Formatting Features

For instance, you can use plain text to write a [LaTeX equation](https://en.wikipedia.org/wiki/LaTeX):

```markdown
$y = mx^2 + b$
```

which will be rendered as:

$y = mx^2 + b$

You can also add page elements, such as colored information boxes:

```markdown
:::
{note} This is an information box
:::
```

which will be rendered as:

:::{note}
This is an information box
:::

Other functions include [cross-references, footnotes, embedded images, tables, colored information boxes and more](https://myst-parser.readthedocs.io/en/latest/index.html). _"If you can do it in Microsoft Word, you can do it in Markdown!"_ To provide this functionality in Jupyter Notebooks, the Brightway Documentation webpage uses the [MyST-NB](https://myst-nb.readthedocs.io/en/latest/index.html) extension.

## Reference

For a complete overview of the MyST Markdown syntax, please refer to the MyST Markdown Guide. This will covery all cases you might want to use in your edits to the Brightway Documentation webpage:

- [MyST Markdown Guide](https://myst-parser.readthedocs.io/en/latest/syntax/typography.html)
    - [Typography](https://myst-parser.readthedocs.io/en/latest/syntax/typography.html)
    - [Admonitions](https://myst-parser.readthedocs.io/en/latest/syntax/admonitions.html)
    - [Images/Figures](https://myst-parser.readthedocs.io/en/latest/syntax/images_and_figures.html)
    - [Tables](https://myst-parser.readthedocs.io/en/latest/syntax/tables.html)
    - [API](https://myst-parser.readthedocs.io/en/latest/syntax/code_and_apis.html)
    - [Cross References](https://myst-parser.readthedocs.io/en/latest/syntax/cross-referencing.html)
    - [Math and Equations](https://myst-parser.readthedocs.io/en/latest/syntax/cross-referencing.html)


