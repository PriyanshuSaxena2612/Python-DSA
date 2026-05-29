class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_num = float('inf')
        for num in nums:
            sum_num = sum(map(int, str(num)))
            min_num = min(min_num, sum_num)
        return min_num
