# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # longest left path
        # longest right path
        # longest observed diameter

        def dfs(root):
            if root is None:
                return 0, 0
            left_depth, left_diameter = dfs(root.left)
            right_depth, right_diameter = dfs(root.right) 
            max_diameter = max(left_depth + right_depth + 1, left_diameter, right_diameter)
            max_depth = max(left_depth, right_depth) + 1
            # print(root.val, left_depth, left_diameter, right_depth, right_diameter, max_depth, max_diameter)
            return max_depth, max_diameter
        
        depth, diameter = dfs(root)
        return diameter-1 # asked edge count, not the no of nodes involved