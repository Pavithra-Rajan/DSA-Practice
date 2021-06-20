class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        # O(1) space and O(n) time complexity
        beg=0
        end=len(s)
        ret=[]
        for i in s:
            if i=='I':
                ret.append(beg)
                beg+=1
            else:
                ret.append(end)
                end-=1
        if s[-1]=='D':
            ret.append(end)
        else:
            ret.append(beg)
        return ret
        """ret=[]
        temp=[]
        for i in range(len(s)+1):
            temp.append(i)
        # print(temp)
        for i in s:
            if i=='I':
                ret.append(temp.pop(0))
            else:
                ret.append(temp.pop())
        ret.append(temp.pop())
        return ret"""
        