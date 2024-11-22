class NodeNotFoundError(Exception):
    # Exception raised when a node is not found in the graph.
    def __init__(self, node):
        super().__init__(f"Node '{node}' not found in the graph.")
        self.node = node

class EdgeNotFoundError(Exception):
    # Exception raised when an edge is not found in the graph.
    def __init__(self, origin, destination):
        super().__init__(f"Edge from '{origin}' to '{destination}' not found in the graph.")
        self.origin = origin
        self.destination = destination
