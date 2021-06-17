class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        map_={}
        sort=sorted(nums)
        ret=[]
        for i in range(len(sort)):
            if sort[i] not in map_:
                map_[sort[i]]=i
        for i in range(len(sort)):
            ret.append(map_[nums[i]])
        return ret
        """res=list()
        
        for i in range(0,len(nums)):
            small=0
            for j in range(0,len(nums)):
                if i!=j:
                    if nums[j]<nums[i]:
                        small+=1
            res.append(small)
            
        return res"""
                    
                    
                    
                    
                    
                    
