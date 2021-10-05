from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None: return False
#       if root.left == None and root.right == None and root.val == targetSum: return True
        if root.val == targetSum: return True

        remainder = targetSum - root.val
        leftReply = self.hasPathSum(root.left, remainder)
        rightReply = self.hasPathSum(root.right, remainder)

        return leftReply or rightReply


###
### TEST
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

targetSum = 22

s = Solution()
print(s.hasPathSum(root, targetSum))        #OUTPUT: True