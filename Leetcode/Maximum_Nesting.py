class Solution:
    def maxDepth(self, s: str) -> int:
        
        temp=0
        count=0
        for i in s:
            if i=='(':
                temp+=1
            elif i==')':
                temp-=1
            count=max(temp,count)
        return count        