import argparse
import sys
import timeit

from misc.map_functions import problem_graph, generate_random_map, visualize_map, write_map_to_csv
from algorithms.grassfire import grassfire
from algorithms.dijkstra import dijkstra


def execute_dijkstra(graph_to_use: dict) -> None:
    """
    Executes Dijkstra's algorithm on the given graph and prints the execution time and the shortest path and distance.

    Parameters:
        graph_to_use (dict): The graph to use for the algorithm.

    Returns:
        None
    """
    result = []
    time = timeit.timeit(lambda: result.append(dijkstra(graph_to_use)), number=1)
    print(f'\nDijkstra`s Execution time: {time}')
    print(f'Path: {result[0][0]}')
    print(f'Distance: {result[0][1]}')


def execute_grassfire(graph_to_use: dict) -> None:
    """
    Executes Grassfire's algorithm on the given graph and prints the execution time and the shortest path and distance.

    Parameters:
        graph_to_use (dict): The graph to use for the algorithm.

    Returns:
        None
    """
    result = []
    time = timeit.timeit(lambda: result.append(grassfire(graph_to_use)), number=1)
    print(f'\nGrassfire`s Execution time: {time}')
    print(f'Path: {result[0][0]}')
    print(f'Distance: {result[0][1]}')


def main(args: argparse.Namespace):

    graph_to_use = problem_graph

    if args.gen_map:
        print(f'Using Randomly Generated Map ...')
        graph_to_use = generate_random_map(args)

    if args.visualize:
        visualize_map(graph_to_use)

    if args.dump_map:
        write_map_to_csv(graph_to_use, 'graph_output.csv')

    if args.grassfire or args.all:
        execute_grassfire(graph_to_use)

    if args.dijkstra or args.all:
        execute_dijkstra(graph_to_use)

    else:
        sys.exit(1)


if __name__ == '__main__':
    """ Create Argument NameSpace obj. and pass to main"""

    parser = argparse.ArgumentParser()
    # Required positional argument
    required = parser.add_mutually_exclusive_group(required=True)
    required.add_argument('-a', '--all', action='store_true', default=False, help='Run both algorithms')
    required.add_argument('-d', '--dijkstra', action='store_true', default=False, help='Run Dijkstra`s algorithm only')
    required.add_argument('-g', '--grassfire', action='store_true', default=False, help='Run Grassfire algorithm only')

    extra = parser.add_argument_group('Extra optionals')
    extra.add_argument('--gen_map', default=False, action='store_true',
                       help='set this flag to generate a random map')
    extra.add_argument('-n', '--nodes', type=int, help='set this flag to define number of nodes', default=10)
    extra.add_argument('-e', '--edges', type=int, help='set this flag to define the number of edges', default=20)
    extra.add_argument('-w', '--max_weight', type=int, help='set this flag to define max-weight', default=15)
    extra.add_argument('-v', '--visualize', action='store_true', default=False,
                       help='set this flag to visualize the graph')
    extra.add_argument('--dump_map', action='store_true', default=False,
                       help='set this flag if you would like to dump the map to .csv')

    arguments = parser.parse_args()

    # Execute main
    main(arguments)
