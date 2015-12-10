from collections import deque

def bfs_connected_components(graph, starting_node):
    '''
    Returns the connected component of a graph containing the starting_node
    '''
    visited = set()
    queue = deque([starting_node])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            neighbors = graph[node]
            queue.extend(neighbors)
    return visited

def bfs_shortest_path_length(graph, starting_node, target_node):
    '''
    Returns the distance between a starting_node and target_node in a graph
    '''
    visited = set()
    distance = 0
    queue = deque([(starting_node, distance)])
    while queue:
        node, distance = queue.popleft()
        if node == target_node:
            return distance
        elif node not in visited:
            distance += 1
            visited.add(node)
            neighbors = [(neighbor, distance) for neighbor in graph[node]]
            queue.extend(neighbors)
    return visited

def bfs_shortest_path(graph, starting_node, target_node):
    '''
    Returns the shortest path between a starting_node and target_node in a graph
    '''
    visited = set()
    queue = deque([(starting_node, [])])
    while queue:
        node, path = queue.popleft()
        visited.add(node)
        path.append(node)
        if node == target_node:
            return path
        else:
            neighbors = graph[node] - visited
            for neighbor in neighbors:
                queue.append((neighbor, path[:]))

if __name__ == '__main__':
    graph = {'A': {'B', 'C'},
             'B': {'A', 'E'},
             'C': {'A', 'D', 'E'},
             'D': {'C', 'E'},
             'E': {'B', 'C', 'D'}}
    starting_node = 'A'
    target_node = 'E'
    print bfs_connected_components(graph, starting_node)
    print bfs_shortest_path_length(graph, starting_node, target_node)
    print bfs_shortest_path(graph, starting_node, target_node)
