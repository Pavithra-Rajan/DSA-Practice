class Solution:
    def isNumber(self, s: str) -> bool:
        if("inf" in s.lower()):
            return False
        try:
            fl=float(s)
            return True
        except:
            return False

        """
	if len(s)==1 and (s[0].lower()=='e' or s[0]=='.'):
            return False
        ns=0
        nd=0
        ne=0
        if s[0].lower()=='e' or s[len(s)-1].lower()=='e':
            return False
        for i in range(0,len(s)):
            if nd>1 or ne>1 or ns>1 or(nd==1 and ne==1):
                return False
            if s[i]=='.':
                nd=nd+1
                if nd>1:
                    return False
            if (s[i]=='+' or s[i]=='-') and s[i-1].lower()!='e':
                ns+=1
                try:
                    if s[i+1].isdigit() and i!=0:
                        return False
                except:
                    pass
            if s[i].lower()=='e':
                ne+=1
            if nd==1 and (s[i]=='+' or s[i]=='-'):
                return False
            if s[i].isalpha() and s[i].lower()!='e':
                return False
        if (nd==1 and ne==1): 
            return False
        return True
                """
            
                
            