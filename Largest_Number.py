from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comp(a,b):
            if int(a+b)<int(b+a):
                return -1
            if int(a+b)>int(b+a):
                return 1
            return 0
            
        nums = list(map(str, nums))
        nums=sorted(nums,key=cmp_to_key(comp), reverse = True)
        return '0' if nums[0] == '0' else ''.join(nums)