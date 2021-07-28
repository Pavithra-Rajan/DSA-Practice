from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        dic=Counter(s)
       
        ret=[]
        #print(dic)
        for i in sorted(dic,key=dic.get,reverse=True):
            ret.append(i*dic[i])
        return "".join(ret)
            
        