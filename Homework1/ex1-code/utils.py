import networkx as nx
import yaml
import random
import matplotlib.pyplot as plt
import os

# draw flows and capacities
def draw_all(G, save_fig=True):
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
    format = lambda data : f"flow = {data['flow']}\ncapacity = {data['capacity']}"
    edge_labels = {(x, y): format(data) for x, y, data in edge_labels}

    # set up color_mapping and pos
    color_mapping = nx.get_node_attributes(G, 'color').values()
    layout = nx.get_node_attributes(G, 'pos')
    
    # draw graph with edge labels
    nx.draw(G, layout, node_color=color_mapping, with_labels=True)
    nx.draw_networkx_edge_labels(G, layout, edge_labels=edge_labels)
    plt.title(f"Graph with flow and capacity attributes")

    # save it
    if save_fig:
        plt.savefig(f"plots/graph_flow_capacity.png")
    plt.show()

# functions which can be useful
def draw(G, attribute='name', save_fig=True):
    """
    Draw a graph with optional edge labels and save it as a PNG file.

    Parameters:
    - G (networkx.Graph): The graph to be drawn.
    - attribute (str): The attribute to be used as edge labels (default: 'name').
    - save_fig (bool): Whether to save the figure as a PNG file (default: True).
    """
    # set up color_mapping and pos
    color_mapping = nx.get_node_attributes(G, 'color').values()
    layout = nx.get_node_attributes(G, 'pos')

    # set up edge_labels
    edge_labels = nx.get_edge_attributes(G, attribute)

    # draw graph with edge labels
    nx.draw(G, layout, node_color=color_mapping, with_labels=True)
    nx.draw_networkx_edge_labels(G, layout, edge_labels=edge_labels)
    plt.title(f"Graph with {attribute} attribute")
    
    # save it
    if save_fig:
        plt.savefig(f"plots/graph_{attribute}.png")
    plt.show()

def update_edge_flows(G, source='o', dest='d'):
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
    max_flow = nx.maximum_flow(G, source, dest)

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

def update_residual_capacities(G, source='o', dest='d'):
    """Update residual capacities of edges in G

    Args:
        G (nx.DiGraph): graph
        source (str, optional): source node. Defaults to 'o'.
        dest (str, optional): destination node. Defaults to 'd'.

    Returns:
        dict: dictionary of residual capacities of edges
    """
    edge_flows = nx.get_edge_attributes(G, 'flow')
    edge_capacities = nx.get_edge_attributes(G, 'capacity')

    # compute residual capacities
    residual_capacities = {
        edge: edge_capacities[edge] - edge_flows[edge]
        for edge in G.edges
    }

    # update attribute
    nx.set_edge_attributes(G, residual_capacities, 'residual_capacity')

    # return them
    return residual_capacities

def create_G():
    """
    Creates a directed graph G with predefined nodes, edges, attributes, and capacities.

    Returns:
    G (networkx.DiGraph): The created directed graph.
    """
    # create graph
    G = nx.DiGraph()

    # edges list
    edges = [('o','a'),('o','b'),('a','d'),('b','d'),('b','c'),('c','d')]

    # add edges
    G.add_edges_from(edges) 

    # setup graph layout
    layout = {
        'o':(0,0), 
        'd':(1,0), 
        'a':(0.5,0.5), 
        'b':(0.5,0), 
        'c':(0.5,-0.5)
    }
    nx.set_node_attributes(G, layout, 'pos')

    # setup node colors
    color_mapping = {
        'o':'red', 
        'd':'green', 
        'a':'blue', 
        'b':'blue', 
        'c':'blue'
    }
    nx.set_node_attributes(G, color_mapping, 'color')

    # setup edges names
    edge_names = {
        ('o','a'):'e1', 
        ('o','b'):'e3', 
        ('a','d'):'e2', 
        ('b','d'):'e4', 
        ('b','c'):'e5', 
        ('c','d'):'e6'
    }
    nx.set_edge_attributes(G, edge_names, 'name')

    # edge capacities
    edge_capacities = {
        ('o','a'): 3, 
        ('o','b'): 3, 
        ('a','d'): 2, 
        ('b','d'): 2, 
        ('b','c'): 3, 
        ('c','d'): 1
    }
    nx.set_edge_attributes(G, edge_capacities, 'capacity')    
    return G