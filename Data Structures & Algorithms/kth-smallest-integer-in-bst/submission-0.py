# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        def dfs(root,k):
            if not root:
                return
            left = dfs(root.left,k)
            if left != None:
                return left
            self.count += 1
            if self.count == k:
                return root.val
            return dfs(root.right,k)
        return dfs(root,k)
