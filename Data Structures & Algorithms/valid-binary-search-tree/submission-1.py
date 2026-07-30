# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.mini = float('-inf')
        def validBst(root):
            if not root:
                return True
            lh = validBst(root.left)
            if self.mini >= root.val:
                return False
            else:
                self.mini = root.val
            rh = validBst(root.right)
            return lh and rh
        return validBst(root)
            
            