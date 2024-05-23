class ListNode:
    def __init__(self, val=None, key=None, next=None, prev=None) -> None:
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return f"val: {self.val},  next: {self.next} prev: {self.prev}"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, value: object) -> bool:
        return self.__str__() == value.__str__()




class LRUCache:

    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError
        self.capacity = capacity
        self.lookup = dict()

        self.head = None
        self.tail = self.head

    def get(self, key: int) -> int:
        if key in self.lookup:
            self.move_to_end(key)
            return self.lookup[key].val
            # next = node.next, next.prev = prev
        return -1

    def move_to_end(self, key):
        if key in self.lookup:
            node = self.lookup[key]
            if node.prev is not None and node.next is not None:
                prev = node.prev
                prev.next = node.next
                next = prev.next
                next.prev = prev
            elif node.prev is None and node.next is not None:
                self.head = node.next
                self.head.prev = None
            elif node is self.tail:
                return
            self.tail.next = node
            node.next = None
            node.prev = self.tail
            self.tail = node

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            node = self.lookup[key]
            node.val = value
            self.move_to_end(key)
        else:
            self.lookup[key] = ListNode(value,key)
            if self.head is None:
                self.head = self.lookup[key]
                self.tail = self.head
            self.move_to_end(key)

        if len(self.lookup) > self.capacity:
            del self.lookup[self.head.key]
            self.head = self.head.next
            self.head.prev = None
            
            

def test_one():
    '''
    Example 1:

    Input
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    Output
    [null, null, null, 1, null, -1, null, -1, 3, 4]
    '''
    pass


