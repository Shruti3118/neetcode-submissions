# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return root.val
        self.res = float("-inf")
        def maxPath(root):
            if not root:
                return 0
            if not root.left and not root.right:
                self.res = max(self.res,root.val)
                return root.val
            leftVal = maxPath(root.left)
            rightVal = maxPath(root.right)
            chosenVal = max(leftVal,rightVal)
            self.res = max(self.res,root.val+leftVal+rightVal,root.val,root.val+chosenVal)
            if chosenVal < 0:
                return root.val
            return root.val+chosenVal
        maxPath(root)
        return self.res

                
            
            