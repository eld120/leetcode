class MyHashMap:

    def __init__(self):
        self.contains = []

    def put(self, key: int, value: int) -> None:
        found = False
        for i, tup in enumerate(self.contains):
            if tup[0] == key:
                self.contains[i] = (key, value)
                found = True
        if not found:
            self.contains.append((key, value))

    def get(self, key: int) -> int:
        
        for tup in self.contains:
            if key == tup[0]:
                return tup[1]
        return -1
        

    def remove(self, key: int) -> None:
       
        for i, tup in enumerate(self.contains):
            if key == tup[0]:
                temp = self.contains.pop(i)
                del temp
                


def test_one():
    h = MyHashMap()
    h.put(1,1)
    h.put(2,2)
    assert h.get(1) == 1
    assert h.get(3) == -1
    h.put(2,1)
    assert h.get(2) == 1