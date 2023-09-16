# Cloud Setup

## Amazon AWS Cloud Nine (C9)

You can set up Brightway to run on the Amazon [Cloud 9 service](https://aws.amazon.com/cloud9/).

```{admonition} Prerequisites
:class: important
1. An Amazon AWS account.
2. Basic knowledge of cloud computing.
3. Basic knowledge of [the difference between `brightway2` and `brightway 25`](../faq/brightway.md)
```

1. Create a [new C9 environment](https://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment-main.html).
2. Download and install Brightway using the C9 terminal:

``` bash
wget https://github.com/brightway-lca/brightway2/raw/master/cloud-nine-install.sh && bash cloud-nine-install.sh
```

1.  Click on `Preview > Preview Running Application` to open the introductory Brightway notebook.