'''
                   a
                /      \
              b          c
            /  \       /   \
           d    e     f     g
          / \        / \     \
         h   i      j   k     l

         1. enqueue the root
         2. while (Q is not empty)
            {
                 p = dequeue();
                 print(p)
                 if (p->left)
                     enqueue(p->left)
                 if (p->right)
                     enqueue(p->right)
            }

        result:  a b c d e f h i j k l
'''

class Node(object):
    def __init__(self, value,left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value):
        current = self.root
        while current:
            if value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    break
                else:
                    current = current.right
            else:
                if current.left is None:
                    current.left = Node(value)
                    break
                else:
                    current = current.left


    def BFS(self,root):
        """In BFS the Node Values at each level of the Tree are traversed before going to next level"""
        q = []
        if root:
            q.append(root)                             # enqueue ROOT
        while q:
            current = q.pop(0)                         # dequeuedd
            print(current.value, end=" ")
            if current.left:
                q.append(current.left)                 # enqueue LEFT
            if current.right:
                q.append(current.right)                # enqueue RIGHT


t = BinaryTree(100)
t.insert(90)
t.insert(80)
t.insert(70)
t.insert(110)
t.insert(120)
t.insert(130)

print("Output of Breadth First search is ", end="")
t.BFS(t.root)
