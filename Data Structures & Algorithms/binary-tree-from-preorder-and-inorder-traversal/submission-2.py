# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preInd = 0
        hm = {}
        for i,val in enumerate(inorder):
            hm[val] = i
        def bt(iS,iE):
            if iS > iE:
                return None
            root = TreeNode(preorder[self.preInd])
            self.preInd += 1

            inInd = hm[root.val]
            
            root.left = bt(iS,inInd-1)
            root.right = bt(inInd+1,iE)
            return root
        return bt(0,len(preorder)-1)
            