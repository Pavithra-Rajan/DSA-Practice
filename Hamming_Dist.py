class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res=str(bin(x^y))
        # print(res)
        count=res.count("1")
        return count