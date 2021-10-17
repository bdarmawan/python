class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

"""
        Head -> 1 -> 2 -> 3 -> 4 -> 5 -> None
                |-----------|-------|
                   length-k     k
                   
        Head -> 4 -> 5 -> 1 -> 2 -> 3 -> None
"""

class Solution:
    def rotateList(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        #Get length
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length  # because if length = 5, k = 6
                        # it == as if rotated 1 time only
        if k == 0:
            return head

        # Move to the pivot and rotate
        cur = head
        for jump in range(length - k - 1):
            # we -1 because we start from Node 1, not from head
            cur = cur.next

        newHead = cur.next
        cur.next = None    # terminate this cur.next otherwise it will end up looping forever
        tail.next = head
        return newHead

    def printList(self, head):
        if head == None:
            return None
        while head:
            print(head.val, end="->")
            head = head.next

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)

s = Solution()
k=2
print("Original list: ", end="")
s.printList(a)
s2 = s.rotateList(a, k)
print("\n")
print(f"List rotated {k} times: ", end="")
s.printList(s2)

"""
Original list: 1->2->3->4->5->

List rotated 2 times: 4->5->1->2->3->
"""