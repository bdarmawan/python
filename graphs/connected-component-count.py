graph = {
    '0': ['8', '1', '5'],
    '1': ['0'],
    '5': ['0', '8'],
    '8': ['0', '5'],
    '2': ['3', '4'],
    '3': ['2', '4'],
    '4': ['3', '2']
}

'''
or:
graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}

         5 
         |  \    
     1 - 0 - 8

        3 - 2 - 4
         \  | 
            4

'''

def connectedComponentCount(graph):
    visited = set()
    count = 0

    for node in graph:
        if explore(graph, node, visited) == True:
            count += 1
    return count


def explore(graph, current, visited):
    if str(current) in visited: return False
    visited.add(str(current))

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)
    return True

print(graph)
print(connectedComponentCount(graph))     # OUTPUT: 2