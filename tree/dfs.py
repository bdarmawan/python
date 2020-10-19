##
## This is dfs (Depth First Search):
##    * pre-Order  --- nlr
##    * in-Order   --- lnr
##    * post-Order --- lrn
##
class Node:
   def __init__(self,data):
       self.left = None
       self.right = None
       self.data = data

def inOrder(root):
   if root:
       inOrder(root.left)
       print(root.data, end=" ")
       inOrder(root.right)

def preOrder(root):
   if root:
       print(root.data, end=" ")
       preOrder(root.left)
       preOrder(root.right)

def postOrder(root):
   if root:
       postOrder(root.left)
       postOrder(root.right)
       print(root.data, end=" ")

#making the tree
root = Node(1)                     #               1
root.left = Node(2)                #          2         3
root.right = Node(3)               #       4     5   6      7
root.right.left = Node(6)          #    8     9
root.right.right = Node(7)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left  = Node(8)
root.left.left.right = Node(9)


print("In-Order: ", end="")
inOrder(root)
#8 4 9 2 5 1 6 3 7
print("")
print("Pre-Order: ", end="")
preOrder(root)
#1 2 4 8 9 5 3 6 7
print("")
print("Post-Order: ", end="")
postOrder(root)
#8 9 4 5 2 6 7 3 1
print("")
