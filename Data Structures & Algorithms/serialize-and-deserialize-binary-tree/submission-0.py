# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = []
        def serial(root):
            if not root:
                ans.append("N")
            if root:
                ans.append(str(root.val))
                serial(root.left)
                serial(root.right)
        serial(root)
        return ",".join(ans)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        res = data.split(",")
        self.index = 0
        def deserial():
            if self.index == len(res):
                return
            val = res[self.index]
            self.index += 1
            if val == "N":
                return None
            root = TreeNode(int(val))
            root.left = deserial()
            root.right = deserial()
            return root

        return deserial()
        



