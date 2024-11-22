"""
Depth-First Search (DFS) Algorithm

This algorithm explores as far as possible along each branch before backtracking.
It is useful for exploring a graph's depth and detecting cycles.

Parameters:
- graph: Graph object that provides a get_neighbors method.
- start_node: The node from which to start the traversal.

Returns:
- List of nodes in the order they were visited.
"""

from graph import Graph

def dfs(graph, start):
    if start not in graph.nodes:
        return []
    visited = set()
    path = []
    def _dfs(node):
        visited.add(node)
        path.append(node)
        for neighbor, _ in graph.get_neighbors(node):
            if neighbor not in visited:
                _dfs(neighbor)
    _dfs(start)
    return path