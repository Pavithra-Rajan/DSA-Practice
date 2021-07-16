//Bubble Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def bubble(nums):
            for i in range(len(nums)):
                for j in range(0,len(nums)-i-1):
                    if nums[j]>nums[j+1]:
                        nums[j],nums[j+1]=nums[j+1],nums[j]
        bubble(nums)
        return(nums)

// Selection Sort
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