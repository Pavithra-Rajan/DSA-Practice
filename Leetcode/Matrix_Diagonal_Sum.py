class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        prim=0
        n=len(mat)
        for i in range(n):
            prim+=mat[i][i]+mat[i][n-1-i]
            if n-1==2*i:
                prim-=mat[i][i]
        return prim
            
        
        """primary=0
        
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j:
                    primary+=mat[i][i]
                if i+j==len(mat)-1 and i!=j:
                    primary+=mat[i][j]
        return primary"""
                