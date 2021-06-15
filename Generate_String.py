class Solution:
    def generateTheString(self, n: int) -> str:
        if n==1:
            return "a"
        if n==3:
            return "aaa"
        if n%2==0:
            return "a"*1+"b"*(n-1)
        return "a"*1+"b"*3+"c"*(n-4)