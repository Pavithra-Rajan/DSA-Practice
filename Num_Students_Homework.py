class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count=0
        for i in range(len(startTime)):
            if queryTime in range(startTime[i],endTime[i]+1):
                count+=1
        return count
        """count=0
        for i,j in zip(startTime,endTime):
            if i<=queryTime and j>=queryTime:
                count+=1
        return count"""