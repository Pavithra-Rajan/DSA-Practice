class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        dist=[]
        for i in range(0,len(s)):
            if s[i]==c:
                dist.append(i)
        min_d=[]
        for i in range(0,len(s)): 
            m=9999
            for j in dist:
                if abs(i-j)<m:
                    m=abs(i-j)
            min_d.append(m)
        return min_d
                
            