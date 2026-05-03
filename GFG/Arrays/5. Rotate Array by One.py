# Question Link: https://www.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1
class Solution:
    def rotate(self, arr):
        # first approach
        arr[:] = [arr[-1]] + arr[:-1]
        return arr
        # second approach
        i, j = 0, len(arr)-1
        while i<=j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        return arr
    
