"""
Prim's Algorithm

This algorithm finds the Minimum Spanning Tree (MST) for a connected, undirected graph.
It starts from a given node and grows the MST by adding the smallest edge that connects
a node inside the MST to a node outside it.

Parameters:
- graph: A weighted Graph object.
- start_node: The node from which to start building the MST.

Returns:
- A list of edges that form the MST.
"""

import heapq

def prim(graph, start):
    visited = set()
    min_heap = [(0, start)]  # (weight, node)
    mst = []
    while min_heap:
        weight, current_node = heapq.heappop(min_heap)
        if current_node not in visited:
            visited.add(current_node)
            if weight > 0:  # Ignore the initial 0-weight edge
                mst.append((prev_node, current_node, weight))  # Store edge
            neighbors = graph.get_neighbors(current_node)
            for neighbor, edge_weight in neighbors:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor))
                    prev_node = current_node  # Keep track of the previous node
    return mst