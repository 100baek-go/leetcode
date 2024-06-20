class Solution(object):
    def preorderTraversal(self, root):
        res = []

        def _preorder(root):
            if root:
                res.append(root.val)
                _preorder(root.left)
                _preorder(root.right)
            return
        
        _preorder(root)
        return res
        