import networkx as nx
import os
import matplotlib.pyplot as plt

def create_G(people, books, interests):
    # Create a directed graph
    G = nx.DiGraph()
    # Add nodes for people and books
    G.add_nodes_from(people, color='blue', bipartite=0)
    G.add_nodes_from(books, color='blue', bipartite=1)
    # create list from interests
    interests = [(p, b) for p, books in interests.items() for b in books]
    # Add edges representing the interests of the people
    G.add_edges_from(interests)
    # position of the nodes
    pos = nx.bipartite_layout(G, people)
    pos = {k: (v[0], v[1]) for k, v in pos.items()}
    # add nodes attributes position
    nx.set_node_attributes(G, pos, 'pos')
    return G

def save_G(G, path = "plots/graph.gml"):
    # get the folder path
    folder_path = os.path.dirname(path)
    # check if plots folder exists
    os.makedirs(folder_path, exist_ok=True)
    # save the graph
    nx.write_gml(G, path)

def load_G(path = "plots/graph.gml"):
    # check if plots folder exists
    if not os.path.exists(path):
        return None
    return nx.read_gml(path)

def draw_G(G, title = "Graph", edge_attribute = None, path = None):
    # get the position of the nodes
    pos = nx.get_node_attributes(G, 'pos')
    # get the color of the nodes
    node_color = [c for c in nx.get_node_attributes(G, 'color').values()]
    # draw the graph
    nx.draw(G, pos, node_color=node_color, node_size=500, with_labels=True)
    # draw the edge labels
    if edge_attribute:
        edge_labels = nx.get_edge_attributes(G, edge_attribute)
        nx.draw_networkx_edge_labels(G, pos, label_pos=0.8, edge_labels=edge_labels)
    # set the title
    plt.title(title)
    # save it
    if path:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        plt.savefig(path)
    plt.show()

def add_source_sink(G, people, books, source='o', sink='d'):
    # add source and sink
    G.add_node(source, color='red', pos=(-2, 0))
    G.add_node(sink, color='green', pos=(2, 0))
    # add edges from source to people
    G.add_edges_from([(source, p) for p in people])
    # add edges from books to sink
    G.add_edges_from([(b, sink) for b in books])
    return G

def remove_source_sink(G, source='o', sink='d'):
    # remove source and sink
    G.remove_node(source)
    G.remove_node(sink)

def update_edge_flows(G, source='o', sink='d'):
    """
    Update the edge flows in a network graph.

    Parameters:
    - G (networkx.Graph): The network graph.
    - source (str): The source node.
    - dest (str): The destination node.

    Returns:
    - edge_flows (dict): A dictionary where keys are edges and values are flows.
    """
    # find maximum flow
    max_flow = nx.maximum_flow(G, source, sink)
    # convert maximum flow to dictionary, keys are edges, values are flows
    edge_flows = {
        (x, y): flow
        for x, dictionary in max_flow[1].items()
        for y, flow in dictionary.items()
    }
    #update attribute
    nx.set_edge_attributes(G, edge_flows, 'flow')
    # return them
    return edge_flows

# draw flows and capacities
def draw_all_G(G, path=None, title="Graph with flow and capacity attributes"):
    """
    Draw the graph G with flow and capacity attributes.

    Parameters:
    - G: NetworkX graph object
        The graph to be drawn.
    - save_fig: bool, optional (default=True)
        Whether to save the figure as an image file.
    """
    # create labels
    edge_labels = list(G.edges(data=True))
    format = lambda data : f"{data['flow']}/{data['capacity']}"
    edge_labels = {(x, y): format(data) for x, y, data in edge_labels}

    # set up color_mapping and pos
    node_color = nx.get_node_attributes(G, 'color').values()
    pos = nx.get_node_attributes(G, 'pos')
    
    # draw graph with edge labels
    edge_colors = ['green' if G[x][y]['flow'] else 'lightgray'
        for x,y in G.edges
    ]
    nx.draw(G, pos, node_color=node_color, node_size=500, with_labels=True, edge_color=edge_colors)
    nx.draw_networkx_edge_labels(G, pos, label_pos=0.8, edge_labels=edge_labels)
    plt.title(title)

    # add a legend
    plt.legend(handles=[
        plt.Line2D([], [], color='green', label='Flow'),
        plt.Line2D([], [], color='lightgray', label='No flow')
    ])

    # save it
    if path:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        plt.savefig(path)
    plt.show()