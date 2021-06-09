class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        string=['']*len(indices)
        j=0
        for i in indices:
            string[i]=s[j]
            j+=1
        return "".join(i for i in string)