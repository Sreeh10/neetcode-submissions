# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if root is None:
                return 0, None

            left_max_depth_sum, left_max_path_sum = dfs(root.left)
            right_max_depth_sum, right_max_path_sum = dfs(root.right)

            max_depth_sum = max(
                                left_max_depth_sum + root.val,
                                right_max_depth_sum + root.val,
                                root.val
                            )
            
            max_path_sum = left_max_depth_sum + right_max_depth_sum + root.val
            max_path_sum = max(
                                max_depth_sum,
                                left_max_depth_sum + right_max_depth_sum + root.val
            )
            
            if left_max_path_sum is not None:
                max_path_sum = max(max_path_sum, left_max_path_sum)
            if right_max_path_sum is not None:
                max_path_sum = max(max_path_sum, right_max_path_sum)

            return max_depth_sum, max_path_sum

        depth_sum, path_sum = dfs(root)
        return path_sum