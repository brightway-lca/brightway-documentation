# Brightway Life-Cycle Assessment Framework

[![Mailing List](https://img.shields.io/badge/Community-Mailing%20List-blue.svg?style=flat&logo=Minutemailer&logoColor=white)](https://brightway.groups.io/)
[![Matrix](https://img.shields.io/badge/Community-Chat-ed1965.svg?style=flat&logo=Matrix&logoColor=white)](https://app.element.io/#/room/#brightway/community:matrix.org)
[![SO](https://img.shields.io/badge/Community-Questions-f48024.svg?style=flat&logo=Stack%20Overflow&logoColor=white)](https://stackoverflow.com/questions/tagged/brightway)
[![SO](https://img.shields.io/badge/Community-Meetups-green.svg?style=flat&logo=Google%20Maps&logoColor=white)](https://2022.brightcon.link/)
[![Blog](https://img.shields.io/badge/Development-Blog-lightgrey.svg?style=flat&logo=Blogger&logoColor=white)](https://chris.mutel.org/)

::::{grid} 1 1 3 3
:gutter: 3

:::{grid-item-card} {fab}`github` Contribute
:link: source/contributing/contributing
:link-type: doc

You can directly contribute to the development of Brightway or the Brightway documentation!
+++
Learn more {fas}`arrow-right`
:::

:::{grid-item-card} 🌿 The Brightway Ecosystem
:link: source/other/ecosystem
:link-type: doc

Contributors have built amazing projects extending and using the Brightway ecosystem!
+++
Learn more {fas}`arrow-right`
:::

:::{grid-item-card} 🌐 BrightCon
:link: https://2023.brightcon.link/
:link-type: url

Our annual conference brings together developers and practitioners from across the globe!
+++
Learn more {fas}`arrow-right`
:::

::::

Brightway is an open-source software package for [life cycle assessment](https://en.wikipedia.org/wiki/Life-cycle_assessment) (LCA) and [environmental impact assessment](https://en.wikipedia.org/wiki/Environmental_impact_assessment) written in the [Python](https://www.python.org/) programming language. LCA is a method for evaluating the environmental impacts of a product, process, or service. It involves analyzing all of the inputs and outputs of a system, including raw materials, energy use, and waste products, and quantifying the environmental impacts of these inputs and outputs over the entire lifecycle of the system. 

Brightway is designed to make it easy to work with large datasets and perform LCA calculations quickly and accurately. It thus provides a powerful tool for anyone interested in performing LCA or evaluating the environmental impacts of products and processes. Brightway is not intended to replace software like _SimaPro_ or _OpenLCA_, but instead offers possibilities to break the limits of conventional LCA. Brightway is especially attractive for researchers, especially when used with [Jupyter notebooks](https://jupyter.org/).

## Where to Find What?

::::::{grid} 3
:gutter: 1
:padding: 1

:::::{grid-item}
:child-direction: column
:child-align: end

::::{grid} 1

:::{grid-item-card}
:margin: 1
:text-align: right
*practical* \
*steps*
:::

:::{grid-item-card}
:margin: 1
:text-align: right
*theoretical* \
*knowledge*
:::

::::

:::::

:::::{grid-item}
:child-direction: row
:child-align: start

::::{grid} 1

:::{grid-item-card}
:margin: 1
*serves our* \
*study*
:::

:::{grid-item-card}
:margin: 1
Interactive Tutorials \
[`training.brightway.dev`](https://training.brightway.dev/)
:::

:::{grid-item-card}
:margin: 1
Theory and Explanations \
[Section `LCA`](source/lca/lca.md)
:::

::::

:::::

:::::{grid-item}
:child-direction: row
:child-align: start

::::{grid} 1

:::{grid-item-card}
:margin: 1
*serves our* \
*work*
:::

:::{grid-item-card}
:margin: 1
Example Gallery \
[Section `Gallery`](source/gallery/index.md)
:::

:::{grid-item-card}
:margin: 1
Technical Reference \
[Section `API Reference`](https://documentation.brightway.dev/en/latest/source/api/index.html)
:::

::::

:::::

::::::

:::{note}
The Brightway documentation is using [the Diataxis framework](https://diataxis.fr/). This is a method of organizing the information related to a software package. Depending on what information you are looking for, you can find it in different places:
:::

```{toctree}
---
hidden:
maxdepth: 1
---
source/introduction/introduction
source/setup/setup
source/api/index
source/gallery/index
source/lca/lca
source/contributing/contributing
source/faq/faq
source/changelog/index
source/other/ecosystem
source/other/credits
```