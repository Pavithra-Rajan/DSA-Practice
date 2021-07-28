# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        """for i in range(1,n+1):
            if(isBadVersion(i)==True):
                return i"""
        lo=1
        hi=n
        while lo<=hi:
            mid=(lo+hi)//2
            if isBadVersion(mid)==True:
                hi=mid-1
            else:
                lo=mid+1
        return lo
                
        