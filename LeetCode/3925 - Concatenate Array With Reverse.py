class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        nums[:] = nums + nums[::-1]
        return nums
