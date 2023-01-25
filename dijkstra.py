from typing import List, Tuple


def dijkstra(graph: dict) -> Tuple[List[str], int]:
    """
    Dijkstra's algorithm for finding the shortest path between the START and GOAL nodes in a graph.

    Parameters:
        graph (dict): the graph represented as an adjacency list where each key is a node and the value is a
            dictionary of neighboring nodes and their weights.

    Returns:
        Tuple[List[str], int]: a tuple where the first element is a list of nodes representing the shortest path,
            and the second element is the total weight of that path. Returns (None, None) if no path is found.
    """
    start = 'START'
    goal = 'GOAL'

    # Create a dictionary to store the cost of reaching each node from the start node
    costs = {start: 0}

    # Create a dictionary to store the parent node for each node in the shortest path
    parents = {}

    # Create a list to store the unprocessed nodes
    unprocessed = [start]

    while unprocessed:
        # Get the node with the lowest cost from the unprocessed nodes list
        current_node = min(unprocessed, key=lambda x: costs[x])

        # Remove the current node from the unprocessed nodes list
        unprocessed.remove(current_node)

        # Iterate through the neighbors of the current node
        for neighbour in graph[current_node]:

            # Calculate the new cost to reach the neighbour
            new_cost = costs[current_node] + graph[current_node][neighbour]["weight"]

            # Check if the new cost is lower than the current cost or if the neighbour has not been processed yet
            if neighbour not in costs or new_cost < costs[neighbour]:
                # Update the cost and parent for the neighbour
                costs[neighbour] = new_cost
                parents[neighbour] = current_node

                # Add the neighbour to the unprocessed list
                unprocessed.append(neighbour)

    # Check if there is no path to the goal node
    if goal not in parents:
        return None, None

    # Create a list to store the shortest path
    path = [goal]
    current_node = goal

    # Traverse the parent dictionary to create the path
    while current_node != start:
        current_node = parents[current_node]
        path.append(current_node)

    # Return the reversed path and total cost
    return path[::-1], costs[goal]
