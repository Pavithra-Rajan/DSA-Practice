class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret=[]
        for i in nums1:
            ind=nums2.index(i)
            flag=0
            for j in nums2[ind+1:]:
                if j>i:
                    ret.append(j)
                    flag=1
                    break
            if flag==0:
                ret.append(-1)
        
        return ret
            