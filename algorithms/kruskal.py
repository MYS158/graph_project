"""
Kruskal's Algorithm

This algorithm finds the Minimum Spanning Tree (MST) for a connected, undirected graph.
It sorts all edges by weight and adds edges to the MST as long as they don't form a cycle.

Parameters:
- graph: A Graph object that provides edges with weights in (origin, destination, weight) format.

Returns:
- A list of edges that form the MST.
"""

from graph import Edge

class UnionFind:
    def __init__(self):
        self.parent = {}
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            self.parent[root2] = root1  # Union the trees
    def add(self, node):
        if node not in self.parent:
            self.parent[node] = node  # Initialize parent

def kruskal(graph):
    edges = []
    for origin, edge_list in graph.edges.items():
        for edge in edge_list:
            if graph.directed or (edge.destination, edge.origin, edge.weight) not in edges:
                edges.append((edge.origin, edge.destination, edge.weight))
    # Sort edges by weight
    edges.sort(key=lambda edge: edge[2])
    uf = UnionFind()
    mst = []
    for origin, destination, weight in edges:
        uf.add(origin)
        uf.add(destination)
        if uf.find(origin) != uf.find(destination):
            uf.union(origin, destination)
            mst.append(Edge(origin, destination, weight))
    return mst
