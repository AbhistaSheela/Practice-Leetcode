# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def samet(t1,t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val!=t2.val:
                return False
            lt=samet(t1.left,t2.right)
            rt=samet(t1.right,t2.left)
            if lt and rt:
                return True
            else:
                return False
        return samet(root.left,root.right)