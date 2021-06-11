class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        new=[]
        for i,j in zip(nums,index):
            new.insert(j,i)
        return new
            
        