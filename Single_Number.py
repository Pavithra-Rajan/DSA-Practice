from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic=Counter(nums)
        for i,k in dic.items():
            if k==1:
                return i
        """ ret=0
        for i in nums:
            ret^=i
        return ret"""