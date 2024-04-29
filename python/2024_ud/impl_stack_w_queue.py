

class LeetcodeStack:

    def __init__(self, val:list =None) -> None:
        self.container = [x for x in val]

    def push(self, x: int) -> None:
        self.container.append(x)

    def pop(self) -> int:
        return self.container.pop()
        

    def top(self) -> int:
        return self.container[-1]

    def empty(self) -> bool:
        return self.container