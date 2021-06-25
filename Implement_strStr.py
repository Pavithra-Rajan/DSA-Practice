class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        hlen=len(haystack)
        nlen=len(needle)
        range_len=hlen-nlen
        for i in range(range_len+1):
            if haystack[i:i+nlen]==needle:
                return i
                        
        return -1