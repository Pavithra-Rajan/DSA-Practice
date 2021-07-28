// Heap Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(nums,n,i):
            max_=i
            l=2*i+1
            r=2*i+2
            if l<n and nums[max_]<nums[l]:
                max_=l
            if r<n and nums[max_]<nums[r]:
                max_=r
            if max_!=i:
                nums[max_],nums[i]=nums[i],nums[max_]
                heapify(nums,n,max_)
        def heapsort(nums):
            n=len(nums)
            for i in range(n//2-1,-1,-1):
                heapify(nums,n,i)
        
            for i in range(n-1,0,-1):
                nums[i],nums[0]=nums[0],nums[i]
                heapify(nums,i,0)
            
        heapsort(nums)
        return nums

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