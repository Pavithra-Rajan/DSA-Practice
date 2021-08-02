class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret=0
        temp=0
        for i in nums:
            if i==0:
                ret=max(ret,temp)
                temp=0
                
            else:
                temp+=1
        ret=max(ret,temp)
        return ret