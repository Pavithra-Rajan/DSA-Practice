class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res=list()
        
        for i in range(0,len(nums)):
            small=0
            for j in range(0,len(nums)):
                if i!=j:
                    if nums[j]<nums[i]:
                        small+=1
            res.append(small)
            
        return res
                    
                    
                    