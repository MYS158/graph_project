from graph import Graph
from utils.visualization import draw_graph
from algorithms.dijkstra import dijkstra

def run():

    # Create the graph:
    graph = Graph(weighted=True)
    nodes = [
        "UAEH", 
        "FDA", 
        "FDP", 
        "TIN", 
        "ABA", 
        "INM", 
        "LAV", 
        "C&C", 
        "UBI", 
        "KIN", 
        "FG", 
        "DES"
    ]
    for node in nodes:
        graph.add_node(node)
    edges = [
        ("UAEH", "FDA", 400),
        ("FDA", "FDP", 1200),
        ("FDP", "LAV", 140),
        ("FDP", "TIN", 140),
        ("TIN", "ABA", 120),
        ("ABA", "INM", 220),
        ("INM", "KIN", 260),
        ("KIN", "DES", 150),
        ("LAV", "C&C", 170),
        ("TIN", "C&C", 170),
        ("ABA", "UBI", 190),
        ("C&C", "UBI", 210),
        ("UBI", "KIN", 210),
        ("LAV", "FG", 350),
        ("FG", "DES", 250)
    ]
    for source, destination, weight in edges:
        graph.add_edge(source, destination, weight)

    # Dijkstra's algorithm:
    shortest_path = dijkstra(graph, "UAEH", "DES")
    shortest_path_length = shortest_path[0]
    shortest_path_edges = shortest_path[1]
    shortest_path_nodes = [shortest_path_edges[0][0]]
    shortest_path_nodes += [edge[1] for edge in shortest_path_edges]
    print("\nDijkstra's algorithm results:")
    print(f"- Shortest path nodes: {shortest_path_nodes}")
    print(f"- Shortest path edges: {shortest_path_edges}")
    print(f"- Shortest path length: {shortest_path_length}")
    
    # Define custom colors:
    node_colors = {node: "lightblue" for node in nodes}
    node_colors["UAEH"] = "gold"
    node_colors["DES"] = "orange"
    edge_colors = {edge: "black" for edge in edges}
    for edge in shortest_path_edges:
        edge_colors[(edge[0], edge[1])] = "red"
        edge_colors[(edge[1], edge[0])] = "red"

    # Create a dictionary of positions:
    pos = {
        "UAEH": (0.0, 0.0),
        "FDA": (-0.000944, 0.001723),
        "FDP": (0.000785, 0.00409),
        "TIN": (0.002031, 0.003272),
        "INM": (0.004538, 0.001471),
        "ABA": (0.0032, 0.0025),
        "DES": (0.007, 0.005),
        "FG": (0.0045, 0.0051),
        "LAV": (0.001654, 0.005013),
        "C&C": (0.002924, 0.004329),
        "UBI": (0.0044, 0.0037),
        "KIN": (0.0059, 0.0033)
    }

    # Draw the graph with custom settings:
    draw_graph(
        graph=graph,
        title="Shortest path from UAEH to DES",
        node_colors=node_colors,
        edge_colors=edge_colors,
        node_size=700,
        edge_thickness=2,
        outline_color="black",
        outline_thickness=2,
        font="Times New Roman",
        font_size=8,
        pos=pos,
        show_edge_labels=True
    )

if __name__ == "__main__":
    run()
