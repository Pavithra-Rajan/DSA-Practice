class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        '''return str(int(num1)+int(num2))'''
        def convert(num):
            res=0
            for i in num:
                res=res*10+(ord(i)-ord('0'))
            return res
        return str(convert(num1)+convert(num2))