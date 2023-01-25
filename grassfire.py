import heapq
from typing import Union


def grassfire(graph: dict) -> Union[tuple, None]:
    """
    Grassfire Algorithm for finding the shortest path to the GOAL node from START node.

    Parameters:
        graph (dict):
        start_node (str):
        goal (str):

    Returns:
          Union[tuple, None]:
    """
    start_node = 'START'
    goal = 'GOAL'
    if not graph:
        print("The graph is empty.")
        return None

    distances = {node: float('inf') for node in graph.keys()}
    distances[start_node] = 0
    distances[goal] = float('inf')
    queue = [(0, start_node)]
    prev = {node: None for node in graph.keys()}
    prev[start_node] = None

    while queue:
        dist, node = heapq.heappop(queue)
        if node == goal:
            if dist != float('inf'):
                path = []
                while node is not None:
                    path.append(node)
                    node = prev[node]
                path = path[::-1]
                return path, distances[goal]
            else:
                return None
        for neighbor, weight_dict in graph[node].items():
            weight = weight_dict["weight"]
            if distances[neighbor] > dist + weight:
                distances[neighbor] = dist + weight
                prev[neighbor] = node
                heapq.heappush(queue, (distances[neighbor], neighbor))
    return None
