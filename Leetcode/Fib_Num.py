class Solution:
    def fib(self, n: int) -> int:
        """if n==0:
            return 0
        if n==1:
            return 1
        return self.fib(n-1)+self.fib(n-2)"""
        phi=(1+pow(5,0.5))/2
       
        return round(pow(phi,n)/pow(5,0.5))
        