class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        
        # a= (n-l(l+1)/2)/(l+1)
        l=1
        c=0
        while 2*n>l*(l+1):
            if (n - (l * (l + 1) ) / 2) / (l + 1)%1==0:
                c+=1
            l=l+1
        return c+1
        