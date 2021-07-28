class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ret=[]
        rowi,rowf,coli,colf=0,len(matrix),0,len(matrix[0])
        while rowi<rowf or coli<colf:
            #right
            if rowi<rowf:
                ret.extend([matrix[rowi][i] for i in range(coli,colf)])
           
                rowi+=1
            #down
            if coli<colf:
                ret.extend([matrix[i][colf-1] for i in range(rowi,rowf)])
                colf-=1
            #left
            if rowi<rowf:
                ret.extend([matrix[rowf-1][i] for i in range(colf-1,coli-1,-1)])
            rowf-=1

            #up
            if coli<colf:
                ret.extend([matrix[i][coli] for i in range(rowf-1,rowi-1,-1)])
            coli+=1
        return ret

        