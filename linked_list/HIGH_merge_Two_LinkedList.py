from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
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
        head = ListNode(nums[0])
        cur = head
        for num in nums[1:]:
            while cur.next:
                cur = cur.next
            cur.next = ListNode(num)
        return head

###
### TEST
# l1 = 1 -> 2 -> 4
# l1 = ListNode(1)
# l1.next = ListNode(2)
# l1.next.next = ListNode(4)
#
# # l2 = 1 -> 3 -> 4
# l2 = ListNode(1)
# l2.next = ListNode(3)
# l2.next.next = ListNode(4)



s = Solution()
list1 = [1,2,4]
l1 = s.makeList(list1)
s.printList(l1)
print("")

list2 = [1,3,4]
l2 = s.makeList(list2)
s.printList(l2)
print("")

result = s.mergeTwoLists(l1, l2)     # OUTPUT: 1 1 2 3 4 4
s.printList(result)
