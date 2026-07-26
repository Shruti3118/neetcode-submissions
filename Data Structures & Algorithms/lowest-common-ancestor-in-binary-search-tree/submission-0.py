# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        lca1 = self.lowestCommonAncestor(root.left,p,q)
        lca2 = self.lowestCommonAncestor(root.right,p,q)
        if lca1 and lca2:
            return root
        if lca1:
            return lca1
        return lca2