# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        smallest = root.val
        secondSmallest = sys.maxsize
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node.left and (secondSmallest == sys.maxsize or node.left.val <= secondSmallest):
                if node.left.val != smallest:
                    secondSmallest = min(secondSmallest, node.left.val)
                stack.append(node.left)

            if node.right and (secondSmallest == sys.maxsize or node.right.val <= secondSmallest):
                if node.right.val != smallest:
                    secondSmallest = min(secondSmallest, node.right.val)
                stack.append(node.right)

        return secondSmallest if secondSmallest != sys.maxsize else -1