from graph import Graph
from utils.visualization import draw_graph
import random

def run():

    # Create an instance of a directed and weighted graph:
    graph = Graph(directed=True, weighted=True)

    # Define neuron layers:
    layers = {
        "Input": ["I1", "I2", "I3"],
        "Hidden": ["H1", "H2", "H3", "H4"],
        "Output": ["O1", "O2"]
    }

    # Add nodes from each layer:
    for layer in layers.values():
        for node in layer:
            graph.add_node(node)

    # Connect nodes between layers and assign random weights:
    for origin in layers["Input"]:
        for destination in layers["Hidden"]:
            weight = round(random.uniform(0.1, 1.0), 1)
            graph.add_edge(origin, destination, weight=weight)
    for origin in layers["Hidden"]:
        for destination in layers["Output"]:
            weight = round(random.uniform(0.1, 1.0), 1)
            graph.add_edge(origin, destination, weight=weight)

    # Colors for each layer:
    node_colors = {**{node: "lightblue" for node in layers["Input"]},
                **{node: "lightgreen" for node in layers["Hidden"]},
                **{node: "lightcoral" for node in layers["Output"]}}

    # Create a dictionary of positions for the layers to be in columns:
    pos = {}
    layer_x_positions = {"Input": 0, "Hidden": 1, "Output": 2}
    layer_y_positions = {
        "Input": [1, 0, -1],
        "Hidden": [1.5, 0.5, -0.5, -1.5],
        "Output": [0.5, -0.5]
    }
    for layer_name, nodes in layers.items():
        x = layer_x_positions[layer_name]
        y_positions = layer_y_positions[layer_name]
        for i, node in enumerate(nodes):
            pos[node] = (x, y_positions[i])

    # Draw the graph:
    draw_graph(
        graph=graph,
        title="Neural Network Structure Visualization",
        node_colors=node_colors,
        node_size=700,
        edge_thickness=2,
        outline_color="black",
        outline_thickness=2,
        font="Times New Roman",
        font_size=10,
        pos=pos,
        show_edge_labels=False
    )
    
if __name__ == "__main__":
    run()