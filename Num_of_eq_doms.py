class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hmap={}
        for i in dominoes:
            i=tuple(sorted(i))
            if i in hmap:
                hmap[i]+=1
            else:
                hmap[i]=1
        ret=0
        for i in hmap.values():
            ret=ret+i*(i-1)//2
        return ret
            
        
            
        