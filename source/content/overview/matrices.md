
# Matrix Calculations in Brightway

!!! note

    We use the following limits for the matrix coefficient indices:

    | Index   | Description                    |
    |---------|--------------------------------|
    | $N$     | Number of products=activities  |
    | $R$     | Number of biosphere flows      |
    | $L$     | Number of impact categories    |

## Textbook Convention

| Object                  | Symbol        | Dimension   | Source                                                                                                        |
|-------------------------|---------------|-------------|---------------------------------------------------------------------------------------------------------------|
| final demand vector     | $\mathbf{f}$  | $[N\times 1]$ | Def. 4 (P.21) in [Heijungs & Suh (2001)](https://doi.org/10.1007/978-94-015-9900-9)                         |
| technology matrix       | $\mathbf{A}$  | $[N\times N]$ | Eqn.(2.7) and Eqn.(2.40) in [Heijungs & Suh (2001)](https://doi.org/10.1007/978-94-015-9900-9)              |
| biosphere matrix        | $\mathbf{B}$  | $[R\times N]$ | Eqn.(2.7) and Theorem 2 (P.21) in [Heijungs & Suh (2001)](https://doi.org/10.1007/978-94-015-9900-9)        |
| scaling vector          | $\mathbf{s}$  | $[N\times 1]$ | Eqn.(2.12ff.) and Def. 3 (P.21) in [Heijungs & Suh (2001)](https://doi.org/10.1007/978-94-015-9900-9)       |
| inventory vector        | $\mathbf{g}$  | $[R\times 1]$ | Eqn.(2.10) and Def. 5 (P.21) in [Heijungs & Suh (2001)](https://doi.org/10.1007/978-94-015-9900-9)          |
| characterization matrix | $\mathbf{Q}$  | $[L\times R]$ | Eqn.(8.26) in [Errata of Heijungs & Suh (2001)](https://web.archive.org/web/20230505051343/https://personal.vu.nl/r.heijungs/computational/The%20computational%20structure%20of%20LCA%20-%20Errata.pdf) |
| impact vector           | $\mathbf{h}$  | $[L\times 1]$ | Eqn.(8.27) in [Heijungs & Suh (2001)](https://doi.org/10.1007/978-94-015-9900-9)                            |

The _"solution to the inventory problem"_ is then given by (Eqn.(2.45) and Eqn.(2.47) in [Heijungs & Suh (2001)](https://doi.org/10.1007/978-94-015-9900-9)):

$$
\begin{align}
    \mathbf{s} &= \mathbf{A}^{-1} \mathbf{f} \\
    [N \times 1] &= [N \times N] [N \times 1] \notag \\
    \mathbf{g} &= \mathbf{B} \mathbf{s} \\
    [R \times 1] &= [R \times N] [N \times 1] \notag \\
    \mathbf{h} &= \mathbf{Q} \mathbf{g} \\
    [L \times 1] &= [L \times R] [R \times 1] \notag
\end{align}
$$

which can be written as:

$$
\begin{align}
    \mathbf{h} &= \mathbf{Q} \mathbf{B} \mathbf{A}^{-1} \mathbf{f} \\
    [L \times 1] &= [L \times R] [R \times N] [N \times N] [N \times 1] \notag
\end{align}
$$

## Brightway Convention

!!! warning

    Brightway implements the matrix calculations for the inventory vector $\mathbf{g}$, the characterization matrix $\mathbf{Q}$ and the impact vector $\mathbf{h}$ differently than the standard textbook! Note that these have different dimensions. They are marked with ⚠️ in the table of objects.

| Object | Textbook Equivalent | Dimension | Built by... |
|--------|----------------------|-----------|-------------|
|`lca.demand_array` | ✅ $\mathbf{f}$ | $[N\times 1]$ | [`bw2calc.lca.build_demand_array`](https://github.com/brightway-lca/brightway2-calc/blob/a51ac18348f22ada859e72f9d6c9a8774a4c0cb3/bw2calc/lca.py#L191)|
| `lca.technosphere_matrix` | ✅ $\mathbf{A}$ | $[N\times N]$ | [`bw2calc.lca_base.load_lci_data`](https://github.com/brightway-lca/brightway2-calc/blob/a51ac18348f22ada859e72f9d6c9a8774a4c0cb3/bw2calc/lca_base.py#L37) |
| `lca.biosphere_matrix` | ✅ $\mathbf{B}$ | $[R \times N]$ | [`bw2calc.lca_base.load_lci_data`](https://github.com/brightway-lca/brightway2-calc/blob/a51ac18348f22ada859e72f9d6c9a8774a4c0cb3/bw2calc/lca_base.py#L37) |
| `lca.supply_array` | ✅ $\mathbf{s}$ | $[N \times 1]$ | [`bw2calc.lca_base.lci`](https://github.com/brightway-lca/brightway2-calc/blob/a51ac18348f22ada859e72f9d6c9a8774a4c0cb3/bw2calc/lca_base.py#L155) |
| `lca.inventory` | ⚠️ $\mathbf{g}$ | $[R \times N]$ | [`bw2calc.lca.lci_calculation`](https://github.com/brightway-lca/brightway2-calc/blob/a51ac18348f22ada859e72f9d6c9a8774a4c0cb3/bw2calc/lca.py#L287) |
| `lca.characterization_matrix` | ⚠️ $\mathbf{Q}$ | $[R \times R]$ | [`bw2calc.lca.LCA.load_lcia_data`](https://github.com/brightway-lca/brightway2-calc/blob/a51ac18348f22ada859e72f9d6c9a8774a4c0cb3/bw2calc/lca.py#L219) |
| `lca.characterized_inventory` | ⚠️ $\mathbf{H}$ | $[R \times N]$ | [`bw2calc.lca.lcia_calculation`](https://github.com/brightway-lca/brightway2-calc/blob/a51ac18348f22ada859e72f9d6c9a8774a4c0cb3/bw2calc/lca.py#L301) |

$$
\begin{align}
    \mathbf{s} &= \mathbf{A}^{-1} \mathbf{f} \\
    [N \times 1] &= [N \times N] [N \times 1] \notag \\
    \mathbf{G} &= \mathbf{B} \cdot \text{diag} (\mathbf{s}) \\
    [R \times 1] &= [R \times N] [N \times 1] \notag
\end{align}
$$

Here, we do not have an _inventory vector_ $\mathbf{g}$, but an _inventory matrix_ $\mathbf{G}$. This is because the [`bw2calc.lca.LCA.lci_calculation`](https://github.com/brightway-lca/brightway2-calc/blob/a51ac18348f22ada859e72f9d6c9a8774a4c0cb3/bw2calc/lca.py#L287) function uses this convention:

```python
count = len(self.dicts.activity)
self.inventory = self.biosphere_matrix @ sparse.spdiags(
    data=[self.supply_array],
    diags=[0],
    m=count,
    n=count
)
```

This means that:

\begin{align}
    g_{ij} &= \sum_k b_{ik} \delta_{kj} s_{j} \\
    \mathbf{G} &=
    \begin{bmatrix}
        b_{11}s_1 & b_{12}s_2 \\
        b_{21}s_1 & b_{22}s_2 \\
    \end{bmatrix}
\end{align}

Here, $\delta_{ij}$ is the [Kronecker delta function](https://en.wikipedia.org/wiki/Kronecker_delta), defined as:

$$
\delta_{ij} =
\begin{cases} 
0 & \text{for } i \neq j \\
1 & \text{for } i = j.
\end{cases}
$$

!!! note
    In the Brightway convention, the coefficient $g_{ij}$ of $\mathbf{G}$ is the amount of biosphere flow $i$ produced by activity $j$.  
    In the textbook convention, the coefficient $g_i$ of $\mathbf{g}$ is the amount of biosphere flow $i$ produced by all activities.

    Summing the rows of $\mathbf{G}$ gives the inventory vector $\mathbf{g}$:

    $$
    g_{i} = \sum_j g_{ij} = \sum_j \sum_k b_{ik} \delta_{kj} s_{j}
    $$


Note that Brightway uses only [one impact assessment method at a time](https://github.com/brightway-lca/brightway2-calc/blob/cb4439b3c41cb8ddaf84a186385dde410806b977/bw2calc/lca.py#L47) and therefore $L=1$. Also, the `bd.LCA.characterization_matrix` object is loaded by the [`bw2calc.lca.LCA.load_lcia_data`](https://github.com/brightway-lca/brightway2-calc/blob/a51ac18348f22ada859e72f9d6c9a8774a4c0cb3/bw2calc/lca.py#L219) as a diagonal matrix (`diagonal=True`):

```python
self.characterization_mm = mu.MappedMatrix(
    packages=data_objs or self.packages,
    matrix="characterization_matrix",
    use_arrays=use_arrays,
    use_distributions=use_distributions,
    seed_override=self.seed_override,
    row_mapper=self.biosphere_mm.row_mapper,
    diagonal=True,
    custom_filter=fltr,
)
```

This means that instead of an _impact vector_ $\mathbf{h}$, we have an _impact matrix_ $\mathbf{H}$:

$$
\begin{align}
    \mathbf{H} &= \text{diag}(\mathbf{q}) \cdot \mathbf{G} \\
    [R \times N] &= [R \times R] [R \times N] \notag
\end{align}
$$

where

$$
\begin{align}
    h_{ij} &= \sum_k q_i \delta_{ik} g_{kj} \\
    \mathbf{H} &= \begin{bmatrix}
    q_1 g_{11} & q_1 g_{12} \\
    q_2 g_{21} & q_2 g_{22} \\
    \end{bmatrix} = \begin{bmatrix}
    q_1 (b_{11}s_1) & q_1 (b_{12}s_2) \\
    q_2 (b_{21}s_1) & q_2 (b_{22}s_2) \\
    \end{bmatrix}
\end{align}
$$

!!! note
    In the Brightway convention, the coefficient $h_{ij}$ of $\mathbf{H}$ is the impact of biosphere flow $i$ produced by activity $j$.  
    In the textbook convention, the coefficient $h_i$ of $\mathbf{h}$ is the amount of impact $i$ produced by all activities.


The total impact of all biosphere flows produced by all activities which are induced by the final demand vector $\mathbf{f}$ can be calculated by summing all elements of $\mathbf{H}$.
This is what is done in the [`bw2calc.lca.LCA.score`](https://github.com/brightway-lca/brightway2-calc/blob/a51ac18348f22ada859e72f9d6c9a8774a4c0cb3/bw2calc/lca.py#L330) function.