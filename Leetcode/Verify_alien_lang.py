class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        hmap={}
        for k in range(len(order)):
            hmap[order[k]]=k
        
        # print(hmap)
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                # print("in loops")
                #print(j)
                if j>=len(words[i+1]):
                    return False
                if words[i][j]!=words[i+1][j]:
                    if hmap[words[i+1][j]]<hmap[words[i][j]]:
                        
                        return False
                    
                    break
               
        return True