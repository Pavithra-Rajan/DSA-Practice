class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_r=0
        count_l=0
        fin=0
        for i in s:
            if i=='R':
                count_r+=1
            else:
                count_l+=1
            if count_r==count_l and count_r!=0 and count_l!=0:
                fin+=1
                count_r=0
                count_l=0
        return fin