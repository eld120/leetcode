import heapq
from collections import deque, Counter


class MinStack:
    def __init__(self) -> None:
        self.node = deque()
        self.min = []
        heapq.heapify(self.min)

    def push(self, val: int) -> None:
        self.node.appendleft(val)
        heapq.heappush(self.min, val)

    def pop(self) -> None:
        temp = self.node.popleft()
        if temp == heapq.nsmallest(1, self.min)[0]:
            heapq.heappop(self.min)
        else:
            container = []
            while True:
                smallest = heapq.heappop(self.min)
                if smallest == temp:
                    break
                else:
                    container.append(smallest)
            for val in container:
                heapq.heappush(self.min, val)

    def __repr__(self) -> str:
        return f"{self.node}"

    def __eq__(self, __value: object) -> bool:
        return self.__repr__() == __value.__repr__()

    def top(self) -> int:
        temp = self.node.popleft()
        self.node.appendleft(temp)
        return temp

    def get_min(self) -> int:
        temp = heapq.heappop(self.min)
        heapq.heappush(self.min, temp)
        return temp


def test_three():
    stack_test = MinStack()
    assert stack_test.push(-2) == MinStack().push(-2)
    stack_test.push(0)
    stack_test.push(-1)
    assert stack_test.get_min() == -2
    assert stack_test.top() == -1
    stack_test.pop()
    assert stack_test.top() == 0
    assert stack_test.get_min() == -2
