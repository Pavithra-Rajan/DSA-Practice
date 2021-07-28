
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c=r=o=a=k=max_=curr=0
        for i in croakOfFrogs:
            if i=='c':
                c+=1
                curr+=1
            elif i=='r':
                r+=1
            elif i=='o':
                o+=1
            elif i=='a':
                a+=1
            else:
                k+=1
                curr-=1
            max_=max(max_,curr)
        
            if c<r or r<o or o<a or a<k:
                return -1
        if curr==0 and c==a and a==o and o==r and r==k:
            return max_
        return -1
            
       

            
        