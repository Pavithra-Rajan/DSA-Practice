class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      
        car=1
        i=len(digits)-1
        while i>=0:
            if car==1:
                digits[i]+=1
                if digits[i]>=10:
                    digits[i]-=10
                else:
                    car=0
            i-=1
        if car==1:
            digits.insert(0,1)
        return digits
        