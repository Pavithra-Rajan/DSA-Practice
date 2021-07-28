"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack,temp=[root],[]
        while(len(stack)!=0):
            top=stack.pop()
            temp.append(top.val)
            
            stack.extend(reversed(top.children))
        return temp