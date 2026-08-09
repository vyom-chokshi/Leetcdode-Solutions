# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def rtree(root):
            h=0
            while root:
                h+=1
                root=root.left
            return h
        def ltree(root):
            h=0
            while root:
                h+=1
                root=root.right
            return h
                       
        left=ltree(root)
        right=rtree(root)
        if left==right:
            return (2**left)-1      
        return 1+self.countNodes(root.left)+self.countNodes(root.right)