





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