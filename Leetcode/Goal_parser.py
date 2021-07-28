class Solution:
    def interpret(self, command: str) -> str:
        res=[]
        for i in range(0,len(command)):
            if command[i]=='G':
                res.append("G")
            if command[i]=='(' and command[i+1]==')':
                res.append("o")
            if command[i]=='(' and command[i+1]=='a':
                res.append("al")
        return "".join(res)