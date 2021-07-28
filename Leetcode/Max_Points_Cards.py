class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
       
        max_sum=temp=sum(cardPoints[:k])
        for i in range(1,k+1):
            temp=temp-cardPoints[k-i]+cardPoints[-i]
            if temp>max_sum:
                max_sum=temp
        return max_sum
    
        