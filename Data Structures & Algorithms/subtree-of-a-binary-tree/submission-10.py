# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def isSame(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
    if a is None and b is None:
        return True
    elif (a is None) or (b is None):
        # print("A", a.val if b is None else 'x' , b.val if a is None else 'x' )
        return False
    if a.val != b.val:
        # print("B")
        return False

    return (isSame(a.left,b.left) and isSame(a.right,b.right))
    

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            # print("C")
            return False
        if isSame(root,subRoot):
            return True
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
