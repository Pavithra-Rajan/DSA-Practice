# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(root,ls):
            if root:
                inorder(root.left,ls)
                ls.append(root.val)
                inorder(root.right,ls)
        ls=[]
        inorder(root,ls)
        # return ls==sorted(ls) and ls==list(set(ls))
        for i in range(0,len(ls)-1):
            if ls[i]>=ls[i+1]:
                return Falsec
        return True
        