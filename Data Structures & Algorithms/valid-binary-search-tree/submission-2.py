# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None :
            return True

        def valid_max_min(node):
            right_max = node.val
            left_min = node.val 

            if node.left is not None:
                left_valid, left_max, left_min = valid_max_min(node.left)
                if (not left_valid) or not (left_max < node.val):
                    return False, None, None
            if node.right is not None:
                right_valid, right_max, right_min = valid_max_min(node.right)
                if (not right_valid) or not (right_min > node.val):
                    return False, None, None
            
            return True, right_max, left_min
           
        ans, _, _ = valid_max_min(root)
        return ans
     