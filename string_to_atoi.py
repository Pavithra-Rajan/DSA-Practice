class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        
        """
        s=s.strip()
        if len(s)==0 or not (s[0].isdigit() or s[0] in ['+','-']):
            return 0
        
        if s[0]=='-':
            sign='-'
        else:
            sign='+'
        if s[0]=='+' or s[0]=='-':
            i=1
        else:
            i=0
        num=0
        
        while(i<len(s) and s[i].isdigit()):
            num*=10
            num+=int(s[i])
            i+=1
            
        if sign=='-':
            num=num*(-1)
        if num>pow(2,31)-1:
            return pow(2,31)-1
        if num<-pow(2,31):
            return -pow(2,31)
        return num
        