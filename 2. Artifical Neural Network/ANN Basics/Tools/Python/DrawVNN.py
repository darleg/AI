import matplotlib.pyplot as plt
from nnv import NNV

plt.rcParams["figure.figsize"] = (10,10)

TwoLayers = [
    {"title":"input\n(relu)", "units": 3,  "color": "orange", "edges_color":"red", "edges_width":2},
    {"title":"output\n(sigmoid)", "units": 1,"color": "blue"},
]

NNV(TwoLayers, node_radius=10, spacing_layer=60, font_size=22).render(save_to_file="TwoLayers.png")


plt.rcParams["figure.figsize"] = (100,10)

ThreeLayers = [
    {"title":"input\n(relu)", "units": 3, "color": "yellow"},
    {"title":"hidden\n(relu)", "units": 4, "color": "orange", "edges_color":"red", "edges_width":2},
    {"title":"output\n(sigmoid)", "units": 1,"color": "blue"},
        
]


NNV(ThreeLayers, node_radius=10, spacing_layer=60, font_size=24).render(save_to_file="ThreeLayers.pdf")
