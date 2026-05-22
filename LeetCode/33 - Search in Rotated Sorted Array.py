class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i, mid, j = 0, 0, n-1
        while i <= j:
            mid = (i + j) // 2
            if nums[i] <= nums[mid]: # Left Half is sorted
                if target == nums[mid]:
                    return mid
                elif target < nums[mid] and target >= nums[i]:
                    j = mid - 1
                elif target > nums[mid]:
                    # Check in the other half (might be unsorted)
        return mid
        
