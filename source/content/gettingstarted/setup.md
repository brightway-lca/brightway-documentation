# Setup

Brightway is a Python software package. You can use Brightway in a Python script (`.py` file) or in an interactive Jupyter Notebook (`.ipynb` file).

## Import Python Packages

Which Python packages do I have to import?

```{note}
`brightway2` is a metapackage. It just loads other Brightway packages like `bw2data`, `bw2calc`, `bw2io`, etc.
It is recommended to import the individual packages directly. That way, you can see where each function comes from.
```

```python
import bw2analyzer as ba
import bw2calc as bc
import bw2data as bd
import bw2io as bi
```

You may also want to import some of the most important data science packages:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

## Saving Python Packages

How do I save my Python environment so that I can use it later? \
How can I make sure that my code works on another computer?

```python
conda activate <ENVIRONMENT_NAME>
conda env export --from-history > "<PATH_TO_FILE>/<FILE_NAME>.yml"
```

```{admonition} FAQ Pages
:class: seealso
[Environment Management](../faq/environment_management.md)
```