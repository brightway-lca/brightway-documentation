# Overview

This section gives an overview on *why* and *how* the Brightway life cycle assessment (LCA) framework works, as well as some generic LCA methodology and implementation discussion. It is not designed for people learning about Brightway for the first time - please [see the Brightway book](https://learn.brightway.dev/) which is tailored for newcomers.

```{note}
If you have questions that the documentation cannot answer, you can [get in touch with the Brightway community or the Brightway developers](../contact/contact.md).
```

```{toctree}
---
hidden: true
maxdepth: 2
---
self
core
inventory
matrix
io
```

## Brightway philosophy

Brightway is designed for flexibility, and does not place many constraints on what you are allowed to do while using it. This can be dangerous, as we will happily allow you to delete your database or enter numerical values which can break calculations. If you are first getting started, it's safest to follow the examples and cheat sheet.

## Brightway core concepts introduction

**Projects**: A Brightway project is an isolated set of data sufficient to do LCA calculations. In the core Brightway libraries, each project is implemented as a separate subdirectory with a SQLite3 database and directory for datapackages.

**Databases**: A Brightway database is a container for inventory data. Databases are primarily organization tools, and their precise boundaries are determined by practitioners. Nodes must be associated with one and only one database, but edges can and often do cross from one database to another.

Foreground and background databases: Brightway does not make a distinction between these two labels.

**Datapackages**: A selection of the numerical data in a database, sufficient to create matrices and perform an LCA calculation. Datapackages do not normally contain metadata, such as names, units, or locations - they are normally purely numeric.

Datapackages can represent uncertainty and scenarios in powerful but complex ways which open a lot of modelling flexibility.

**Nodes**: The objects in a database. Nodes can have any type, but are normally processes or products. There can be special kinds of process nodes, such as multifunctional and process_with_reference_product. The *type* of the node determines what fields are required in that node. You can add custom node types to store arbitrary data in the graph.

**Edges**: Brightway uses *directed* edges which show flows throughout the supply chain graph. Inventory and impact assessment edges must be numeric, but custom edges don't need to be.

**Functional edges**: A functional edge is one related directly to the function of the process node. As practitioners, we make an active choice to model some processes and not others - we need to choose what is included, what is excluded, and the level of granularity needed to reflect physical reality. We choose to model certain activities because they achieve a certain function - either the production of a good, or the handling of a waste. A functional edge can therefore be an input *or* an output of a process, and functionality is attached to the edge, as products are functional in some contexts but not in others. In other words, one process may produce a waste (non-functional - not the intended purpose of that process, nor the main reason to model it), and the edge from the process to the waste product edge is non-functional. The waste needs to go somewhere, and the edge from waste product to the treatment process *is* functional, even though it is an input to the waste treatment process. Processes can have more than one functional edge.

**Calculations**: Brightway uses an `LCA` object to do matrix-based LCA calculations, and form the common foundation for most Brightway usage. Subclasses of `LCA` and partner libraries open up additional calculation options, including graph traversal, regionalization, and temporal LCA.
