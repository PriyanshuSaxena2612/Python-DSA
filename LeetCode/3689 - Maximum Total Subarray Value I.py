class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        max_, min_ = max(nums), min(nums)
        return (max_ - min_ )* k
