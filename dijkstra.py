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
    costs = {start: 0}
    parents = {}
    unprocessed = [start]

    while unprocessed:
        current_node = min(unprocessed, key=lambda x: costs[x])
        unprocessed.remove(current_node)

        for neighbor in graph[current_node]:
            new_cost = costs[current_node] + graph[current_node][neighbor]["weight"]
            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = current_node
                unprocessed.append(neighbor)

    if goal not in parents:
        return None, None

    path = [goal]
    current_node = goal
    while current_node != start:
        current_node = parents[current_node]
        path.append(current_node)

    return path[::-1], costs[goal]
