# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(l,r):
            if r is None and l is None:
                return True
            elif r is None or l is None:
                return False
            return (r.val==l.val) and check(l.right,r.left) and check(l.left,r.right) 
        return check(root,root)