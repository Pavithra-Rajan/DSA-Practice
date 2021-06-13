class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums)<3: 
            return max(nums)
        first=second=third=float('-inf')
        for i in nums:
            if i>first:
                first,second,third=i,first,second
            elif i>second and i<first:
                second,third=i,second
            elif i>third and i<first and i<second:
                third=i
        return third if third != float('-inf') else max(nums)
        """
        nums=set(nums)
        nums=list(nums)
        nums=sorted(nums,reverse=True)
        # print(nums)
        if len(nums)>=3:
            return nums[2]
        else:
            return nums[0]"""
        
        
        