class Solution(object):
    def postorderTraversal(self, root):
        stack=[]
        def dfs(root):
            if root:
                dfs(root.left)
                dfs(root.right)
                stack.append(root.val)
        dfs(root)
        return stack