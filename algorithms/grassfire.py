import heapq
from typing import Union


def grassfire(graph: dict) -> Union[tuple, None]:
    """
    Grassfire Algorithm for finding the shortest path from the 'START' node to the 'GOAL' node in a graph represented
        as an adjacency list.

    Parameters:
        - graph (dict): The graph represented as an adjacency list. Each key is a node and its value is a dictionary
            of edges with weights.
                e.g. { 'A': {'B': {'weight': 2}, 'C': {'weight': 4}}, 'B': {'D': {'weight': 1}} }

    Returns:
        - Union[tuple, None]: A tuple of a list of nodes representing the shortest path and the total distance of the
         path, or None if no path is found.

    Notes:
        - Grassfire algorithm uses a heap to determine the next node to process.The Grassfire Algorithm uses a
            distance dictionary and a previous node dictionary to keep track of the minimum distance to a node and the
            previous node in the shortest path. The algorithm stops when the goal node is dequeued from the heap
    """
    start_node = 'START'
    goal = 'GOAL'

    # Checking if the graph is empty
    if not graph:
        print("The graph is empty.")
        return None

    # Creating a dictionary to store the shortest distance to each node
    distances = {node: float('inf') for node in graph.keys()}

    # Set the distance to the start node as 0
    distances[start_node] = 0

    # Set the distance to the goal node as infinity
    distances[goal] = float('inf')

    # Create a queue with the start node
    queue = [(0, start_node)]

    # Create a dictionary to store the previous node in the shortest path to each node
    prev = {node: None for node in graph.keys()}
    prev[start_node] = None

    while queue:
        # Get the node with the smallest distance from the queue
        dist, node = heapq.heappop(queue)

        # Check if the current node is the goal node
        if node == goal:

            # If the distance is not infinity, create the shortest path
            if dist != float('inf'):
                path = []

                # Traverse the previous node dictionary to create the path
                while node is not None:
                    path.append(node)
                    node = prev[node]

                # Reverse the path and return it with the total distance
                path = path[::-1]
                return path, distances[goal]

            else:
                return None

        # Iterate through the neighbors of the current node
        for neighbor, weight_dict in graph[node].items():
            weight = weight_dict["weight"]

            # Check if the new distance to the neighbor is shorter than the current distance
            if distances[neighbor] > dist + weight:
                # Update the distance and previous node for the neighbor
                distances[neighbor] = dist + weight
                prev[neighbor] = node

                # Add the neighbor to the queue
                heapq.heappush(queue, (distances[neighbor], neighbor))

    # If the goal node is not reached, return None
    return None
