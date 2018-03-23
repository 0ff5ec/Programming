#    -*- coding:   utf-8   -*-
'''
Invert a binary tree.
     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''
"""
        :type root: TreeNode
        :rtype: TreeNode
        """
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        sol = Solution()
        if root == None:
            return root
        right = sol.invertTree(root.right)
        left = sol.invertTree(root.left)
        root.left = right
        root.right = left
        return root

if __name__ == "__main__":
	sol = Solution()
