


class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity > 0:
            self.capacity = capacity
        else:
            raise ValueError('Capacity must be greater than 0')
        self.array = [] #* capacity

    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        try:
            self.array[i] = n
        except IndexError:
            last_index = len(self.array) -1
            while last_index < i:
                self.array.append(None)
                last_index += 1
            self.array[i] = n

        

    def pushback(self, n: int) -> None:
        copy = [ x for x in self.array if x is not None]
        if len(copy) == self.capacity:
            self.resize()
            
        try:
            self.array.remove(n)
        except ValueError:
            pass
        self.array.append(n)
        

    def popback(self) -> int:
        return self.array.pop()

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        copy = [x for x in self.array if x is not None]
        return len(copy)
    
    def getCapacity(self) -> int:
        return self.capacity


def test_two():
    arr = DynamicArray(1)
    assert arr.getSize() == 0
    assert arr.getCapacity() == 1

def test_three():
    arr = DynamicArray(1)
    assert arr.pushback(1) == None
    assert arr.getCapacity() == 1
    assert arr.pushback(2) == None
    assert arr.getCapacity() == 2

def test_idk():
    arr = DynamicArray(1)
    arguments = ["getSize", "getCapacity", ["pushback", 1], "getSize", "getCapacity", ["pushback", 2], "getSize", "getCapacity", ["get", 1], ["set", 1, 3], ["get", 1], "popback", "getSize", "getCapacity"]
    answers  = [0,1,None,1,1,None,2,2,2,None,3,3,1,2]
    
    for index, arg in enumerate(arguments):
        if len(arg) == 3:
            assert arr.set(arg[1], arg[2]) == answers[index]
        elif len(arg ) == 2 and arg[0] == 'pushback':
            assert arr.pushback(arg[1]) == answers[index]
        elif len(arg ) == 2 and arg[0] == 'get':
            assert arr.get(arg[1]) == answers[index]
        elif arg == 'getCapacity':
            assert arr.getCapacity() == answers[index]
        elif arg == 'getSize':
            assert arr.getSize() == answers[index]
        elif arg == 'popback':
            
            assert arr.popback() == answers[index]

def test_five():
    arguments = [ ["pushback", 0], ["pushback", 1], ["pushback", 2], "getSize", "getCapacity"]
    answers = [None,None,None,3,4]
    arr = DynamicArray(2)
    for index, arg in enumerate(arguments):
        if len(arg) == 3:
            assert arr.set(arg[1], arg[2]) == answers[index]
        elif len(arg ) == 2 and arg[0] == 'pushback':
            assert arr.pushback(arg[1]) == answers[index]
        elif len(arg ) == 2 and arg[0] == 'get':
            assert arr.get(arg[1]) == answers[index]
        elif arg == 'getCapacity':
            assert arr.getCapacity() == answers[index]
        elif arg == 'getSize':
            assert arr.getSize() == answers[index]
        elif arg == 'popback':
            
            assert arr.popback() == answers[index]