from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1=Counter(s)
        dic2=Counter(t)
        return dic1==dic2