'''
If edges matrix is the only information given in the GRAPH problem,
then it is important for you to convert it to ADJACENCY MATRIX

           x ----- y
        /            \
     w                 z
        \           /
          \       /
              v

shortestPath is about counting edges not the nodes, that's why
BFS is more suitable compare to DFS for this purposes
'''


edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]

def convertToAdjMatrix(edges):
    graph = {}

    for edge in edges:
        a, b = edge
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph



def shortestPath(edges, nodeA, nodeB):
    graph = convertToAdjMatrix(edges)
    visited = set(nodeA)
    queue = []                      # remember queue's operation FIFO
                                    # insert from tail
                                    # pop from head
    queue.insert(0, [nodeA, 0])     # Initial values (both node and its distance)

    while len(queue) > 0:
        node, distance = queue.pop()
        if node == nodeB: return distance

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.insert(0, [neighbor, distance + 1])
    return -1


###
### TEST
print(shortestPath(edges, 'w', 'z'))  # OUTPUT: 2
print(shortestPath(edges, 'z', 'w'))  # OUTPUT: 2
print(shortestPath(edges, 'w', 'w'))  # OUTPUT: 0
print(shortestPath(edges, 'w', 'y'))  # OUTPUT: 2
print(shortestPath(edges, 'y', 'w'))  # OUTPUT: 2
