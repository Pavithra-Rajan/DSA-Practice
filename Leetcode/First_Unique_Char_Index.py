from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic=Counter(list(s))
        ind=-1
        for i,k in dic.items():
            
            if k==1:
                ind=s.index(i)
                break
        return ind