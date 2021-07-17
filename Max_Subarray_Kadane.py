class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=temp=nums[0]
        for i in nums[1:]:
            temp=max(i,temp+i)
            maxsum=max(temp,maxsum)
        return maxsum
        