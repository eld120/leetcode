class ListNode:
    def __init__(self, val=None, nxt=None) -> None:
        self.val = val
        self.nxt = nxt




class MySet:
    def __init__(self) -> None:
        self.container = dict()
        
    def add(self, key: int) -> None:
        if key not in self.container:
            self.container[key] = key

    def remove(self, key: int) -> None:
        del self.container[key]
        
    def contains(self, key: int) -> bool:
        return key in self.container
    