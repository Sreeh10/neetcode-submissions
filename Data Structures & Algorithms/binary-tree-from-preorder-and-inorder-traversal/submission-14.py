# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_indices = { n:i for i,n in enumerate(inorder)}

        # print(preorder[-10:])
        # print(inorder[-10:])
        
        def dfs(preorder_, inorder_, inorder_offset):
            if len(preorder_) == 0:
                return None
            root_val = preorder_[0]
            # find the inorder_index of root_val
            root_index_in_inorder = inorder_indices.get(root_val) - inorder_offset
            # inorder_left = 
            # inorder_right = 
            # print(root_val, preorder_, inorder_, root_index_in_inorder, inorder_offset)

            # now we know the size of left subtree + root
            # so break preorder also at that size because preorder = left, then root , then right
            # find the preorder_index of element at inorder[root_index+1]
            # preorder_left =   # preorder of left should omit the current root
            # preorder_right = 

            # print(root_val, inorder_left, inorder_right)
            return TreeNode(
                root_val,
                dfs(preorder_[1:root_index_in_inorder+1], inorder_[:root_index_in_inorder], inorder_offset=inorder_offset),
                dfs(preorder_[root_index_in_inorder+1:], inorder_[root_index_in_inorder+1:], inorder_offset=inorder_offset+root_index_in_inorder+1)
            )
        
        return dfs(preorder,inorder, inorder_offset=0)
        