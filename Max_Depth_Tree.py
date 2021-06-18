# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        count=0
        def aux(root,count):
            if not root:
                return count
            count+=1
            left_d=aux(root.left,count)
            right_d=aux(root.right,count)
            return max(left_d,right_d)
        
        return aux(root,count)