class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        new=[]
        new.append(first)
        for i in encoded:
            new.append((new[-1]^i))
        return new
        