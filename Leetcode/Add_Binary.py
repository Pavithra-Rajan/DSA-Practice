class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]
        """ret1=0
        for i in a:
            ret1=ret1*2+int(i)
        ret2=0
        for i in b:
            ret2=ret2*2+int(i)
        
        return (str(bin(ret1+ret2)))[2:]"""
            