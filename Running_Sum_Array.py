class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        run_sum=nums[0]
        for i in range(1,len(nums)):
            nums[i]+=run_sum
            run_sum=nums[i]

        return nums
