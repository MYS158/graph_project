from config import VISUALIZATION_SETTINGS
from matplotlib import colors as mcolors
import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(graph, **kwargs):
    settings = {**VISUALIZATION_SETTINGS, **kwargs}
    def get_text_color(bg_color):
        try:
            bg_color = mcolors.to_hex(bg_color)
        except ValueError:
            pass
        r, g, b = int(bg_color[1:3], 16), int(bg_color[3:5], 16), int(bg_color[5:7], 16)
        luminosity = (0.299 * r + 0.587 * g + 0.114 * b) / 255
        return "black" if luminosity > 0.5 else "white"
    G = nx.DiGraph() if graph.directed else nx.Graph()
    G.add_nodes_from(graph.nodes.keys())
    for origin in graph.edges:
        for edge in graph.edges[origin]:
            G.add_edge(edge.origin, edge.destination, weight=edge.weight)
    default_node_color = "blue"
    node_colors_list = [settings["node_colors"].get(node.id, default_node_color) if settings["node_colors"] else default_node_color for node in graph.nodes.values()]
    node_text_colors = [get_text_color(color) for color in node_colors_list]
    if settings["pos"] is None:
        settings["pos"] = nx.spring_layout(G)
    nx.draw_networkx_nodes(
        G, 
        settings["pos"], 
        node_color=node_colors_list, 
        node_size=settings["node_size"], 
        edgecolors=settings["outline_color"], 
        linewidths=settings["outline_thickness"]
    )
    nx.draw_networkx_labels(
        G, 
        settings["pos"], 
        font_size=settings["font_size"], 
        font_family=settings["font"],
        font_weight="bold",
        font_color=dict(zip(G.nodes, node_text_colors))
    )
    arrow_size = settings["node_size"] / 45
    edge_colors_list = []
    for edge in G.edges:
        if settings["edge_colors"] and edge in settings["edge_colors"]:
            edge_colors_list.append(settings["edge_colors"][edge])
        else:
            edge_colors_list.append("black")
    if graph.directed:
        nx.draw_networkx_edges(
            G, 
            settings["pos"],
            arrowstyle='-|>',
            arrowsize=arrow_size,
            width=settings["edge_thickness"],
            edge_color=edge_colors_list
        )
    else:
        nx.draw_networkx_edges(
            G, 
            settings["pos"], 
            width=settings["edge_thickness"], 
            edge_color=edge_colors_list
        )
    if settings["show_edge_labels"] and graph.weighted:
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(
            G, 
            settings["pos"], 
            edge_labels=labels, 
            font_size=settings["font_size"], 
            font_family=settings["font"], 
            font_color="black",
            rotate=False
        )
    plt.title(settings["title"], fontdict={'family': settings["font"], 'color': 'black', 'weight': 'normal', 'size': 16})
    plt.axis('off')
    plt.show()
