"""
Dijkstra's Algorithm

This algorithm finds the shortest path from a starting node to all other nodes in a weighted graph.
It only works with non-negative weights.

Parameters:
- graph: A weighted Graph object that provides a get_neighbors method, where neighbors return (neighbor, weight).
- start_node: The node from which to start the traversal.

Returns:
- A dictionary with each node as a key and the minimum distance from start_node as the value.
"""

import heapq

def dijkstra(graph, start_node, end_node=None):
    distances = {node_id: float('inf') for node_id in graph.nodes}
    distances[start_node] = 0
    priority_queue = [(0, start_node)] # (distance, node)
    predecessors = {node_id: None for node_id in graph.nodes} # Store the predecessor of each node
    # Algorithm loop:
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        # If the distance is greater than the recorded, skip:
        if current_distance > distances[current_node]:
            continue
        # Explore neighbors:
        for neighbor, weight in graph.get_neighbors(current_node):
            distance = current_distance + weight
            # Update if a shorter path is found:
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    # If end_node is provided, reconstruct only the path to end_node:
    if end_node is not None:
        path = []
        current = end_node
        while current is not None:
            path.append(current)
            current = predecessors[current]
        path.reverse()
        # Return the path to end_node along with its distance:
        if path[0] == start_node:
            return [distances[end_node], [(path[i], path[i+1]) for i in range(len(path)-1)]]
        else:
            return None # No path exists to end_node:
    # If no end_node is provided, return paths for all nodes:
    paths = {}
    for node in graph.nodes:
        path = []
        current = node
        while current is not None:
            path.append(current)
            current = predecessors[current]
        path.reverse()
        # Only include the path if it's not the start node:
        if path[0] == start_node:
            paths[node] = [distances[node], [(path[i], path[i+1]) for i in range(len(path)-1)]]
    return paths  # Return distances along with paths
