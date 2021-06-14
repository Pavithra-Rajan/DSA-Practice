class Solution:
    def minOperations(self, n: int) -> int:
        return n*n//4 #AP sum of 1,3,5 etc with sum=n//4(2+(n//2-1)2)
        '''return n*(n//2)//2 if n%2==0 else (n-1)*(n//2+1)//2'''
        '''count=0
        mid=n//2
        # print(mid)
        if n%2==1:
            mid=2*mid+1
        else:
            mid=2*mid
            # print(mid)
        for i in range(n//2):
            # print(count)
            count+=abs(2*i+1-mid)
        return count'''
                