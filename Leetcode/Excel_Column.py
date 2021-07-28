class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        ret=[]
        while columnNumber>0:
            columnNumber-=1
            
            columnNumber,i=divmod(columnNumber,26)
            ret.insert(0,chr(i+65))
            
            
            #print(ins)
        return "".join(ret)
    
    # 701 % 26 =25 Y
    # 701//26=26 Z
    