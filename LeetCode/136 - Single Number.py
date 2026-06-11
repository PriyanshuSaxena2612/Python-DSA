from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return counter.most_common()[-1][0]
