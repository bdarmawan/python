'''
    3 ------> 2 ------> 0 ------> -4
              ^                   |
              |                   |
              *-------------------*
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        ctr = 0

        while (fast.next.next != None) and slow.next:
            if (ctr != 0) and (slow.val == fast.val):
                return True
            ctr = 1
            slow = slow.next
            fast = fast.next.next

        return False


###
### TEST
ll = ListNode(3)
ll.next = saved = ListNode(2)
ll.next.next = ListNode(0)
ll.next.next.next = ListNode(-4)
ll.next.next.next.next = saved

s = Solution()
print(s.hasCycle(ll))       # OUTPUT: True

