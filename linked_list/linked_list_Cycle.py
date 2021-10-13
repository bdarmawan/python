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
        slow, fast = head, head.next.next

        while (fast.next.next) and (slow.next):
            if slow.val == fast.val:
                return True
            else:
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


ll2 = ListNode(3)
ll2.next = saved = ListNode(2)
ll2.next.next = ListNode(0)
ll2.next.next.next = ListNode(-4)

s = Solution()
print(s.hasCycle(ll))       # OUTPUT: True
print(s.hasCycle(ll2))      # OUTPUT: False

