# Brightway core libraries

The four core libraries in Brightway are:

| Project | Description |
| ------- | ----------- |
| [`bw2data`](https://github.com/brightway-lca/brightway2-data) | Project management, graph storage and ORM using SQLite, search |
| [`bw2calc`](https://github.com/brightway-lca/brightway2-calc) | Matrix-based calculations |
| [`bw2io`](https://github.com/brightway-lca/brightway2-io) | [ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load) for LCA data |
| [`bw2analyzer`](https://github.com/brightway-lca/brightway2-analyzer) | Analyze inventory data and LCA results |

These core libraries in turn build on the following support libraries:

| Project | Description |
| ------- | ----------- |
| [`bw2parameters`](https://github.com/brightway-lca/brightway2-parameters) | Library for storing, validating, and calculating with parameters |
| [`bw_graph_tools`](https://docs.brightway.dev/projects/graphtools/) | [Path traversal](https://en.wikipedia.org/wiki/Graph_traversal) and graph manipulation |
| [`bw_interface_schemas `](https://github.com/brightway-lca/bw_interface_schemas/) | Interface schemas for data transfer in Brightway |
| [`bw_parameters`](https://github.com/brightway-lca/bw_processing) | Tools to create datapackages in a common format  |
| [`bw_simapro_csv`](https://docs.brightway.dev/projects/bw-simapro-csv/) | Importing [SimaPro](http://simapro.com) CSV files into Brightway |
| [`ecoinvent_migrate`](https://github.com/brightway-lca/ecoinvent_migrate) | Code to generate Randonneur migration files for ecoinvent releases |
| [`ecoinvent_interface`](https://github.com/brightway-lca/ecoinvent_interface) | Unofficial python interface to ecoinvent data |
| [`matrix_utils`](https://github.com/brightway-lca/matrix_utils) | Build and iterate on matrices using datapackages |
| [`multifunctional`](https://github.com/brightway-lca/multifunctional) | Multifunctional activities in Brightway  |
| [`pyecospold`](https://github.com/brightway-lca/pyecospold) | Read and write `ecospold` XML versions 1 and 2 |
| [`randonneur_data`](https://github.com/brightway-lca/randonneur_data) | Data for the randonneur ETL library and specification |
| [`randonneur`](https://github.com/brightway-lca/randonneur) | Library to apply flexible changes to datasets |
| [`stats_arrays`](https://github.com/brightway-lca/stats_arrays/) | NumPy array interface for defining uncertain parameters |

There are a number of additional libraries building on or contributing to Brightway - see [the Brightway software ecosystem](https://docs.brightway.dev/en/latest/content/other/framework.html).
