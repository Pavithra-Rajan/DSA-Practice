class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        end=len(nums)
        while i<end:
            if nums[i]==nums[i-1]:
                temp=nums.pop(i)
                nums.append(temp)
                end-=1
            else:
                i+=1
            
        return len(nums[0:end])
                