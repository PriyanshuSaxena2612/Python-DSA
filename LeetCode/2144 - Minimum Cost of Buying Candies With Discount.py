class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        if len(cost) <= 2:
            return sum(cost)
        sum_ = 0
        for i in range(len(cost)):
            if i %3 != 2:
                sum_ += cost[i]
        return sum_
