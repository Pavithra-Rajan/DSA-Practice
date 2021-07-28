class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ret=[]
        for i in range(n+1):
            s=str(bin(i))
            ret.append(s.count('1'))
        return ret
            
        