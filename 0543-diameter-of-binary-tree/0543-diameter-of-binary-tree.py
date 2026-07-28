# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia=0
        def height(root):
            if root == None:
                return 0
            left=height(root.left)
            right=height(root.right)
            self.dia=max(self.dia,left+right)
            return 1+max(left,right)
        height(root)
        return self.dia
