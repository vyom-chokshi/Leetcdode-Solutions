# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        level=0
        def tree(root,level):
            if root==None:
                return None
            if level==len(l):
                l.append(root.val)
            tree(root.right,level+1)
            tree(root.left,level+1)
            return root
        tree(root,0)
        return l