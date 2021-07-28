class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #O(m+n) algo
        stack=[]
        hashm={}
        ret=[]
        for i in nums2:
            while stack and i>stack[-1]:
                hashm[stack.pop()]=i
            stack.append(i)
        while stack:
            hashm[stack.pop()]=-1
        for i in nums1:
            ret.append(hashm[i])
        return ret
            
            
        # O(nm) algo
        """ret=[]
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
        
        return ret"""
            