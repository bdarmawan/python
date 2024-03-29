'''
For GRAPH problem, if there's a cyclic especially on the
undirected graph, you need to keep track on VISITED node
'''

def undirectedPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    return hasPath(graph, nodeA, nodeB, set())


def hasPath(graph, src, dst, visited):
    if (src == dst): return True
    if src in visited:
        return False     #if it has been visited, no need to process again
    visited.add(src)

    for neighbor in graph[src]:
        if hasPath(graph, neighbor, dst, visited) == True:
            return True

    return False



def buildGraph(edges):
   graph = {}

   for edge in edges:
       (a, b) = edge
       if (a not in graph): graph[a] = []
       if (b not in graph): graph[b] = []
       graph[a].append(b)    #
       graph[b].append(a)    # This is because of UNDIRECTED GRAPH

   return graph

# UNDIRECTED GRAPH's EDGES
edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]


print(f"Is there a path from j to m? {undirectedPath(edges, 'j', 'm')}")
print(f"Is there a path from m to j? {undirectedPath(edges, 'm', 'j')}")
print(f"Is there a path from j to l? {undirectedPath(edges, 'j', 'l')}")
print(f"Is there a path from i to o? {undirectedPath(edges, 'i', 'o')}")

"""
GRAPH:
i:['j', 'k']
j:['i']
k:['i', 'm', 'l']
m:['k']
l:['k'] 
o:['n']
n:['o']

OUTPUT:
Is there a path from j to m? True
Is there a path from m to j? True
Is there a path from j to l? True
Is there a path from i to o? False
"""