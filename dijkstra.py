from typing import Any, List, Tuple


def dijkstra(graph: dict) -> Tuple[List[str], int]:
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