# Convert edges matrix to adjacency list

def buildGraph(edges):
   graph = {}

   for edge in edges:
       (a, b) = edge
       if (not(a in graph)):
           graph[a] = []
       if (not(b in graph)):
           graph[b] = []
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
"""
    i --- j
    |   
    k --- l
    |
    m
    
    o --- n
"""

for k,v in buildGraph(edges).items():
    print(f"{k}:{v}")

'''
OUTPUT:
i:['j', 'k']
j:['i']
k:['i', 'm', 'l']
m:['k']
l:['k'] 
o:['n']
n:['o']
'''
