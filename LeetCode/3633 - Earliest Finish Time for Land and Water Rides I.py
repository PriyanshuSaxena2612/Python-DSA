class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        l = len(landStartTime)
        w = len(waterStartTime)
        min_ = float('inf')
        for i in range(l):
            for j in range(w):
                land_route = landStartTime[i] + landDuration[i]
                water_start = max(land_route, waterStartTime[j])
                total_A = water_start + waterDuration[j]

                water_route = waterStartTime[j] + waterDuration[j]
                land_start = max(water_route, landStartTime[i])
                total_B = land_start + landDuration[i]

                min_ = min(min_, total_A, total_B)
                
        return min_
        
