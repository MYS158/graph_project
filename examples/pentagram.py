from graph import Graph
from utils.visualization import draw_graph
import math

def run():

    # Create an instance of an undirected graph:
    graph = Graph()

    # Define nodes:
    nodes = ['A', 'B', 'C', 'D', 'E']
    for node in nodes:
        graph.add_node(node)

    # Define edges in a pentagram form:
    edges = [
        ('A', 'C'),
        ('C', 'E'),
        ('E', 'B'),
        ('B', 'D'),
        ('D', 'A')
    ]
    for origin, destination in edges:
        graph.add_edge(origin, destination)

    # Calculate positions in a circular layout for the pentagon shape:
    pos = {}
    angle_offset = 2 * math.pi / len(nodes)
    radius = 1
    for i, node in enumerate(nodes):
        angle = i * angle_offset + math.pi / 10
        pos[node] = (radius * math.cos(angle), radius * math.sin(angle))

    # Draw the graph:
    draw_graph(
        graph=graph,
        title="Pentagram Structure Visualization",
        node_size=700,
        edge_thickness=2,
        outline_thickness=2,
        font="Times New Roman",
        font_size=10,
        pos=pos,
    )

if __name__ == "__main__":
    run()