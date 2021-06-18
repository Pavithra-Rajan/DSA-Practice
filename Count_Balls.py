class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ball=[0]*47
        for i in range(lowLimit,highLimit+1):
            res=0
            while i>0:
                
                res+=i%10
                i=i//10
 
            """stri = str(i)
            list_ = list(map(int, stri))
            res=sum(list_)"""
            ball[res-1]+=1
        return max(ball)