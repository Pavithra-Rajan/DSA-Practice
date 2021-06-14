class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s=list(s.split())
        return " ".join(s[0:k])