from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic=Counter(nums)
        for i in dic.values():
            if i>=2:
                return True
        return False
        