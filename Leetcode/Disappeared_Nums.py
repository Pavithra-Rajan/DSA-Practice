class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret=[]
        n=len(nums)
        nums=set(nums)
        for i in range(1,n+1):
            if i not in nums:
                ret.append(i)
        return ret
        """comp=set(list(range(1,len(nums)+1)))
        #print(comp)
        temp=set(nums)
        return list(comp-comp.intersection(temp))"""