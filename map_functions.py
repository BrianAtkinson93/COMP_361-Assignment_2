import argparse
import csv
import random
import string
from typing import Dict
import networkx as nx
import matplotlib.pyplot as plt

problem_graph = {
    "START": {"d": {"weight": 3}, 'p': {"weight": 1}, 'e': {"weight": 9}},
    "p": {"q": {"weight": 15}},
    "q": {},
    "h": {"q": {"weight": 4}, "p": {"weight": 4}},
    "e": {"h": {"weight": 8}, "r": {"weight": 2}},
    "r": {"f": {"weight": 2}},
    "f": {"GOAL": {"weight": 2}, "c": {"weight": 3}},
    "c": {"a": {"weight": 2}},
    "a": {},
    "b": {"a": {"weight": 2}},
    "d": {"b": {"weight": 1}, "c": {"weight": 8}, "e": {"weight": 2}},
    "GOAL": {}
}


def generate_random_map(args: argparse.Namespace) -> Dict[str, Dict[str, int]]:
    """
    Generates a random graph with a given number of nodes, edges, and maximum weight.

    Parameters:
        - args (argparse.NameSpace): argparse.NameSpace to pass command line arguments

    Returns:
        - Dict[str, Dict[str, int]]: a dictionary representing the graph, where keys are the nodes and values are a
            dictionary of neighboring nodes and the weights of the edges between them.
    """

    num_nodes, num_edges, max_weight = args.nodes, args.edges, args.max_weight

    problem_graph = {}
    nodes = ["START"] + [random.choice(string.ascii_lowercase) for _ in range(num_nodes)] + ["GOAL"]
    for node in nodes:
        problem_graph[node] = {}

    for _ in range(num_edges):
        node1 = random.choice(nodes)
        node2 = random.choice(nodes)
        while node1 == node2 or node2 in problem_graph[node1]:
            node2 = random.choice(nodes)
        problem_graph[node1][node2] = {"weight": random.randint(1, max_weight)}
    return problem_graph


def visualize_map(graph: dict) -> None:
    """
    Displays the graph visually using NetworkX and Matplotlib

    Parameters:
        - graph (dict): a dictionary representing the graph, where keys are the nodes and values are a dictionary of
            neighboring nodes and the weights of the edges between them.

    Returns:
        - None
    """

    print('Visualizing...')
    G = nx.DiGraph(graph)
    pos = nx.spring_layout(G, k=10)
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_nodes(G, pos, node_size=300, node_color='lightblue')
    nx.draw_networkx_edges(G, pos, width=1, edge_color='black', arrows=True, arrowsize=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
    plt.show()


def write_map_to_csv(graph: dict, file_name: str) -> None:
    """
    Writes the graph to a csv file

    Parameters:
    - graph (dict): a dictionary representing the graph, where keys are the nodes and values are a dictionary of
        neighboring nodes and the weights of the edges between them.
    - file_name (str): a string representing the file_path being passed to open()

    Returns:
    - None
    """
    with open(file_name, mode='w') as csv_file:
        fieldnames = ['Source', 'Destination', 'Weight']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for source in graph:
            for destination in graph[source]:
                writer.writerow(
                    {'Source': source, 'Destination': destination, 'Weight': graph[source][destination]['weight']})
