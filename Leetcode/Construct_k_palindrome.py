from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k>len(s):
            return False
        hmap=Counter(s)
        odd=0
        for i in hmap.values():
            if i%2==1:
                odd+=1
        if odd>k:
            return False
        return True