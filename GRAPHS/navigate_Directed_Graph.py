# There are 2 ways to navigate a graph:
#       depthFirstPrint
#       breathFirstPrint
'''
For GRAPH problem, if there's a cyclic especially on the
undirected graph, you need to keep track on VISITED node
'''



### 1 ###
#   depthFirstPrint
#   --- Depth First Search
#   --- ---  using STACK, thus LIFO
###
def depthFirstPrint(graph, source):
    stack = [ source ]    # initialize the stack with "source" node

    while len(stack) > 0:
        current = stack.pop()
        print(current, end=" ")
        for neighbor in graph[current]:
            stack.append(neighbor)
    print("")


### 2 ###
#   breathFirstPrint
#   --- Breath First Search
#   --- ---  using QUEUE, thus FIFO
###
def breadthFirstPrint(graph, source):
    queue = [ source ]

    while len(queue) > 0:
        current = queue.pop()
        print(current, end=" ")
        for neighbor in graph[current]:
            queue.insert(0, neighbor)
    print("")


'''
    a --> c --> e
    |
    v
    b --> d --> f
'''

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

depthFirstPrint(graph, 'a')     # a c e b d f
depthFirstPrint(graph, 'c')     # c e
depthFirstPrint(graph, 'e')     # e
depthFirstPrint(graph, 'b')     # b d f
depthFirstPrint(graph, 'e')     # e

print("")

breadthFirstPrint(graph, 'a')     # a b c d e f
breadthFirstPrint(graph, 'c')     # c e
breadthFirstPrint(graph, 'e')     # e
breadthFirstPrint(graph, 'b')     # b d f
breadthFirstPrint(graph, 'e')     # e