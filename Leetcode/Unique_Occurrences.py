from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_tab=Counter(arr)
        ls=[]
        for i in hash_tab.values():
            if i in ls:
                return False
            ls.append(i)
        return True
        