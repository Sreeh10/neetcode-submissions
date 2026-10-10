class MinStack:
    s : list # (val)
    mins : list # (val, index)

    def __init__(self):
        self.s = []
        self.mins = []
        return

    def push(self, val: int) -> None:
        self.s.append(val)
        if len(self.mins) == 0 or val < self.mins[-1][0]:
            self.mins.append((val,len(self.s)))
        return

    def pop(self) -> None:
        if len(self.s) == self.mins[-1][1]:
            self.mins.pop()
        self.s.pop()
        return

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.mins[-1][0]
        
