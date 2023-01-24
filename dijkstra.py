import heapq


def dijkstra(graph: dict, start: str, goal: str) -> tuple | None:
    """

    Finds the shortest path from the starting node to the goal node using Dijkstra's algorithm.

    Parameters:
    - graph (dict): a dictionary representing the graph, where keys are the nodes and values are a dictionary of
                    neighboring nodes and the weights of the edges between them.
    - start (str): the starting node
    - goal (str): the goal node

    Returns:
    - tuple: a tuple of two elements, the first element is a list representing the path from start to goal,
             and the second element is the distance from the start to the goal. If there is no path from start to goal
             the function returns None.
    """
    # Initialize the distances of all nodes to infinity
    distances = {node: float('inf') for node in graph}
    # Set the distance of the starting node to 0
    distances[start] = 0
    # initialize the queue with the starting node and its distance
    queue = [(0, start)]
    # initialize the prev dictionary to keep track of the previous node for each node on the path
    prev = {node: None for node in graph}

    # Repeat the following steps until the goal node is reached or the queue is empty
    while queue:
        # pop the node with the shortest distance from the queue
        dist, node = heapq.heappop(queue)
        if node == goal:
            # if the goal is reached check if the goal node is reachable
            if prev[goal] is not None:
                # backtrack the path using the prev dictionary
                path = []
                while node is not None:
                    path.append(node)
                    node = prev[node]
                # return the path and the distance from the start to the goal
                return list(reversed(path)), distances[goal]
            else:
                return None
        for neighbor, weight in graph[node].items():
            if distances[neighbor] > dist + weight:
                distances[neighbor] = dist + weight
                prev[neighbor] = node
                heapq.heappush(queue, (distances[neighbor], neighbor))
    return None
