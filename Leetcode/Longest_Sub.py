class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        l,r,ret=0,0,0
        while r<len(s):
            if s[r] in d and d[s[r]]>=l:
                l=d[s[r]]+1
            ret=max(ret,r-l+1)
            d[s[r]]=r
            r+=1
        return ret