# https://leetcode.com/problems/range-sum-query-immutable/
class NumArray:

    def __init__(self, nums: List[int]):
        sums: int = []
        sums.append(0)
        for index in range(0, len(nums)):
            sums.append(sums[index] + nums[index])
        self.sums = sums
            

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)