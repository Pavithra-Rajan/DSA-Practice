class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        ret={}
        for num in range(2,int(sqrt(n))+1):
            if num not in ret:
                for i in range(num*num,n,num):
                    ret[i]=1
                    
        return n-len(ret)-2
        
        """numbers = {}
        for p in range(2, int(sqrt(n)) + 1):
            if p not in numbers:
                for multiple in range(p*p, n, p):
                    numbers[multiple] = 1
        
        # Exclude "1" and the number "n" itself.
        return n - len(numbers) - 2"""