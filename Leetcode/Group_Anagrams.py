from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret=defaultdict(list)
        for i in strs:
            ret[tuple(sorted(i))].append(i)
        return ret.values()
        