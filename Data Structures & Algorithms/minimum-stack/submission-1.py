class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = 0  

    def push(self, val: int) -> None:
        if len(self.stack) < 1:
            self.mini = val
            self.stack.append(val)
        elif val <= self.mini:
            self.stack.append(2*val - self.mini)
            self.mini = val
        else:
            self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] <= self.mini:
            self.mini = 2*self.mini - self.stack[-1]
            self.stack.pop()
            return
        self.stack.pop()

    def top(self) -> int:
        if self.stack[-1] <= self.mini:
            return self.mini
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mini
        
