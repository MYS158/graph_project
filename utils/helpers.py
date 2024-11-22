def format_edge(edge):
    # Format an edge for display
    return f"{edge[0]} --({edge[2]})--> {edge[1]}"

def validate_node(node):
    # Check if the node is valid (non-empty and string)
    if not isinstance(node, str) or not node:
        raise ValueError("Node must be a non-empty string.")

def validate_weight(weight):
    # Check if the weight is valid (non-negative number)
    if not isinstance(weight, (int, float)) or weight < 0:
        raise ValueError("Weight must be a non-negative number.")

def get_node_degree(graph, node):
    # Get the degree of a node in the graph
    if node not in graph.nodes:
        raise ValueError(f"Node '{node}' not found in the graph.")
    return len(graph.edges.get(node, [])) + sum(node in edges for edges in graph.edges.values())
