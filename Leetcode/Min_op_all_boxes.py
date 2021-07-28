class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        l_sum,r_sum,lc,rc,n=0,0,0,0,len(boxes)
        ret=[0]*n
        for i in range(1,n): 
            if boxes[i-1]=='1':
                    l_sum+=1
            lc+=l_sum
            ret[i]=lc
                
        for i in range(n-2,-1,-1): 
            if boxes[i+1]=='1':
                    r_sum+=1
            rc+=r_sum
            ret[i]+=rc
        return ret
            
        """boxes=list(boxes)
        res=[]
        
        for i in range(len(boxes)):
            count=0
            for j in range(len(boxes)):
                if i!=j and boxes[j]=='1':
                    count+=abs(j-i)
            res.append(count)
        return res"""
            
        