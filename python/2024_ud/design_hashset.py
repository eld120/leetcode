class ListNode:
    def __init__(self, val=None, nxt=None) -> None:
        self.val = val
        self.nxt = nxt




class MySet:
    def __init__(self) -> None:
        self.container = []
        

    def add(self, key: int) -> None:
        self.container.append(key)

    def remove(self, key: int) -> None:
        self.container.remove(key)
        
    def contains(self, key: int) -> bool:
        return key in self.container
    