# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        values = []
        def dfs(node):
            if node:
                values.append(node.val)
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        return len(set(values)) == 1
