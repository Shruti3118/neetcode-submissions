# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxVal = float('-inf')
        def countGoodNodes(root,maxVal):
            if not root:
                return 0
            if maxVal <= root.val:
                return 1 + countGoodNodes(root.left,root.val) + countGoodNodes(root.right,root.val)
            return countGoodNodes(root.left,maxVal) + countGoodNodes(root.right,maxVal)
        return countGoodNodes(root,maxVal)    
            