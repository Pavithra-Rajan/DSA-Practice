class Solution:
    def judgeCircle(self, moves: str) -> bool:
        origin=[0,0]
        for i in moves:
            if i=='R':
                origin[0]+=1
            elif i=='L':
                origin[0]-=1
            elif i=='U':
                origin[1]+=1
            else:
                origin[1]-=1
        return True if origin[0]==origin[1] and origin[0]==0 else False
            