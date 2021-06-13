class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        
        def subpow(x1=x,n1=abs(n)):
            if n1==0:
                return 1
            elif n1%2==0:
                return subpow(x1*x1,n1//2)
            elif n1%2!=0:
                return x1*subpow(x1*x1,(n1-1)//2)
            
        ret=subpow()
        return ret if n>0 else 1/ret
        
        
        