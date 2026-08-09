# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=0
        def left(root):
            nonlocal count
            if root is None:
                return None

            ans = left(root.left)

            if ans is not None:
                return ans

        
            count += 1

            if count == k:
                return root.val

        
            return left(root.right)
        return left(root)
            
