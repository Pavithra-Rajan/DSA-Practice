class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ret=[]
        for i in range(0,len(nums),2):
            for j in range(1,nums[i]+1):
                ret.append(nums[i+1])
                
        return ret