
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ss=s[1:]+s[:-1]
        return s in ss