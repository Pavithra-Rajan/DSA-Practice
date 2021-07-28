class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        ref={'(':')','[':']','{':'}'}
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            else:
                try:
                    temp=stack.pop()
                    # print(ref.get(temp))
                    if ref.get(temp)!=i:
                        return False
                except:
                    return False
        if stack:
            return False
        return True