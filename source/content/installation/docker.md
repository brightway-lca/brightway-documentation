# Docker Setup

```{admonition} Prerequisites
:class: important
1. Basic knowledge of [Docker](https://www.docker.com).
2. Basic knowledge of [the difference between `brightway2` and `brightway 25`](../faq/brightway.md)
```
Brightway publishes two official docker images:

- [brightway/bw2](https://hub.docker.com/r/brightway/bw2), for brightway 2
- [brightway/bw25](https://hub.docker.com/r/brightway/bw25), for brightway 2.5

Based on the [Jupyter minimal notebook](https://github.com/jupyter/docker-stacks/tree/master/minimal-notebook).

## What it Gives You

| bw2 | bw25 |
|-----|-------|
|+ micromamba | micromamba |
|+ Python 3.11| python 3.12|
|+ Jupyterlab| Jupyterlab|
|+ brightway2 framework| brightway25 framework |

Docker instances are ephemeral. You will almost certainly want to mount a [data volume](https://docs.docker.com/storage/volumes/).

## Usage of bw images

To run an instance of Jupyter Lab, accessible at [localhost:8888](http://localhost:8888/) for **bw2**

    docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes brightway/bw2

and the following for **bw25**:

    docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes brightway/bw25


Jupyterlab also allows you to run iPython sessions or even a terminal.

See the [Jupyter documentation](https://github.com/jupyter/docker-stacks) for more usage options.

## Tags

### brightway2

The [brightway2](https://github.com/brightway-lca/brightway2) docker images are currently built and
tagged based on the following different components of the image

+ brightway2 metapackage version (2.4.7)
+ python version (py310, py311, py312)
+ the python distribution (official python 3 or micromamba)



The following images are built:

| Image Name | components |
| ---------- | ---------- |
| brightway/bw2:latest | brightway 2.4.7, py311, micromamba|
| brightway/bw2:2.4.7-py311-micromamba | brightway 2.4.7, py311, micromamba|
| brightway/bw2:2.4.7-py310-micromamba | brightway 2.4.7, py310, micromamba|


### brightway25

The [brightway25](https://github.com/brightway-lca/brightway25) docker images are currently built and
tagged based on the following different components of the image

+ brightway25 metapackage version (1.1.0)
+ python version (py310, py311, py312)
+ the python distribution (micromamba)

The following images are built:

| Image Name | components |
| ---------- | ---------- |
| brightway/bw25:latest | brightway25 1.1.0, py312, micromamba |
| brightway/bw25:1.1.0-py312-micromamba| brightway25 1.1.0, py312, micromamba |
| brightway/bw25:1.1.0-py311-micromamba| brightway25 1.1.0, py311, micromamba |
| brightway/bw25:1.1.0-py310-micromamba| brightway25 1.1.0, py310, micromamba |
| brightway/bw25:1.1.0-py39-micromamba| brightway25 1.1.0, py39, micromamba |
