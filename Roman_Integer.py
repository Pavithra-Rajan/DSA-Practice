class Solution:
    def romanToInt(self, s: str) -> int:
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ret=0
        i=0
        
        while i<len(s):
            #print(i)
            ret+=dic[s[i]]
            
            if s[i]=='I' and (i+1)<len(s) and (s[i+1]=='V' or s[i+1]=='X'):
                ret-=1
                ret=ret+dic[s[i+1]]-1
                i+=1
               
                #print(ret)
                #print(i)
            if s[i]=='X' and (i+1)<len(s) and (s[i+1]=='L' or s[i+1]=='C'):
                ret-=10
                ret=ret+dic[s[i+1]]-10
                i+=1
                #print(ret)
                
            if s[i]=='C' and (i+1)<len(s) and (s[i+1]=='D' or s[i+1]=='M'):
                ret-=100
                ret=ret+dic[s[i+1]]-100
                i+=1
                
                #print(ret)
            i+=1
        return ret