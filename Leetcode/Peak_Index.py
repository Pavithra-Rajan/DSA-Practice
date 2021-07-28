class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """return arr.index(max(arr))"""
        lo,hi=0,len(arr)-1
        while lo<hi:
            mid=(lo+hi)//2
            if arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid
            if arr[mid]<arr[mid+1]:
                lo=mid
            else:
                hi=mid
        