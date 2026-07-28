# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def hight(root):
            if root == None:
                return 0
            left=hight(root.left)
            right=hight(root.right)
            return 1+max(left,right)
        if root == None:
            return True
        left_height = hight(root.left)
        right_height = hight(root.right)

        balance_factor = abs(left_height - right_height)

        if balance_factor >1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)