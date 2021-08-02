class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        check=0
        for i in range(1,int(math.sqrt(num))+1):
            if num%i==0:
                check+=i
                if i*i!=num:
                    check+=num/i
        return num==check//2
        
        
        """
        TLE
        check=0
        for i in range(1,num//2+1):
            if num%i==0:
                check+=i
        if check==num:
            return True
        return False"""