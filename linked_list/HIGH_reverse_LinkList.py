class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
#  https://www.bing.com/videos/search?q=reverse+link+list+python&docid=607990507016750550&mid=0FFEC9B3D05313A672FD0FFEC9B3D05313A672FD&view=detail&FORM=VIRE
#
# iterative
    def reverseList(self, head):           ### OPTION 1
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev


    def reversedRecursively(self, head):   ### OPTION 2
        if head is None:
            return head
        if head.next is None:
            return head
        newHead = self.reversedRecursively(head.next)
        head.next.next = head
        head.next = None
        return newHead


    def printList(self, head):
        if head == None:
            return None
        while (head):
            print(head.val, end='->')
            head = head.next



if __name__ == '__main__':
    root = Node(1)
    root.next = Node(2)
    root.next.next = Node(3)
    root.next.next.next = Node(4)
    root.next.next.next.next = Node(5)

    s = Solution()
    s.printList(root)
    '''
    1->2->3->4->5->
    '''
    print()
    newRoot = s.reverseList(root)
    s.printList(newRoot)
    '''
    5->4->3->2->1->
    '''

    """
    With Recursive
    """
    print()
    root = Node(1)
    root.next = Node(2)
    root.next.next = Node(3)
    root.next.next.next = Node(4)
    root.next.next.next.next = Node(5)

    newRoot2 = s.reversedRecursively(root)
    s.printList(newRoot2)
    '''
    5->4->3->2->1->
    '''
