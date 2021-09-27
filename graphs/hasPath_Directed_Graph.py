'''
acyclic GRAPH:  (no circular)  ::  cyclic GRAPH
    f ---> g ---> h                a <-- b
    |    *                         |   /
    v  /                           v *
    i <--- j                       c
    |
    v
    k

   n = # nodes                     n = # nodes
   e = # edges                     e = # edges
   Time =  O(e)                    Time =  O(n^2)
   Space = O(n)                    Space = O(n)
'''

graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}


def hasPath_usingDFS (graph, src, dst):
    if src == dst: return True

    for neighbor in graph[src]:
        if hasPath_usingDFS(graph, neighbor, dst) == True:
            return True
    return False



def hasPath_usingBFS (graph, src, dst):
    queue = [src]

    while len(queue) > 0:
        current = queue.pop()
        if current == dst: return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False


print(hasPath_usingDFS(graph, 'f', 'k'))    # True
print(hasPath_usingDFS(graph, 'g', 'i'))    # False
print(hasPath_usingDFS(graph, 'i', 'g'))    # True
print("")
print(hasPath_usingBFS(graph, 'f', 'k'))    # True
print(hasPath_usingBFS(graph, 'g', 'i'))    # False
print(hasPath_usingBFS(graph, 'i', 'g'))    # True