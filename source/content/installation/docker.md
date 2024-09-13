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

## What it gives You

* Miniconda
* Python 3.10
* Jupyterlab
* brightway2 framework

Docker instances are ephemeral. You will almost certainly want to mount a [data volume](https://docs.docker.com/storage/volumes/).

## Usage of bw2 image

To run an instance of Jupyter Lab, accessible at [localhost:8888](http://localhost:8888/):

    docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes brightway/bw2

Jupyterlab also allows you to run iPython sessions or even a terminal.

See the [Jupyter documentation](https://github.com/jupyter/docker-stacks) for more usage options.
