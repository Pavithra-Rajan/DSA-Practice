class Solution:
    def sumZero(self, n: int) -> List[int]:
        ret=[]
        i=1
        if n%2==0:
            while n>0:
                ret.extend([i,-i])
                i+=1
                n-=2
        else:
            while n>1:
                ret.extend([i,-i])
                i+=1
                n-=2
            ret.append(0)
        return ret