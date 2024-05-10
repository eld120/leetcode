class MyHashMap:
    def __init__(self):
        self.contains = dict()

    def put(self, key: int, value: int) -> None:
        self.contains[key] = value

    def get(self, key: int) -> int:
        try:
            return self.contains[key]
        except KeyError:
            return -1

    def remove(self, key: int) -> None:
        try:
            del self.contains[key]
        except KeyError:
            pass


def test_one():
    h = MyHashMap()
    h.put(1, 1)
    h.put(2, 2)
    assert h.get(1) == 1
    assert h.get(3) == -1
    h.put(2, 1)
    assert h.get(2) == 1
