# Brightway Software Ecosystem

The ![Brightway](https://img.shields.io/static/v1?label=Brightway&message=Framework&color=45bfb0&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA2NSIgaGVpZ2h0PSI2OTAiIHZlcnNpb249IjEuMSIgdmlld0JveD0iMCAwIDEwNjUgNjkwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogPGRlZnM+CiAgPGNsaXBQYXRoIGlkPSJjbGlwUGF0aDIxNzMiPgogICA8cGF0aCBkPSJtLTU5NSA0NDBoMWUzdi0xZTNoLTFlM3oiLz4KICA8L2NsaXBQYXRoPgogPC9kZWZzPgogPGcgdHJhbnNmb3JtPSJtYXRyaXgoMS4zIDAgMCAtMS4zIDY1MyA0MDMpIiBjbGlwLXBhdGg9InVybCgjY2xpcFBhdGgyMTczKSIgZmlsbD0iI2ZmZiI+CiAgPHBhdGggZD0ibTAgMGMwLTEuMi0xLjUtMy40LTAuNDctNS4yIDEuMy0yLjQgNS40LTEuNSA1LjgtM3YtMC4wMThsLTQuNy0wLjA1NC0yLTQuMWMtMS45IDAuNzEtMi40IDMuMi0zLjIgNi42LTAuNDQgMi0wLjcxIDMuNCAwLjA4OSA0LjctMTQtMy4zLTMwLTUuNC00NS01LjQtNDkgMC4wMzYtNzEgMTctMTA3IDI0IDEuNS0xLjEgMi43LTMuMyAyLjEtNC45bC02LjEgMi4yLTQtMy4xYy0xLjQgMS40LTAuNTggMi44LTIuMiA0LjgtMi4xIDIuNS01LjMgMi42LTUuMiAzIDAuODctMC4wNzIgMS43LTAuMTQgMi42LTAuMjItMS42IDAuMjQtMi41IDAuNC0yLjYgMC4yMi0zLjkgMC4zMS04IDAuNDktMTIgMC41MS02NiAwLjIyLTEwMi00Mi0xMjItNzkgMy42IDIuOSA4LjcgMS41IDEwIDEuMSA0LjItMS4xIDguOC00LjEgOC40LTYuMWwtNC41LTEuNSAwLjUyLTAuNTRjLTAuMjItMC4wMTktMC40My0wLjAxOS0wLjY1LTAuMDE5LTQuMiAwLjA1NS01LjEgMy45LTkuMiA0LjItMy44IDAuMjktNi40LTIuNy03LjItMS45LTEzLTI3LTE4LTUwLTE4LTUwaC0zNHM2LjcgMzQgMzAgNjhjLTEuNiAxIDEgNS0xLjEgOC4zLTIuNSAzLjgtOC40IDIuNC04LjggNC41LTAuMDE4IDAuMTMtMC4wMzYgMC4yNSAwIDAuMzhsNy4yLTAuNTIgMi41IDUuNWMxLjEtMC40IDItMS43IDMuOS00LjIgMS40LTEuOCAyLjQtMy4yIDMuMS00LjMgMjYgMzQgNjkgNjcgMTM5IDY3IDIuNSAwIDUtMC4wNzMgNy40LTAuMi0wLjU4IDIuMSA1IDMuNSA1LjcgOC4xIDAuNzQgNC44LTQuNyA3LjgtMy40IDEwIDAuMDE4IDAuMDE4IDAuMDM2IDAuMDU0IDAuMDU0IDAuMDcybDUuOC00LjQgNC43IDMuMWMwLjU2LTAuODcgMC42My0xLjctMC40NS04LTEuNC04LjItMS45LTktMi43LTkuNyA0MS01LjIgNjgtMjggMTE4LTI5IDE1LTAuNTQgMzAgMC43OCA0NCAzLjEtMC4yNyAwLjE2LTAuNTIgMC4zNi0wLjc2IDAuNjItMSAxLjEtMS4xIDMuMS0xLjQgNy4xLTAuMjUgNC4zLTAuNCA2LjYgMC40MiA3LjdsMi44LTMuMiAzLjIgMS4yYzAuMDM2LTAuMDcyIDAuMDU0LTAuMTYgMC4wNzItMC4yNCAwLjQ0LTEuOC0xLjEtMi43LTEuMS01LjYgMC0zLjUgMi4zLTQuOSAxLjgtNi41LTAuMDM2LTAuMDktMC4wNzItMC4xOC0wLjExLTAuMjUgNDUgOC43IDc4IDI4IDc5IDI4IDAtMC42My0zNS0yMi03OS0zM20tMzMyLTMwLTU1IDQuMS0zNSA0MC0xNyAyOC0xNSAyNC05LjcgMjctMjYgMTYgMzgtOS40IDM5LTI0IDMxLTI4IDI3LTM5IDE5LTMzem00MTEgNjUgMTEgNzkgNTcgNDYgNjggOS4zIDQ1LTAuMzkgNDcgMTYtMTYtMzYtMTMtMzQtMjQtNTgtMzItNDktMzktMjAtNDMgMy43em04OC0yNDktMTggMzItMjEgMjYtMzUgMzQtMjEgMjYtMjAgMjItMzcgNDgtMTcgMjAgNzAgMC44NyA1Ni00OSAyMi00MCAxNS0zNyAyLjgtMzJ6bTAgMC0xNyAxNy0zOSA2LjItNDQgMTMtNTAgMzMtMzAgNTUtMy4zIDUzIDEzIDI3IDEuOSAzLjcgMTctMjAgMzctNDggMjAtMjIgMjEtMjYgMzUtMzQgMjEtMjZ6bS05MSAzNDgtMTYtNTctMzEtNDYtMzMtMTIgMC4xNSAzLjkgMS42IDQ0IDQuNCAzNiA1LjEgMzQgNC4zIDQwIDIgMzQgMi4zIDM2IDEzIDQyIDQuNS0zNyAxNi0yMiAyMC0zN3ptLTQ3IDE1NC0xMy00Mi0yLjMtMzYtMi0zNC00LjMtNDAtNS4xLTM0LTQuNC0zNi0xLjYtNDQtMC4xNS0zLjktMi44IDMuMi00OCA1NS03LjIgMzcgMC43OCA2NCAyNiA0OCAzMyAyOXptLTE0NS0zOTktMjAgNDMtMTIgNDEtNi4xIDI0LTYuNyAyMCA1OC0yMSAxNS0yNiAxNi00NC00LjItMzctMTItNjEtNS4yIDI0em0yOC02MS0yNyAxOS0yMCAxMS0yOCAyMC0zMSAzMC02LjggNDggMTcgNDIgMjQgMTggMS41LTQuNiA1LjItMTYgNi4xLTI0IDEyLTQxIDIwLTQzIDIyLTM3em0tMTEgMzA1LTE4LTUxLTUyLTM0LTAuMjUgNS44LTAuODMgMTkgMS4yIDM5LTMuMSA0My02LjcgMzgtMTEgNDYtMTUgNjMgMjAtMjUgNDMtNDEgMzAtNDl6bS03MC03OSAwLjI1LTUuOC01NiA0Mi0xNyA2NSAyLjcgNTAgOS40IDQwIDE2IDE3IDguNCA0MCAxNS02MyAxMS00NiA2LjctMzggMy4xLTQzLTEuMi0zOXptLTU0LTE5NC0xMiAyMC0yMiAyNi0xOCAxNS0xNyAxNy0wLjEzLTAuNTYtOS43LTQ1IDIxLTM0IDIzLTEzIDIxLTguMiAzNy0xOS0xNSAxM3ptMjQtNDEtMTUgMTMtOC4zIDI4LTEyIDIwLTIyIDI2LTE4IDE1LTE3IDE3IDQyIDE0IDI0LTQuOCAxNS0xNiA4LjYtMzMgMS41LTI4LTMuNC0yMHptLTExMCAyMDItMjMtNTEtMi44IDQuOS0xOSAzMy0yNyAzOS0zMSAyOC0zOSAyNC0zOCA5LjQgMzIgMS4zIDMxIDEuNiAzMC0wLjI5IDQzLTE2IDMwLTMweiIvPgogPC9nPgo8L3N2Zz4K) is growing larger every year! This page lists different Brightway packages. If you would like to add your own project, simply add it to this page [by opening a pull request](https://github.com/brightway-lca/brightway-documentation/blob/main/sphinx/source/other/ecosystem.md).

```{mermaid}
mindmap
  root((🌿 Brightway))
    id(📈 VISUALIZATION)
        bw2analyzer
        polyviz
    id(🧮 ASSESSMENT)
        bw2calc
        bw_temporalis
        bw2regional
        lca_algebraic
        pathways
        bw_timex
    id(💿 DATABASE)
        bw2data
        bw_processing
        ScenarioLink
    id(🧩 INVENTORY)
        ocelot
        wurst
        futura
        premise
    id(🖋️ IN/OUT)
        bw2io
        ecoinvent_interface
        brightpath
        unfold
    id(💻 WebApp)
        Panel WebApp
    id(🖥️ USER INTERFACE)
       Activity Browser
```

## Core Brightway Libraries

| Project | Description |
| ------- | ----------- |
| [`bw2data`](https://github.com/brightway-lca/brightway2-data) | Project management, graph storage and ORM using SQLite, search |
| [`bw2calc`](https://github.com/brightway-lca/brightway2-calc) | Matrix-based calculations |
| [`bw2io`](https://github.com/brightway-lca/brightway2-io) | [ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load) for LCA data |
| [`bw2analyzer`](https://github.com/brightway-lca/brightway2-analyzer) | Analyze inventory data and LCA results |

## Supporting Brightway Libraries

| Project | Description |
| ------- | ----------- |
| [`bw2parameters`](https://github.com/brightway-lca/brightway2-parameters) | Library for storing, validating, and calculating with parameters |
| [`bw_graph_tools`](https://docs.brightway.dev/projects/graphtools/) | [Path traversal](https://en.wikipedia.org/wiki/Graph_traversal) and graph manipulation |
| [`bw_interface_schemas `](https://github.com/brightway-lca/bw_interface_schemas/) | Interface schemas for data transfer in Brightway |
| [`bw_processing`](https://github.com/brightway-lca/bw_processing) | Tools to create datapackages in a common format  |
| [`bw_simapro_csv`](https://docs.brightway.dev/projects/bw-simapro-csv/) | Importing [SimaPro](http://simapro.com) CSV files into Brightway |
| [`ecoinvent_migrate`](https://github.com/brightway-lca/ecoinvent_migrate) | Code to generate Randonneur migration files for ecoinvent releases |
| [`ecoinvent_interface`](https://github.com/brightway-lca/ecoinvent_interface) | Unofficial python interface to ecoinvent data |
| [`matrix_utils`](https://github.com/brightway-lca/matrix_utils) | Build and iterate on matrices using datapackages |
| [`multifunctional`](https://github.com/brightway-lca/multifunctional) | Multifunctional activities in Brightway  |
| [`pyecospold`](https://github.com/brightway-lca/pyecospold) | Read and write `ecospold` XML versions 1 and 2 |
| [`randonneur_data`](https://github.com/brightway-lca/randonneur_data) | Data for the randonneur ETL library and specification |
| [`randonneur`](https://github.com/brightway-lca/randonneur) | Library to apply flexible changes to datasets |
| [`stats_arrays`](https://github.com/brightway-lca/stats_arrays/) | NumPy array interface for defining uncertain parameters |

## Major Community Projects

| Project | Description |
| ------- | ----------- |
| [`bw_hestia_bridge`](https://docs.brightway.dev/projects/hestiabridge/) | Importing [Hestia](https://www.hestia.earth) data into Brightway |
| [`bw_graph_tools`](https://docs.brightway.dev/projects/graphtools/) | [Path traversal](https://en.wikipedia.org/wiki/Graph_traversal) and graph manipulation in Brightway |
| [`bw_simapro_csv`](https://docs.brightway.dev/projects/bw-simapro-csv/) | Importing [SimaPro](http://simapro.com) CSV files into Brightway |
| [`bw_processing`](https://docs.brightway.dev/projects/bw-processing/) | Creation of structured arrays in a common format |
| [`bw_temporalis`](https://docs.brightway.dev/projects/bw-temporalis/) | [Dynamic LCA](https://doi.org/10.1021/es9030003), considering time in both inventory and impact assessment |
| [`bw_timex`](https://docs.brightway.dev/projects/bw-timex/) | Account for temporal distribution and evolution in [Time-explicit LCA](https://docs.brightway.dev/projects/bw-timex/en/latest/content/theory.html#terminology) |
| [`bw_aggregation`](https://docs.brightway.dev/projects/bw_aggregation) | Flexibly use aggregated unit processes for faster calculations |
| [`bw_regional`](https://docs.brightway.dev/projects/bw-regional/) | Regionalized LCA calculations |

## Other Community Projects

### Projects _extending_ Brightway

| Project | Authors | Development | Contributors | Stargazers |
| ------- | ------- | ----------- | ------------ | ---------- |
| [Activity Browser](https://github.com/LCA-ActivityBrowser/activity-browser) | [Activity Browser team](https://github.com/LCA-ActivityBrowser/activity-browser/graphs/contributors) | ![GitHub last commit](https://img.shields.io/github/last-commit/LCA-ActivityBrowser/activity-browser?logo=GitHub) |  ![GitHub contributors](https://img.shields.io/github/contributors/LCA-ActivityBrowser/activity-browser?logo=GitHub) | ![GitHub Repo stars](https://img.shields.io/github/stars/LCA-ActivityBrowser/activity-browser?style=social)| 
| [`presamples`](https://presamples.readthedocs.io/en/latest/) | [Pascal Lesage](https://github.com/PascalLesage/) | ![GitHub last commit](https://img.shields.io/github/last-commit/PascalLesage/presamples?logo=GitHub) | ![GitHub contributors](https://img.shields.io/github/contributors/PascalLesage/presamples?logo=GitHub) | ![GitHub Repo stars](https://img.shields.io/github/stars/PascalLesage/presamples?style=social) | 
| [`brightway2-aggregated`](https://brightway2-aggregated.readthedocs.io/en/latest/) | [CIRAIG](https://github.com/CIRAIG) | ![GitHub last commit](https://img.shields.io/github/last-commit/CIRAIG/brightway2-aggregated?logo=GitHub) | ![GitHub contributors](https://img.shields.io/github/contributors/CIRAIG/brightway2-aggregated?logo=GitHub) | ![GitHub Repo stars](https://img.shields.io/github/stars/CIRAIG/brightway2-aggregated?style=social) |
| [`bw2landbalancer`](https://github.com/CIRAIG/bw2landbalancer) | [CIRAIG](https://github.com/CIRAIG) | ![GitHub last commit](https://img.shields.io/github/last-commit/CIRAIG/bw2landbalancer?logo=GitHub) | ![GitHub contributors](https://img.shields.io/github/contributors/CIRAIG/bw2landbalancer?logo=GitHub) | ![GitHub Repo stars](https://img.shields.io/github/stars/CIRAIG/bw2landbalancer?style=social) | 
| [`bw2waterbalancer`](https://github.com/CIRAIG/bw2waterbalancer) | [CIRAIG](https://github.com/CIRAIG) | ![GitHub last commit](https://img.shields.io/github/last-commit/CIRAIG/bw2waterbalancer?logo=GitHub) | ![GitHub contributors](https://img.shields.io/github/contributors/CIRAIG/bw2waterbalancer?logo=GitHub) | ![GitHub Repo stars](https://img.shields.io/github/stars/CIRAIG/bw2waterbalancer?style=social) |
| [`lca_algebraic`](https://github.com/oie-mines-paristech/lca_algebraic) | [oie-mines-paristech](https://github.com/oie-mines-paristech) | ![GitHub last commit](https://img.shields.io/github/last-commit/oie-mines-paristech/lca_algebraic?logo=GitHub) | ![GitHub contributors](https://img.shields.io/github/contributors/oie-mines-paristech/lca_algebraic?logo=GitHub) | ![GitHub Repo stars](https://img.shields.io/github/stars/oie-mines-paristech/lca_algebraic?style=social) |
| [`premise`](https://github.com/polca/premise) | [Romain Sacchi](https://github.com/romainsacchi) | ![GitHub last commit](https://img.shields.io/github/last-commit/polca/premise?logo=GitHub) | ![GitHub contributors](https://img.shields.io/github/contributors/polca/premise?logo=GitHub) | ![GitHub Repo stars](https://img.shields.io/github/stars/polca/premise?style=social) |
| [`polyviz`](https://github.com/romainsacchi/polyviz) | [Romain Sacchi](https://github.com/romainsacchi) | ![GitHub last commit](https://img.shields.io/github/last-commit/romainsacchi/polyviz?logo=GitHub) | ![GitHub contributors](https://img.shields.io/github/contributors/romainsacchi/polyviz?logo=GitHub) | ![GitHub Repo stars](https://img.shields.io/github/stars/romainsacchi/polyviz?style=social) |
| [`wurst`](https://github.com/polca/wurst) | [Chris Mutel](https://github.com/cmutel) et al. | ![GitHub last commit](https://img.shields.io/github/last-commit/polca/wurst?logo=GitHub) | ![GitHub contributors](https://img.shields.io/github/contributors/polca/wurst?logo=GitHub) | ![GitHub Repo stars](https://img.shields.io/github/stars/polca/wurst?style=social) |

### Projects _using_ Brightway

| Project | Authors | Development | Contributors | Stargazers |
| ------- | ------- | ----------- | ------------ | ---------- |
| [`lca-global-sensitivity-analysis`](https://github.com/bsteubing/lca-global-sensitivity-analysis) | [bsteubing](https://github.com/bsteubing) | ![GitHub last commit](https://img.shields.io/github/last-commit/bsteubing/lca-global-sensitivity-analysis?logo=GitHub) | ![GitHub contributors](https://img.shields.io/github/contributors/bsteubing/lca-global-sensitivity-analysis?logo=GitHub) | ![GitHub Repo stars](https://img.shields.io/github/stars/bsteubing/lca-global-sensitivity-analysis?style=social) |
| [`modular-lca`](https://github.com/bsteubing/modular-lca) | [bsteubing](https://github.com/bsteubing) | ![GitHub last commit](https://img.shields.io/github/last-commit/bsteubing/modular-lca?logo=GitHub) | ![GitHub contributors](https://img.shields.io/github/contributors/bsteubing/modular-lca?logo=GitHub) | ![GitHub Repo stars](https://img.shields.io/github/stars/bsteubing/modular-lca?style=social) |
