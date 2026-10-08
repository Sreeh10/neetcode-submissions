# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # root left right traversal
        out = ""
        def dfs(root):
            nonlocal out
            if root is None:
                out += ",null"
                return 
            out += "," + str(root.val)
            dfs(root.left)
            dfs(root.right)
            return
            # ",1,2,null,null,3,4,null,null,5,null,null"
        dfs(root)
        # print("encoding:", out)
        return out

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # print("decoding: ", data)
        vals = data.split(",")
        # ",1,2,null,null,3,4,null,null,5,null,null"
        i= 0
        def dfs():
            nonlocal i
            i+= 1
            # print(vals, i)
            if vals[i] == "null":
                return None
            node = TreeNode()
            node.val = vals[i]
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
