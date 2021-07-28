class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        return (n*(n+1)//2)-sum(nums)
        """nums.sort()
        # print(nums)
        if nums[0]!=0: # 0 1 2 3 4 6
            return 0
        for i in range(len(nums)):
            
            if nums[i]!=nums[i-1]+1 and i!=0:
                return i
        return len(nums)"""
        