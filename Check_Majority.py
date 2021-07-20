class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        def binser(nums,tar):
            lo,hi=0,len(nums)
            while lo<hi:
                mid=(lo+hi)//2
                if nums[mid]<tar:
                    lo=mid+1
                else:
                    hi=mid
            return lo
                
            
        n=len(nums)
        if nums[n//2]!=target:
            return False
        lo=binser(nums,target)
        hi=binser(nums,target+1)
        
        return (hi-lo)>n//2
    
        """n=len(nums)
        if nums[n//2]!=target:
            return False
        lo=bisect.bisect_left(nums,target)
        hi=bisect.bisect_right(nums,target)
        return (hi-lo)>n//2"""
        """return nums.count(target)>len(nums)//2"""
        