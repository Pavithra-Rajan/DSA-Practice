class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain.insert(0,0)
        for i in range(len(gain)):
            if i!=0:
                gain[i]=gain[i]+gain[i-1]
        return max(gain)