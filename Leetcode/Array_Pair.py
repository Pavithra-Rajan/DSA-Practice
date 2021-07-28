class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum_ret=0
        for i in range(0,len(nums),2):
            # print(nums[i])
            sum_ret+=nums[i]
            
        return sum_ret