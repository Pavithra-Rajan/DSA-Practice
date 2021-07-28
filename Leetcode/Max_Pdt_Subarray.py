class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_i=min_i=res=nums[0]
        for i in nums[1:]:
            temp=max(i,max_i*i,min_i*i)
            min_i=min(i,min_i*i,max_i*i)
            max_i=temp
            res=max(max_i,res)
        return res
       
        