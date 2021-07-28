class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        res1=0
        for i,j in zip(sorted(nums1),sorted(nums2,reverse=True)):
            res1+=i*j
        res2=0
        for i,j in zip(sorted(nums1,reverse=True),sorted(nums2)):
            res2+=i*j
        return min(res1,res2)