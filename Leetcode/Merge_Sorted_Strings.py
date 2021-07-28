class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=[]
        if len(word1)>len(word2):
            length=len(word2)
        else:
            length=len(word1)
            
        for i in range(0,length):
            res.append(word1[i])
            res.append(word2[i])
            
        if len(word1)>len(word2):
            res=res+list(word1[length:])
        else:
            res=res+list(word2[length:])
            
        return "".join(res)
            
        