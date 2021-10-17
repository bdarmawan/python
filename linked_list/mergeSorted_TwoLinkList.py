class ListNode:
	def __init__(self, val, next=None):
		self.val = val
		self.next = next


class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		if l1 is None: return l2
		if l2 is None: return l1

		if l1.val < l2.val:
			l1.next = self.mergeTwoLists(l1.next, l2)
			return l1
		else:
			l2.next = self.mergeTwoLists(l2.next, l1)
			return l2



def makeList(elements):
	head = ListNode(elements[0])
	ptr = head
	for element in elements[1:]:
		while ptr.next:
			ptr = ptr.next
		ptr.next = ListNode(element)
	return head


def printList(head):
	ptr = head
	print('[', end = "")
	while ptr:
		print(ptr.val, end = ", ")
		ptr = ptr.next
	print(']')


if __name__ == '__main__':
	a = makeList([1,3,5])
	b = makeList([2,4,6])
	print("a: ", end = "")
	printList(a)
	print("b: ", end = "")
	printList(b)
	s = Solution()
	print("a merge b: ", end = "")
	printList(s.mergeTwoLists(a, b))



"""
a: [1, 3, 5, ]
b: [2, 4, 6, ]
a merge b: [1, 2, 3, 4, 5, 6, ]
"""