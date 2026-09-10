# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,co):
    
        if not root:
            return 0,0,co

        l_s,l_c,co=self.dfs(root.left,co)
        r_s,r_c,co=self.dfs(root.right,co)

        sm=l_s+r_s+root.val
        c=l_c+r_c+1

        if sm//c == root.val:
            co+=1

        return sm,c,co

    
    def averageOfSubtree(self, root: TreeNode) -> int:
        co=0

        _,_,co=self.dfs(root,co)
        return co