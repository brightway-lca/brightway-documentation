# Matrix Construction

We normally use Brightway to do life cycle assessment calculations using matrices. This section describes how matrices are constructed. In a standard calculation, we would have three matrices:

* `technosphere` matrix: Our model of the supply chain. It has columns of processes, and rows of products. Chimaera process+product nodes will have both a row and a column.
* `biosphere` matrix: The interactions our processes have with the natural environment - either consumption of resources, or emissions to the natural environment. It has columns of processes (in the same order and dimension as the `technosphere` matrix), and rows of biosphere flows.
* `characterization` matrix: The unit conversion from physical amounts of biosphere flows to the unit of damage. It has columns and rows of biosphere flows (same order and dimension as the `biosphere` matrix), and only has values along the diagonal.

## Processed Datapackages

To speed up calculations, Brightway maintains a separate cache of the numerical data. When a change is made to a `Database`, it is marked as `dirty` in its metadata. When a calculation is initiated, the cache of all dirty databases is refreshed from the relational data store.

## Positive and Negative Values in the `technosphere`

````{admonition} Technosphere Matrix Normalization
:class: important
You may have seen the following matrix equation for IO or LCA: $h = (I - A)^{-1}f$. Brightway **does not** use this equation - instead, we use the following: $h = A^{-1}f$. We do not assume that each column in our technosphere matrix (**A**) is [normalized to one unit of production](production-normalization), nor do we assume that rows are in the same order as columns. These are [unnecessary and arbitrary restrictions](https://doi.org/10.1111/jiec.13323), and Brightway does not like arbitrary restrictions. So we choose to manually construct the technosphere matrix, and choose which numbers are positive and which are negative.```
````

The sign convention in Brightway is:

* Positive numbers in the technosphere are products (goods and services) being *produced* by a process. This can include waste.
* Negative numbers in the technosphere are products (goods and services) being *consumed* by a process. This can include waste.

Remember, in the technosphere matrix products are rows, processes are columns, but sometimes we have chimaera nodes which act as both products and processes.

The *sign* of an edge numeric value is not related to whether or not that edge is *functional*. Wastes can be produced (positive value), but producing waste is never the function of a process.

Brightway will automatically insert the correct numerical sign based on the `Node` and `Edge` types you provide.

## Positive and Negative Values in the `biosphere` and LCIA Matrices

The convention in almost all parts of the LCA community is for characterization factors to be positive numbers, representing the *production* of environmental damage. This is true even if the characterization factors are for resource consumption, which is the net removal of a resource from its reserve.

Similarly, every database that we are aware of gives positive values in the biosphere matrx, even if the biosphere flow is the consumption of natural resources.

A more logical sign convention would be consistency with the technosphere, where consumption is negative and production is positive.

Brightway does not take a position on this debate - the signs of values in biosphere and characterization (and normalization and weighting) edges are entered into those matrices without change. Brightway does allow you to follow this more logical sign convention, but does not implement it when importing common databases and LCIA methods, as we prefer to not modify imported data (at least most of the time 😉), and because trying to fix things could easily lead to mistakes. Whatever sign convention you do follow, make sure that both the biosphere edges and any LCIA data you use are consistent with each other.

## What Data Enters the `technosphere` Matrix?

Brightway uses a combination of the node and edge *types* to determine where to put edge data in the technosphere and biosphere matrices. These type filter values are configurable, and can be customized if needed.

Here are the rules Brightway follows:

1. If an edge (exchange on a `Node` instance) has a type in `bw2data.labels.technosphere_positive_edge_types`, and the edge *output* `Node` has a type in `bw2data.labels.process_node_types`, then the numeric amount of the edge will be added to the *technosphere* matrix without modification, with a row index derived from the edge *input* and a column index derived from the edge *output*.

That was a mouthful! Let's break it down:

* We want to be able to put additional data in the graph data store and not have it be used in matrix construction. For example, we could create a `Node` which gives data lineage, or revision history, or review comments, or links to external models. These nodes would have a `type` value like "ignore me please", and this *process node type* is not in `bw2data.labels.process_node_types` (which defaults to "process", "processwithreferenceproduct", and a missing type value), so this node and its edges would not be used in matrix construction.
* Every section in `bw2data.labels` is a list, and can be appended to or even replaced completely, if you want to use different labels.
* We will put both positive numbers and negative numbers into the technosphere matrix, and the meaning of positive and negative values is given above. If the edge type is in `bw2data.labels.technosphere_positive_edge_types` (which defaults to "production" and "substitution"), then we know the numeric value should be entered without modification.
* Why did I just say "without modification" instead of with a positive value? Because maybe you chose to put in a negative amount in your production edge. Brightway won't judge, it just does what you tell it to. In general, this isn't the greatest idea (why model it as a negative production instead of a consumption edge?), but it will work.
* We have an exchange data model for inputs and outputs which **doesn't make sense**, because it needs to labels the products being produced by the process as an *input* to that process, even though it is definitely an *output* of the physical process. Sorry about that, we will fix this, but for now follow this rule:

```{important}
The terms `input` and `output` in the Brightway data schema do no indicate directionality. Products and biosphere flows always need to be edge *inputs* in Brightway, even if they are *outputs* in the real world. Edge *outputs* should always be processes.
```

When using chimaera process+product nodes there is no distinction between a process and a product, so you don't need to think about any of this - that's how this weird design choice came into Brightway in the first place.

2. If an edge (exchange on a `Node` instance) has a type in `bw2data.labels.technosphere_negative_edge_types`, and the edge *output* `Node` has a type in `bw2data.labels.process_node_types`, then the numeric amount of the edge will be added to the *technosphere* matrix after mutiplication be `-1`, with a row index derived from the edge *input* and a column index derived from the edge *output*.

Very similiar to the first rule, but with different edge types - `bw2data.labels.technosphere_negative_edge_types`, which defaults to "technosphere", and a multiplication of the numeric amount by `-1`. Remember that this doesn't mean the number is negative, just that its sign is flipped.

3. If an edge (exchange on a `Node` instance) has a type in `bw2data.labels.biosphere_edge_types`, and the edge *output* `Node` has a type in `bw2data.labels.process_node_types`, then the numeric amount of the edge will be added to the *biosphere* matrix without modification, with a row index derived from the edge *input* and a column index derived from the edge *output*.

## What Data Enters the `biosphere` Matrix?

When building the `biosphere` matrix, Brightway iterates over all process nodes present in the `technosphere`; for each edge attached to one of those process nodes, we check:

1. The edge `type`; it must be in `bw2data.labels.biosphere_edge_types`, which has a default of `["biosphere"]`.

That's it! This single rule means that we **don't check the biosphere node `type`** - the only way we determine what biosphere flows we have in our matrix are whether they are refenced by an edge with a biosphere edge type.

We can therefore do a better job reflecting the real world, where the distinction between products in the technosphere and biosphere flows breaks down upon examination. Think of pesticides or other agricultural chemicals, which are both produced but then applied and have environmental effects, or industrial gases including $CO_{2}$ which are used in the technosphere but also released and cause impacts. In Brightway, you could use the same `Node` as a product in the technosphere matrix *and* as a biosphere flow in the biosphere matrix.

## What Data Enters the `characterization`, `normalization`, and `weighting` Matrices?

Any biosphere flows returned [when iterating over LCIA objects](iterate-lcia-method) which **are also in the biosphere matrix** are used to construct these LCIA matrices.

In non-regionalized LCIA, we also remove region-specific characterization factors. The characterization factor [data schema](lcia-tuple-structure) allows for an optional "location" third element. In non-regionalized LCIA, we only use characterization factors who don't have a "location" element, or whose "location" element is equal to `bw2data.config.global_location`.
