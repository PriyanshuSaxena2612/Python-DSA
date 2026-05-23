class Solution:
    def maxSubarraySum(self, arr, k):
        """
        Logic: Take the initial sum till k, and consider it the max_sum, and then to move forward, remove the last element and add the new element
        """
        n = len(arr)
        sum_sub = sum(arr[:k])
        max_sum = sum_sub
        for i in range(1, n-k+1):
            sum_sub = sum_sub - arr[i-1] + arr[i + k - 1]
            max_sum = max(max_sum, sum_sub)
        return max_sum
