# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # find k-th smallest in left smallest and left nodecount
        # if left nodecount > k 

        # do in order traversal , keep count of explored nodes (i.e, inorder index)
        
        inorder_index = 0

        def dfs(root, inorder_index): # returns count(including root), found_ans
            if root is None:
                return 0, None 
            
            print(root.val, inorder_index)
            
            left_count, found_ans = dfs(root.left,inorder_index) 

            if found_ans is not None: 
                # print("already found ans", found_ans)
                return None, found_ans # None means dont care

            inorder_index += left_count
            # print("left completed, back at root - ", root.val, inorder_index)

            if inorder_index == k-1:
                # print("found ans", root.val)
                return None, root.val # None means dont care

            right_count, found_ans = dfs(root.right, inorder_index+1)
            # print("right completed, back at root - ", root.val, inorder_index)
            if found_ans is not None: 
                # print("already found ans", found_ans)
                return None, found_ans # None means dont care

            return left_count + right_count + 1 , None # None means dont care

        _, ans = dfs(root,0)
        return ans
    
