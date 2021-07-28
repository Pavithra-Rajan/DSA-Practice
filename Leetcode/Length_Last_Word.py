class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split()
        try:
            return len(s[-1])
        except:
            return 0
        