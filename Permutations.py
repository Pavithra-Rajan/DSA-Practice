class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def DFS(nums,path,res):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                DFS(nums[:i]+nums[i+1:], path+[nums[i]], res)
        res=[]
        DFS(nums,[],res)
        return res