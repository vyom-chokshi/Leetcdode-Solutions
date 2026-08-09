# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = 0
        maxLevel = -1

        def left(root, level):
            nonlocal ans, maxLevel

            if root is None:
                return

        
            if level > maxLevel:
                ans = root.val
                maxLevel = level

            left(root.left, level + 1)
            left(root.right, level + 1)

        left(root, 0)

        return ans
