class Solution:
    def missingNum(self, arr):
        # code here
        n,arr_sum = len(arr)+1,sum(arr)
        return (n*(n+1))//2-arr_sum
