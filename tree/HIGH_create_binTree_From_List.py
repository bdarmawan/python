from typing import List

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value



def createBinTree(myList: List[int]):
    if len(myList) > 0:     # To handle empty list case
        root = Node(myList[0])
        for i in range(1, len(myList)):
            insert(root, myList[i])
        printTree(root)


def insert(root, value):
    if value == root.data:      # to handle repeating value
        return ""               # so, it will just ignore it
    if value < root.data:
        if root.left is None:
            node = Node(value)
            root.left = node
        else:
            insert(root.left, value)
    else:
        if root.right is None:
            node = Node(value)
            root.right = node
        else:
            insert(root.right, value)


def printTree(root):
    if root.left is not None:
        printTree(root.left)
    print(root.data, end=" ")
    if root.right is not None:
        printTree(root.right)



myList = [12, 6, 14, 3]
createBinTree(myList)       #OUTPUT: 3 6 12 14
'''
            12
          /     \
        6         14
      /  
    3
'''

print("")
myList = [12, 6, 14, 9, 3]
createBinTree(myList)       #OUTPUT: 3 6 9 12 14
'''
            12
          /     \
        6         14
      /   \
    3      9
'''

print("")
myList = [6, 14, 9, 3, 12]
createBinTree(myList)       #OUTPUT: 3 6 9 12 14
'''
            12
          /     \
        6         14
      /   \
    3      9
'''

print("")
myList = [6, 14, 9, 3, 6, 12]
createBinTree(myList)       #OUTPUT: 3 6 9 12 14
'''
            12
          /     \
        6         14
      /   \
    3      9
'''
print("")
myList = []
createBinTree(myList)       #OUTPUT: 3 6 9 12 14