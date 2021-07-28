from collections import Counter 
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # print(Counter(nums))
        dic=Counter(nums)
        nums.sort(reverse=True)
        
        def get_val(x):
            return dic[x]
        
        nums.sort(key=get_val)
        return nums
        