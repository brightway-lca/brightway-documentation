"""
Plotting the Technosphere Matrix
================================
"""


# %%
# .. admonition:: Prerequisites
#    
#    1. local download of the correct Ecoinvent 3.9 database
#    2. working Brightway installation (:code:`bw2io>0.7.8``)

# brightway packages
import bw2data
import bw2io
# brightway type hints
from bw2io import SingleOutputEcospold2Importer

bw2data.projects.set_current("ecoinvent39")
bw2io.bw2setup()

print("Default biosphere flows:", len(Database("biosphere3")))
print("Default LCIA methods:", len(methods))

path_dir_datasets_ecoinvent39: str = '/Users/<USER>/<PATH_TO_ECOINVENT_39>/datasets'

ecoinvent39_importer: SingleOutputEcospold2Importer = bw2io.SingleOutputEcospold2Importer(
    dirpath = path_dir_datasets_ecoinvent39,
    db_name = 'ei39'
)
ecoinvent39_importer.apply_strategies()
ecoinvent39_importer.statistics()

bw2data.Database('ei39').graph_technosphere()

# %%
# .. image:: ./examples/visualizations/graph_technosphere.png
#    :alt: An example image

# sphinx_gallery_thumbnail_path = './examples/visualizations/graph_technosphere.png'
