class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        return nums.index(max(nums)) if sorted(nums)[-2]*2<=max(nums) else -1
                
        