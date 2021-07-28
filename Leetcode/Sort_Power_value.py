class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        ret={}
        for i in range(lo,hi+1):
            temp=i
            count=0
            while i!=1:
                if i%2==0:
                    i=i/2
                else:
                    i=3*i+1
                count+=1
            ret[temp]=count
            
        ret=sorted(ret,key=lambda x:(ret[x],x))
        return ret[k-1]
        
       
        