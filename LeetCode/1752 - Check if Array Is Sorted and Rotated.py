"""
Logic: Check number of drops here, a sorted rotated array cannot have more than 1 drops
"""
class Solution:
    def check(self, arr: List[int]) -> bool:
        n = len(arr)
        drop = 0
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                drop += 1
            if drop > 1:
                return False
        if arr[n-1] > arr[0]:
            drop += 1
        return drop <= 1
