'''
For GRAPH problem, if there's a cyclic especially on the
undirected graph, you need to keep track on VISITED node
'''
import math

graph = {
    '1': ['0'],
    '0': ['8', '1', '5'],
    '5': ['0', '8'],
    '8': ['0', '5'],
    '2': ['3', '4'],
    '3': ['2', '4'],
    '4': ['3', '2']
}
'''
         5 
         |  \    
     1 - 0 - 8

        3 - 2 
         \  | 
            4
'''

def largestComponent(graph):
    visited = set()
    largest= 0

    for node in graph:
        size = explore(graph, node, visited)
        if size > largest:  largest = size
    return largest


def explore(graph, current, visited):
    if current in visited:  return 0
    visited.add(current)
    count = 1    # this represents the current node you're visiting

    for neighbor in graph[current]:
        count += explore(graph, neighbor, visited)
    return count


def smallestComponent(graph):
    visited = set()
    smallest = math.inf

    for node in graph:
        size = explore(graph, node, visited)
        if size > 0 and size < smallest: smallest = size
    return smallest



###
### TEST
print(largestComponent(graph))     # OUTPUT: 4
print(smallestComponent(graph))    # OUTPUT: 3
