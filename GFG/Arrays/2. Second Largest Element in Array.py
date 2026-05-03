# Question Link: https://www.geeksforgeeks.org/problems/second-largest3735/1
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        # O(nlogn) approach
        arr = sorted(list(set(arr)))
        if len(arr) == 1: return -1
        return arr[-2]
        
        # O(n) approach
        largest = -1
        second_largest = -1
        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num
        return second_largest
