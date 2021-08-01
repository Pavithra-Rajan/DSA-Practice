class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.mini=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        temp_min=self.mini[-1] if self.mini else math.inf
        if val<=temp_min:
            self.mini.append(val)

    def pop(self) -> None:
        if self.mini and self.stack.pop()==self.mini[-1]:
            self.mini.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()