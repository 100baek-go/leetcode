# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def solver(root):
            nonlocal diameter
            if root is None:
                return -1
            left = 1 + solver(root.left)
            right = 1 + solver(root.right)
            # print(left, right, root.val)
            diameter = max(diameter,left + right)
            return max(left, right)
        solver(root)
        return diameter