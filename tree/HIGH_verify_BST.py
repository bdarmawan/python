from typing import List
import math

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
    return root


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


### OPTION 1
###
### BST requires all data on the left  <= ROOT
###                       on the right >= ROOT
def verifyBST(root):
    return is_valid(root, -math.inf, math.inf)

def is_valid(node, leftValueBoundary, rightValueBoundary):
    if node is None:
        return True

    if node.data < leftValueBoundary or node.data > rightValueBoundary:
        return False

    return (is_valid(node.left, leftValueBoundary, node.data) and
            is_valid(node.right, node.data, rightValueBoundary))




### OPTION 2 - Using inOrder print
###             inOrder print will print all element in the correct order
###             if the result NOT in order, that means it is not BST
def verifyBST2(root):
    stack = []

    def inOrderPrint(root):
        if root:
            inOrderPrint(root.left)
            stack.append(root.data)
            inOrderPrint(root.right)
        return stack

    def isInOrder(stack):
        for i in range(1, len(stack)):
            if stack[i] < stack[i-1]:
                return False
        return True


    stack = inOrderPrint(root)
    print(stack)
    return isInOrder(stack)


###
###TEST
myList = [100, 90, 95, 105, 80, 70, 120, 110, 130, 140]
root = createBinTree(myList)
print("")
print(verifyBST(root))      #OUTPUT: True
print(verifyBST2(root))     #OUTPUT: True

n = Node(200)
n.left = Node(100)
n.left.left = Node(50)
n.left.right = Node(250)
n.right = Node(300)
print(verifyBST(n))         #OUTPUT: False
print(verifyBST2(n))        #OUTPUT: False
