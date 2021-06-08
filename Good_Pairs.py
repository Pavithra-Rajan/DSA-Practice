class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    count+=1
        return count

# with dictionary
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs={}
        for i in nums:
            if i in pairs:
                pairs[i]+=1
            else:
                pairs[i]=1
        good=0
        for i in pairs:
            if pairs[i]>1:
                good=good+pairs[i]*(pairs[i]-1)//2
        return good