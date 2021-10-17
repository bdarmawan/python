from typing import List
from typing import Optional

class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
        dummy = Node(-1)
        head = dummy
        while (l1 != None and l2 != None):
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next  # Tricky -> make sure move dummy to the next one

        # now check if there is any remainder
        if l1 != None:
            dummy.next = l1
        else:
            dummy.next = l2

        return head.next    # because head is pointing to first dummy



    def printList(self, head):
        while head:
            print(head.val, end = " ")
            head = head.next


    def makeList(self, nums):
        head = Node(nums[0])
        cur = head
        for num in nums[1:]:
            while cur.next:
                cur = cur.next
            cur.next = Node(num)
        return head

###
### TEST
# l1 = 1 -> 3 -> 5
# l1 = Node(1)
# l1.next = Node(3)
# l1.next.next = Node(5)
#
# # l2 = 2 -> 4 -> 6
# l2 = Node(1)
# l2.next = Node(3)
# l2.next.next = Node(4)



s = Solution()
list1 = [1,3,5]
l1 = s.makeList(list1)
s.printList(l1)
print("")

list2 = [2,4,6]
l2 = s.makeList(list2)
s.printList(l2)
print("")

result = s.mergeTwoLists(l1, l2)     # OUTPUT: 1 2 3 4 5 6
s.printList(result)
