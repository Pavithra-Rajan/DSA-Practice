class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust)==0 and n==1:
            return  1
        col0=[i[0] for i in trust]
        col1=[i[1] for i in trust]
        for i in range(n):
            if (i+1) in col1 and col1.count(i+1)==n-1 and (i+1) not in col0:
                return i+1
        return -1
         
   
        
