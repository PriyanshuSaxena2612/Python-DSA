# Question Link: https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1
class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        n = len(arr)
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                return False
        return True
