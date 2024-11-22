# Graph Project

Graph Project is a Python library for creating and managing graphs. It supports directed and undirected, weighted and unweighted graphs, along with algorithms like BFS, DFS, Dijkstra's shortest path, Hierholzer's, Kruskal's, and Prim's. The project also provides visualization tools with customizable node and edge properties to represent network structures effectively.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Examples](#examples)
- [Testing](#testing)

## Features
- **Graph Creation**: Supports directed and undirected graphs, with optional weights on edges.
- **Graph Algorithms**: Implements several algorithms, including:
    - Breadth-First Search (BFS)
    - Depth-First Search (DFS)
    - Dijkstra's Shortest Path
    - Hierholzer's Algorithm for Eulerian Circuits
    - Kruskal's Minimum Spanning Tree
    - Prim's Minimum Spanning Tree
- **Visualization**: Provides tools for graph visualization with options for custom colors, edge thickness, node size, and more.

## Installation
1. **Install Python and Visual Studio Code**:
    - Download and install the latest version of Python from the official website: [python.org](https://www.python.org/)
    - Make sure to check the option to add Python to your system PATH during installation.
    - Download and install the latest version of Visual Studio Code from the official website: [visualstudio.com](https://code.visualstudio.com/)
2. **Clone the repository**:
    Use Git to clone the repository or download it directly. If using Git, run the following command in your terminal: 
    ```bash
    git clone https://drive.google.com/drive/folders/1jXMeYYUYiB7u1rKwhD1znut63Tdrv2k2?usp=sharing
    ```
3. **Navigate to the project directory**:
    Open your terminal or command prompt and run: 
    ```bash
    cd graph_project
    ```
4. **Install the required packages**:
    Ensure you have pip installed. If you have Python installed, pip should be included. Run the following command to install the necessary packages:
    ```bash
    pip install -r requirements.txt
    ```
5. **Run the example**:
    After installing the required packages, you can run one of the example codes provided in the examples folder by executing main.py 
    (from examples.<your_example> import run):
    ```bash
    python main.py
    ```
    Make sure to replace `<your_example>` with the actual name of the script you wish to run.
6. **Verify the installation**:
    To verify that everything is working correctly, you can run the unit tests included in the project. Execute the following command:
    ```bash
    python -m unittest discover -s tests
    ```

## Project Structure

The project is organized as follows:

```
graph_project/
│
├── .venv/                   # Virtual environment
│   ├── Include/             # C headers for Python packages
│   ├── Lib/                 # Installed Python libraries
│   ├── Scripts/             # Executables, including Python and pip
│   ├── share/               # Shared files and data for some packages
│   ├── .gitignore           # Ensures the virtual environment isn't pushed to git
│   └── pyvenv.cfg           # Configuration file for the virtual environment
│
├── .vscode/                 # Visual Studio Code settings
│   ├── launch.json          # Debugger configuration
│   └── settings.json        # Custom editor settings
│
├── algorithms/              # Graph algorithms
│   ├── bfs.py               # Breadth-First Search
│   ├── dfs.py               # Depth-First Search
│   ├── dijkstra.py          # Dijkstra's algorithm
│   ├── hierholzer.py        # Hierholzer's algorithm
│   ├── kruskal.py           # Kruskal's algorithm
│   ├── prim.py              # Prim's algorithm
│   └── __init__.py          # Marks this folder as a Python package
│
├── data/                    # Data files for loading graphs
│
├── docs/                    # Documentation
│   ├── LEAME.md             # Documentation in Spanish
│   └── README.md            # Main project documentation in English
│
├── examples/                # Usage examples
│   ├── algorithm_example.py # Example usage of algorithms
│   ├── neural_network.py    # Visualization of a neural network as a graph
│   ├── pentagram.py         # Graphical example with a pentagram
│   └── __init__.py
│
├── tests/                   # Unit tests
│   ├── test_algorithms.py   # Tests for graph algorithms
│   ├── test_graph.py        # Tests for the graph methods
│   └── __init__.py
│
├── utils/                   # Utility functions
│   ├── errors.py            # Custom error classes
│   ├── helpers.py           # Helper functions
│   ├── visualization.py     # Visualization utilities
│   └── __init__.py
│
├── config.py                # Configuration file for global settings
├── graph.py                 # Main Graph class
├── main.py                  # Entry point for the project
└── requirements.txt         # Required Python packages
```

## Usage

### Creating a Graph

To create a basic graph, import the `Graph` class and add nodes and edges:

```python
from graph import Graph
graph = Graph(directed=True, weighted=True)
graph.add_node("A")
graph.add_node("B")
graph.add_edge("A", "B", weight=3)
graph.draw(title="Example Graph")
```

### Algorithms

GraphProject supports several algorithms. Here's an example of using BFS and Dijkstra's algorithm:

```python
from graph import Graph
from algorithms.bfs import bfs
from algorithms.dijkstra import dijkstra

# Create an undirected graph
graph = Graph(directed=False, weighted=True)
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_edge("A", "B", weight=2)
graph.add_edge("B", "C", weight=3)

# Perform BFS
print("BFS Traversal starting from node 'A':")
bfs_result = bfs(graph, "A")
print(bfs_result)

# Perform Dijkstra's algorithm
print("Dijkstra's algorithm starting from node 'A':")
dijkstra_result = dijkstra(graph, "A")
print(dijkstra_result)
```

### Visualization

Customize visual properties like node colors, size, edge thickness, and more:

```python
node_colors = {"A": "red", "B": "green", "C": "blue"}
graph.draw(
    title="Custom Graph",
    node_colors=node_colors,
    node_size=700,
    edge_thickness=2,
    font="Times New Roman",
    font_size=12
)
```

## Examples

The 'examples/' directory contains example scripts demonstrating different use cases:

- `algorithm_example.py`: Basic example of creating and visualizing a graph.
- `neural_network.py`: Example of a neural network structure visualization.
- `pentagram.py`: Visualization of a pentagram-shaped graph.

## Testing

To run the unit tests, use the following command:

```bash
python -m unittest discover tests/
```

This will run tests in `tests/test_graph.py` and `tests/test_algorithms.py` to ensure everything works as expected.

Made by Miguel Muñoz, 2024  
UAEH - Licenciatura en Ciencias Computacionales
