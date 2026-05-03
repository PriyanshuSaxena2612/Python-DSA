# Question Link: https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1
class Solution:
    def largest(self, arr):
        max_num = float('-inf')
        for i in range(len(arr)):
            if arr[i] >= max_num:
                max_num = arr[i]
        return max_num
