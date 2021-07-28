class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ret=[]
        for i in range(left,right+1):
            
            dig=[]
            dig=list(str(i))
            flag=1
            for j in dig:
                j=int(j)
                if j==0 or i%j!=0 :
                    flag=0
                    break
            if flag==1:
                ret.append(i)
        return ret