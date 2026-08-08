# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        l = []

        def traverse(root):
            if not root:
                return

            l.append(root)
            traverse(root.left)
            traverse(root.right)

        traverse(root)

        for i in range(len(l) - 1):
            l[i].left = None
            l[i].right = l[i + 1]

        l[-1].left = None
        l[-1].right = None
        return l