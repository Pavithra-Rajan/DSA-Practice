class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        satisfaction.sort(reverse=True)
        while sum(satisfaction)<0:
            satisfaction.pop()
        satisfaction.sort()
        level=0
        for i in range(0,len(satisfaction)):
            level=level+satisfaction[i]*(i+1)
        return level
        