# Running on the Cloud

## Docker

Docker is one of the easiest ways to run Brightway on a server. The [Brightway2 Dockerfile](https://hub.docker.com/r/cmutel/brightway2/) is based on the [Jupyter minimal-notebook](https://github.com/jupyter/docker-stacks/tree/master/minimal-notebook) Docker file, and lets you run a notebook server or iPython shell.

To run the Brightway2 Docker file:

1.  [Install Docker](https://docs.docker.com/engine/installation/)
2.  Run the Docker file:

``` bash
docker run -d -p 8888:8888 jupyter/minimal-notebook
```

```{note}
This will start a detached container (`-d`) with port `8888` on your machine forwarded to port `8888` in the container, where the notebook server is listening.
```

3. Start an iPython shell:

``` bash
docker run -i -t --entrypoint ipython cmutel/brightway2
```

```{note}
This creates an container with STDIN open (`-i`) and a TTY shell (`-t`). Instead of running the  `start-notebook.sh` shell, this uses a different `entrypoint`.
```

3. Alternatively, start a Bash shell:

``` bash
docker run -i -t --entrypoint bash cmutel/brightway2
```
### Using Data Volumes

The default data directory in the Docker container is `/home/jovyan/data/`. You can use an existing data directory by [mounting a data volume](https://docs.docker.com/storage/volumes/), e.g.:

``` bash
docker run -i -t -v "/Users/cmutel/Library/Application Support/Brightway3":/home/jovyan/data --entrypoint ipython cmutel/brightway2
```

```{warning}
Compare the [Jupyter minimal-notebook documentation](https://github.com/jupyter/docker-stacks/tree/master/minimal-notebook) for information on how to secure your server using https.
```

You may also want to mount the following:

| directory | description | 
| --------- | ----------- |
| `/home/jovyan/notebooks` | directory in which the notebook server starts |
| `/home/jovyan/output` | output directory for most Brightway IO functions |

## Amazon AWS Cloud Nine (C9)

1. Create an [Amazon AWS account] to use the [Cloud 9 service](https://aws.amazon.com/cloud9/?nc1=h_ls).
2. Create a [new C9 environment](https://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment-main.html).
3. Download and install Brightway using the C9 terminal:

``` bash
wget https://github.com/brightway-lca/brightway2/raw/master/cloud-nine-install.sh && bash cloud-nine-install.sh
```

1.  Click on `Preview > Preview Running Application` to open the introductory Brightway notebook. You can also copy/paste the URL into a new tab.
