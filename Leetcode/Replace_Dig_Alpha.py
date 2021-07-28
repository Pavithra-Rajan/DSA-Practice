class Solution:
    def replaceDigits(self, s: str) -> str:
        s=list(s)
        for i in range(len(s)):
            if i%2==1:
                s[i]=chr(ord(s[i-1])+ord(s[i])-48)
        return "".join(s)