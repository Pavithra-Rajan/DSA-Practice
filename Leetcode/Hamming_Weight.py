class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        while n > 0:
            counter += n & 1
            n = n >> 1
        return counter
        """# print(n)
        n=str(bin(n))
        
        return n.count('1')
        """