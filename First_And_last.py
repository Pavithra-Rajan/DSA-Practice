class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binser(nums,target):
            l,r=0,len(nums)
            while l<r:
                mid=(l+r)//2
                if nums[mid]<target:
                    l=mid+1
                else:
                    r=mid
            return l
        """if len(nums)==1 and nums[0]==target:
            return [0,0]"""
        lo=binser(nums,target)
        hi=binser(nums,target+1)-1
        if lo<=hi:
            return [lo,hi]
        return [-1,-1]
    
        