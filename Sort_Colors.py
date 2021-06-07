class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
    
        end=len(nums)-1
        i=0
        
        while i<=end:
            if nums[i]==0:
                
                nums.insert(0,nums.pop(i))
                i+=1
                
            elif nums[i]==2:
                
                nums.append(nums.pop(i))
                end-=1 
                
            else:
                i+=1
      