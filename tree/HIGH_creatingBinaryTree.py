class Node:
    def __init__(self, data):
        self.left  = None
        self.right = None
        self.data  = data

####### insert
    def insert(self, data):
        if data < self.data:
            if self.left is None:                # if it has reached the MOST LEFT node
                self.left = Node(data)                # then PUT the new NODE here
            else:
                self.left.insert(data)                # else recursive
        elif data > self.data:
            if self.right is None:               # if it has reached the MOST RIGHT node
                self.right = Node(data)               # then PUT the new NODE here
            else:
                self.right = self.right.insert(data)  # else recursive


####### findVal
    def findVal(self, value):
        if value < self.data:       # if value is on the LEFT of current NODE
            if self.left is None:   # if it has reached the MOST LEFT node
                print(str(value) + " Not Found!")
                return
            self.left.findVal(value)
        elif value > self.data:    # if value is on the RIGHT of current NODE
            if self.right is None: # if it has reached the MOST RIGHT node
                print(str(value) + " Not Found!")
                return
            self.right.findVal(value)
        else:
            print(str(self.data) + " is Found!")


####### printTree
    def printTree(self):
        if self.left:
            self.left.printTree()
        #print(self.data),         # this is python 2
        print(self.data, end=" ")   #this is python 3
        if self.right:
            self.right.printTree()

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.printTree()
print("")
root.findVal(3)
root.findVal(13)
