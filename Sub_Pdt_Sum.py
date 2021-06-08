class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pdt,sumd=1,0
        
        while n>0:
            dig=n%10
            pdt*=dig
            sumd+=dig
            n/=10
            n=int(n)
        return pdt-sumd
            