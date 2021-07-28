class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def binary_search(sub_list):
            l,r=0,len(sub_list)
            while l<r:
                m=(l+r)//2
                if sub_list[m]<0:
                    r=m
                else:
                    l=m+1
            return len(sub_list)-l
        
        c=0
        for i in grid:
            c+=binary_search(i)
        return c
        
        """j=-1
        count=0
        #print(len(grid))
        for i in range(len(grid)):
            j=-1
            while j>=-len(grid[i]):
                if grid[i][j]<0:
                    count+=1
                j-=1
        return count"""