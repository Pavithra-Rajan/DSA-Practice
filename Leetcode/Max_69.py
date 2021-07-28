class Solution:
    def maximum69Number (self, num: int) -> int:
        """try:
            return int(str(num).replace('6','9',1))
        except:
            return num"""
        num=str(num)
        num=list(num)
        for i in range(len(num)):
            if num[i]=='6':
                num[i]='9'
                break
        return "".join(num)
                
        