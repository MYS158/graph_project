from graph import Graph
from utils.visualization import draw_graph
from algorithms import *

def run():
    
    # Create the graph
    graph = Graph(directed=False, weighted=True)

    # List of nodes to add
    nodes = ["A", "B", "C", "D", "E", "F"]
    for node in nodes:
        graph.add_node(node)

    # List of edges with weights to add
    edges_with_weights = [
        ("A", "C", 1),
        ("A", "E", 2),
        ("B", "C", 3),
        ("B", "D", 4),
        ("C", "D", 5),
        ("C", "E", 6),
        ("D", "E", 7),
        ("D", "F", 8),
        ("E", "F", 9),
    ]
    for origin, destination, weight in edges_with_weights:
        graph.add_edge(origin, destination, weight=weight)

    # Run and print the results of BFS
    print("BFS Traversal starting from node 'A':")
    bfs_result = bfs(graph, "A")
    print(bfs_result)
    print()

    # Run and print the results of DFS
    print("DFS Traversal starting from node 'A':")
    dfs_result = dfs(graph, "A")
    print(dfs_result)
    print()

    # Run and print the results of Dijkstra's algorithm
    print("Dijkstra's algorithm starting from node 'A':")
    dijkstra_result = dijkstra(graph, "A")
    for node in dijkstra_result:
        distance, path = dijkstra_result[node]
        print(f"- To '{node}': Distance = {distance}, Path = {path}")
    print()

    # Run and print the results of Hierholzer's algorithm
    print("Running Hierholzer's algorithm for Eulerian path or cycle:")
    if hierholzer(graph, "A") == None:
        print("Graph does not have an Eulerian path or cycle.")
    if graph.has_eulerian_cycle():
        print("Graph has an Eulerian cycle.")
        eulerian_path = hierholzer(graph, "A")
        print("Eulerian cycle: ", eulerian_path)
    elif graph.has_eulerian_path():
        print("Graph has an Eulerian path.")
        eulerian_path = hierholzer(graph, "A")
        print("Eulerian path: ", eulerian_path)
    print()

    # Run and print the results of Kruskal's algorithm
    print("Kruskal's algorithm for Minimum Spanning Tree:")
    kruskal_result = kruskal(graph)
    kruskal_edges = [(edge.origin, edge.destination, edge.weight) for edge in kruskal_result]
    print(kruskal_edges)
    print()

    # Run and print the results of Prim's algorithm
    print("Prim's algorithm for Minimum Spanning Tree starting from node 'A':")
    prim_result = prim(graph, "A")
    prim_edges = [(origin, destination, weight) for origin, destination, weight in prim_result]
    print(prim_edges)
    print()

    # Prepare edge colors for visualization
    edge_colors = {}

    # Set MST edges to red
    for edge in kruskal_result:
        edge_colors[(edge.origin, edge.destination)] = "red"
        edge_colors[(edge.destination, edge.origin)] = "red"

    # Set non-MST edges to black
    for origin, edges in graph.edges.items():
        for edge in edges:
            if (edge.origin, edge.destination) not in edge_colors:
                edge_colors[(edge.origin, edge.destination)] = "black"
                edge_colors[(edge.destination, edge.origin)] = "black"

    # Visualize the graph with edge colors
    draw_graph(
        graph, 
        title="Undirected Weighted Graph with MST Highlighted", 
        node_colors={"A": "red", "B": "green", "C": "blue", "D": "yellow", "E": "purple", "F": "orange"},
        show_edge_labels=True,
        edge_colors=edge_colors
    )

if __name__ == "__main__":
    run()