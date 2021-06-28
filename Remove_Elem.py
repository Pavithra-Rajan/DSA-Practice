class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=len(nums)
        
        while i<j:
            if nums[i]==val:
                nums.pop(i)
                j-=1
                continue
            else:
                i+=1
        return len(nums)
            
        """i=0
        j=len(nums)
        
        while i<j:
            if nums[i]==val:
                temp=nums.pop(i)
                nums.append(temp)
                j-=1
                continue
            else:
                i+=1
        return len(nums[:j])
            """
        