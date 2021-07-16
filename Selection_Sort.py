class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def selection(nums):
            for i in range(len(nums)):
                start=i
                for j in range(i+1,len(nums)):
                    if nums[start]>nums[j]:
                        start=j
                nums[start],nums[i]=nums[i],nums[start]
        selection(nums)
        return nums