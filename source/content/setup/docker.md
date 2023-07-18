# Using docker images to run brightway

brightway publishes the following official docker images, one per current brightway versions (2 and 2.5):

+ [brightway/bw2](https://hub.docker.com/r/brightway/bw2), for brightway 2
+ [brightway/bw25](https://hub.docker.com/r/brightway/bw25), for brightway 2.5


Based on the [Jupyter minimal notebook](https://github.com/jupyter/docker-stacks/tree/master/minimal-notebook).

## What it Gives You

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

## Tags

### brightway2

The [brightway2](https://github.com/brightway-lca/brightway2) docker images are currently built and
tagged based on the following different components of the image

+ brightway2 metapackage version (2.4.3)
+ python version (py310, py311, py312)
+ the python distribution (official python 3 or miniconda3)
+ Ecoinvent 3.X compatibility (3.8, 3.9) version [^1]

The following images are built:

| Image Name | components |
| ---------- | ---------- |
| brightway/bw2:latest | brightway 2.4.3, py310, miniconda3, compatible with ecoinvent 3.9 |
| brightway/bw2:2.4.3-py310-miniconda3-ecoinvent-3.9 |
| brightway/bw2:2.4.3-py310-miniconda3-ecoinvent-3.8 |



[^1]: Until a release of [bw2io](https://github.com/brightway-lca/brightway2-io) that is compatible with any ecoinvent version and all bw2x.
