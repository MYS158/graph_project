from collections import defaultdict
from utils.errors import NodeNotFoundError, EdgeNotFoundError

class Node:
    
    def __init__(self, id, data=None):
        self.id = id
        self.data = data
        
    def __eq__(self, other):
        if isinstance(other, Node):
            return (
                self.id == other.id and
                self.data == other.data
            )
        return False

    def __repr__(self):
        return f"Node({self.id}, data={self.data})"


class Edge:
    
    def __init__(self, origin, destination, weight=1):
        self.origin = origin
        self.destination = destination
        self.weight = weight
        
    def __eq__(self, other):
        if isinstance(other, Edge):
            return (
                self.origin == other.origin and
                self.destination == other.destination and
                self.weight == other.weight
            )
        return False

    def __repr__(self):
        return f"Edge(from={self.origin}, to={self.destination}, weight={self.weight})"

class Graph:
    
    def __init__(self, directed=False, weighted=False):
        self.directed = directed
        self.weighted = weighted
        self.nodes = {}
        self.edges = defaultdict(list)

    def add_node(self, node_id, data=None):
        if node_id not in self.nodes:
            self.nodes[node_id] = Node(node_id, data)

    def add_edge(self, origin, destination, weight=1):
        if origin not in self.nodes or destination not in self.nodes:
            raise NodeNotFoundError("Both nodes must exist in the graph.")
        if not self.weighted:
            weight = 1
        edge = Edge(origin, destination, weight)
        self.edges[origin].append(edge)
        if not self.directed:
            self.edges[destination].append(Edge(destination, origin, weight))

    def remove_node(self, node_id):
        if node_id in self.nodes:
            del self.nodes[node_id]
            self.edges.pop(node_id, None)
            for origin in list(self.edges.keys()):
                self.edges[origin] = [edge for edge in self.edges[origin] if edge.destination != node_id]

    def remove_edge(self, origin, destination):
        if origin in self.edges:
            self.edges[origin] = [edge for edge in self.edges[origin] if edge.destination != destination]
        if not self.directed:
            if destination in self.edges:
                self.edges[destination] = [edge for edge in self.edges[destination] if edge.destination != origin]

    def get_neighbors(self, node_id):
        return [(edge.destination, edge.weight) for edge in self.edges[node_id]]
    
    def degree(self, node_id):
        if not self.directed:
            return len(self.get_neighbors(node_id))
        else:
            return self.in_degree(node_id) + self.out_degree(node_id)

    def in_degree(self, node_id):
        return sum(1 for node in self.nodes if node_id in [neighbor for neighbor, _ in self.get_neighbors(node)])

    def out_degree(self, node_id):
        return len(self.get_neighbors(node_id))

    def has_eulerian_cycle(self):
        def _dfs(start_node, visited):
            stack = [start_node]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    for neighbor, _ in self.get_neighbors(node):
                        if neighbor not in visited:
                            stack.append(neighbor)
        visited = set()
        start_node = next(iter(self.nodes))
        if self.directed:
            # Check in-degrees and out-degrees match for all nodes:
            if any(self.in_degree(node) != self.out_degree(node) for node in self.nodes):
                return False
        else:
            # Check all nodes have even degrees:
            if any(len(self.get_neighbors(node)) % 2 != 0 for node in self.nodes):
                return False
        # Perform DFS to check connectivity:
        _dfs(start_node, visited)
        return all(node in visited for node in self.nodes if self.get_neighbors(node))

    def has_eulerian_path(self):
        def _dfs(start_node, visited):
            stack = [start_node]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    for neighbor, _ in self.get_neighbors(node):
                        if neighbor not in visited:
                            stack.append(neighbor)
        visited = set()
        start_node = next(iter(self.nodes))
        # Ensure to start DFS from a node with neighbors
        while start_node and not self.get_neighbors(start_node):
            start_node = next(iter(self.nodes))
        if not start_node:
            return False  # No nodes with edges to start from
        if self.directed:
            start_nodes = end_nodes = 0
            for node in self.nodes:
                out_deg = self.out_degree(node)
                in_deg = self.in_degree(node)
                if out_deg == in_deg + 1:
                    start_nodes += 1
                elif in_deg == out_deg + 1:
                    end_nodes += 1
                elif in_deg != out_deg:
                    return False
            if not (start_nodes == 1 and end_nodes == 1) and not (start_nodes == 0 and end_nodes == 0):
                return False
        else:
            odd_degree_nodes = sum(1 for node in self.nodes if len(self.get_neighbors(node)) % 2 != 0)
            if odd_degree_nodes not in [0, 2]:
                return False

        _dfs(start_node, visited)
        return all(node in visited for node in self.nodes if self.get_neighbors(node))

    def __eq__(self, other):
        if isinstance(other, Graph):
            return (
                self.directed == other.directed and
                self.weighted == other.weighted and
                self.nodes == other.nodes and
                self.edges == other.edges
            )
        return False

    def __repr__(self):
        return f"Graph(directed={self.directed}, weighted={self.weighted}, nodes={list(self.nodes.keys())}, edges={dict(self.edges)})"