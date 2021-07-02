class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r=0,len(arr)-1
        while l<r:
            mid=(l+r)//2
            if mid+k<len(arr) and x-arr[mid]>arr[mid+k]-x:
                l=mid+1
            else:
                r=mid
        return arr[l:(l+k)]
        
        