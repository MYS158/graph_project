"""
Breadth-First Search (BFS) Algorithm

This algorithm explores a graph layer by layer, starting from a given node.
It visits all nodes at the present 'depth' level before moving on to nodes
at the next depth level.

Parameters:
- graph: Graph object that provides a get_neighbors method.
- start_node: The node from which to start the traversal.

Returns:
- List of nodes in the order they were visited.
"""

def bfs(graph, start):
    if start not in graph.nodes:
        return []
    visited = set()
    queue = [start]
    path = []
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            path.append(node)
            for neighbor, _ in graph.get_neighbors(node):
                if neighbor not in visited:
                    queue.append(neighbor)
    return path