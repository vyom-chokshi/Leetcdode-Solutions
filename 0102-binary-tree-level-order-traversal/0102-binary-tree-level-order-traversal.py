# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:        
        x = []

        def level(root, depth):
            if root is None:
                return

            if len(x) == depth:
                x.append([])

            x[depth].append(root.val)

            level(root.left, depth + 1)
            level(root.right, depth + 1)

        level(root, 0)
        return x