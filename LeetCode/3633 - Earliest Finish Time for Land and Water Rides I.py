class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        l = len(landStartTime)
        w = len(waterStartTime)
        sum_, min_ = float('inf'), float('inf')
        for i in range(l):
            for j in range(w):
                if (landStartTime[i] + landDuration[i]) >= waterStartTime[j]:
                    sum_ = landStartTime[i] + landDuration[i] + waterDuration[j]
                if (waterStartTime[j] + waterDuration[j]) >= landStartTime[i]:
                    sum_ = waterStartTime[j] + waterDuration[j] + landDuration[i]
                else:
                    sum_ = landStartTime[i] + landDuration[i] + waterStartTime[j] + waterDuration[j]
                min_ = min(sum_, min_)
        return min_
        
