"""
Hierholzer's Algorithm

This algorithm finds an Eulerian path or cycle in a graph. An Eulerian path visits every edge in the graph exactly once, and an Eulerian cycle is an Eulerian path that starts and ends at the same node. The algorithm works by following unused edges, backtracking when necessary, and ensuring that every edge is covered exactly once.

Parameters:
- graph: An undirected Graph object that provides a get_neighbors method, where neighbors return (neighbor, weight). The graph must have either all nodes with even degrees (Eulerian cycle) or exactly two nodes with odd degrees (Eulerian path).
- start_node: The node from which to start the traversal. If the graph has an Eulerian cycle, this can be any node with an even degree. If it has an Eulerian path, this should be one of the two nodes with odd degrees.

Returns:
- A list representing the Eulerian path or cycle. If no Eulerian path or cycle exists, it returns an empty list.
"""

from collections import defaultdict
from graph import Graph

def hierholzer(graph, start_node):
    # Check if the graph has either all even degrees (Eulerian cycle)
    # or exactly two nodes with odd degrees (Eulerian path)
    if all(len(graph.get_neighbors(node)) % 2 == 0 for node in graph.nodes) or \
       sum(1 for node in graph.nodes if len(graph.get_neighbors(node)) % 2 != 0) == 2:
        stack = [start_node]
        path = []
        used_edges = defaultdict(set) # To track visited edges
        while stack:
            node = stack[-1]
            neighbors = graph.get_neighbors(node)
            for neighbor, _ in neighbors:
                if neighbor not in used_edges[node]: # Check if the edge has been used
                    stack.append(neighbor)
                    used_edges[node].add(neighbor)
                    used_edges[neighbor].add(node)
                    break
            else:
                path.append(stack.pop())
        return path[::-1] # Return reversed path to get the correct order
    return None
