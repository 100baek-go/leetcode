# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(u):
            if not u:
                return []
            return dfs(u.left) + [u] + dfs(u.right)
        nodes = dfs(root)
        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i+1]
        nodes[-1].left = None
        nodes[-1].right = None
        return nodes[0]