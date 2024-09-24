(glossary)=

# Glossary

## Graph

```{glossary}

Project
    A Brightway project is an isolated set of data sufficient to do LCA calculations. In the core Brightway libraries, each project is implemented as a separate subdirectory with a SQLite3 database and directory for datapackages.

Graph
    A graph is a collection of nodes, and edges which connect those nodes. Brightway uses the graph to store inventory and impact assessment information, and allows you to store additional information via the use of custom nodes.

Node
    The nouns in a graph. Nodes can have any type, but are normally processes, products, biosphere flows, and impact categories. There can be special kinds of process nodes, such as "multifunctional" and "process_with_reference_product". The *type* of the node determines what fields are required in that node. You can add custom node types to store arbitrary data in the graph.

Edge
    The verbs in a graph. In Brightway, all edges have directed, i.e. they have a source and a target. Inventory and impact assessment edges must be numeric, but custom edges don't need to be.

Functional edge
    A functional edge is an edge which expresses the function of the process to which it is attached. As practitioners, we make an active choice to model some processes and not others - we need to choose what is included, what is excluded, and the level of granularity needed to reflect physical reality. We choose to model certain activities because they achieve a certain function - either the production of a good, or the handling of a waste. A functional edge can therefore be an input *or* an output of a process, and functionality is attached to the edge, as products can be functional in some contexts but not in others. In other words, one process may produce a waste (non-functional - not the intended purpose of that process, nor the main reason to model it), and the edge from the process to the waste product edge is non-functional. The waste needs to go somewhere, and the edge from waste product to the treatment process *is* functional, even though it is an input to the waste treatment process. Processes can have more than one functional edge.

Database
    A Brightway database is a container for inventory nodes. Databases are primarily organization tools, and their precise boundaries are determined by practitioners. Nodes must be associated with one and only one database, but edges can and often do cross from one database to another.

    Brightway does not make a distinction between foreground and background databases.

Process
    An `process` in Brightway is the name used for both processes and elementary flows. Other terms used frequently:

    | Source | Terminology |
    | ------ | ----------- |
    | Brightway | `activity` |
    | ISO | `(unit) process` or `elementary flow`[^1]
    | [Ghose et al. (2021)](https://doi.org/10.1111/jiec.13220) | `Activity` |

Multifunctional process
    A process which has more than one functional edge.

Impact Category
    A set of `characterization factors` and associated metadata. The Brightway class name is `Method`, but this is not technically correct, does not follow ISO, and we encourage and will use the term "Impact Category". Other terms used frequently:

```

## Caculations

```{glossary}

Functional unit
    The demand of goods and services used in a given calculation. A functional unit is made up of products, not processes, although it can include chimaera process+product objects when they act as a product. Functional units can have more than one product.

Datapackage
    The numerical data in a `Database`, `Impact Category`, `Normalization`, or `Weighting` written as [numpy](https://numpy.org/) arrays and [record arrays](https://numpy.org/doc/stable/user/basics.rec.html). Follows the Open Knowledge Foundation's [datapackage standard](https://datapackage.org/), and includes metadata like author, license, and version. Can optionally include metadata on the graph.

    A datapackage contains all information needed to do matrix calculations. They can also represent uncertainty and scenarios in powerful but complex ways which open a lot of modelling flexibility.

Technosphere Exchange
    An exchange between two technosphere `activities`. Other terms used frequently:

    | Source | Terminology |
    | ------ | ----------- |
    | Brightway | `technosphere exchange` |
    | ISO | `intermediate flow` |
    | [Ghose et al. (2021)](https://doi.org/10.1111/jiec.13220) | `Flow` |

```
