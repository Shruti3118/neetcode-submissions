# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preInd = 0
        def bt(preorder,inorder,iS,iE):
            if iS > iE:
                return None
            root = TreeNode(preorder[self.preInd])
            self.preInd += 1
            inInd = 0
            for i in range(iS,iE+1):
                if root.val == inorder[i]:
                    inInd = i
                    break
            root.left = bt(preorder,inorder,iS,inInd-1)
            root.right = bt(preorder,inorder,inInd+1,iE)
            return root
        return bt(preorder,inorder,0,len(preorder)-1)
            