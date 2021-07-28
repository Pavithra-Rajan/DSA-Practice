class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret=[]
        for i in zip(*strs):
            if len(set(i))==1:
                ret.append(i[0])
            else:
                break
        return "".join(ret)
        