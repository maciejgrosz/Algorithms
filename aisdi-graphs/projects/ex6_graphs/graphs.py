from queue import PriorityQueue
import sys

INF = 1000000

def read_file(filename: str):
    array = []
    with open(filename, 'r') as file:
        for line in file: # read rest of lines
            row = [int(n) for n in line.split()]
            array.extend(row)
    dims = (len(row), int(len(array)/len(row))) # (width, height)
    return array, dims

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[INF for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight

def board_to_graph(board: list, dims: tuple, graph: Graph):
    for i, v in enumerate(board):
        if i < dims[0]: # top
            if i % dims[0] == 0:  # left
                graph.add_edge(i, i+1, board[i+1])
                graph.add_edge(i, i+dims[0], board[i+dims[0]])
            elif i % dims[0] == dims[0]-1: # right
                graph.add_edge(i, i+1, board[i-1])
                graph.add_edge(i, i+dims[0], board[i+dims[0]])
            else:
                graph.add_edge(i, i+1, board[i+1])
                graph.add_edge(i, i-1, board[i-1])
                graph.add_edge(i, i+dims[0], board[i+dims[0]])

        elif i >= dims[0] * (dims[1]-1): # bottom
            if i % dims[0] == 0:  # left
                graph.add_edge(i, i+1, board[i+1])
                graph.add_edge(i, i-dims[0], board[i-dims[0]])
            elif i % dims[0] == dims[0]-1: # right
                graph.add_edge(i, i-1, board[i-1])
                graph.add_edge(i, i-dims[0], board[i-dims[0]])
            else:
                graph.add_edge(i, i+1, board[i+1])
                graph.add_edge(i, i-1, board[i-1])
                graph.add_edge(i, i-dims[0], board[i-dims[0]])
        else:
            graph.add_edge(i, i+1, board[i+1])
            graph.add_edge(i, i-1, board[i-1])
            graph.add_edge(i, i+dims[0], board[i+dims[0]])
            graph.add_edge(i, i-dims[0], board[i-dims[0]])

def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)} # initial priority queue full of inf for each node beside starting one
    D[start_vertex] = 0

    pq = PriorityQueue() # holds neighbours, expands cheapest nodes
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != INF: # if there is connection
                distance = graph.edges[current_vertex][neighbor] # take the distance
                if neighbor not in graph.visited: # if it is not visited then compare costs
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost: 
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

# TODO: make it in dijkstra function, more simple
def get_path(result, graph, start, end):
    results_dic = [(k, v) for k, v in result.items()]
    path = [end]
    visited = [end]
    x = end
    while x is not start:
        neighbours = [i for i, x in enumerate(graph.edges[x]) if x != INF]
        neighbours_dic = [i for i in results_dic if i[0] in neighbours]
        min_neighbour = min(neighbours_dic, key=lambda t: t[1])
        x_p = min_neighbour[0]
        while x_p in visited:
            graph.edges[x][x_p] = INF
            neighbours = [i for i, x in enumerate(graph.edges[x]) if x != INF]
            neighbours_dic = [i for i in results_dic if results_dic[0] in neighbours]
            min_neighbour = min(neighbours_dic, key=neighbours.get)
            x_p = min_neighbour[0]
        path.append(x_p)
        visited.append(x_p)
        graph.edges[x][x_p] = INF
        x = x_p 
    return path

def print_path(board, dims, path):
    for i, x in enumerate(board):
        if i in path:
            print(f"{x}", end="")
        else:
            print(" ", end="")
        if i % dims[0] == dims[0]-1:
                print("\n", end="")
            

if __name__ == "__main__":
    # Creating board from file. It will be also our graph
    filename = sys.argv[1]
    # filename = "./projects/ex6_graphs/input_2.txt"
    board, dims = read_file(filename)

    # Creating graph based on board
    graph = Graph(len(board))
    board_to_graph(board, dims, graph)

    # Start and end of graph
    start, end = [i for i, v in enumerate(board) if v == 0]

    # Results
    result = dijkstra(graph, start)
    print(f"The shortest path cost is: {result[end]}")

    # Get path
    path = get_path(result, graph, start, end)
    
    # Print the output
    print_path(board, dims, path)

    

