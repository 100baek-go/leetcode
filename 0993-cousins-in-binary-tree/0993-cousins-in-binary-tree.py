# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def findLevelAndParent(node, parent, val, level):
            if not node:
                return None
            if node.val == val:
                return (level, parent)
            return findLevelAndParent(node.left, node, val, level + 1) or \
                   findLevelAndParent(node.right, node, val, level + 1)

        x_level, x_parent = findLevelAndParent(root, None, x, 0)
        y_level, y_parent = findLevelAndParent(root, None, y, 0)
        return x_level == y_level and x_parent != y_parent