class Solution:

    def __init__(self, nums: List[int]):
        self.arr=nums
        
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """

        return self.arr
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        ret=self.arr.copy()
        n=len(ret)
        for i in range(n):
            ind=random.randint(0,n-1)
            ret[i],ret[ind]=ret[ind],ret[i]
        return ret
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()