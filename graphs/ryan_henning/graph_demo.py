import pandas as pd
from pprint import pprint
from collections import deque


def build_friends_adj_list():
    '''
    Builds and returns an adjacency list that representing the friends graph
    on the whiteboard.
    '''
    n = ['Ryan', 'Elizabeth', 'Justin', 'Ashley', 'West', 'Bri',
         'Meg', 'Andre', 'Ben', 'Cecilia', 'Other Ben']
    adj_list = {n[0] : {n[1], n[2], n[3], n[7], n[8]},
                n[1] : {n[0], n[2], n[3], n[6]},
                n[2] : {n[0], n[1], n[3], n[4]},
                n[3] : {n[0], n[2], n[1], n[5], n[4]},
                n[4] : {n[2], n[3]},
                n[5] : {n[3]},
                n[6] : {n[1]},
                n[7] : {n[0], n[9]},
                n[8] : {n[0], n[10]},
                n[9] : {n[7]},
                n[10]: {n[8]}}
    return adj_list


def bfs_visit_all(graph, start_node):
    '''
    INPUT:
        - graph: an adjacency list representation of an unweighted graph
        - start_node: the starting point in the graph, from which will will
                      begin our exploration

    This function will traverse the graph in a breadth-first way.
    This function implements the breadth-first-search (BFS) algorithm.
    '''
    pass


def dfs_visit_all(graph, start_node):
    '''
    INPUT:
        - graph: an adjacency list representation of an unweighted graph
        - start_node: the starting point in the graph, from which will will
                      begin our exploration

    This function will traverse the graph in a depth-first way.
    This function implements the depth-first-search (DFS) algorithm.

    WHAT CHANGED?
    '''
    pass


def bfs_visit_all_limit(graph, start_node, max_depth):
    '''
    INPUT:
        - graph: an adjacency list representation of an unweighted graph
        - start_node: the starting point in the graph, from which will will
                      begin our exploration

    This function will traverse the graph in a breadth-first way.
    This function implements the breadth-first-search (BFS) algorithm.

    This function will quit when we reach a certain max_depth.
    '''
    pass


def dfs_visit_all_recursive(graph, node, found_nodes=None):
    '''
    INPUT:
        - graph: an adjacency list representation of an unweighted graph
        - node: the starting point in the graph, from which will will
                begin our exploration
        - found_nodes: if not None, the set of nodes we've already processed

    This function will traverse the graph in a depth-first way.
    This function implements the depth-first-search (DFS) algorithm.

    This version uses recursion.

    Side note: WHAT IS STACK OVERFLOW?
    '''
    pass


def connected_component(graph, start_node):
    '''
    INPUT:
        - graph: an adjacency list representation of an unweighted graph
        - start_node: the starting point in the graph, from which will will
                      begin our exploration
    RETURN:
        - set_of_nodes: the set of nodes in this connected component

    This function will return the nodes in the connected component that
    contains start_node.
    '''
    pass


def build_cities_adj_matrix():
    '''
    Builds and returns an adjacency matrix representing the cities graph
    on the whiteboard.
    '''
    inf = float('inf')
    cities = ['OKC', 'Dallas', 'Waco', 'Austin', 'San Antonio',
              'Houston', 'Midland', 'El Paso']
    adj_matrix = [[  0, 207, inf, inf, inf, inf, inf, inf],
                  [207,   0,  95, inf, inf, inf, 330, inf],
                  [inf,  95,   0, 102, inf, inf, inf, inf],
                  [inf, inf, 102,   0,  80, 165, inf, inf],
                  [inf, inf, inf,  80,   0, 197, inf, inf],
                  [inf, inf, inf, 165, 197,   0, inf, inf],
                  [inf, 330, inf, inf, inf, inf,   0, 305],
                  [inf, inf, inf, inf, inf, inf, 305,   0]]
    graph = pd.DataFrame(adj_matrix, index=cities, columns=cities)
    return graph


def floyd_warshall(graph):
    '''
    INPUT:
        - graph: an adjacency matrix representation of a graph
    RETURN:
        - a pandas dataframe of the length of the shortest path between
          all pairs of nodes

    WHAT IS THE EFFICIENCY CLASS OF THIS ALGORITHM?
    '''
    pass


if __name__ == '__main__':

    friend_graph = build_friends_adj_list()
    pprint(friend_graph)

    #bfs_visit_all(friend_graph, 'Ryan')
    #print

    #dfs_visit_all(friend_graph, 'Ryan')
    #print

    #bfs_visit_all_limit(friend_graph, 'Ryan', 1)
    #print

    #dfs_visit_all_recursive(friend_graph, 'Ryan')
    #print

    #print connected_component(friend_graph, 'Ryan')

    #city_graph = build_cities_adj_matrix()
    #print city_graph

    #print floyd_warshall(city_graph)

