from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic=Counter(nums)
        sum_=0
        for i,k in dic.items():
            if k==1:
                sum_+=i
        return sum_
                
        