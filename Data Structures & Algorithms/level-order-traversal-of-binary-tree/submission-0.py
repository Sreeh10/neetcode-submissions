# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        tracking_level = 0
        q.append((root,0))
        level_list = []
        full_list = []
        while len(q) > 0:
            # print([(x[0].val,x[1]) if x[0] is not None else None for x in q])
            # print(level_list)
            node, node_level = q.popleft()
            if node is not None:
                q.append((node.left, node_level+1))
                q.append((node.right, node_level+1))
                if tracking_level < node_level:
                    full_list.append(level_list)
                    level_list = []
                    tracking_level += 1
                level_list.append(node.val)

        if len(level_list) > 0:
            full_list.append(level_list)
        return full_list

        