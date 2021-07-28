class Solution:
    def getSum(self, a: int, b: int) -> int:

        comp=0b11111111111111111111111111111111
        MAX=0b01111111111111111111111111111111
        
        if b==0:
            return a if a<=MAX else ~(a^comp)
        return self.getSum((a^b)&comp,((a&b)<<1)&comp)
        
        
        """  
        return int(log2(pow(2,a)*pow(2,b)))
	comp is used if there is an overflow so it will 'and'ed to keep it within 32 bits
	MAX is the negative 32 bit possible so if any value goes beyond that we take 2s complement
        """
        