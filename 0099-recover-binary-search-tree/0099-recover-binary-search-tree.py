# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.f = self.s = self.prev = None

        def inorder(node):

            if not node:
                return
            inorder(node.left)

            if (self.prev is not None) and self.prev.val > node.val:
                if not self.f:
                    self.f = self.prev
                self.s = node
            
            self.prev = node

            inorder(node.right)
        
        inorder(root)

        self.f.val, self.s.val = self.s.val, self.f.val