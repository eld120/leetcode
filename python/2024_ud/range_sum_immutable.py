





class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.answer = 0

    def sumRange(self, left: int, right: int) -> int:
        while left <= right:
            self.answer += self.nums[left]
            
            left+= 1
        temp = self.answer
        self.answer = 0
        return temp

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

def test_example_one():
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    test_input = [[0, 2], [2, 5], [0, 5]]
    test_output = [1, -1, -3]
    for index, val in enumerate(test_input):
        assert obj.sumRange(val[0], val[1]) == test_output[index]