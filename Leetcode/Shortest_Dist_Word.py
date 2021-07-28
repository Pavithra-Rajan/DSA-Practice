class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        x=-1
        y=-1
        ret=9999
        for i in range(len(wordsDict)):
            if wordsDict[i]==word1:
                x=i
            if wordsDict[i]==word2:
                y=i
            if x!=-1 and y!=-1:
                ret=min(ret,abs(x-y))
        return ret
        """w1=[i for i,x in enumerate(wordsDict) if x==word1]
        w2=[i for i,x in enumerate(wordsDict) if x==word2]
        min_=9999
        for i in w1:
            for j in w2:
                if abs(i-j)<min_:
                    min_=abs(i-j)
        return min_"""