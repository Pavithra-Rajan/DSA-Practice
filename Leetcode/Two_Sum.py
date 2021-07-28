class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={} # potential value dictionary
        
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]],i]
            else:
                dic[target-nums[i]]=i 
            
        """ret=[]
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    ret.append(i)
                    ret.append(j)
                    break
        return ret"""